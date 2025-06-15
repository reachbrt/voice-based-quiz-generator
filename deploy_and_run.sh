#!/bin/bash

# Complete deployment and run script for Voice-Based Quiz Generator
# This script will push to GitHub and run the application locally

echo "🎤 Voice-Based Quiz Generator - Deploy & Run"
echo "============================================="

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py not found. Please run this script from the project directory."
    echo "Current directory: $(pwd)"
    echo "Expected directory: /Users/bharat/Projects/Voice-Based Quiz Generator"
    exit 1
fi

echo "✅ Found project files in: $(pwd)"

# Step 1: Git Setup and Push to GitHub
echo ""
echo "📦 Step 1: Setting up Git repository..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "🔧 Initializing Git repository..."
    git init
    git branch -M main
else
    echo "✅ Git repository already exists"
fi

# Add all files
echo "📝 Adding files to Git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "ℹ️  No new changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "Voice-Based Quiz Generator: Complete Implementation

🎤 AI-Powered Voice-Based Quiz System

✨ Features:
• Streamlit web application with intuitive UI
• Multi-format document processing (PDF, DOCX, TXT)
• OpenAI GPT-powered question generation
• Voice interaction with speech recognition and TTS
• Real-time performance tracking and analytics
• Adaptive difficulty adjustment
• Session export and data management
• Comprehensive error handling

🛠 Technical Stack:
• Frontend: Streamlit
• AI: OpenAI GPT-3.5/4
• Voice: Google Speech Recognition + gTTS
• Documents: PyPDF2, python-docx
• Audio: pygame, streamlit-audio-recorder
• Analytics: pandas, plotly

📚 Documentation:
• Complete setup guides
• Installation instructions
• Contributing guidelines
• CI/CD pipeline with GitHub Actions
• Cross-platform support

🚀 Ready for production use and portfolio showcase!"
fi

# Add remote if not exists
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/reachbrt/voice-based-quiz-generator.git
else
    echo "✅ GitHub remote already configured"
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
if git push -u origin main; then
    echo "✅ Successfully pushed to GitHub!"
    echo "🌐 Repository: https://github.com/reachbrt/voice-based-quiz-generator"
else
    echo "⚠️  Push failed. You may need to authenticate with GitHub first."
    echo "Try: gh auth login"
    echo "Or set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh"
fi

# Step 2: Install Dependencies and Run Application
echo ""
echo "📦 Step 2: Installing dependencies..."

# Check Python version
python_version=$(python3 --version 2>&1)
echo "🐍 Python version: $python_version"

# Install basic dependencies first
echo "📥 Installing basic dependencies..."
if pip3 install streamlit python-dotenv; then
    echo "✅ Basic dependencies installed"
else
    echo "❌ Failed to install basic dependencies"
    echo "Try: python3 -m pip install streamlit python-dotenv"
fi

# Step 3: Run Demo
echo ""
echo "🎮 Step 3: Running demo..."
echo "This will run the demo version without requiring API keys"
echo ""

if python3 demo.py; then
    echo "✅ Demo completed successfully!"
else
    echo "❌ Demo failed to run"
fi

# Step 4: Setup for Full Application
echo ""
echo "🔧 Step 4: Setting up full application..."

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and add your OpenAI API key:"
    echo "   OPENAI_API_KEY=your_actual_api_key_here"
else
    echo "✅ .env file already exists"
fi

# Install full dependencies
echo "📥 Installing full dependencies..."
if pip3 install -r requirements.txt; then
    echo "✅ All dependencies installed successfully!"
    
    # Step 5: Run Full Application
    echo ""
    echo "🚀 Step 5: Starting full application..."
    echo "The application will open in your browser at http://localhost:8501"
    echo ""
    echo "Press Ctrl+C to stop the application"
    echo ""
    
    # Check if .env has API key
    if grep -q "your_openai_api_key_here" .env 2>/dev/null; then
        echo "⚠️  Warning: Please add your OpenAI API key to .env file for full functionality"
        echo "You can still use the app for document processing and manual quiz creation"
        echo ""
    fi
    
    # Start Streamlit
    streamlit run app.py
    
else
    echo "❌ Failed to install full dependencies"
    echo ""
    echo "Manual installation steps:"
    echo "1. pip3 install -r requirements.txt"
    echo "2. Edit .env file with your OpenAI API key"
    echo "3. streamlit run app.py"
fi

echo ""
echo "🎉 Deployment and setup complete!"
echo ""
echo "📚 Quick Reference:"
echo "• Repository: https://github.com/reachbrt/voice-based-quiz-generator"
echo "• Demo: python3 demo.py"
echo "• Full app: streamlit run app.py"
echo "• Test setup: python3 test_installation.py"
echo ""
echo "📖 Documentation:"
echo "• README.md - Main documentation"
echo "• INSTALL.md - Installation guide"
echo "• SETUP_INSTRUCTIONS.md - Complete setup guide"
