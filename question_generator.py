import json
import streamlit as st
from typing import List, Dict, Optional
from config import Config
import random

# Import OpenAI with error handling
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError as e:
    st.error(f"OpenAI import failed: {e}")
    OPENAI_AVAILABLE = False
    OpenAI = None

class QuestionGenerator:
    """Generates quiz questions using OpenAI GPT"""

    def __init__(self):
        self.client = None

        if not OPENAI_AVAILABLE:
            st.warning("⚠️ OpenAI library not available. Using sample questions.")
        elif not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == 'your_openai_api_key_here':
            st.warning("⚠️ OpenAI API key not configured. Please add your API key to the .env file.")
        else:
            try:
                self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
                st.success("✅ OpenAI client initialized successfully!")
            except Exception as e:
                st.error(f"Error initializing OpenAI client: {str(e)}")

        self.model = Config.OPENAI_MODEL
        self.max_tokens = Config.OPENAI_MAX_TOKENS
        self.temperature = Config.OPENAI_TEMPERATURE
    
    def generate_questions(self, content: str, num_questions: int = 5,
                         difficulty: str = "medium", topic: str = "") -> List[Dict]:
        """Generate quiz questions from content"""

        # Check if OpenAI is available and configured
        if not OPENAI_AVAILABLE:
            st.info("🔄 Using sample questions (OpenAI not available)")
            return self._generate_sample_questions(num_questions, difficulty)

        if not self.client:
            st.info("🔄 Using sample questions (API key not configured)")
            return self._generate_sample_questions(num_questions, difficulty)

        try:
            st.info("🤖 Generating questions using OpenAI GPT...")
            prompt = self._create_prompt(content, num_questions, difficulty, topic)

            # Use the new OpenAI API format
            response = self.client.chat.completions.create(
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

            if questions:
                st.success(f"✅ Generated {len(questions)} AI-powered questions!")
                return questions
            else:
                st.warning("⚠️ AI generation failed, using sample questions")
                return self._generate_sample_questions(num_questions, difficulty)

        except Exception as e:
            error_msg = str(e)
            st.error(f"❌ Error generating questions: {error_msg}")

            # Check for specific OpenAI API errors
            if "ChatCompletion" in error_msg:
                st.error("🔧 OpenAI API compatibility issue detected. Please restart the application.")

            st.info("🔄 Falling back to sample questions for demonstration.")
            return self._generate_sample_questions(num_questions, difficulty)
    
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
{content[:3000]}

Requirements:
- Difficulty level: {difficulty} - {difficulty_instructions.get(difficulty, '')}
- Each question should have 4 options (A, B, C, D)
- Include the correct answer
- Provide a brief explanation for the correct answer
- Questions should be relevant to the main topics in the content
{f"- Focus on the topic: {topic}" if topic else ""}

IMPORTANT: Respond ONLY with valid JSON. No additional text before or after the JSON.

Format your response as a JSON array with this exact structure:
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

Return ONLY the JSON array. Do not include any explanatory text, markdown formatting, or code blocks.
"""
        return prompt
    
    def _parse_questions(self, questions_text: str) -> List[Dict]:
        """Parse generated questions from GPT response"""
        try:
            # Debug: Show the raw response
            st.write("🔍 **Debug - Raw GPT Response:**")
            st.code(questions_text[:500] + "..." if len(questions_text) > 500 else questions_text)

            # Method 1: Try to find JSON array
            start_idx = questions_text.find('[')
            end_idx = questions_text.rfind(']') + 1

            if start_idx != -1 and end_idx > start_idx:
                json_text = questions_text[start_idx:end_idx]
                st.write("🔍 **Extracted JSON:**")
                st.code(json_text[:300] + "..." if len(json_text) > 300 else json_text)

                try:
                    questions = json.loads(json_text)

                    # Validate question structure
                    validated_questions = []
                    for i, q in enumerate(questions):
                        if self._validate_question(q):
                            validated_questions.append(q)
                        else:
                            st.warning(f"Question {i+1} failed validation")

                    if validated_questions:
                        st.success(f"✅ Successfully parsed {len(validated_questions)} questions")
                        return validated_questions
                    else:
                        st.error("❌ No valid questions found after validation")

                except json.JSONDecodeError as e:
                    st.error(f"❌ JSON parsing failed: {str(e)}")

            # Method 2: Try to find JSON objects individually
            st.info("🔄 Trying alternative parsing method...")
            import re

            # Look for individual question objects
            pattern = r'\{[^{}]*"question"[^{}]*\}'
            matches = re.findall(pattern, questions_text, re.DOTALL)

            if matches:
                st.write(f"Found {len(matches)} potential question objects")
                questions = []
                for match in matches:
                    try:
                        q = json.loads(match)
                        if self._validate_question(q):
                            questions.append(q)
                    except:
                        continue

                if questions:
                    st.success(f"✅ Parsed {len(questions)} questions using alternative method")
                    return questions

            # Method 3: Fallback - create questions from text
            st.warning("⚠️ JSON parsing failed, falling back to sample questions")
            return []

        except Exception as e:
            st.error(f"❌ Error processing questions: {str(e)}")
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

    def _generate_sample_questions(self, num_questions: int, difficulty: str) -> List[Dict]:
        """Generate sample questions when OpenAI is not available"""
        sample_questions = [
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
            },
            {
                "question": "What does 'overfitting' mean in machine learning?",
                "options": {
                    "A": "The model performs well on training data but poorly on new data",
                    "B": "The model is too simple to capture patterns",
                    "C": "The model has too few parameters",
                    "D": "The model trains too quickly"
                },
                "correct_answer": "A",
                "explanation": "Overfitting occurs when a model learns the training data too well, including noise and outliers, making it perform poorly on new, unseen data.",
                "difficulty": "medium",
                "topic": "Model Performance"
            },
            {
                "question": "What is the main advantage of using cross-validation?",
                "options": {
                    "A": "It makes training faster",
                    "B": "It reduces the need for data preprocessing",
                    "C": "It provides a more reliable estimate of model performance",
                    "D": "It eliminates the need for a test set"
                },
                "correct_answer": "C",
                "explanation": "Cross-validation provides a more reliable estimate of how well a model will perform on unseen data by testing it on multiple different subsets of the training data.",
                "difficulty": "medium",
                "topic": "Model Validation"
            }
        ]

        # Filter by difficulty if specified
        if difficulty != "medium":
            filtered_questions = [q for q in sample_questions if q['difficulty'] == difficulty]
            if filtered_questions:
                sample_questions = filtered_questions

        # Return requested number of questions
        return sample_questions[:min(num_questions, len(sample_questions))]
