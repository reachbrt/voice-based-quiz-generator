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
            print("⚠️  Warning: OPENAI_API_KEY not set. Some features will be limited.")
            return False

        return True

    @classmethod
    def check_optional_dependencies(cls):
        """Check for optional dependencies and return availability"""
        dependencies = {
            'pyaudio': False,
            'pygame': False,
            'speech_recognition': False,
            'gtts': False
        }

        try:
            import pyaudio
            dependencies['pyaudio'] = True
        except ImportError:
            pass

        try:
            import pygame
            dependencies['pygame'] = True
        except ImportError:
            pass

        try:
            import speech_recognition
            dependencies['speech_recognition'] = True
        except ImportError:
            pass

        try:
            import gtts
            dependencies['gtts'] = True
        except ImportError:
            pass

        return dependencies
