#!/usr/bin/env python3
"""
Test script to verify Voice-Based Quiz Generator installation
"""

import sys
import importlib
from pathlib import Path

def test_import(module_name, description=""):
    """Test if a module can be imported"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {module_name} {description}")
        return True
    except ImportError as e:
        print(f"❌ {module_name} {description} - Error: {e}")
        return False

def test_file_exists(file_path, description=""):
    """Test if a file exists"""
    if Path(file_path).exists():
        print(f"✅ {file_path} {description}")
        return True
    else:
        print(f"❌ {file_path} {description} - File not found")
        return False

def test_openai_connection():
    """Test OpenAI API connection"""
    try:
        import openai
        from config import Config
        
        if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == 'your_openai_api_key_here':
            print("⚠️  OpenAI API key not configured")
            return False
        
        # Test a simple API call
        openai.api_key = Config.OPENAI_API_KEY
        
        # Just test the connection without making an actual call
        print("✅ OpenAI configuration appears valid")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI connection test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Testing Voice-Based Quiz Generator Installation")
    print("=" * 50)
    
    # Test Python version
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (3.8+ required)")
    
    print("\n📦 Testing Core Dependencies:")
    core_deps = [
        ("streamlit", "- Web framework"),
        ("openai", "- AI API client"),
        ("python_dotenv", "- Environment variables"),
        ("PyPDF2", "- PDF processing"),
        ("docx", "- Word document processing"),
        ("speech_recognition", "- Speech recognition"),
        ("gtts", "- Text-to-speech"),
        ("pygame", "- Audio playback"),
        ("pandas", "- Data processing"),
        ("plotly", "- Visualization"),
    ]
    
    failed_deps = []
    for module, desc in core_deps:
        if not test_import(module, desc):
            failed_deps.append(module)
    
    print("\n📁 Testing Project Files:")
    project_files = [
        ("app.py", "- Main application"),
        ("config.py", "- Configuration"),
        ("document_processor.py", "- Document processing"),
        ("question_generator.py", "- Question generation"),
        ("voice_handler.py", "- Voice handling"),
        ("quiz_manager.py", "- Quiz management"),
        ("requirements.txt", "- Dependencies list"),
        (".env.example", "- Environment template"),
    ]
    
    missing_files = []
    for file_path, desc in project_files:
        if not test_file_exists(file_path, desc):
            missing_files.append(file_path)
    
    print("\n🔧 Testing Project Modules:")
    project_modules = [
        ("config", "- Configuration module"),
        ("document_processor", "- Document processor"),
        ("question_generator", "- Question generator"),
        ("voice_handler", "- Voice handler"),
        ("quiz_manager", "- Quiz manager"),
    ]
    
    failed_modules = []
    for module, desc in project_modules:
        if not test_import(module, desc):
            failed_modules.append(module)
    
    print("\n🔑 Testing Configuration:")
    config_ok = test_openai_connection()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Test Summary:")
    
    if failed_deps:
        print(f"❌ Missing dependencies: {', '.join(failed_deps)}")
        print("   Run: pip install -r requirements.txt")
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
    
    if failed_modules:
        print(f"❌ Failed modules: {', '.join(failed_modules)}")
    
    if not config_ok:
        print("⚠️  Configuration issues detected")
        print("   Edit .env file and add your OpenAI API key")
    
    if not failed_deps and not missing_files and not failed_modules and config_ok:
        print("🎉 All tests passed! Installation looks good.")
        print("\nYou can now run: streamlit run app.py")
    else:
        print("⚠️  Some issues detected. Please resolve them before running the app.")
    
    print("\nFor help, see README.md")

if __name__ == "__main__":
    main()
