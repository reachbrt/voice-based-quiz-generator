import PyPDF2
import docx
import streamlit as st
from typing import Optional, List
import tempfile
import os

class DocumentProcessor:
    """Handles document upload and content extraction"""
    
    def __init__(self):
        self.supported_formats = ['pdf', 'docx', 'txt']
    
    def extract_text_from_file(self, uploaded_file) -> Optional[str]:
        """Extract text content from uploaded file"""
        try:
            file_extension = uploaded_file.name.split('.')[-1].lower()
            
            if file_extension == 'pdf':
                return self._extract_from_pdf(uploaded_file)
            elif file_extension == 'docx':
                return self._extract_from_docx(uploaded_file)
            elif file_extension == 'txt':
                return self._extract_from_txt(uploaded_file)
            else:
                st.error(f"Unsupported file format: {file_extension}")
                return None
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            return None
    
    def _extract_from_pdf(self, uploaded_file) -> str:
        """Extract text from PDF file"""
        text = ""
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            # Read PDF
            with open(tmp_file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            
            # Clean up temporary file
            os.unlink(tmp_file_path)
            
        except Exception as e:
            st.error(f"Error reading PDF: {str(e)}")
            
        return text.strip()
    
    def _extract_from_docx(self, uploaded_file) -> str:
        """Extract text from DOCX file"""
        text = ""
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            # Read DOCX
            doc = docx.Document(tmp_file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            # Clean up temporary file
            os.unlink(tmp_file_path)
            
        except Exception as e:
            st.error(f"Error reading DOCX: {str(e)}")
            
        return text.strip()
    
    def _extract_from_txt(self, uploaded_file) -> str:
        """Extract text from TXT file"""
        try:
            # Decode the uploaded file
            text = uploaded_file.getvalue().decode('utf-8')
            return text.strip()
        except UnicodeDecodeError:
            try:
                # Try with different encoding
                text = uploaded_file.getvalue().decode('latin-1')
                return text.strip()
            except Exception as e:
                st.error(f"Error reading text file: {str(e)}")
                return ""
    
    def preprocess_text(self, text: str) -> str:
        """Clean and preprocess extracted text"""
        if not text:
            return ""
        
        # Basic text cleaning
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:  # Filter out very short lines
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def chunk_text(self, text: str, chunk_size: int = 2000) -> List[str]:
        """Split text into manageable chunks for processing"""
        if not text:
            return []
        
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 > chunk_size and current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
            else:
                current_chunk.append(word)
                current_length += len(word) + 1
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
