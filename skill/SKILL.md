---
name: wasr-repo
version: 1.0.0
description: wasr 仓库：9 个文件，主语言Python 2，Shell 1，JSON 1
trigger_conditions:
  - 需要理解、修改或排障 wasr 的代码
  - 在 wasr 里定位入口、数据表、对外契约或构建方式
---

# wasr 仓库技能

> 由仓库实际内容生成的骨架（README/目录/模型定义/契约/构建脚本逐项取证）。新增判断与坑位请直接在下面对应小节补充。

## 定位

- 远端：`https://github.com/yumoqing/wasr.git`
- 默认分支：`main`（共 2 个提交）
- 最近提交：2026-11-03 `961bc90` chore: 忽略构建/测试临时文件
- 规模：9 个文件；Python 2，Shell 1，JSON 1

## 目录结构

- `conf/` — 配置（`config.json`；密码为 AES 密文）（1 个文件）
- 根文件：`.gitignore`、`requirements.txt`、`run.sh`、`test.wav`、`test_en_1_ref_short.wav`、`test_zh_1_ref_short.wav`、`zmq_client.py`、`zmq_whisper.py`

## 代码入口（顶层 Python）

- `zmq_client.py`
- `zmq_whisper.py`

## 构建与运行

- `requirements.txt`：2 项（git+https://git.kaiyuancloud.cn/yumoqing/apppublic、openai-whisper）

