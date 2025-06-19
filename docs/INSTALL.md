# Installation Guide

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- OpenAI API key

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/voice-based-quiz-generator.git
cd voice-based-quiz-generator
```

### 2. Install Dependencies
```bash
# Option 1: Using pip
pip install -r requirements.txt

# Option 2: Using the setup script
python setup.py

# Option 3: Using Make (if available)
make install
```

### 3. Configure Environment
```bash
# Copy the environment template
cp .env.example .env

# Edit .env file and add your OpenAI API key
# OPENAI_API_KEY=your_actual_api_key_here
```

### 4. Test Installation
```bash
# Run the test script
python test_installation.py

# Or try the demo (no API key required)
python demo.py
```

### 5. Run the Application
```bash
# Start the Streamlit app
streamlit run app.py

# Or use Make
make run
```

## Troubleshooting

### Common Issues

#### PyAudio Installation Error
```bash
# macOS
brew install portaudio
pip install pyaudio

# Ubuntu/Debian
sudo apt-get install portaudio19-dev
pip install pyaudio

# Windows
pip install pipwin
pipwin install pyaudio
```

#### OpenAI API Issues
- Ensure your API key is valid and has credits
- Check that the key is properly set in the .env file
- Verify network connectivity

#### Microphone/Audio Issues
- Check browser permissions for microphone access
- Ensure audio devices are properly connected
- Try refreshing the browser page

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB for dependencies
- **Internet**: Required for OpenAI API and speech services

### Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Features Overview

- 📄 **Document Processing**: Upload PDF, DOCX, TXT files
- 🤖 **AI Question Generation**: GPT-powered quiz creation
- 🎤 **Voice Interaction**: Speech recognition and text-to-speech
- 📊 **Performance Tracking**: Analytics and progress monitoring
- 🎯 **Adaptive Difficulty**: Dynamic difficulty adjustment
- 💾 **Export Results**: Download quiz data and statistics

## Getting Help

1. Check the [README.md](README.md) for detailed documentation
2. Run `python demo.py` to try the system without full setup
3. Use `python test_installation.py` to diagnose issues
4. Check the [Issues](https://github.com/yourusername/voice-based-quiz-generator/issues) page on GitHub
