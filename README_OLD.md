# 🎤 Voice-Based Quiz Generator

A comprehensive Streamlit application that generates quiz questions from uploaded documents and conducts voice-based quiz sessions with immediate feedback and explanations through synthesized speech.

## Features

### 📄 Document Processing
- **Multi-format Support**: Upload PDF, DOCX, or TXT files
- **Intelligent Text Extraction**: Automatically extracts and preprocesses content
- **Content Preview**: Review extracted content before quiz generation

### 🤖 AI-Powered Question Generation
- **GPT Integration**: Uses OpenAI GPT models for intelligent question generation
- **Adaptive Difficulty**: Three difficulty levels (Easy, Medium, Hard)
- **Topic Focusing**: Optional topic-specific question generation
- **Multiple Choice Format**: Generates 4-option multiple choice questions with explanations

### 🎤 Voice Interaction
- **Text-to-Speech**: Questions and feedback delivered via synthesized speech
- **Speech Recognition**: Voice-based answer input using Whisper/Google Speech API
- **Audio Controls**: Play/pause functionality for questions and feedback
- **Fallback Text Input**: Always available as backup option

### 📊 Performance Tracking
- **Real-time Progress**: Visual progress tracking during quizzes
- **Detailed Analytics**: Comprehensive performance statistics
- **Performance Trends**: Track improvement over time
- **Adaptive Difficulty**: Automatically adjusts based on performance

### 💾 Data Management
- **Session Export**: Download quiz results in JSON format
- **Performance History**: Track long-term learning progress
- **Detailed Results**: Question-by-question breakdown

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Microphone access for voice features

### Setup Instructions

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd voice-based-quiz-generator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Install System Dependencies (macOS)**
   ```bash
   # For audio processing
   brew install portaudio
   
   # If you encounter PyAudio installation issues:
   pip install --global-option='build_ext' --global-option='-I/opt/homebrew/include' --global-option='-L/opt/homebrew/lib' pyaudio
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Usage Guide

### Getting Started

1. **Launch the Application**
   - Run `streamlit run app.py`
   - Open your browser to the provided URL (usually http://localhost:8501)

2. **Configure Quiz Settings**
   - Use the sidebar to set number of questions, difficulty level, and topic focus
   - Enable/disable voice mode and auto-play features

3. **Upload Content**
   - **Option 1**: Upload a document (PDF, DOCX, or TXT)
   - **Option 2**: Enter topic or content manually

4. **Generate Quiz**
   - Click "Generate Quiz Questions" to create your quiz
   - Wait for AI processing to complete

### Taking a Quiz

1. **Voice Mode** (Recommended)
   - Click "🔊 Play Question" to hear the question
   - Click the microphone button to record your answer
   - Say "A", "B", "C", or "D" clearly

2. **Text Mode** (Backup)
   - Read the question and options on screen
   - Select your answer using radio buttons
   - Click "Submit Answer"

3. **Receive Feedback**
   - Get immediate feedback on correctness
   - Listen to or read detailed explanations
   - View your current score and progress

### Voice Commands

The system recognizes various voice inputs for answers:
- **Direct**: "A", "B", "C", "D"
- **Spelled**: "Alpha", "Bravo", "Charlie", "Delta"
- **Descriptive**: "Option A", "Option B", etc.

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_MODEL` | GPT model to use | gpt-3.5-turbo |
| `DEFAULT_QUESTIONS_PER_QUIZ` | Default number of questions | 10 |
| `TTS_LANGUAGE` | Text-to-speech language | en |
| `SPEECH_RECOGNITION_LANGUAGE` | Speech recognition language | en-US |

### Customization

- **Difficulty Levels**: Modify `DIFFICULTY_LEVELS` in config.py
- **Performance Thresholds**: Adjust `PERFORMANCE_THRESHOLD` for adaptive difficulty
- **Audio Settings**: Configure timeout values for speech recognition
- **File Limits**: Modify `MAX_FILE_SIZE_MB` and `ALLOWED_EXTENSIONS`

## Troubleshooting

### Common Issues

1. **PyAudio Installation Error**
   ```bash
   # macOS with Homebrew
   brew install portaudio
   pip install pyaudio
   
   # Ubuntu/Debian
   sudo apt-get install portaudio19-dev
   pip install pyaudio
   ```

2. **OpenAI API Errors**
   - Verify your API key is correct
   - Check your OpenAI account has sufficient credits
   - Ensure API key has proper permissions

3. **Microphone Not Working**
   - Check browser permissions for microphone access
   - Verify microphone is working in other applications
   - Try refreshing the page

4. **Audio Playback Issues**
   - Ensure speakers/headphones are connected
   - Check system audio settings
   - Try different browsers (Chrome recommended)

### Performance Tips

- **Large Documents**: For documents over 10MB, consider splitting into smaller sections
- **Internet Connection**: Stable connection required for OpenAI API and speech services
- **Browser Compatibility**: Chrome and Firefox work best for audio features

## Technical Architecture

### Components

- **Document Processor**: Handles file upload and text extraction
- **Question Generator**: Interfaces with OpenAI GPT for question creation
- **Voice Handler**: Manages speech recognition and text-to-speech
- **Quiz Manager**: Orchestrates quiz sessions and performance tracking
- **Streamlit App**: Provides the user interface and coordination

### Data Flow

1. Document upload → Text extraction → Content preprocessing
2. Content + settings → GPT API → Generated questions
3. Questions → TTS → Audio playback
4. Voice input → Speech recognition → Answer processing
5. Answer evaluation → Feedback generation → TTS feedback
6. Performance tracking → Adaptive difficulty adjustment

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please:
1. Check the troubleshooting section above
2. Review the GitHub issues
3. Create a new issue with detailed information about your problem
