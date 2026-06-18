# 🚀 Deployment Guide — ABD Screen Recorder

---

## Local Development

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/abd-screen-recorder.git
cd abd-screen-recorder

# 2. (Optional) virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install
pip install -r requirements.txt

# 4. Run
streamlit run app.py
```

App opens at **http://localhost:8501**

> ⚠️ Use **Chrome** or **Edge** — `getDisplayMedia` requires a secure context (localhost qualifies).

---

## GitHub Setup

```bash
git init
git add .
git commit -m "feat: ABD Screen Recorder v1.0"
git remote add origin https://github.com/YOUR_USERNAME/abd-screen-recorder.git
git branch -M main
git push -u origin main
```

---

## Streamlit Community Cloud

1. Go to **https://share.streamlit.io** → sign in with GitHub.
2. Click **"New app"**.
3. Repository: `YOUR_USERNAME/abd-screen-recorder`
4. Branch: `main`
5. Main file path: `app.py`
6. Click **"Deploy!"**

Live URL: `https://YOUR_USERNAME-abd-screen-recorder-app-XXXX.streamlit.app`

### Important Cloud Notes

- Streamlit Cloud serves over **HTTPS** automatically — required for `getDisplayMedia`.
- No server resources needed for recording; all processing happens **in the browser**.
- Free tier is sufficient — the Python backend only serves the HTML component.

---

## Docker (Optional)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
docker build -t abd-screen-recorder .
docker run -p 8501:8501 abd-screen-recorder
```

---

## Updating the Deployed App

```bash
git add .
git commit -m "fix: description of change"
git push origin main
# Streamlit Cloud auto-redeploys on push
```
