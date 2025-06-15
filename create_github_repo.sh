#!/bin/bash

# Script to create GitHub repository for Voice-Based Quiz Generator
# Run this script to automatically set up the repository

echo "🎤 Creating Voice-Based Quiz Generator Repository"
echo "================================================"

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py not found. Please run this script from the project directory."
    exit 1
fi

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git branch -M main
else
    echo "✅ Git repository already exists"
fi

# Add all files
echo "📝 Adding files to repository..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "Voice-Based Quiz Generator: Complete implementation

Features:
✅ Streamlit web application with intuitive UI
✅ Multi-format document processing (PDF, DOCX, TXT)
✅ AI-powered question generation using OpenAI GPT
✅ Voice interaction with speech recognition and TTS
✅ Real-time performance tracking and analytics
✅ Adaptive difficulty adjustment based on performance
✅ Session export and data management
✅ Comprehensive error handling and fallbacks

Technical Stack:
- Frontend: Streamlit
- AI: OpenAI GPT-3.5/4
- Voice: Google Speech Recognition + gTTS
- Document Processing: PyPDF2, python-docx
- Audio: pygame, streamlit-audio-recorder
- Analytics: pandas, plotly

Setup:
- Automated installation scripts
- Environment configuration
- Testing and demo capabilities
- CI/CD pipeline with GitHub Actions
- Cross-platform support (Windows, macOS, Linux)"
fi

# Check if GitHub CLI is available
if command -v gh &> /dev/null; then
    echo "🚀 GitHub CLI found! Creating repository..."
    
    # Check if already logged in
    if gh auth status &> /dev/null; then
        echo "✅ Already authenticated with GitHub"
    else
        echo "🔐 Please authenticate with GitHub..."
        gh auth login
    fi
    
    # Create repository
    echo "📦 Creating repository 'voice-based-quiz-generator'..."
    gh repo create voice-based-quiz-generator \
        --public \
        --description "🎤 AI-powered voice-based quiz generator with document processing, speech recognition, and adaptive difficulty. Built with Streamlit, OpenAI GPT, and advanced voice interaction capabilities." \
        --homepage "https://github.com/reachbrt/voice-based-quiz-generator" \
        --add-readme=false
    
    # Add remote and push
    echo "🔗 Adding remote and pushing to GitHub..."
    git remote add origin https://github.com/reachbrt/voice-based-quiz-generator.git
    git push -u origin main
    
    echo "✅ Repository created successfully!"
    echo "🌐 Repository URL: https://github.com/reachbrt/voice-based-quiz-generator"
    
else
    echo "⚠️  GitHub CLI not found. Manual setup required:"
    echo ""
    echo "1. Go to: https://github.com/new"
    echo "2. Repository name: voice-based-quiz-generator"
    echo "3. Description: 🎤 AI-powered voice-based quiz generator with document processing, speech recognition, and adaptive difficulty"
    echo "4. Make it public"
    echo "5. Don't initialize with README"
    echo "6. Create repository"
    echo ""
    echo "Then run these commands:"
    echo "git remote add origin https://github.com/reachbrt/voice-based-quiz-generator.git"
    echo "git push -u origin main"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Install dependencies: pip install -r requirements.txt"
echo "2. Copy .env.example to .env and add your OpenAI API key"
echo "3. Test with demo: python demo.py"
echo "4. Run full app: streamlit run app.py"
echo ""
echo "📚 Documentation:"
echo "- README.md - Main documentation"
echo "- INSTALL.md - Installation guide"
echo "- CONTRIBUTING.md - How to contribute"
echo ""
echo "🔧 Quick commands:"
echo "- make demo    # Run demo"
echo "- make install # Install dependencies"
echo "- make run     # Start application"
echo "- make test    # Test installation"
