# Moonkite Skills

[English Version](README.md)

本仓库托管了一系列专为 AI 智能体设计的专业技能，旨在通过结构化的方法论帮助智能体执行复杂的创意任务。

## 精选技能：Moonkite-Maliang (UMPF 创意总监)

**Moonkite-Maliang** 是一个基于 **Universal Modular Prompt Framework (UMPF)** 的复杂结构化提示词生成系统。它充当 AI 创意总监，通过深度的交互式对话引导用户将模糊的想法打磨成电影级的视觉提示词，适用于 Midjourney 和 Stable Diffusion 等图像生成工具。

### 核心功能

*   **7 大专用视觉引擎**：
    *   **A. 摄影 (Photography)**：模拟胶片质感（Kodak Portra, 35mm）。
    *   **B. 印刷与平面 (Print & Graphic)**：孔版印刷 (Risograph)、半色调、扁平化设计。
    *   **C. 3D 与数字艺术 (3D & Digital)**：C4D 渲染、粘土材质、柔光。
    *   **D. 厚涂与纯艺术 (Impasto & Fine Art)**：厚油画、可见笔触。
    *   **E. 像素艺术 (Pixel Art)**：8-bit 复古美学。
    *   **F. 中国水墨 (Chinese Ink)**：水墨晕染、留白、传统纹理。
    *   **G. 定格动画 (Claymation)**：定格动画、手工细节。

*   **大师角色扮演**：系统采用世界级艺术家（如亨利·卡蒂埃-布列松、何藩）的人格和美学哲学来引导创作过程。

*   **三种创作模式**：
    1.  **手动模式**：一对一交互式问答，精细打磨细节。
    2.  **自动模式**：AI 大师自我迭代，快速生成方案。
    3.  **🧠 脑暴模式**：“创意圆桌会议”，召集多位来自不同领域的 AI 专家进行讨论和碰撞，形成独特的视觉方案。

### 如何使用

要激活 Moonkite-Maliang 技能，请在与智能体的对话中使用以下任一触发词：
*   "生成提示词"
*   "画一个..."
*   "帮我设计画面"
*   提及 "UMPF" 或 "moonkite-maliang"

智能体随后将：
1.  分析您的初始想法并推荐合适的视觉引擎。
2.  展示大师艺术家列表供您选择。
3.  进入导演问询阶段（手动、自动或脑暴模式），打磨视觉元素（主体、环境、光影、氛围）。
4.  生成高度结构化、专业且兼容主流 AI 图像生成器的提示词。

### UMPF 公式

最终输出遵循此结构化公式：
```
[Composition] + [Subject & Imperfections] + [Style Engine] + [Environment] + [Palette & Mood] + [Tech Specs]
```

## 仓库结构

*   `moonkite-maliang/`：包含 Moonkite-Maliang 技能的核心逻辑和资源。
    *   `SKILL.md`：技能逻辑、交互流程和规则的详细定义。
    *   `references/`：存储辅助数据，如大师艺术家列表。

---
*专为 Moonkite AI 社区打造。*
