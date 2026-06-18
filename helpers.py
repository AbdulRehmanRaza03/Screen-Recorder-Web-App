"""
ABD Screen Recorder — Helper Utilities
Author: Abdul
"""

import os


def load_recorder_component() -> str:
    """
    Load and return the HTML recorder component as a string.
    Falls back to an inline error message if the file is missing.
    """
    component_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "components",
        "recorder_component.html",
    )

    if not os.path.exists(component_path):
        return (
            "<div style='color:#ef4444;padding:24px;font-family:monospace'>"
            "❌ recorder_component.html not found at: "
            + component_path
            + "</div>"
        )

    with open(component_path, "r", encoding="utf-8") as f:
        return f.read()


def get_app_config() -> dict:
    """
    Return static application configuration used across the app.
    """
    return {
        "app_name": "ABD Screen Recorder",
        "version": "1.0.0",
        "author": "Abdul",
        "description": "Premium browser-based screen recorder built with Streamlit.",
        "supported_browsers": ["Chrome 74+", "Edge 79+", "Firefox 66+"],
        "output_format": "WEBM",
        "fps_options": [30, 60],
        "quality_options": ["high", "medium", "low"],
    }
