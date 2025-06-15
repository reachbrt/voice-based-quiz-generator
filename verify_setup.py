#!/usr/bin/env python3
"""
Verification script for Voice-Based Quiz Generator
Run this to check if everything is ready for deployment
"""

import os
import sys
from pathlib import Path

def check_files():
    """Check if all required files exist"""
    print("📁 Checking project files...")
    
    required_files = {
        'app.py': 'Main Streamlit application',
        'config.py': 'Configuration management',
        'document_processor.py': 'Document processing',
        'question_generator.py': 'AI question generation',
        'voice_handler.py': 'Voice processing',
        'quiz_manager.py': 'Quiz management',
        'requirements.txt': 'Dependencies list',
        '.env.example': 'Environment template',
        'README.md': 'Main documentation',
        'demo.py': 'Demo application',
        'MANUAL_SETUP.md': 'Setup instructions'
    }
    
    all_present = True
    for file, description in required_files.items():
        if Path(file).exists():
            size = Path(file).stat().st_size
            print(f"✅ {file:<25} ({size:,} bytes) - {description}")
        else:
            print(f"❌ {file:<25} - MISSING - {description}")
            all_present = False
    
    return all_present

def check_git_status():
    """Check git repository status"""
    print("\n🔧 Checking Git status...")
    
    if Path('.git').exists():
        print("✅ Git repository initialized")
        
        # Check if there are uncommitted changes
        import subprocess
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                if result.stdout.strip():
                    print("⚠️  Uncommitted changes detected")
                    print("   Run: git add . && git commit -m 'Update'")
                else:
                    print("✅ No uncommitted changes")
            else:
                print("⚠️  Could not check git status")
        except FileNotFoundError:
            print("❌ Git not found in PATH")
            return False
    else:
        print("❌ Git repository not initialized")
        print("   Run: git init")
        return False
    
    return True

def check_python_environment():
    """Check Python environment"""
    print("\n🐍 Checking Python environment...")
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version compatible")
    else:
        print("❌ Python 3.8+ required")
        return False
    
    # Check if we can import basic modules
    try:
        import json
        import datetime
        print("✅ Standard library modules available")
    except ImportError as e:
        print(f"❌ Standard library issue: {e}")
        return False
    
    return True

def test_demo():
    """Test if demo can be imported and run"""
    print("\n🎮 Testing demo functionality...")
    
    try:
        # Import demo module
        import demo
        print("✅ Demo module imports successfully")
        
        # Test demo components
        quiz_manager = demo.DemoQuizManager()
        question = quiz_manager.get_current_question()
        
        if question and 'question' in question:
            print("✅ Demo quiz manager working")
            print(f"   Sample question: {question['question'][:60]}...")
            return True
        else:
            print("❌ Demo quiz manager not working properly")
            return False
            
    except Exception as e:
        print(f"❌ Demo test failed: {e}")
        return False

def check_environment_setup():
    """Check environment configuration"""
    print("\n⚙️  Checking environment setup...")
    
    if Path('.env.example').exists():
        print("✅ Environment template exists")
        
        if Path('.env').exists():
            print("✅ Environment file exists")
            
            # Check if API key is configured
            try:
                with open('.env', 'r') as f:
                    content = f.read()
                    if 'OPENAI_API_KEY=' in content and 'your_openai_api_key_here' not in content:
                        print("✅ OpenAI API key appears to be configured")
                    else:
                        print("⚠️  OpenAI API key not configured")
                        print("   Edit .env file and add your API key")
            except Exception as e:
                print(f"⚠️  Could not read .env file: {e}")
        else:
            print("⚠️  .env file not created")
            print("   Run: cp .env.example .env")
    else:
        print("❌ .env.example template missing")
        return False
    
    return True

def generate_commands():
    """Generate the commands needed for deployment"""
    print("\n🚀 Deployment Commands:")
    print("=" * 50)
    
    print("\n1. Push to GitHub:")
    print("git init")
    print("git branch -M main")
    print("git add .")
    print('git commit -m "Voice-Based Quiz Generator: Complete Implementation"')
    print("git remote add origin https://github.com/reachbrt/voice-based-quiz-generator.git")
    print("git push -u origin main")
    
    print("\n2. Install Dependencies:")
    print("pip3 install streamlit python-dotenv")
    print("# Or for full installation:")
    print("pip3 install -r requirements.txt")
    
    print("\n3. Run Demo:")
    print("python3 demo.py")
    
    print("\n4. Setup Environment:")
    print("cp .env.example .env")
    print("# Edit .env and add your OpenAI API key")
    
    print("\n5. Run Full Application:")
    print("streamlit run app.py")

def main():
    """Main verification function"""
    print("🎤 Voice-Based Quiz Generator - Setup Verification")
    print("=" * 60)
    
    # Run all checks
    files_ok = check_files()
    git_ok = check_git_status()
    python_ok = check_python_environment()
    demo_ok = test_demo()
    env_ok = check_environment_setup()
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 VERIFICATION SUMMARY")
    print("=" * 60)
    
    all_good = files_ok and python_ok and demo_ok
    
    if all_good:
        print("🎉 ALL CHECKS PASSED!")
        print("\nYour Voice-Based Quiz Generator is ready for deployment!")
        print("\n✅ Files: Complete")
        print("✅ Python: Compatible")
        print("✅ Demo: Working")
        
        if git_ok:
            print("✅ Git: Ready")
        else:
            print("⚠️  Git: Needs setup")
            
        if env_ok:
            print("✅ Environment: Configured")
        else:
            print("⚠️  Environment: Needs API key")
            
    else:
        print("⚠️  SOME ISSUES DETECTED")
        if not files_ok:
            print("❌ Missing required files")
        if not python_ok:
            print("❌ Python environment issues")
        if not demo_ok:
            print("❌ Demo functionality issues")
    
    # Always show commands
    generate_commands()
    
    print(f"\n📁 Current directory: {os.getcwd()}")
    print(f"📊 Total files: {len(list(Path('.').glob('*')))}")
    print("\n🌐 Target repository: https://github.com/reachbrt/voice-based-quiz-generator")
    
    if all_good:
        print("\n🚀 Ready to deploy! Run the commands above to push to GitHub and start the app.")
    else:
        print("\n🔧 Please fix the issues above before deploying.")

if __name__ == "__main__":
    main()
