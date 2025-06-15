import streamlit as st
import time
from typing import List, Dict, Optional
import pandas as pd
from datetime import datetime
import json

class QuizManager:
    """Manages quiz sessions, scoring, and performance tracking"""
    
    def __init__(self):
        self.reset_session()
    
    def reset_session(self):
        """Reset quiz session data"""
        if 'quiz_session' not in st.session_state:
            st.session_state.quiz_session = {
                'questions': [],
                'current_question': 0,
                'answers': [],
                'scores': [],
                'start_time': None,
                'end_time': None,
                'difficulty': 'medium',
                'performance_history': [],
                'session_active': False
            }
    
    def start_quiz(self, questions: List[Dict], difficulty: str = 'medium'):
        """Start a new quiz session"""
        st.session_state.quiz_session.update({
            'questions': questions,
            'current_question': 0,
            'answers': [],
            'scores': [],
            'start_time': datetime.now(),
            'end_time': None,
            'difficulty': difficulty,
            'session_active': True
        })
    
    def get_current_question(self) -> Optional[Dict]:
        """Get the current question"""
        session = st.session_state.quiz_session
        if (session['session_active'] and 
            session['current_question'] < len(session['questions'])):
            return session['questions'][session['current_question']]
        return None
    
    def submit_answer(self, user_answer: str, time_taken: float = 0) -> Dict:
        """Submit an answer and get feedback"""
        session = st.session_state.quiz_session
        current_q = self.get_current_question()
        
        if not current_q:
            return {'error': 'No active question'}
        
        correct_answer = current_q['correct_answer']
        is_correct = user_answer.upper() == correct_answer.upper()
        
        # Calculate score (considering time bonus)
        base_score = 1.0 if is_correct else 0.0
        time_bonus = max(0, (30 - time_taken) / 30 * 0.2) if time_taken > 0 else 0
        final_score = base_score + (time_bonus if is_correct else 0)
        
        # Store answer data
        answer_data = {
            'question_index': session['current_question'],
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct,
            'time_taken': time_taken,
            'score': final_score,
            'timestamp': datetime.now()
        }
        
        session['answers'].append(answer_data)
        session['scores'].append(final_score)
        
        # Move to next question
        session['current_question'] += 1
        
        # Check if quiz is complete
        if session['current_question'] >= len(session['questions']):
            self.end_quiz()
        
        return {
            'is_correct': is_correct,
            'correct_answer': correct_answer,
            'explanation': current_q.get('explanation', ''),
            'score': final_score,
            'quiz_complete': session['current_question'] >= len(session['questions'])
        }
    
    def end_quiz(self):
        """End the current quiz session"""
        session = st.session_state.quiz_session
        session['end_time'] = datetime.now()
        session['session_active'] = False
        
        # Calculate overall performance
        if session['scores']:
            performance = sum(session['scores']) / len(session['scores'])
            session['performance_history'].append(performance)
    
    def get_quiz_progress(self) -> Dict:
        """Get current quiz progress"""
        session = st.session_state.quiz_session
        total_questions = len(session['questions'])
        current = session['current_question']
        
        return {
            'current_question': current + 1,
            'total_questions': total_questions,
            'progress_percentage': (current / total_questions * 100) if total_questions > 0 else 0,
            'questions_remaining': total_questions - current
        }
    
    def get_session_stats(self) -> Dict:
        """Get comprehensive session statistics"""
        session = st.session_state.quiz_session
        
        if not session['answers']:
            return {'no_data': True}
        
        correct_answers = sum(1 for ans in session['answers'] if ans['is_correct'])
        total_answers = len(session['answers'])
        accuracy = (correct_answers / total_answers * 100) if total_answers > 0 else 0
        
        total_score = sum(session['scores'])
        average_score = total_score / len(session['scores']) if session['scores'] else 0
        
        # Time statistics
        times = [ans['time_taken'] for ans in session['answers'] if ans['time_taken'] > 0]
        avg_time = sum(times) / len(times) if times else 0
        
        # Session duration
        duration = None
        if session['start_time'] and session['end_time']:
            duration = (session['end_time'] - session['start_time']).total_seconds()
        
        return {
            'total_questions': total_answers,
            'correct_answers': correct_answers,
            'accuracy_percentage': accuracy,
            'total_score': total_score,
            'average_score': average_score,
            'average_time_per_question': avg_time,
            'session_duration': duration,
            'difficulty': session['difficulty']
        }
    
    def get_detailed_results(self) -> pd.DataFrame:
        """Get detailed results as DataFrame"""
        session = st.session_state.quiz_session
        
        if not session['answers']:
            return pd.DataFrame()
        
        results_data = []
        for i, answer in enumerate(session['answers']):
            question = session['questions'][i]
            results_data.append({
                'Question': f"Q{i+1}",
                'Question Text': question['question'][:50] + "..." if len(question['question']) > 50 else question['question'],
                'Your Answer': answer['user_answer'],
                'Correct Answer': answer['correct_answer'],
                'Result': '✓' if answer['is_correct'] else '✗',
                'Score': f"{answer['score']:.2f}",
                'Time (s)': f"{answer['time_taken']:.1f}" if answer['time_taken'] > 0 else "N/A"
            })
        
        return pd.DataFrame(results_data)
    
    def export_session_data(self) -> str:
        """Export session data as JSON"""
        session = st.session_state.quiz_session
        
        export_data = {
            'session_info': {
                'start_time': session['start_time'].isoformat() if session['start_time'] else None,
                'end_time': session['end_time'].isoformat() if session['end_time'] else None,
                'difficulty': session['difficulty']
            },
            'questions': session['questions'],
            'answers': [
                {
                    **answer,
                    'timestamp': answer['timestamp'].isoformat()
                }
                for answer in session['answers']
            ],
            'statistics': self.get_session_stats()
        }
        
        return json.dumps(export_data, indent=2)
    
    def get_performance_trend(self) -> List[float]:
        """Get performance trend over recent questions"""
        session = st.session_state.quiz_session
        
        if len(session['scores']) < 3:
            return session['scores']
        
        # Calculate moving average of last 3 questions
        trend = []
        for i in range(2, len(session['scores'])):
            avg = sum(session['scores'][i-2:i+1]) / 3
            trend.append(avg)
        
        return trend
    
    def should_adjust_difficulty(self) -> Optional[str]:
        """Determine if difficulty should be adjusted"""
        trend = self.get_performance_trend()
        
        if len(trend) < 3:
            return None
        
        recent_performance = sum(trend[-3:]) / 3
        current_difficulty = st.session_state.quiz_session['difficulty']
        
        if recent_performance > 0.8 and current_difficulty != 'hard':
            return 'increase'
        elif recent_performance < 0.4 and current_difficulty != 'easy':
            return 'decrease'
        
        return None
