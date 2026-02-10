#!/usr/bin/env python3
"""
Banana Image Generation Script
使用 Gemini 3 Pro Image API 生成图片
"""

import argparse
import base64
import mimetypes
import os
import sys
from pathlib import Path
from google import genai
from google.genai import types


def save_binary_file(file_path, data):
    """保存二进制文件"""
    with open(file_path, "wb") as f:
        f.write(data)
    print(f"✓ 图片已保存到: {file_path}")


def load_image_file(image_path):
    """加载图片文件并返回 Part 对象"""
    with open(image_path, 'rb') as f:
        image_data = f.read()

    ext = Path(image_path).suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.webp': 'image/webp',
        '.gif': 'image/gif'
    }
    mime_type = mime_types.get(ext, 'image/png')

    return types.Part.from_bytes(data=image_data, mime_type=mime_type)


def generate_image(prompt, api_key, output_path, reference_images=None, aspect_ratio='auto', image_size='2K'):
    """
    调用Gemini API生成图片

    Args:
        prompt: 文本提示词
        api_key: Gemini API密钥
        output_path: 输出图片路径
        reference_images: 参考图片路径列表（可选）
        aspect_ratio: 图片宽高比，默认16:9
        image_size: 图片尺寸，可选1K/2K，默认2K
    """

    # 创建客户端
    client = genai.Client(api_key=api_key)

    model = "gemini-3-pro-image-preview"

    # 构建 parts 列表
    parts = []

    # 如果有参考图片，先添加参考图片
    if reference_images:
        for img_path in reference_images:
            if not os.path.exists(img_path):
                print(f"警告: 参考图片不存在: {img_path}")
                continue

            parts.append(load_image_file(img_path))
            print(f"已加载参考图片: {img_path}")

    # 添加文本提示词
    parts.append(types.Part.from_text(text=prompt))

    # 构建请求内容
    contents = [
        types.Content(
            role="user",
            parts=parts,
        ),
    ]

    # 配置生成参数
    # 构建 image_config 参数（aspect_ratio 为 auto 时不传递该参数）
    image_config_params = {"image_size": image_size}
    if aspect_ratio != 'auto':
        image_config_params["aspect_ratio"] = aspect_ratio
    
    generate_content_config = types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        image_config=types.ImageConfig(**image_config_params),
    )

    print(f"\n正在生成图片...")
    print(f"模型: {model}")
    print(f"提示词: {prompt}")
    print(f"宽高比: {aspect_ratio}")
    print(f"尺寸: {image_size}")

    try:
        # 使用流式生成
        file_index = 0
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if (
                chunk.candidates is None
                or chunk.candidates[0].content is None
                or chunk.candidates[0].content.parts is None
            ):
                continue

            for part in chunk.candidates[0].content.parts:
                if part.inline_data and part.inline_data.data:
                    # 获取图片数据
                    inline_data = part.inline_data
                    data_buffer = inline_data.data

                    # 根据 MIME 类型确定文件扩展名
                    file_extension = mimetypes.guess_extension(inline_data.mime_type)

                    # 确定输出文件名
                    if file_index == 0:
                        # 第一张图片使用指定的输出路径
                        final_output = output_file.with_suffix(file_extension or output_file.suffix)
                    else:
                        # 多张图片添加序号
                        stem = output_file.stem
                        final_output = output_file.with_name(f"{stem}_{file_index}{file_extension or output_file.suffix}")

                    save_binary_file(str(final_output), data_buffer)
                    file_index += 1
                elif part.text:
                    print(f"模型回复: {part.text}")

        if file_index == 0:
            print("\n错误: 响应中未生成图片")
            sys.exit(1)

    except Exception as e:
        print(f"\n错误: API请求失败")
        print(f"详情: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='使用Gemini 3 Pro Image API生成图片',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本文本生图
  python3 generate_image.py "一只可爱的猫咪" -o cat.png

  # 指定宽高比和尺寸
  python3 generate_image.py "日落风景" -o sunset.png --aspect-ratio 1:1 --size 2K

  # 使用参考图片
  python3 generate_image.py "把这张图片改成卡通风格" -o cartoon.png -r reference.jpg

  # 使用多张参考图片
  python3 generate_image.py "结合这些图片的风格" -o result.png -r img1.jpg -r img2.jpg
        """
    )

    parser.add_argument('prompt', help='图片生成提示词')
    parser.add_argument('-o', '--output', required=True, help='输出图片路径')
    parser.add_argument('-r', '--reference', action='append', dest='references',
                        help='参考图片路径（可多次使用以添加多张参考图）')
    parser.add_argument('--aspect-ratio', default='auto',
                        choices=['auto', '1:1', '16:9', '9:16', '4:3', '3:4', '2:3', '3:2', '4:5', '5:4', '21:9'],
                        help='图片宽高比（默认: auto，由模型自动决定）')
    parser.add_argument('--size', default='2K',
                        choices=['1K', '2K'],
                        help='图片尺寸（默认: 2K）')
    parser.add_argument('--api-key', help='Gemini API密钥（默认从环境变量GEMINI_API_KEY读取）')

    args = parser.parse_args()

    # 获取API密钥
    api_key = args.api_key or os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("错误: 未提供API密钥")
        print("请设置环境变量 GEMINI_API_KEY 或使用 --api-key 参数")
        sys.exit(1)

    # 生成图片
    generate_image(
        prompt=args.prompt,
        api_key=api_key,
        output_path=args.output,
        reference_images=args.references,
        aspect_ratio=args.aspect_ratio,
        image_size=args.size
    )


if __name__ == '__main__':
    main()
