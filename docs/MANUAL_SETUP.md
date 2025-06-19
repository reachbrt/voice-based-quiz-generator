# 🚀 Manual Setup Guide - Voice-Based Quiz Generator

## Step-by-Step Instructions

### 1. Open Terminal
Open Terminal (macOS) or Command Prompt (Windows) and navigate to your project:

```bash
cd "/Users/bharat/Projects/Voice-Based Quiz Generator"
```

### 2. Push to GitHub

```bash
# Initialize git repository
git init
git branch -M main

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Voice-Based Quiz Generator

🎤 Complete AI-powered voice-based quiz system featuring:
✅ Streamlit web application
✅ Document processing (PDF, DOCX, TXT)
✅ OpenAI GPT question generation
✅ Speech recognition and text-to-speech
✅ Performance analytics and adaptive difficulty
✅ Professional documentation and CI/CD pipeline"

# Add GitHub remote
git remote add origin https://github.com/reachbrt/voice-based-quiz-generator.git

# Push to GitHub
git push -u origin main
```

### 3. Install Dependencies

```bash
# Install basic dependencies
pip3 install streamlit python-dotenv

# Or install all dependencies
pip3 install -r requirements.txt
```

### 4. Test the Demo (No API Key Required)

```bash
python3 demo.py
```

This will run an interactive demo with sample questions.

### 5. Set Up Environment for Full Application

```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your OpenAI API key
# You can use any text editor:
nano .env
# or
open .env
```

Add your OpenAI API key to the .env file:
```
OPENAI_API_KEY=your_actual_api_key_here
```

### 6. Run the Full Application

```bash
streamlit run app.py
```

The application will open in your browser at: http://localhost:8501

## 🎯 What Each Command Does

### Git Commands
- `git init` - Creates a new Git repository
- `git add .` - Adds all files to staging
- `git commit -m "..."` - Creates a commit with your changes
- `git remote add origin ...` - Links to your GitHub repository
- `git push -u origin main` - Pushes code to GitHub

### Python Commands
- `pip3 install ...` - Installs Python packages
- `python3 demo.py` - Runs the demo version
- `streamlit run app.py` - Starts the web application

## 🔧 Troubleshooting

### If Git Push Fails
```bash
# You may need to authenticate with GitHub
gh auth login

# Or set up SSH keys (recommended)
# Follow: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```

### If pip3 Not Found
```bash
# Try using python3 -m pip instead
python3 -m pip install streamlit python-dotenv
```

### If Python3 Not Found
```bash
# Try using python instead
python --version
python demo.py
```

### If Streamlit Command Not Found
```bash
# Use python3 -m streamlit instead
python3 -m streamlit run app.py
```

## 📱 Application Features

Once running, you can:

### 📄 Upload Documents
- PDF files
- Word documents (.docx)
- Text files (.txt)

### 🤖 Generate Questions
- AI-powered question creation
- Multiple difficulty levels
- Topic-focused questions

### 🎤 Voice Interaction
- Listen to questions
- Speak your answers
- Get audio feedback

### 📊 Track Performance
- Real-time analytics
- Progress tracking
- Export results

## 🌐 Repository Links

- **GitHub Repository**: https://github.com/reachbrt/voice-based-quiz-generator
- **Live Demo**: Run `python3 demo.py` locally
- **Documentation**: See README.md in the repository

## 🎉 Success Indicators

You'll know everything is working when:

1. ✅ **GitHub Repository**: Your code appears at https://github.com/reachbrt/voice-based-quiz-generator
2. ✅ **Demo Works**: `python3 demo.py` runs an interactive quiz
3. ✅ **App Starts**: `streamlit run app.py` opens a web interface
4. ✅ **Browser Opens**: Application loads at http://localhost:8501

## 📞 Quick Help

If you encounter issues:

1. **Check Python**: `python3 --version` (should be 3.8+)
2. **Check Git**: `git --version`
3. **Check Files**: `ls -la` (should show app.py, demo.py, etc.)
4. **Test Demo**: `python3 demo.py` (should work without any setup)

## 🚀 Next Steps

After successful setup:

1. **Test the demo** to see core functionality
2. **Get OpenAI API key** from https://platform.openai.com/api-keys
3. **Run full application** with voice features
4. **Upload documents** and generate custom quizzes
5. **Share your repository** as a portfolio project!

---

**Your Voice-Based Quiz Generator is ready to showcase your AI and full-stack development skills!** 🎤✨
