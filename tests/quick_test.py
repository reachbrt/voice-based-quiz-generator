#!/usr/bin/env python3
"""
Quick test script to verify the Voice-Based Quiz Generator setup
"""

import os
import sys
from pathlib import Path

def test_files():
    """Test if all required files exist"""
    required_files = [
        'app.py',
        'config.py', 
        'document_processor.py',
        'question_generator.py',
        'voice_handler.py',
        'quiz_manager.py',
        'requirements.txt',
        '.env.example',
        'README.md',
        'demo.py'
    ]
    
    print("🔍 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
    
    return len(missing_files) == 0

def test_demo():
    """Test if demo can be imported"""
    try:
        print("\n🧪 Testing demo import...")
        import demo
        print("✅ Demo module imported successfully")
        
        # Test demo components
        quiz_manager = demo.DemoQuizManager()
        question = quiz_manager.get_current_question()
        
        if question:
            print("✅ Demo quiz manager working")
            print(f"📝 Sample question: {question['question'][:50]}...")
            return True
        else:
            print("❌ Demo quiz manager failed")
            return False
            
    except Exception as e:
        print(f"❌ Demo import failed: {e}")
        return False

def test_python_version():
    """Test Python version"""
    version = sys.version_info
    print(f"\n🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version compatible")
        return True
    else:
        print("❌ Python 3.8+ required")
        return False

def main():
    """Main test function"""
    print("🎤 Voice-Based Quiz Generator - Quick Test")
    print("=" * 50)
    
    # Test Python version
    python_ok = test_python_version()
    
    # Test files
    files_ok = test_files()
    
    # Test demo
    demo_ok = test_demo()
    
    print("\n" + "=" * 50)
    print("📋 Test Summary:")
    
    if python_ok and files_ok and demo_ok:
        print("🎉 All tests passed! Your setup looks good.")
        print("\nNext steps:")
        print("1. Run demo: python3 demo.py")
        print("2. Create GitHub repository (see SETUP_INSTRUCTIONS.md)")
        print("3. Install full dependencies: pip3 install -r requirements.txt")
        print("4. Run full app: streamlit run app.py")
    else:
        print("⚠️  Some issues detected:")
        if not python_ok:
            print("- Update Python to 3.8+")
        if not files_ok:
            print("- Some files are missing")
        if not demo_ok:
            print("- Demo has issues")
    
    print(f"\n📁 Current directory: {os.getcwd()}")
    print(f"📊 Total files: {len(list(Path('.').glob('*')))}")

if __name__ == "__main__":
    main()
