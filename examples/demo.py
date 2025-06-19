#!/usr/bin/env python3
"""
Demo script for Voice-Based Quiz Generator
Shows the system capabilities without requiring full setup
"""

import json
from datetime import datetime

# Sample quiz data for demonstration
SAMPLE_QUESTIONS = [
    {
        "question": "What is the primary function of machine learning?",
        "options": {
            "A": "To replace human intelligence completely",
            "B": "To enable computers to learn and improve from experience",
            "C": "To create robots that look like humans",
            "D": "To store large amounts of data"
        },
        "correct_answer": "B",
        "explanation": "Machine learning enables computers to learn and improve their performance on a specific task through experience, without being explicitly programmed for every scenario.",
        "difficulty": "medium",
        "topic": "Machine Learning Basics"
    },
    {
        "question": "Which of the following is NOT a type of machine learning?",
        "options": {
            "A": "Supervised learning",
            "B": "Unsupervised learning",
            "C": "Reinforcement learning",
            "D": "Deterministic learning"
        },
        "correct_answer": "D",
        "explanation": "Deterministic learning is not a recognized type of machine learning. The main types are supervised, unsupervised, and reinforcement learning.",
        "difficulty": "easy",
        "topic": "Machine Learning Types"
    },
    {
        "question": "What is the purpose of a neural network's activation function?",
        "options": {
            "A": "To store the network's weights",
            "B": "To introduce non-linearity into the model",
            "C": "To reduce the size of the input data",
            "D": "To connect different layers physically"
        },
        "correct_answer": "B",
        "explanation": "Activation functions introduce non-linearity into neural networks, allowing them to learn complex patterns and relationships in data that linear models cannot capture.",
        "difficulty": "hard",
        "topic": "Neural Networks"
    }
]

class DemoQuizManager:
    """Simplified quiz manager for demonstration"""
    
    def __init__(self):
        self.questions = SAMPLE_QUESTIONS
        self.current_question = 0
        self.answers = []
        self.start_time = datetime.now()
    
    def get_current_question(self):
        """Get current question"""
        if self.current_question < len(self.questions):
            return self.questions[self.current_question]
        return None
    
    def submit_answer(self, user_answer):
        """Submit answer and get feedback"""
        question = self.get_current_question()
        if not question:
            return None
        
        is_correct = user_answer.upper() == question['correct_answer']
        
        result = {
            'question': question['question'],
            'user_answer': user_answer,
            'correct_answer': question['correct_answer'],
            'is_correct': is_correct,
            'explanation': question['explanation'],
            'difficulty': question['difficulty']
        }
        
        self.answers.append(result)
        self.current_question += 1
        
        return result
    
    def get_results(self):
        """Get quiz results"""
        if not self.answers:
            return None
        
        correct_count = sum(1 for ans in self.answers if ans['is_correct'])
        total_count = len(self.answers)
        accuracy = (correct_count / total_count) * 100
        
        return {
            'total_questions': total_count,
            'correct_answers': correct_count,
            'accuracy': accuracy,
            'answers': self.answers
        }

def display_question(question):
    """Display a question"""
    print(f"\n{'='*60}")
    print(f"QUESTION: {question['question']}")
    print(f"{'='*60}")
    print("\nOPTIONS:")
    for key, value in question['options'].items():
        print(f"  {key}: {value}")
    print()

def display_feedback(result):
    """Display answer feedback"""
    if result['is_correct']:
        print("✅ CORRECT!")
    else:
        print(f"❌ INCORRECT. The correct answer was {result['correct_answer']}")
    
    print(f"\nExplanation: {result['explanation']}")
    print(f"Difficulty: {result['difficulty']}")

def display_results(results):
    """Display final results"""
    print(f"\n{'='*60}")
    print("QUIZ RESULTS")
    print(f"{'='*60}")
    print(f"Questions Answered: {results['total_questions']}")
    print(f"Correct Answers: {results['correct_answers']}")
    print(f"Accuracy: {results['accuracy']:.1f}%")
    
    print(f"\n{'='*60}")
    print("DETAILED BREAKDOWN")
    print(f"{'='*60}")
    
    for i, answer in enumerate(results['answers'], 1):
        status = "✅" if answer['is_correct'] else "❌"
        print(f"\nQ{i}: {status} Your answer: {answer['user_answer']} | Correct: {answer['correct_answer']}")
        print(f"     {answer['question'][:80]}...")

def simulate_voice_features():
    """Simulate voice features"""
    print("\n🎤 VOICE FEATURES SIMULATION")
    print("=" * 40)
    print("In the full application, you would:")
    print("• Hear questions read aloud via text-to-speech")
    print("• Record your answers using voice recognition")
    print("• Receive spoken feedback and explanations")
    print("• Experience adaptive difficulty based on performance")
    print()

def simulate_document_processing():
    """Simulate document processing"""
    print("\n📄 DOCUMENT PROCESSING SIMULATION")
    print("=" * 40)
    print("In the full application, you can:")
    print("• Upload PDF, DOCX, or TXT files")
    print("• Extract and preprocess content automatically")
    print("• Generate questions from any document content")
    print("• Focus on specific topics within documents")
    print()

def main():
    """Main demo function"""
    print("🎤 VOICE-BASED QUIZ GENERATOR DEMO")
    print("=" * 60)
    print("This demo shows the core functionality without requiring")
    print("full installation of dependencies or API keys.")
    print()
    
    # Show simulated features
    simulate_voice_features()
    simulate_document_processing()
    
    # Interactive quiz demo
    print("📝 INTERACTIVE QUIZ DEMO")
    print("=" * 40)
    print("Let's try a sample quiz with 3 questions about machine learning!")
    
    input("\nPress Enter to start the demo quiz...")
    
    quiz_manager = DemoQuizManager()
    
    # Run through questions
    while True:
        question = quiz_manager.get_current_question()
        if not question:
            break
        
        display_question(question)
        
        # Get user input
        while True:
            user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("Please enter A, B, C, or D")
        
        # Submit answer and show feedback
        result = quiz_manager.submit_answer(user_answer)
        display_feedback(result)
        
        if quiz_manager.current_question < len(quiz_manager.questions):
            input("\nPress Enter for the next question...")
    
    # Show final results
    results = quiz_manager.get_results()
    display_results(results)
    
    print(f"\n{'='*60}")
    print("DEMO COMPLETE")
    print(f"{'='*60}")
    print("To experience the full voice-based quiz system:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Configure OpenAI API key in .env file")
    print("3. Run: streamlit run app.py")
    print()
    print("Features in the full version:")
    print("• Voice-based question delivery and answer input")
    print("• Document upload and processing")
    print("• AI-powered question generation")
    print("• Adaptive difficulty adjustment")
    print("• Performance tracking and analytics")
    print("• Export capabilities")
    print()
    print("See README.md for detailed setup instructions.")

if __name__ == "__main__":
    main()
