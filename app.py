import streamlit as st
import time
from document_processor import DocumentProcessor
from question_generator import QuestionGenerator
from voice_handler import VoiceHandler
from quiz_manager import QuizManager
from config import Config
import plotly.express as px
import plotly.graph_objects as go
# from streamlit_audio_recorder import audio_recorder  # Optional dependency

# Page configuration
st.set_page_config(
    page_title="Voice-Based Quiz Generator",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize components
@st.cache_resource
def initialize_components():
    """Initialize all components"""
    try:
        Config.validate_config()
        doc_processor = DocumentProcessor()
        question_generator = QuestionGenerator()
        voice_handler = VoiceHandler()
        quiz_manager = QuizManager()
        return doc_processor, question_generator, voice_handler, quiz_manager
    except Exception as e:
        st.error(f"Initialization error: {str(e)}")
        st.stop()

def main():
    """Main application function"""
    
    # Initialize components
    doc_processor, question_generator, voice_handler, quiz_manager = initialize_components()
    
    # Sidebar
    with st.sidebar:
        st.title("🎤 Quiz Settings")
        
        # Quiz configuration
        st.subheader("Quiz Configuration")
        num_questions = st.slider("Number of Questions", 3, 20, Config.DEFAULT_QUESTIONS_PER_QUIZ)
        difficulty = st.selectbox("Difficulty Level", Config.DIFFICULTY_LEVELS, index=1)
        topic_focus = st.text_input("Topic Focus (optional)", placeholder="e.g., Machine Learning")
        
        # Voice settings
        st.subheader("Voice Settings")
        use_voice = st.checkbox("Enable Voice Mode", value=True)
        auto_play = st.checkbox("Auto-play Questions", value=True)
        
        # Session controls
        st.subheader("Session Controls")
        if st.button("Reset Session", type="secondary"):
            quiz_manager.reset_session()
            st.rerun()
    
    # Main content
    st.title("🎤 Voice-Based Quiz Generator")
    st.markdown("Upload documents, generate quiz questions, and take voice-based quizzes with immediate feedback!")
    
    # Check if quiz is active
    if st.session_state.get('quiz_session', {}).get('session_active', False):
        display_quiz_interface(quiz_manager, voice_handler, use_voice, auto_play)
    else:
        display_setup_interface(doc_processor, question_generator, quiz_manager, 
                               num_questions, difficulty, topic_focus)

def display_setup_interface(doc_processor, question_generator, quiz_manager, 
                           num_questions, difficulty, topic_focus):
    """Display the quiz setup interface"""
    
    tab1, tab2, tab3 = st.tabs(["📄 Document Upload", "📝 Manual Topic", "📊 Previous Results"])
    
    with tab1:
        st.subheader("Upload Document")
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=Config.ALLOWED_EXTENSIONS,
            help=f"Supported formats: {', '.join(Config.ALLOWED_EXTENSIONS)}"
        )
        
        if uploaded_file:
            with st.spinner("Processing document..."):
                # Extract text
                raw_text = doc_processor.extract_text_from_file(uploaded_file)
                
                if raw_text:
                    # Preprocess text
                    processed_text = doc_processor.preprocess_text(raw_text)
                    
                    # Display preview
                    with st.expander("Document Preview"):
                        st.text_area("Extracted Content", processed_text[:1000] + "..." if len(processed_text) > 1000 else processed_text, height=200)
                    
                    # Generate questions button
                    if st.button("Generate Quiz Questions", type="primary"):
                        generate_and_start_quiz(question_generator, quiz_manager, 
                                              processed_text, num_questions, difficulty, topic_focus)
    
    with tab2:
        st.subheader("Enter Topic Manually")
        manual_topic = st.text_area(
            "Enter topic or content for quiz generation:",
            height=200,
            placeholder="Enter the topic, concepts, or content you want to be quizzed on..."
        )
        
        if manual_topic and st.button("Generate Quiz from Topic", type="primary"):
            generate_and_start_quiz(question_generator, quiz_manager, 
                                  manual_topic, num_questions, difficulty, topic_focus)
    
    with tab3:
        display_previous_results(quiz_manager)

def generate_and_start_quiz(question_generator, quiz_manager, content, 
                          num_questions, difficulty, topic_focus):
    """Generate questions and start quiz"""
    with st.spinner("Generating quiz questions..."):
        questions = question_generator.generate_questions(
            content, num_questions, difficulty, topic_focus
        )
        
        if questions:
            quiz_manager.start_quiz(questions, difficulty)
            st.success(f"Generated {len(questions)} questions! Starting quiz...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Failed to generate questions. Please try again.")

def display_quiz_interface(quiz_manager, voice_handler, use_voice, auto_play):
    """Display the active quiz interface"""
    
    # Quiz progress
    progress = quiz_manager.get_quiz_progress()
    st.progress(progress['progress_percentage'] / 100)
    st.write(f"Question {progress['current_question']} of {progress['total_questions']}")
    
    # Get current question
    current_question = quiz_manager.get_current_question()
    
    if current_question:
        display_question(current_question, quiz_manager, voice_handler, use_voice, auto_play)
    else:
        display_quiz_results(quiz_manager)

def display_question(question, quiz_manager, voice_handler, use_voice, auto_play):
    """Display current question"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Question")
        st.write(question['question'])
        
        # Display options
        st.subheader("Options")
        for key, value in question['options'].items():
            st.write(f"**{key}:** {value}")
    
    with col2:
        if use_voice:
            st.subheader("Voice Controls")
            
            # Play question audio
            if st.button("🔊 Play Question"):
                with st.spinner("Generating audio..."):
                    audio_file = voice_handler.create_question_audio(question)
                    if audio_file:
                        audio_html = voice_handler.get_audio_html(audio_file)
                        st.markdown(audio_html, unsafe_allow_html=True)
                        voice_handler.cleanup_temp_files([audio_file])
            
            # Voice answer recording (simplified for demo)
            st.write("🎤 Voice Recording:")
            st.info("Voice recording feature requires additional setup. For now, please use the text input below.")

            # Placeholder for future voice recording implementation
            if st.button("🎤 Record Answer (Coming Soon)"):
                st.warning("Voice recording will be available after installing additional audio dependencies.")
    
    # Text answer input (always available as backup)
    st.subheader("Text Answer")
    answer_choice = st.radio("Select your answer:", ['A', 'B', 'C', 'D'], horizontal=True)
    
    if st.button("Submit Answer", type="primary"):
        process_answer(answer_choice, quiz_manager, voice_handler, use_voice)

def process_answer(user_answer, quiz_manager, voice_handler, use_voice):
    """Process submitted answer"""
    
    # Submit answer
    result = quiz_manager.submit_answer(user_answer)
    
    if 'error' in result:
        st.error(result['error'])
        return
    
    # Display feedback
    if result['is_correct']:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer was {result['correct_answer']}")
    
    st.info(f"**Explanation:** {result['explanation']}")
    st.write(f"**Score:** {result['score']:.2f}")
    
    # Voice feedback
    if use_voice:
        with st.spinner("Generating audio feedback..."):
            feedback_audio = voice_handler.create_feedback_audio(
                result['is_correct'], 
                result['correct_answer'], 
                result['explanation'],
                user_answer
            )
            if feedback_audio:
                audio_html = voice_handler.get_audio_html(feedback_audio)
                st.markdown(audio_html, unsafe_allow_html=True)
                voice_handler.cleanup_temp_files([feedback_audio])
    
    # Continue button
    if result['quiz_complete']:
        st.balloons()
        st.success("🎉 Quiz Complete!")
        if st.button("View Results"):
            st.rerun()
    else:
        if st.button("Next Question"):
            st.rerun()

def display_quiz_results(quiz_manager):
    """Display quiz results and statistics"""
    
    st.title("📊 Quiz Results")
    
    stats = quiz_manager.get_session_stats()
    
    if stats.get('no_data'):
        st.warning("No quiz data available.")
        return
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", f"{stats['accuracy_percentage']:.1f}%")
    
    with col2:
        st.metric("Total Score", f"{stats['total_score']:.1f}")
    
    with col3:
        st.metric("Questions", f"{stats['correct_answers']}/{stats['total_questions']}")
    
    with col4:
        if stats['session_duration']:
            st.metric("Duration", f"{stats['session_duration']:.0f}s")
    
    # Detailed results
    st.subheader("Detailed Results")
    results_df = quiz_manager.get_detailed_results()
    if not results_df.empty:
        st.dataframe(results_df, use_container_width=True)
    
    # Performance chart
    if len(quiz_manager.get_performance_trend()) > 0:
        st.subheader("Performance Trend")
        trend_data = quiz_manager.get_performance_trend()
        fig = px.line(
            x=list(range(1, len(trend_data) + 1)),
            y=trend_data,
            title="Performance Over Time",
            labels={'x': 'Question Number', 'y': 'Score'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Export options
    st.subheader("Export Results")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Download Results (JSON)"):
            export_data = quiz_manager.export_session_data()
            st.download_button(
                label="Download JSON",
                data=export_data,
                file_name=f"quiz_results_{int(time.time())}.json",
                mime="application/json"
            )
    
    with col2:
        if st.button("Start New Quiz"):
            quiz_manager.reset_session()
            st.rerun()

def display_previous_results(quiz_manager):
    """Display previous quiz results"""
    st.write("Previous quiz results will be displayed here.")
    st.info("This feature will show historical performance data in future versions.")

if __name__ == "__main__":
    main()
