#!/usr/bin/env python3
"""
Test JSON parsing for question generation
"""

import json
import sys
import os
sys.path.append('.')

from question_generator import QuestionGenerator

def test_json_parsing():
    """Test the JSON parsing functionality"""
    print("🧪 Testing JSON Parsing")
    print("=" * 40)
    
    # Sample GPT response that might cause issues
    sample_responses = [
        # Good JSON
        '''[
  {
    "question": "What is machine learning?",
    "options": {
      "A": "A type of computer",
      "B": "A learning algorithm",
      "C": "A programming language",
      "D": "A database"
    },
    "correct_answer": "B",
    "explanation": "Machine learning is a learning algorithm.",
    "difficulty": "medium",
    "topic": "ML Basics"
  }
]''',
        
        # JSON with extra text
        '''Here are the quiz questions:

[
  {
    "question": "What is AI?",
    "options": {
      "A": "Artificial Intelligence",
      "B": "Automated Intelligence",
      "C": "Advanced Intelligence",
      "D": "Algorithmic Intelligence"
    },
    "correct_answer": "A",
    "explanation": "AI stands for Artificial Intelligence.",
    "difficulty": "easy",
    "topic": "AI Basics"
  }
]

These questions test basic AI knowledge.''',
        
        # Malformed JSON
        '''[
  {
    "question": "What is deep learning?",
    "options": {
      "A": "A type of machine learning",
      "B": "A programming language",
      "C": "A database system",
      "D": "A web framework"
    },
    "correct_answer": "A",
    "explanation": "Deep learning is a subset of machine learning.",
    "difficulty": "medium",
    "topic": "Deep Learning"
  }
  // Missing comma here
  {
    "question": "What is a neural network?",
    "options": {
      "A": "A computer network",
      "B": "A brain-inspired algorithm",
      "C": "A social network",
      "D": "A wireless network"
    },
    "correct_answer": "B",
    "explanation": "Neural networks are inspired by biological neural networks.",
    "difficulty": "medium",
    "topic": "Neural Networks"
  }
]'''
    ]
    
    qg = QuestionGenerator()
    
    for i, response in enumerate(sample_responses, 1):
        print(f"\n--- Test {i} ---")
        print(f"Response length: {len(response)} characters")
        
        try:
            questions = qg._parse_questions(response)
            print(f"✅ Parsed {len(questions)} questions")
            
            if questions:
                print(f"First question: {questions[0]['question']}")
        except Exception as e:
            print(f"❌ Parsing failed: {e}")

def test_real_generation():
    """Test real question generation"""
    print("\n" + "=" * 40)
    print("🤖 Testing Real Question Generation")
    print("=" * 40)
    
    qg = QuestionGenerator()
    
    test_content = """
    Python is a high-level programming language known for its simplicity and readability.
    It supports multiple programming paradigms including procedural, object-oriented, and functional programming.
    Python is widely used in web development, data science, artificial intelligence, and automation.
    """
    
    try:
        questions = qg.generate_questions(test_content, num_questions=1, difficulty="easy")
        
        if questions:
            print(f"✅ Successfully generated {len(questions)} questions")
            for i, q in enumerate(questions, 1):
                print(f"\nQuestion {i}: {q['question']}")
                print(f"Correct Answer: {q['correct_answer']} - {q['options'][q['correct_answer']]}")
        else:
            print("⚠️ No questions generated")
            
    except Exception as e:
        print(f"❌ Generation failed: {e}")

if __name__ == "__main__":
    test_json_parsing()
    test_real_generation()
