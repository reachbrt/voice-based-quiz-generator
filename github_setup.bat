@echo off
REM GitHub Repository Setup Script for Voice-Based Quiz Generator (Windows)

echo 🎤 Voice-Based Quiz Generator - GitHub Setup
echo =============================================

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed. Please install Git first.
    pause
    exit /b 1
)

REM Check if we're already in a git repository
if exist ".git" (
    echo ⚠️  Git repository already exists.
    set /p "continue=Do you want to continue? This will reset the repository. (y/N): "
    if /i not "%continue%"=="y" (
        echo Aborted.
        pause
        exit /b 1
    )
    rmdir /s /q .git
)

REM Initialize git repository
echo 📁 Initializing Git repository...
git init

REM Add all files
echo 📝 Adding files to Git...
git add .

REM Create initial commit
echo 💾 Creating initial commit...
git commit -m "Initial commit: Voice-Based Quiz Generator

Features:
- Streamlit web application for voice-based quizzes
- Document processing (PDF, DOCX, TXT)
- AI-powered question generation using OpenAI GPT
- Speech recognition and text-to-speech
- Performance tracking and analytics
- Adaptive difficulty adjustment
- Export capabilities

Components:
- Main application (app.py)
- Document processor
- Question generator
- Voice handler
- Quiz manager
- Configuration management
- Setup and testing scripts"

REM Set main branch
git branch -M main

echo.
echo ✅ Git repository initialized successfully!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub:
echo    - Go to https://github.com/new
echo    - Repository name: voice-based-quiz-generator
echo    - Description: AI-powered voice-based quiz generator with document processing
echo    - Make it public or private as desired
echo    - Don't initialize with README (we already have one)
echo.
echo 2. Connect your local repository to GitHub:
echo    git remote add origin https://github.com/YOUR_USERNAME/voice-based-quiz-generator.git
echo.
echo 3. Push to GitHub:
echo    git push -u origin main
echo.
echo 4. Set up environment:
echo    - Copy .env.example to .env
echo    - Add your OpenAI API key
echo    - Install dependencies: pip install -r requirements.txt
echo.
echo 5. Test the application:
echo    python demo.py  # For demo without dependencies
echo    streamlit run app.py  # For full application
echo.

REM Check if GitHub CLI is available
gh --version >nul 2>&1
if not errorlevel 1 (
    echo 🚀 GitHub CLI detected!
    set /p "create_repo=Do you want to create the GitHub repository automatically? (y/N): "
    if /i "%create_repo%"=="y" (
        echo Creating GitHub repository...
        gh repo create voice-based-quiz-generator --public --description "AI-powered voice-based quiz generator with document processing and speech recognition" --push
        echo ✅ Repository created and pushed to GitHub!
    )
) else (
    echo 💡 Tip: Install GitHub CLI (gh) for easier repository management
)

echo.
echo 📚 Documentation available:
echo - README.md - Main documentation
echo - INSTALL.md - Installation guide
echo - CONTRIBUTING.md - Contribution guidelines
echo.
echo 🎉 Setup complete! Your Voice-Based Quiz Generator is ready for GitHub!
pause
