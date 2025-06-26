# 🧠 Identify.ai – AI Forensic Sketch Generator

Generate suspect sketches from text descriptions using generative AI.

**Identify.ai** is an experimental forensic tool that converts natural language descriptions (e.g., *"a man with a beard and a scar under his right eye"*) into AI-generated facial sketches. Built with Stable Diffusion on the backend and a full-stack architecture (Flask + React), it showcases how generative models can assist in criminal investigation workflows.

---

## 🎯 Features

- 🖼️ Text-to-sketch generation using Stable Diffusion
- 🧠 Natural language input with no structured formatting required
- ⚛️ React frontend with clean, minimal UI
- 🔗 Flask backend to manage prompt handling and model inference
- 🔌 Can run on local GPU or Hugging Face-hosted models

---

## 🧰 Tech Stack

| Layer     | Stack                                      |
|-----------|---------------------------------------------|
| Backend   | Python, Flask, Stable Diffusion             |
| Frontend  | React, Tailwind CSS (optional styling)      |
| Model API | Local SD 1.5 / Hugging Face Diffusers       |

---

## 🚀 Demo Preview

<p align="center">
  <img src="https://your-demo-gif-or-img-url" width="500" alt="Identify.ai sketch demo" />
</p>

**Input:** "Bald man in his 40s with a square jaw, thick eyebrows, and a piercing look"  
**Output:** AI-generated suspect sketch

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ThomasPaulCJ/identify-ai.git
cd identify-ai
