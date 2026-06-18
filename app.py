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
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --- Load Recorder HTML Component ---
recorder_html = load_recorder_component()

# --- Hero Section ---
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">
        <span class="badge-dot"></span>
        Browser-Native Recording
    </div>
    <h1 class="hero-title">
        <span class="title-accent">ABD</span> Screen Recorder
    </h1>
    <p class="hero-subtitle">
        Create stunning project demos with high-quality screen recording.<br/>
        No installs. No plugins. Just open and record.
    </p>
    <div class="hero-stats">
        <div class="stat-item">
            <span class="stat-number">60</span>
            <span class="stat-label">FPS Support</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item">
            <span class="stat-number">4K</span>
            <span class="stat-label">Resolution</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item">
            <span class="stat-number">∞</span>
            <span class="stat-label">Duration</span>
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
