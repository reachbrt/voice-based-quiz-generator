import openai
import json
import streamlit as st
from typing import List, Dict, Optional
from config import Config
import random

class QuestionGenerator:
    """Generates quiz questions using OpenAI GPT"""
    
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.model = Config.OPENAI_MODEL
        self.max_tokens = Config.OPENAI_MAX_TOKENS
        self.temperature = Config.OPENAI_TEMPERATURE
    
    def generate_questions(self, content: str, num_questions: int = 5, 
                         difficulty: str = "medium", topic: str = "") -> List[Dict]:
        """Generate quiz questions from content"""
        try:
            prompt = self._create_prompt(content, num_questions, difficulty, topic)
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert quiz generator. Create engaging and educational quiz questions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            questions_text = response.choices[0].message.content
            questions = self._parse_questions(questions_text)
            
            return questions
            
        except Exception as e:
            st.error(f"Error generating questions: {str(e)}")
            return []
    
    def _create_prompt(self, content: str, num_questions: int, 
                      difficulty: str, topic: str) -> str:
        """Create prompt for question generation"""
        
        difficulty_instructions = {
            "easy": "Create simple, straightforward questions that test basic understanding.",
            "medium": "Create moderately challenging questions that require some analysis.",
            "hard": "Create complex questions that require deep understanding and critical thinking."
        }
        
        prompt = f"""
Based on the following content, generate {num_questions} multiple-choice quiz questions.

Content:
{content[:3000]}  # Limit content to avoid token limits

Requirements:
- Difficulty level: {difficulty} - {difficulty_instructions.get(difficulty, '')}
- Each question should have 4 options (A, B, C, D)
- Include the correct answer
- Provide a brief explanation for the correct answer
- Questions should be relevant to the main topics in the content
{f"- Focus on the topic: {topic}" if topic else ""}

Format your response as a JSON array with this structure:
[
  {{
    "question": "Question text here?",
    "options": {{
      "A": "Option A text",
      "B": "Option B text", 
      "C": "Option C text",
      "D": "Option D text"
    }},
    "correct_answer": "A",
    "explanation": "Brief explanation of why this is correct",
    "difficulty": "{difficulty}",
    "topic": "Main topic of this question"
  }}
]

Make sure the JSON is valid and properly formatted.
"""
        return prompt
    
    def _parse_questions(self, questions_text: str) -> List[Dict]:
        """Parse generated questions from GPT response"""
        try:
            # Try to extract JSON from the response
            start_idx = questions_text.find('[')
            end_idx = questions_text.rfind(']') + 1
            
            if start_idx != -1 and end_idx != 0:
                json_text = questions_text[start_idx:end_idx]
                questions = json.loads(json_text)
                
                # Validate question structure
                validated_questions = []
                for q in questions:
                    if self._validate_question(q):
                        validated_questions.append(q)
                
                return validated_questions
            else:
                st.error("Could not find valid JSON in response")
                return []
                
        except json.JSONDecodeError as e:
            st.error(f"Error parsing questions JSON: {str(e)}")
            return []
        except Exception as e:
            st.error(f"Error processing questions: {str(e)}")
            return []
    
    def _validate_question(self, question: Dict) -> bool:
        """Validate question structure"""
        required_fields = ['question', 'options', 'correct_answer', 'explanation']
        
        for field in required_fields:
            if field not in question:
                return False
        
        # Validate options
        if not isinstance(question['options'], dict):
            return False
        
        required_options = ['A', 'B', 'C', 'D']
        for option in required_options:
            if option not in question['options']:
                return False
        
        # Validate correct answer
        if question['correct_answer'] not in required_options:
            return False
        
        return True
    
    def generate_adaptive_questions(self, content: str, performance_history: List[float],
                                  current_difficulty: str) -> List[Dict]:
        """Generate questions with adaptive difficulty based on performance"""
        
        # Calculate average performance
        if performance_history:
            avg_performance = sum(performance_history) / len(performance_history)
        else:
            avg_performance = 0.5  # Default to medium
        
        # Adjust difficulty based on performance
        if avg_performance > Config.PERFORMANCE_THRESHOLD and current_difficulty != "hard":
            new_difficulty = "hard" if current_difficulty == "medium" else "medium"
        elif avg_performance < (1 - Config.PERFORMANCE_THRESHOLD) and current_difficulty != "easy":
            new_difficulty = "easy" if current_difficulty == "medium" else "medium"
        else:
            new_difficulty = current_difficulty
        
        return self.generate_questions(content, 
                                     Config.DEFAULT_QUESTIONS_PER_QUIZ, 
                                     new_difficulty)
