# 🧠 Identify.ai – AI Forensic Sketch Generator

Generate suspect sketches from natural language descriptions using Stable Diffusion.

**Identify.ai** is an experimental forensic tool that converts descriptive text (e.g., *“a tall man with a beard and a scar on his left cheek”*) into AI-generated facial sketches. Powered by Stable Diffusion on the backend and a full-stack integration with Flask and React, it simulates how generative AI could assist in law enforcement investigations.

> ⚠️ **Note:** The full Stable Diffusion integration logic is not included in this public version. This repo is for UI/API structure and educational reference only.


---

## 🎯 Features

- 🖼️ Convert plain-text descriptions into realistic facial sketches
- 🧠 Utilizes Stable Diffusion for generative image synthesis
- 🔗 Flask backend for prompt handling and model inference
- ⚛️ React frontend with intuitive input/output interface
- 🔌 Local or hosted model compatibility (Diffusers or Hugging Face)

---

## 🧰 Tech Stack

| Layer         | Tools Used                             |
|---------------|----------------------------------------|
| Backend       | Python · Flask · Diffusers (Stable Diffusion) |
| Frontend      | React · Tailwind CSS (optional)        |
| Model Hosting | Local SD 1.5 / Hugging Face API        |
| Integration   | REST APIs (Flask ↔ SD ↔ React)         |

---

## 🚀 Demo Preview

<p align="center">
  <img src="https://github.com/manu-mathew1/Identify.ai--AI_Forensic_Sketch_Generator/blob/master/demo_preview/demo_preview.jpg" width="500" alt="Identify.ai demo preview" />
</p>

**Input:**  
`"Generate a detailed AI-assisted forensic sketch of a young adult male suspect, approximately in his early 30s. The subject has straight black hair, short in length and combed slightly forward, with a soft part near the center. The face is oval-shaped with a smooth forehead and well-defined cheekbones. Emphasize low-set, straight eyebrows and narrow, almond-shaped eyes with a calm, neutral gaze. The nose is straight with a moderately narrow bridge and defined nostrils.
The lips are medium in fullness, closed, and expressionless, forming a straight line. The jawline is angular but not overly sharp, with a subtle chin cleft and no facial hair. Ears are average in size and clearly visible. Render the sketch in high-contrast grayscale, using realistic shading to highlight facial structure—especially around the eyes, nose bridge, and jaw. Maintain a front-facing pose with no background elements, following traditional forensic standards but with subtle emphasis on distinctive traits to support witness memory and recognition accuracy."`

**Output:**  

<p align="center">
  <img src="https://github.com/manu-mathew1/Identify.ai--AI_Forensic_Sketch_Generator/blob/master/demo_preview/output_image.png" width="300" alt="Identify.ai demo preview" />
</p>

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/manu-mathew1/Identify.ai--AI_Forensic_Sketch_Generator.git
cd identify-ai
```
### 2. Backend Setup (Flask + Stable Diffusion)
```bash
cd backend
pip install -r requirements.txt
```
Configure your app.py to connect with:

Local Stable Diffusion pipeline (e.g., Diffusers)

Or remote inference API (e.g., Hugging Face endpoint)

Then, start the server:

```bash
python app.py
```
### 3. Frontend Setup (React)
```bash
cd frontend
npm install
npm start
Frontend should run on: http://localhost:3000
```

## 🔧 System Architecture

```text
[ Text Input ]
      ↓
[ Flask Backend ]
  ↳ Calls Stable Diffusion Model
      ↓
[ AI Sketch Output ]
      ↓
[ React Frontend Display ]
```
## 🔮 Future Improvements

☑ Prompt history / sketch log UI

🎨 Realism toggle: sketch vs semi-photorealistic

🧠 Trait tags (e.g., glasses, scars, beard toggles)

🌍 Multi-language input support (e.g., Malayalam, Hindi, Spanish)

⚡ Inference speedup with ONNX or optimized SD engines

## 🤝 Contributing

Got improvements in image quality, UI/UX, or prompt parsing?
Open a PR or drop your ideas in an issue. All contributions welcome.

## 👥 Contributors & Ownership

This project was collaboratively developed and maintained by:

- [**Manu Mathew**](https://github.com/manu-mathew1)  
- [**Thomas Paul C J**](https://github.com/thomaspaulcj)  
- [**Nayif Nazar**](https://github.com/MrNayif)  
- [**Vidhusankar C H**](https://github.com/vidhusankar-hozo)

All four contributors share equal ownership and recognition for the design, development, and vision of Identify.ai.

Please credit **all authors** when referencing, reusing, or building upon this project.


## 📄 License

This project is licensed under the MIT License.

Note: Stable Diffusion and third-party models have their own licenses. Please review and comply with them before use.

## ⚠️ Disclaimer

This tool is for educational and experimental purposes only. It is not intended for real-world forensic use or as a law enforcement utility.

> ⚠️ **Important Notice**  
> This project is protected under copyright.  
> Do **NOT** copy, reuse, deploy, or distribute any part of this codebase without explicit permission.  
> All rights reserved © 2025 Manu Mathew, Thomas Paul CJ, Nayif Nazar, and Vidhusankar CH.
