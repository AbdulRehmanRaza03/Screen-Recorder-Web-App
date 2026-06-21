<div align="center">

<img src="assets/images/logo.svg" width="90" height="90" alt="ABD Screen Recorder Logo"/>

# 🎬 ABD Screen Recorder

### *Create stunning screen recordings — directly in your browser. No installs. No plugins. Just open and record.*

<br/>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-ABD_Screen_Recorder-6366f1?style=for-the-badge&logoColor=white)](https://abd-screen-recorder-web-app.streamlit.app/)
[![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live_&_Active-22c55e?style=for-the-badge)](https://abd-screen-recorder-web-app.streamlit.app/)

<br/>

> **A premium SaaS-style screen recording web application** built with Python, Streamlit, and the native browser MediaRecorder API. Designed with a dark futuristic UI — ready for portfolio showcase and real-world use.

<br/>

**[🔴 Open Live App](https://abd-screen-recorder-web-app.streamlit.app/)** &nbsp;|&nbsp; **[👨‍💻 View Portfolio](https://abdulrehmanraza03.github.io/My-Portfolio/)** &nbsp;|&nbsp; **[🐙 GitHub](https://github.com/AbdulRehmanRaza03)** &nbsp;|&nbsp; **[💼 LinkedIn](https://www.linkedin.com/in/abdul-rehman-raza-7a125b332)**

</div>

---

## 📸 Overview

**ABD Screen Recorder** is a fully browser-native screen recording application that requires zero desktop installation. Built as a premium SaaS product experience, it leverages the HTML5 `getDisplayMedia` API and `MediaRecorder` API embedded inside a polished Streamlit interface.

The app was designed and developed entirely by **Abdul Rehman Raza** as a portfolio-grade project demonstrating full-stack web development, UI/UX design, browser API integration, and cloud deployment skills.

---

## ✨ Key Features

| Feature | Details |
|---|---|
| 🖥️ **Browser Screen Capture** | Uses `getDisplayMedia` — capture any screen, window, or tab |
| ⏺️ **Start / Pause / Resume / Stop** | Full recording lifecycle control |
| ⏱️ **Live Recording Timer** | Real-time HH:MM:SS counter |
| 🎞️ **30 / 60 FPS** | Smooth or ultra-smooth recording options |
| 🎚️ **Quality Presets** | High / Medium / Low bitrate selection |
| 🖱️ **Cursor Capture Toggle** | Include or hide mouse cursor |
| 🔊 **System Audio Toggle** | Capture desktop audio (Chrome/Edge) |
| 💾 **Auto-Named Downloads** | Files named `ABD_Recording_YYYYMMDD_HHMMSS.webm` |
| 👁️ **In-Browser Preview** | Review your recording before downloading |
| ⚠️ **Error Handling** | Graceful errors for permissions & unsupported browsers |
| 📱 **Responsive Design** | Works on desktop, tablet, and laptop viewports |
| 🌑 **Premium Dark UI** | Glassmorphism, gradients, glow animations |

---

## 🏗️ How It Works — Architecture Deep Dive

```
┌─────────────────────────────────────────────────────────┐
│                    User's Browser                        │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │           Streamlit Python App (app.py)          │   │
│  │                                                  │   │
│  │  • Renders page layout & hero section            │   │
│  │  • Loads external CSS (assets/styles.css)        │   │
│  │  • Injects HTML component via st.components.v1   │   │
│  └──────────────────────┬───────────────────────────┘   │
│                         │ st.components.v1.html()        │
│  ┌──────────────────────▼───────────────────────────┐   │
│  │      recorder_component.html (iframe)             │   │
│  │                                                   │   │
│  │  ┌──────────────────────────────────────────┐    │   │
│  │  │         JavaScript Engine                 │    │   │
│  │  │                                           │    │   │
│  │  │  getDisplayMedia()  ──►  MediaStream      │    │   │
│  │  │  MediaRecorder()    ──►  Blob chunks      │    │   │
│  │  │  URL.createObjectURL() ─► Download link   │    │   │
│  │  └──────────────────────────────────────────┘    │   │
│  │                                                   │   │
│  │  CSS: Glassmorphism cards, glow animations        │   │
│  │  State Machine: idle → recording → paused → done  │   │
│  └───────────────────────────────────────────────────┘   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Step-by-Step Data Flow

```
1. User clicks "Start Recording"
        │
        ▼
2. JS calls navigator.mediaDevices.getDisplayMedia()
        │
        ▼
3. Browser shows native screen-share permission dialog
        │
        ▼
4. User selects screen / window / tab → grants permission
        │
        ▼
5. MediaStream created with chosen FPS + cursor settings
        │
        ▼
6. MediaRecorder starts → collects Blob chunks every 250ms
        │
        ▼
7. Timer ticks, status indicator animates (● Recording)
        │
        ▼
8. User clicks Stop → MediaRecorder.stop() fires
        │
        ▼
9. All Blob chunks assembled → single video/webm Blob
        │
        ▼
10. URL.createObjectURL() → preview <video> + download link
        │
        ▼
11. User previews in-browser, clicks Download
        │
        ▼
12. Auto-named .webm file saved to user's device
```

---

## 🛠️ Technology Stack

```
Backend / Framework
├── Python 3.10+
└── Streamlit 1.32+        → Web framework & component host

Frontend (Embedded Component)
├── HTML5                  → Structure & iframe component
├── CSS3                   → Glassmorphism, gradients, animations
├── JavaScript (ES2020)    → Recording logic & state machine
├── MediaRecorder API      → Video encoding & chunk collection
├── getDisplayMedia API    → Screen / window / tab capture
└── Blob + URL API         → In-memory file handling & download

Fonts & Design
├── Inter (Google Fonts)   → Body typography
└── Space Grotesk          → Headings & display text

Deployment
├── Streamlit Community Cloud  → Hosting (HTTPS auto-configured)
└── GitHub                     → Version control & CI trigger
```

---

## 📁 Project Structure

```
abd-screen-recorder/
│
├── app.py                          # Main Streamlit application entry point
│                                   # Hero section, layout, footer
│
├── components/
│   ├── __init__.py
│   └── recorder_component.html     # Self-contained recording UI
│                                   # (HTML + CSS + JavaScript in one file)
│
├── assets/
│   ├── styles.css                  # Global premium dark theme styles
│   └── images/
│       └── logo.svg                # App logo (SVG, theme-compatible)
│
├── utils/
│   ├── __init__.py
│   └── helpers.py                  # Component loader + app config
│
├── .streamlit/
│   ├── config.toml                 # Theme colours, server settings
│   └── secrets.toml                # (gitignored) Cloud secrets stub
│
├── requirements.txt                # Python dependencies (streamlit only)
├── pyproject.toml                  # Project metadata
├── DEPLOYMENT.md                   # Full local + cloud deploy guide
├── README.md                       # This file
├── LICENSE                         # MIT License
└── .gitignore                      # Python, venv, secrets, video files
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Google Chrome or Microsoft Edge (for screen recording)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/AbdulRehmanRaza03/abd-screen-recorder.git
cd abd-screen-recorder

# 2. (Recommended) Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
```

Open **http://localhost:8501** in Chrome or Edge and start recording.

---

## 📖 Usage Guide

```
Step 1 → Configure Settings
         Choose FPS (30 or 60), quality preset, cursor and audio toggles

Step 2 → Click "Start Recording"
         Browser prompts you to choose a screen, window, or browser tab

Step 3 → Select what to share → Click "Share"
         Recording begins immediately — live timer starts ticking

Step 4 → Pause / Resume as needed
         Click Pause to temporarily halt, Resume to continue

Step 5 → Click "Stop" when done
         In-browser preview appears automatically

Step 6 → Click "Download"
         File saved as ABD_Recording_YYYYMMDD_HHMMSS.webm
```

---

## 🌐 Browser Compatibility

| Browser | Screen Recording | System Audio | 60 FPS |
|:--------|:---:|:---:|:---:|
| ✅ Chrome 74+ | ✅ | ✅ | ✅ |
| ✅ Edge 79+ | ✅ | ✅ | ✅ |
| ⚠️ Firefox 66+ | ✅ | ⚠️ Limited | ✅ |
| ❌ Safari | ❌ Not Supported | ❌ | ❌ |
| ❌ Mobile Browsers | ❌ Not Supported | ❌ | ❌ |

> **Why Chrome/Edge?** The `getDisplayMedia` API requires a secure context (HTTPS or localhost) and is most fully implemented in Chromium-based browsers.

---

## ☁️ Deployment

### Live App
**[https://abd-screen-recorder-web-app.streamlit.app/](https://abd-screen-recorder-web-app.streamlit.app/)**

### Deploy Your Own — Streamlit Community Cloud

```
1. Push this repo to GitHub
2. Visit https://share.streamlit.io → New App
3. Repository: AbdulRehmanRaza03/abd-screen-recorder
4. Branch: main
5. Main file: app.py
6. Click Deploy → Done ✅
```

> Streamlit Cloud provides HTTPS automatically — required for `getDisplayMedia` to function in production.

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for Docker and advanced options.

---

## ⚠️ Known Limitations

- **Safari** — `getDisplayMedia` is not supported; users must use Chrome or Edge
- **Mobile** — Screen recording via `getDisplayMedia` is unavailable on iOS and Android
- **Output format** — Recordings export as `.webm`. Convert to `.mp4` using [ffmpeg](https://ffmpeg.org) or [HandBrake](https://handbrake.fr)
- **System audio** — Availability depends on OS and browser; most reliable on Windows with Chrome

---

## 🔮 Roadmap & Future Features

- [ ] MP4 / GIF export via server-side `ffmpeg` processing
- [ ] Webcam picture-in-picture overlay
- [ ] Screen annotation tools (draw, highlight, zoom)
- [ ] Cloud upload (Google Drive / S3)
- [ ] Auto-generated captions via OpenAI Whisper
- [ ] Shareable link generation
- [ ] Recording history dashboard
- [ ] Custom watermark / branding overlay

---

## 🧑‍💻 Skills Demonstrated

This project was built to showcase a professional skill set across multiple disciplines:

| Skill Area | What Was Applied |
|:-----------|:----------------|
| **Python** | Streamlit app architecture, utility modules, clean code structure |
| **Streamlit** | `st.components.v1`, custom theming, `config.toml`, responsive layout |
| **JavaScript** | MediaRecorder state machine, async API calls, Blob handling, DOM manipulation |
| **Browser APIs** | `getDisplayMedia`, `MediaRecorder`, `Blob`, `URL.createObjectURL`, stream management |
| **HTML5 / CSS3** | Glassmorphism design, CSS animations, keyframes, responsive grid |
| **UI/UX Design** | Dark premium theme, micro-interactions, empty states, error feedback |
| **Web Deployment** | Streamlit Cloud, HTTPS requirements, GitHub integration |
| **Software Architecture** | Component separation, helper utilities, clean folder structure |

---

## 🌟 More Projects

| Project | Description | Link |
|:--------|:-----------|:-----|
| 🎬 **ABD Screen Recorder** | This project — browser-native screen recorder | [Live](https://abd-screen-recorder-web-app.streamlit.app/) |
| 📊 **Customer Churn Prediction** | ML / Data Science — predictive analytics dashboard | [Live](https://customer-churn-prediction-analytics-5syak8uuar5rp4f8ihphvs.streamlit.app/) |
| 👗 **ABD Wears Website** | E-commerce fashion website | [Live](https://abdulrehmanraza03.github.io/ABD-Wears-Weabsite/#/) |
| 🍕 **FFC Pizza Restaurant** | Restaurant website with full menu | [Live](https://abdulrehmanraza03.github.io/FFC_Pizza_Restaurent/) |
| 🛠️ **The Abdul Service** | Services & collections platform | [Live](https://replit-tool--theabdulservice.replit.app/#collections) |

---

## 👨‍💻 About the Developer

<div align="center">

### Abdul Rehman Raza

*Full Stack Developer · Data Science Enthusiast · UI/UX Designer*

I build clean, functional, and visually polished web applications — from interactive data science dashboards to premium SaaS-style tools. Passionate about turning ideas into production-ready products.

<br/>

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-Visit_Site-6366f1?style=for-the-badge)](https://abdulrehmanraza03.github.io/My-Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-AbdulRehmanRaza03-181717?style=for-the-badge&logo=github)](https://github.com/AbdulRehmanRaza03)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdul_Rehman_Raza-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/abdul-rehman-raza-7a125b332)
[![Email](https://img.shields.io/badge/Email-abdulrehmanraza60@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdulrehmanraza60@gmail.com)
[![Phone](https://img.shields.io/badge/WhatsApp-+92_318_1678758-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/923181678758)

</div>

---

## 📄 License

```
MIT License — Copyright (c) 2024 Abdul Rehman Raza

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, subject to the above copyright notice appearing in all copies.
```

See [LICENSE](LICENSE) for full terms.

---

<div align="center">

**⭐ If this project helped you or impressed you, please star the repository!**

<br/>

*Made with* ♥ *by* **Abdul Rehman Raza** *— Pakistan 🇵🇰*

<br/>

[![Live App](https://img.shields.io/badge/🔴_Live_Now-abd--screen--recorder-6366f1?style=for-the-badge)](https://abd-screen-recorder-web-app.streamlit.app/)

</div>
