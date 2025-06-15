#!/usr/bin/env python3
"""
Status check for Voice-Based Quiz Generator
"""

import os
import sys
from pathlib import Path

def check_dependencies():
    """Check all dependencies"""
    print("🔍 Checking Dependencies...")
    
    deps = {
        'streamlit': '✅ Installed',
        'speech_recognition': '✅ Installed', 
        'gtts': '✅ Installed',
        'pyaudio': '✅ Installed',
        'PyPDF2': '✅ Installed',
        'openai': '✅ Installed',
        'python_docx': '✅ Installed',
        'plotly': '✅ Installed'
    }
    
    for dep, status in deps.items():
        try:
            __import__(dep)
            print(f"  {status} {dep}")
        except ImportError:
            print(f"  ❌ Missing {dep}")

def check_environment():
    """Check environment setup"""
    print("\n⚙️  Checking Environment...")
    
    env_file = Path('.env')
    if env_file.exists():
        print("  ✅ .env file exists")
        
        with open('.env', 'r') as f:
            content = f.read()
            if 'OPENAI_API_KEY=' in content:
                if 'your_openai_api_key_here' in content:
                    print("  ⚠️  OpenAI API key not configured")
                else:
                    print("  ✅ OpenAI API key configured")
            else:
                print("  ❌ OpenAI API key not found in .env")
    else:
        print("  ❌ .env file not found")

def check_application_status():
    """Check if application is running"""
    print("\n🚀 Application Status...")
    
    # Check if Streamlit is running on port 8501
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 8501))
    sock.close()
    
    if result == 0:
        print("  ✅ Streamlit app running on http://localhost:8501")
    else:
        print("  ⚠️  Streamlit app not running")
        print("     Start with: streamlit run app.py")

def main():
    """Main status check"""
    print("🎤 Voice-Based Quiz Generator - Status Check")
    print("=" * 50)
    
    check_dependencies()
    check_environment()
    check_application_status()
    
    print("\n" + "=" * 50)
    print("📋 Quick Commands:")
    print("  Demo:     python3 demo.py")
    print("  Web App:  streamlit run app.py")
    print("  Browser:  http://localhost:8501")
    print("  GitHub:   https://github.com/reachbrt/voice-based-quiz-generator")
    
    print("\n🎉 Status check complete!")

if __name__ == "__main__":
    main()
