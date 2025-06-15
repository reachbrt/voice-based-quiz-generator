#!/usr/bin/env python3
"""
Setup script for Voice-Based Quiz Generator
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        print("\n📝 Creating .env file from template...")
        with open(env_example, 'r') as src, open(env_file, 'w') as dst:
            dst.write(src.read())
        print("✅ .env file created")
        print("⚠️  Please edit .env file and add your OpenAI API key")
        return True
    elif env_file.exists():
        print("✅ .env file already exists")
        return True
    else:
        print("❌ .env.example not found")
        return False

def install_dependencies():
    """Install Python dependencies"""
    commands = [
        ("pip install --upgrade pip", "Upgrading pip"),
        ("pip install -r requirements.txt", "Installing Python dependencies")
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    return True

def check_openai_key():
    """Check if OpenAI API key is configured"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key and api_key != 'your_openai_api_key_here':
            print("✅ OpenAI API key is configured")
            return True
        else:
            print("⚠️  OpenAI API key not configured")
            print("Please edit .env file and add your OpenAI API key")
            return False
    except ImportError:
        print("⚠️  Cannot check OpenAI API key (python-dotenv not installed)")
        return False

def main():
    """Main setup function"""
    print("🎤 Voice-Based Quiz Generator Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if not install_dependencies():
        print("\n❌ Setup failed during dependency installation")
        print("Please check the error messages above and try again")
        sys.exit(1)
    
    # Check OpenAI configuration
    print("\n🔑 Checking configuration...")
    check_openai_key()
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Edit .env file and add your OpenAI API key if not done already")
    print("2. Run: streamlit run app.py")
    print("3. Open your browser to the provided URL")
    
    print("\nFor troubleshooting, see README.md")

if __name__ == "__main__":
    main()
