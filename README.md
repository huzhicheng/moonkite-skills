# Moonkite Skills

[中文版](README_CN.md)

This repository hosts a collection of specialized skills designed for AI agents, enabling them to perform complex creative tasks with structured methodologies.

## Featured Skill: Moonkite-Maliang (UMPF 创意总监)

**Moonkite-Maliang** is a sophisticated structured prompt generation system based on the **Universal Modular Prompt Framework (UMPF)**. It acts as an AI Creative Director, guiding users through a deep, interactive dialogue to refine vague ideas into cinema-grade visual prompts for image generation tools like Midjourney and Stable Diffusion.

### Core Features

*   **7 Specialized Visual Engines**:
    *   **A. Photography**: Analog film textures (Kodak Portra, 35mm).
    *   **B. Print & Graphic**: Risograph, halftone, flat design.
    *   **C. 3D & Digital**: C4D renders, clay materials, soft lighting.
    *   **D. Impasto & Fine Art**: Thick oil painting, visible brushstrokes.
    *   **E. Pixel Art**: 8-bit retro aesthetics.
    *   **F. Chinese Ink**: Ink wash, negative space, traditional textures.
    *   **G. Claymation**: Stop motion, handcrafted details.

*   **Master Role-Playing**: The system adopts the persona and aesthetic philosophy of world-class artists (e.g., Henri Cartier-Bresson, Fan Ho) to guide the creative process.

*   **Three Creation Modes**:
    1.  **Manual Mode**: One-on-one interactive Q&A to fine-tune details.
    2.  **Auto Mode**: The AI master self-iterates to generate a plan quickly.
    3.  **🧠 Brainstorm Mode**: A "Creative Roundtable" where multiple AI experts from different fields discuss and collide ideas to form a unique visual solution.

### How to Use

To install these skills, run the following command:
```bash
npx skills add huzhicheng/moonkite-skills
```

To activate the Moonkite-Maliang skill, use any of the following triggers in your conversation with the agent:
*   "生成提示词" (Generate prompts)
*   "画一个..." (Draw a...)
*   "帮我设计画面" (Help me design a scene)
*   Mention "UMPF" or "moonkite-maliang"

The agent will then:
1.  Analyze your initial idea and recommend suitable visual engines.
2.  Present a list of master artists for you to choose from.
3.  Enter the director inquiry phase (Manual, Auto, or Brainstorm) to refine the visual elements (Subject, Environment, Lighting, Mood).
4.  Generate a highly structured, professional prompt compatible with major AI image generators.

### UMPF Formula

The final output follows this structured formula:
```
[Composition] + [Subject & Imperfections] + [Style Engine] + [Environment] + [Palette & Mood] + [Tech Specs]
```

## Repository Structure

*   `skills/moonkite-maliang/`: Contains the core logic and resources for the Moonkite-Maliang skill.
    *   `SKILL.md`: Detailed definition of the skill's logic, interaction flows, and rules.
    *   `references/`: Stores auxiliary data such as the master artist list.

## Showcase: Ancient Fairies Night Gathering

Here is an example of a cinematic prompt generated using the **Auto Mode** with **Roger Deakins** as the creative director:

**User Input:** "Ancient style group portrait, 5 beautiful fairies in a pavilion, each visible full body/face, night background, fairyland atmosphere."

**Generated Prompt:**
> **Composition/Shot**: Wide candid shot of 5 stunning ancient Chinese fairies relaxing in a bright, glowing pavilion. Action is natural and unposed: chatting, sipping tea, leaning back. 35mm lens, crystal clear focus.
>
> **Subject & Imperfections**: 5 distinct fairies with peerless, breathtaking beauty (perfect exquisite faces, porcelain skin). One fairy is wearing a magnificent, extra-long trailing skirt. All wearing pristine, colorful luxurious Hanfu. No imperfections.
>
> **Style Engine Keywords**: (Roger Deakins style), Bright and Airy, High-Key lighting, soft global illumination, ultra-detailed, flawless aesthetic.
>
> **Environment & Lighting**: A fairyland pavilion at night but brightly lit. Surroundings are filled with bioluminescent clouds, glowing jade architecture, and bright starlight. Luminous and clear.
>
> **Color & Mood**: Pastel and Bright Jewel Tones. White, Gold, Cyan, Pink, Lavender. Dreamy, divine, heavenly.
>
> --ar 16:9 --v 6.0

---
*Created for the Moonkite AI community.*
