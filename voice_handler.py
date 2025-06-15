import tempfile
import os
import streamlit as st
import io
import base64
from typing import Optional
from config import Config

# Optional imports with graceful fallbacks
try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    sr = None

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    gTTS = None

try:
    import pydub
    PYDUB_AVAILABLE = True
except ImportError:
    PYDUB_AVAILABLE = False
    pydub = None

try:
    import pyaudio
    PYAUDIO_AVAILABLE = True
except ImportError:
    PYAUDIO_AVAILABLE = False
    pyaudio = None

class VoiceHandler:
    """Handles speech recognition and text-to-speech functionality"""

    def __init__(self):
        self.tts_language = Config.TTS_LANGUAGE
        self.recognition_language = Config.SPEECH_RECOGNITION_LANGUAGE

        # Initialize speech recognition if available
        if SPEECH_RECOGNITION_AVAILABLE:
            self.recognizer = sr.Recognizer()
            if PYAUDIO_AVAILABLE:
                try:
                    self.microphone = sr.Microphone()
                except Exception as e:
                    st.warning(f"Microphone initialization failed: {e}")
                    self.microphone = None
            else:
                self.microphone = None
        else:
            self.recognizer = None
            self.microphone = None

        # Check dependencies and show status
        self._check_dependencies()
    
    def _check_dependencies(self):
        """Check and report dependency status"""
        missing_deps = []

        if not SPEECH_RECOGNITION_AVAILABLE:
            missing_deps.append("speech_recognition")
        if not GTTS_AVAILABLE:
            missing_deps.append("gtts")
        if not PYAUDIO_AVAILABLE:
            missing_deps.append("pyaudio")

        if missing_deps:
            st.sidebar.warning(f"⚠️ Missing voice dependencies: {', '.join(missing_deps)}")
            st.sidebar.info("Install with: pip install " + " ".join(missing_deps))

    def text_to_speech(self, text: str) -> Optional[str]:
        """Convert text to speech and return audio file path"""
        if not GTTS_AVAILABLE:
            st.warning("Text-to-speech not available. Please install gtts: pip install gtts")
            return None

        try:
            # Create TTS object
            tts = gTTS(text=text, lang=self.tts_language, slow=False)

            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                tts.save(tmp_file.name)
                return tmp_file.name

        except Exception as e:
            st.error(f"Error generating speech: {str(e)}")
            return None
    
    def play_audio(self, audio_file_path: str):
        """Play audio file using Streamlit's HTML audio player"""
        try:
            audio_html = self.get_audio_html(audio_file_path)
            st.markdown(audio_html, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error playing audio: {str(e)}")
    
    def speech_to_text(self, audio_data) -> Optional[str]:
        """Convert speech to text using speech recognition"""
        if not SPEECH_RECOGNITION_AVAILABLE:
            st.warning("Speech recognition not available. Please install speechrecognition: pip install speechrecognition")
            return None

        if not self.recognizer:
            st.warning("Speech recognizer not initialized.")
            return None

        try:
            # Save audio data to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                tmp_file.write(audio_data)
                tmp_file_path = tmp_file.name

            # Load audio file
            with sr.AudioFile(tmp_file_path) as source:
                audio = self.recognizer.record(source)

            # Recognize speech
            text = self.recognizer.recognize_google(
                audio,
                language=self.recognition_language
            )

            # Clean up temporary file
            os.unlink(tmp_file_path)

            return text.strip()

        except sr.UnknownValueError:
            st.warning("Could not understand the audio. Please try again.")
            return None
        except sr.RequestError as e:
            st.error(f"Error with speech recognition service: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Error processing audio: {str(e)}")
            return None
    
    def get_audio_html(self, audio_file_path: str) -> str:
        """Generate HTML audio player for Streamlit"""
        try:
            with open(audio_file_path, 'rb') as audio_file:
                audio_bytes = audio_file.read()
            
            audio_base64 = base64.b64encode(audio_bytes).decode()
            
            audio_html = f"""
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
            """
            
            return audio_html
            
        except Exception as e:
            st.error(f"Error creating audio player: {str(e)}")
            return ""
    
    def create_question_audio(self, question_data: dict) -> Optional[str]:
        """Create audio for a complete question including options"""
        try:
            question_text = question_data['question']
            options = question_data['options']
            
            # Build complete question text
            full_text = f"Question: {question_text}\n\n"
            full_text += "Options:\n"
            for key, value in options.items():
                full_text += f"{key}: {value}\n"
            
            full_text += "\nPlease say your answer: A, B, C, or D."
            
            return self.text_to_speech(full_text)
            
        except Exception as e:
            st.error(f"Error creating question audio: {str(e)}")
            return None
    
    def create_feedback_audio(self, is_correct: bool, correct_answer: str, 
                            explanation: str, user_answer: str = "") -> Optional[str]:
        """Create audio feedback for answer"""
        try:
            if is_correct:
                feedback_text = f"Correct! Well done. {explanation}"
            else:
                feedback_text = f"Incorrect. You answered {user_answer}, but the correct answer is {correct_answer}. {explanation}"
            
            return self.text_to_speech(feedback_text)
            
        except Exception as e:
            st.error(f"Error creating feedback audio: {str(e)}")
            return None
    
    def cleanup_temp_files(self, file_paths: list):
        """Clean up temporary audio files"""
        for file_path in file_paths:
            try:
                if file_path and os.path.exists(file_path):
                    os.unlink(file_path)
            except Exception as e:
                st.warning(f"Could not clean up temporary file {file_path}: {str(e)}")
    
    def parse_voice_answer(self, voice_text: str) -> Optional[str]:
        """Parse voice input to extract answer choice"""
        if not voice_text:
            return None
        
        voice_text = voice_text.upper().strip()
        
        # Look for single letter answers
        for option in ['A', 'B', 'C', 'D']:
            if option in voice_text:
                # Check if it's a clear single option
                if voice_text == option or f" {option} " in voice_text or voice_text.startswith(f"{option} ") or voice_text.endswith(f" {option}"):
                    return option
        
        # Look for spelled out options
        spelled_options = {
            'ALPHA': 'A', 'BRAVO': 'B', 'CHARLIE': 'C', 'DELTA': 'D',
            'OPTION A': 'A', 'OPTION B': 'B', 'OPTION C': 'C', 'OPTION D': 'D'
        }
        
        for spelled, letter in spelled_options.items():
            if spelled in voice_text:
                return letter
        
        return None
