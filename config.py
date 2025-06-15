import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', 1000))
    OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', 0.7))
    
    # Quiz Configuration
    DEFAULT_QUESTIONS_PER_QUIZ = int(os.getenv('DEFAULT_QUESTIONS_PER_QUIZ', 10))
    DIFFICULTY_LEVELS = os.getenv('DIFFICULTY_LEVELS', 'easy,medium,hard').split(',')
    PERFORMANCE_THRESHOLD = float(os.getenv('PERFORMANCE_THRESHOLD', 0.7))
    
    # Voice Configuration
    TTS_LANGUAGE = os.getenv('TTS_LANGUAGE', 'en')
    SPEECH_RECOGNITION_LANGUAGE = os.getenv('SPEECH_RECOGNITION_LANGUAGE', 'en-US')
    AUDIO_TIMEOUT = int(os.getenv('AUDIO_TIMEOUT', 10))
    AUDIO_PHRASE_TIMEOUT = int(os.getenv('AUDIO_PHRASE_TIMEOUT', 5))
    
    # File Upload Configuration
    MAX_FILE_SIZE_MB = 10
    ALLOWED_EXTENSIONS = ['pdf', 'docx', 'txt']
    
    # Session Configuration
    SESSION_TIMEOUT_MINUTES = 30
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in your .env file.")
        
        return True
