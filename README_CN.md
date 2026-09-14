# CineForge Skills

中文 · [English](README.md)

[![Validate](https://github.com/Laihiujin/CineForge-Skills/actions/workflows/validate.yml/badge.svg)](https://github.com/Laihiujin/CineForge-Skills/actions/workflows/validate.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**面向 AI 影视制作的专业级、模型无关 Skill 库。**

CineForge 的目标不是“写更长的 Prompt”，而是把 AI 视频制作变成真正可管理的影视生产流程。人物身份、服装、空间、灯光、道具、表演状态、镜头方向、时间状态与视觉语言都被显式记录，不依赖模型自己“记住”。

## 完整流程

`创意 Brief → 故事 → 剧本 → Canon → 人物 → 世界 → 视觉语言 → Shotlist → 参考资产 → 生成 → 连续性 → 剪辑 → 声音 → 调色 → QC → 母版`

`00-film-director` 是总控入口。你可以直接给它创意、Brief、剧本、Treatment、参考图，甚至一个已经做到一半的项目。它会判断当前阶段、缺失资产、下一步应该调用哪个专业 Skill，以及什么时候允许进入生成。

## 核心生产原则

1. **先锁 Canon，再生成。** 稳定事实进入 Bible，不靠上下文记忆。
2. **先声明状态，再写 Prompt。** 每个镜头都明确继承什么、改变什么。
3. **镜头先有任务，再谈漂亮。** 每一镜必须承担叙事、情绪、信息或节奏功能。
4. **连续性是图，不是备注。** 前后镜头之间存在人物、空间、视线、方向、时间和资产依赖。
5. **生成模型可替换。** 影视生产逻辑独立于某一家模型或平台。

详细结构、安装方式与目录见英文 `README.md`。默认建议从 `00-film-director` 开始。

## 持续迭代

CineForge Skills 将持续迭代优化。制作规则、数据结构、模板与模型适配策略会结合真实影视生产实践及生成技术演进持续更新。
