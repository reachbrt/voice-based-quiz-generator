#!/usr/bin/env python3
"""
Test session state initialization for Voice-Based Quiz Generator
"""

import sys
import os
sys.path.append('.')

# Mock Streamlit session state for testing
class MockSessionState:
    def __init__(self):
        self._state = {}
    
    def __getattr__(self, key):
        if key in self._state:
            return self._state[key]
        raise AttributeError(f"st.session_state has no attribute '{key}'")
    
    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            if not hasattr(self, '_state'):
                super().__setattr__('_state', {})
            self._state[key] = value
    
    def get(self, key, default=None):
        return self._state.get(key, default)
    
    def __contains__(self, key):
        return key in self._state

# Mock streamlit module
class MockStreamlit:
    def __init__(self):
        self.session_state = MockSessionState()
    
    def error(self, message):
        print(f"ERROR: {message}")
    
    def warning(self, message):
        print(f"WARNING: {message}")
    
    def info(self, message):
        print(f"INFO: {message}")
    
    def success(self, message):
        print(f"SUCCESS: {message}")

# Replace streamlit import
sys.modules['streamlit'] = MockStreamlit()
import streamlit as st

def test_quiz_manager_initialization():
    """Test QuizManager session state initialization"""
    print("🧪 Testing QuizManager Session State Initialization")
    print("=" * 60)
    
    # Test 1: Import QuizManager
    print("1. Testing QuizManager import...")
    try:
        from quiz_manager import QuizManager
        print("✅ QuizManager imported successfully")
    except Exception as e:
        print(f"❌ QuizManager import failed: {e}")
        return False
    
    # Test 2: Initialize QuizManager
    print("\n2. Testing QuizManager initialization...")
    try:
        qm = QuizManager()
        print("✅ QuizManager initialized successfully")
    except Exception as e:
        print(f"❌ QuizManager initialization failed: {e}")
        return False
    
    # Test 3: Check session state
    print("\n3. Testing session state initialization...")
    try:
        if hasattr(st.session_state, 'quiz_session'):
            print("✅ quiz_session exists in session state")
            
            # Check required fields
            required_fields = [
                'questions', 'current_question', 'answers', 'scores',
                'start_time', 'end_time', 'difficulty', 'performance_history',
                'session_active'
            ]
            
            session = st.session_state.quiz_session
            missing_fields = []
            
            for field in required_fields:
                if field not in session:
                    missing_fields.append(field)
            
            if missing_fields:
                print(f"❌ Missing fields in quiz_session: {missing_fields}")
                return False
            else:
                print("✅ All required fields present in quiz_session")
                
        else:
            print("❌ quiz_session not found in session state")
            return False
    except Exception as e:
        print(f"❌ Session state check failed: {e}")
        return False
    
    # Test 4: Test methods that access session state
    print("\n4. Testing session state access methods...")
    try:
        # Test get_current_question
        current_q = qm.get_current_question()
        print(f"✅ get_current_question() returned: {current_q}")
        
        # Test get_quiz_progress
        progress = qm.get_quiz_progress()
        print(f"✅ get_quiz_progress() returned: {progress}")
        
        # Test get_session_stats
        stats = qm.get_session_stats()
        print(f"✅ get_session_stats() returned: {stats}")
        
    except Exception as e:
        print(f"❌ Session state access methods failed: {e}")
        return False
    
    # Test 5: Test reset_session
    print("\n5. Testing reset_session...")
    try:
        qm.reset_session()
        print("✅ reset_session() completed successfully")
        
        # Verify session is still accessible
        session = st.session_state.quiz_session
        if session['session_active'] == False:
            print("✅ Session reset to default state")
        else:
            print("❌ Session not properly reset")
            return False
            
    except Exception as e:
        print(f"❌ reset_session() failed: {e}")
        return False
    
    return True

def test_session_state_edge_cases():
    """Test edge cases for session state"""
    print("\n" + "=" * 60)
    print("🔍 Testing Session State Edge Cases")
    print("=" * 60)
    
    # Test multiple initializations
    print("1. Testing multiple QuizManager instances...")
    try:
        from quiz_manager import QuizManager
        
        qm1 = QuizManager()
        qm2 = QuizManager()
        
        # Both should access the same session state
        qm1.reset_session()
        st.session_state.quiz_session['test_field'] = 'test_value'
        
        qm2.initialize_session_state()
        if st.session_state.quiz_session.get('test_field') == 'test_value':
            print("✅ Multiple instances share same session state")
        else:
            print("❌ Session state not shared between instances")
            return False
            
    except Exception as e:
        print(f"❌ Multiple instance test failed: {e}")
        return False
    
    return True

def main():
    """Main test function"""
    print("🎤 Voice-Based Quiz Generator - Session State Tests")
    print("=" * 60)
    
    # Run tests
    test1_passed = test_quiz_manager_initialization()
    test2_passed = test_session_state_edge_cases()
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 Test Summary")
    print("=" * 60)
    
    if test1_passed and test2_passed:
        print("🎉 All session state tests PASSED!")
        print("\nThe QuizManager session state initialization is working correctly.")
        print("The Streamlit app should now run without AttributeError.")
    else:
        print("❌ Some session state tests FAILED!")
        print("Please check the QuizManager implementation.")
    
    print(f"\nTest Results:")
    print(f"  ✅ Basic Initialization: {'PASS' if test1_passed else 'FAIL'}")
    print(f"  ✅ Edge Cases: {'PASS' if test2_passed else 'FAIL'}")

if __name__ == "__main__":
    main()
