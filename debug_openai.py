#!/usr/bin/env python3
"""
Debug OpenAI API issue
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_openai_import():
    """Test OpenAI import and basic functionality"""
    print("🔍 Debugging OpenAI API Issue")
    print("=" * 40)
    
    # Test 1: Check OpenAI import
    print("1. Testing OpenAI import...")
    try:
        from openai import OpenAI
        print("✅ OpenAI imported successfully")
        print(f"   OpenAI module location: {OpenAI.__module__}")
    except Exception as e:
        print(f"❌ OpenAI import failed: {e}")
        return False
    
    # Test 2: Check old import (should fail)
    print("\n2. Testing old OpenAI import (should fail)...")
    try:
        import openai
        if hasattr(openai, 'ChatCompletion'):
            print("⚠️  Old OpenAI API still available - this might cause conflicts")
        else:
            print("✅ Old ChatCompletion not available (good)")
    except Exception as e:
        print(f"❌ Error checking old API: {e}")
    
    # Test 3: Test our question generator
    print("\n3. Testing question generator import...")
    try:
        from question_generator import QuestionGenerator
        print("✅ QuestionGenerator imported successfully")
    except Exception as e:
        print(f"❌ QuestionGenerator import failed: {e}")
        return False
    
    # Test 4: Test initialization
    print("\n4. Testing QuestionGenerator initialization...")
    try:
        qg = QuestionGenerator()
        print("✅ QuestionGenerator initialized successfully")
        print(f"   Client type: {type(qg.client)}")
    except Exception as e:
        print(f"❌ QuestionGenerator initialization failed: {e}")
        return False
    
    # Test 5: Test question generation
    print("\n5. Testing question generation...")
    try:
        questions = qg.generate_questions("Test content about machine learning", num_questions=1)
        if questions:
            print(f"✅ Generated {len(questions)} questions")
            return True
        else:
            print("⚠️  No questions generated (might be using fallback)")
            return True
    except Exception as e:
        print(f"❌ Question generation failed: {e}")
        print(f"   Error type: {type(e)}")
        print(f"   Error details: {str(e)}")
        return False

def check_environment():
    """Check environment variables"""
    print("\n" + "=" * 40)
    print("🔧 Environment Check")
    print("=" * 40)
    
    # Check .env file
    if os.path.exists('.env'):
        print("✅ .env file exists")
        with open('.env', 'r') as f:
            content = f.read()
            if 'OPENAI_API_KEY=' in content:
                if 'your_openai_api_key_here' in content:
                    print("⚠️  API key placeholder found")
                else:
                    print("✅ API key appears to be set")
            else:
                print("❌ No API key found in .env")
    else:
        print("❌ .env file not found")
    
    # Check config
    try:
        from config import Config
        print(f"✅ Config loaded")
        print(f"   API key configured: {'Yes' if Config.OPENAI_API_KEY and Config.OPENAI_API_KEY != 'your_openai_api_key_here' else 'No'}")
    except Exception as e:
        print(f"❌ Config load failed: {e}")

def main():
    """Main debug function"""
    success = test_openai_import()
    check_environment()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 OpenAI debugging completed successfully!")
    else:
        print("❌ OpenAI debugging found issues!")
    
    print("\nIf you're still seeing the old API error, try:")
    print("1. Restart the Streamlit app completely")
    print("2. Clear Python cache: find . -name '*.pyc' -delete")
    print("3. Restart your terminal/IDE")

if __name__ == "__main__":
    main()
