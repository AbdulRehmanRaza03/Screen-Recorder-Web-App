"""
ABD Screen Recorder - Main Application
Author: Abdul
A premium SaaS-style screen recording application built with Streamlit.
"""

import streamlit as st
import os
from helpers import load_recorder_component, get_app_config

# --- Page Configuration ---
st.set_page_config(
    page_title="ABD Screen Recorder",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
) 

# --- Load External CSS ---
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

config = get_app_config()

# --- App Banner ---
st.markdown(f"""
<div class="page-hero">
  <div class="hero-copy">
    <div class="hero-pill">Premium browser screen recorder</div>
    <h1 class="hero-title"><span class="title-accent">ABD</span> Screen Recorder</h1>
    <p class="hero-description">Record your screen directly from the browser, export in high-quality WEBM, and share polished demos instantly.</p>
    <div class="hero-actions">
      <span>Chrome & Edge ready</span>
      <span>{config['output_format']} export</span>
      <span>{config['version']} release</span>
    </div>
  </div>
  <div class="hero-highlight">
    <div class="highlight-card">
      <strong>Why choose ABD?</strong>
      <p>Fast start, clean UI, lightweight recording, and instant download support without extra plugins.</p>
    </div>
    <div class="highlight-grid">
      <div class="highlight-item"><strong>60 FPS</strong><span>Smooth motion</span></div>
      <div class="highlight-item"><strong>High Quality</strong><span>4K ready</span></div>
      <div class="highlight-item"><strong>Easy Share</strong><span>Instant capture</span></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Load Recorder HTML Component ---
recorder_html = load_recorder_component()

# --- Recorder Card ---
st.markdown('<div class="recorder-wrapper">', unsafe_allow_html=True)
st.components.v1.html(recorder_html, height=780, scrolling=False)
st.markdown('</div>', unsafe_allow_html=True)

# --- How It Works Section ---
st.markdown("""
<div class="how-section">
    <div class="section-header">
      <h2>How It Works</h2>
      <p>Follow these steps to capture your next screen recording in seconds.</p>
    </div>
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-icon">⚙️</div>
            <div class="step-number">01</div>
            <h3>Configure Settings</h3>
            <p>Choose FPS, quality, and cursor options then hit start.</p>
        </div>
        <div class="step-card">
            <div class="step-icon">🖥️</div>
            <div class="step-number">02</div>
            <h3>Select Screen</h3>
            <p>Pick a full screen, window, or browser tab to capture.</p>
        </div>
        <div class="step-card">
            <div class="step-icon">⏺️</div>
            <div class="step-number">03</div>
            <h3>Record & Pause</h3>
            <p>Pause and resume recording with smooth browser controls.</p>
        </div>
        <div class="step-card">
            <div class="step-icon">💾</div>
            <div class="step-number">04</div>
            <h3>Download</h3>
            <p>Save your screen demo instantly as a high-quality WEBM file.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Main Recorder Component ---
st.markdown('<div class="recorder-wrapper">', unsafe_allow_html=True)
st.components.v1.html(recorder_html, height=780, scrolling=False)
st.markdown('</div>', unsafe_allow_html=True)

# --- How It Works Section ---
st.markdown("""
<div class="how-section">
    <h2 class="section-title">How It Works</h2>
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-icon">⚙️</div>
            <div class="step-number">01</div>
            <h3>Configure Settings</h3>
            <p>Choose your FPS, quality level, and cursor visibility preferences before recording.</p>
        </div>
        <div class="step-card">
            <div class="step-icon">🖥️</div>
            <div class="step-number">02</div>
            <h3>Select Screen</h3>
            <p>Click Start Recording and choose which screen, window, or tab to capture.</p>
        </div>
        <div class="step-card">
            <div class="step-icon">⏺️</div>
            <div class="step-number">03</div>
            <h3>Record & Pause</h3>
            <p>Record your screen with live timer feedback. Pause and resume anytime you need.</p>
        </div>
        <div class="step-card">
            <div class="step-icon">💾</div>
            <div class="step-number">04</div>
            <h3>Download</h3>
            <p>Stop and instantly download your recording as a high-quality WEBM file.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Browser Compatibility Notice ---
st.markdown("""
<div class="notice-section">
    <div class="notice-card">
        <div class="notice-icon">💡</div>
        <div class="notice-content">
            <h4>Browser Compatibility</h4>
            <p>For the best experience, use <strong>Google Chrome</strong> or <strong>Microsoft Edge</strong>. 
            Firefox supports screen recording with some limitations. Safari currently does not support 
            the <code>getDisplayMedia</code> API required for screen capture.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-brand">
            <span class="footer-logo">🎬</span>
            <span class="footer-name">ABD Screen Recorder</span>
        </div>
        <div class="footer-divider">|</div>
        <div class="footer-credit">
            Made with <span class="heart">♥</span> by <strong>Abdul</strong>
        </div>
        <div class="footer-divider">|</div>
        <div class="footer-tech">
            Built with Streamlit & Browser Media APIs
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
