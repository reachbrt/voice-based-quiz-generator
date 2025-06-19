#!/bin/bash

# GitHub Repository Setup Script for Voice-Based Quiz Generator

echo "🎤 Voice-Based Quiz Generator - GitHub Setup"
echo "============================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're already in a git repository
if [ -d ".git" ]; then
    echo "⚠️  Git repository already exists."
    read -p "Do you want to continue? This will reset the repository. (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
    rm -rf .git
fi

# Initialize git repository
echo "📁 Initializing Git repository..."
git init

# Add all files
echo "📝 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
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

# Set main branch
git branch -M main

echo ""
echo "✅ Git repository initialized successfully!"
echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Repository name: voice-based-quiz-generator"
echo "   - Description: AI-powered voice-based quiz generator with document processing"
echo "   - Make it public or private as desired"
echo "   - Don't initialize with README (we already have one)"
echo ""
echo "2. Connect your local repository to GitHub:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/voice-based-quiz-generator.git"
echo ""
echo "3. Push to GitHub:"
echo "   git push -u origin main"
echo ""
echo "4. Set up environment:"
echo "   - Copy .env.example to .env"
echo "   - Add your OpenAI API key"
echo "   - Install dependencies: pip install -r requirements.txt"
echo ""
echo "5. Test the application:"
echo "   python demo.py  # For demo without dependencies"
echo "   streamlit run app.py  # For full application"
echo ""

# Check if GitHub CLI is available
if command -v gh &> /dev/null; then
    echo "🚀 GitHub CLI detected!"
    read -p "Do you want to create the GitHub repository automatically? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Creating GitHub repository..."
        gh repo create voice-based-quiz-generator --public --description "AI-powered voice-based quiz generator with document processing and speech recognition" --push
        echo "✅ Repository created and pushed to GitHub!"
    fi
else
    echo "💡 Tip: Install GitHub CLI (gh) for easier repository management"
fi

echo ""
echo "📚 Documentation available:"
echo "- README.md - Main documentation"
echo "- INSTALL.md - Installation guide"
echo "- CONTRIBUTING.md - Contribution guidelines"
echo ""
echo "🎉 Setup complete! Your Voice-Based Quiz Generator is ready for GitHub!"
