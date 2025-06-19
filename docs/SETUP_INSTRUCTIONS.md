# 🚀 Complete Setup Instructions

## Step 1: Create GitHub Repository

**The GitHub new repository page is now open in your browser.**

Fill in the following details:

### Repository Settings:
- **Repository name**: `voice-based-quiz-generator`
- **Description**: `🎤 AI-powered voice-based quiz generator with document processing, speech recognition, and adaptive difficulty. Built with Streamlit, OpenAI GPT, and advanced voice interaction capabilities.`
- **Visibility**: ✅ Public (recommended for portfolio)
- **Initialize repository**: 
  - ❌ Do NOT check "Add a README file"
  - ❌ Do NOT add .gitignore
  - ❌ Do NOT choose a license
  
  (We already have all these files)

### Click "Create repository"

## Step 2: Set Up Local Repository

Open Terminal/Command Prompt in your project directory and run:

```bash
# Navigate to project directory
cd "/Users/bharat/Projects/Voice-Based Quiz Generator"

# Initialize git repository
git init
git branch -M main

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Voice-Based Quiz Generator

🎤 Complete AI-powered voice-based quiz system with:
✅ Streamlit web application
✅ Document processing (PDF, DOCX, TXT)
✅ OpenAI GPT question generation
✅ Speech recognition & text-to-speech
✅ Performance tracking & analytics
✅ Adaptive difficulty adjustment
✅ Session export capabilities
✅ Comprehensive documentation & CI/CD"

# Connect to GitHub (replace with your actual repository URL)
git remote add origin https://github.com/reachbrt/voice-based-quiz-generator.git

# Push to GitHub
git push -u origin main
```

## Step 3: Install Dependencies and Run Locally

### Option A: Quick Setup
```bash
# Install basic dependencies
pip3 install streamlit python-dotenv

# Run demo (no API key required)
python3 demo.py
```

### Option B: Full Setup
```bash
# Install all dependencies
pip3 install -r requirements.txt

# Set up environment
cp .env.example .env

# Edit .env file and add your OpenAI API key:
# OPENAI_API_KEY=your_actual_api_key_here

# Test installation
python3 test_installation.py

# Run full application
streamlit run app.py
```

### Option C: Using Make (if available)
```bash
make install    # Install dependencies
make setup      # Full setup
make demo       # Run demo
make run        # Start application
make test       # Test installation
```

## Step 4: Test the Application

### Demo Mode (No Dependencies)
```bash
python3 demo.py
```
This runs a sample quiz without requiring any external dependencies or API keys.

### Full Application
```bash
streamlit run app.py
```
This starts the complete application with all features.

## Step 5: Verify GitHub Repository

After pushing, your repository should be available at:
**https://github.com/reachbrt/voice-based-quiz-generator**

### Repository Features:
✅ Complete source code
✅ Comprehensive documentation
✅ Installation guides
✅ Demo capabilities
✅ CI/CD pipeline
✅ Issue templates
✅ Contributing guidelines
✅ MIT License

## Troubleshooting

### Common Issues:

#### 1. Git Not Found
```bash
# Install Git first
# macOS: Install Xcode Command Line Tools
xcode-select --install

# Or install Git from https://git-scm.com/
```

#### 2. Python Dependencies
```bash
# If pip3 not found, try:
python3 -m pip install streamlit

# For PyAudio issues on macOS:
brew install portaudio
pip3 install pyaudio
```

#### 3. OpenAI API Key
- Get your API key from: https://platform.openai.com/api-keys
- Add it to the .env file: `OPENAI_API_KEY=your_key_here`

#### 4. Streamlit Issues
```bash
# If streamlit command not found:
python3 -m streamlit run app.py
```

## Quick Commands Reference

```bash
# Repository setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/reachbrt/voice-based-quiz-generator.git
git push -u origin main

# Application setup
pip3 install -r requirements.txt
cp .env.example .env
# Edit .env with your OpenAI API key

# Run application
python3 demo.py              # Demo mode
streamlit run app.py         # Full application
python3 test_installation.py # Test setup
```

## Next Steps

1. **Test the demo**: `python3 demo.py`
2. **Get OpenAI API key**: https://platform.openai.com/api-keys
3. **Install full dependencies**: `pip3 install -r requirements.txt`
4. **Run the application**: `streamlit run app.py`
5. **Share your repository**: Add it to your portfolio!

## Repository URL
Once created: **https://github.com/reachbrt/voice-based-quiz-generator**

---

🎉 **Your Voice-Based Quiz Generator is ready!**

This is a complete, production-ready application with professional documentation, testing, and deployment capabilities. Perfect for showcasing your AI and full-stack development skills!
