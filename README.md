# 🎬 ABD Screen Recorder

> Create stunning project demos with high-quality screen recording — directly in your browser.

A premium SaaS-style screen recording web application built with **Streamlit**, **HTML5**, and the **MediaRecorder API**. No desktop installs, no plugins — just open and record.

---

## ✨ Features

- **Browser-native recording** via `getDisplayMedia` API
- **30 / 60 FPS** selection
- **High / Medium / Low** quality presets (adjustable bitrate)
- **Cursor capture** toggle
- **System audio** capture toggle (Chrome / Edge)
- **Pause & Resume** recording at any time
- **Live recording timer**
- **Status indicators** — Idle / Recording / Paused
- **In-browser preview** after recording
- **Auto-named downloads** — `ABD_Recording_YYYYMMDD_HHMMSS.webm`
- **Error handling** for permissions and unsupported browsers
- **Premium dark UI** — glassmorphism, gradients, smooth animations

---

## 🛠 Technology Stack

| Layer | Technology |
|-------|-----------|
| Web framework | Python · Streamlit |
| UI/Styling | HTML5 · CSS3 · Google Fonts |
| Recording API | JavaScript MediaRecorder API |
| Screen capture | `navigator.mediaDevices.getDisplayMedia` |
| Output format | WEBM (VP8 / VP9 codec) |
| Deployment | Streamlit Community Cloud |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/abd-screen-recorder.git
cd abd-screen-recorder
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

Open `http://localhost:8501` in Chrome or Edge.

---

## 📖 Usage Guide

1. **Open the app** in Chrome or Edge (recommended).
2. **Configure settings** — choose FPS, quality, and toggles.
3. **Click Start Recording** — your browser will prompt you to share a screen, window, or tab.
4. **Select what to capture** and click Share.
5. Use **Pause / Resume** as needed during recording.
6. **Click Stop** when finished.
7. **Preview** your recording in-browser, then **Download** it.

---

## 🔐 Browser Permissions

When you click **Start Recording**, the browser asks permission to share your screen.

- You choose exactly **which screen, window, or tab** to share.
- The app never accesses your camera or microphone (unless system audio is enabled, which captures desktop audio).
- Permissions are **not stored** — you are asked each time you start a new recording.

---

## 🌐 Browser Compatibility

| Browser | Screen Recording | Audio Capture | 60 FPS |
|---------|:---:|:---:|:---:|
| Chrome 74+ | ✅ | ✅ | ✅ |
| Edge 79+ | ✅ | ✅ | ✅ |
| Firefox 66+ | ✅ | ⚠️ Partial | ✅ |
| Safari | ❌ | ❌ | ❌ |

> **Note:** Safari does not support `getDisplayMedia`. Use Chrome or Edge for full functionality.

---

## ☁️ Deploy to Streamlit Community Cloud

1. Push this repository to GitHub (see below).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in.
3. Click **New app**.
4. Select your repository, branch (`main`), and set **Main file path** to `app.py`.
5. Click **Deploy**.

Your app will be live at `https://YOUR_USERNAME-abd-screen-recorder.streamlit.app`.

---

## 🐙 GitHub Setup

```bash
# Initialize repo
git init
git add .
git commit -m "Initial release — ABD Screen Recorder v1.0"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/abd-screen-recorder.git
git branch -M main
git push -u origin main
```

---

## ⚠️ Known Browser Limitations

- **Safari**: `getDisplayMedia` is not supported — screen recording is unavailable.
- **Firefox**: System audio capture is limited and may not capture desktop audio on all OS.
- **Mobile browsers**: Screen recording via `getDisplayMedia` is not supported on iOS/Android.
- **HTTPS required**: The app must run on HTTPS (or localhost) for `getDisplayMedia` to work. Streamlit Cloud provides HTTPS automatically.
- **Output format**: Recordings are saved as `.webm`. Use a tool like [HandBrake](https://handbrake.fr) or [ffmpeg](https://ffmpeg.org) to convert to MP4 if needed.

---

## 🔮 Future Improvements

- [ ] MP4 / GIF export via server-side `ffmpeg`
- [ ] Screen annotation tools (draw, highlight)
- [ ] Webcam picture-in-picture overlay
- [ ] Cloud storage integration (Google Drive / S3)
- [ ] Shareable link generation
- [ ] Recording history & management
- [ ] Transcript / caption generation via Whisper API
- [ ] Custom watermark overlay

---

## 🧑‍💻 Skills Demonstrated

| Skill | Usage |
|-------|-------|
| **Python** | Streamlit app structure, utility helpers |
| **Streamlit** | Page config, custom components, layout |
| **JavaScript** | MediaRecorder API, state machine, timer |
| **Browser Media APIs** | `getDisplayMedia`, `MediaRecorder`, `Blob`, `URL.createObjectURL` |
| **HTML / CSS** | Glassmorphism UI, animations, responsive layout |
| **UI/UX Design** | Premium dark theme, micro-interactions, empty states |
| **Web Deployment** | Streamlit Community Cloud, GitHub Actions-ready |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">Made with ♥ by <strong>Abdul</strong></div>
