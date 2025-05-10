import streamlit as st
from transformers import pipeline
import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
import docx
import os

# --- AI-based Sentiment Analysis Class ---
class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis")
    
    def analyze(self, text):
        result = self.analyzer(text)
        return result[0]['label'], result[0]['score']

# --- Text Extraction Class for Different File Types ---
class TextExtractor:
    def extract_text(self, file_path):
        raise NotImplementedError("This method should be overridden by subclasses")

class PDFTextExtractor(TextExtractor):
    def extract_text(self, file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

class DOCXTextExtractor(TextExtractor):
    def extract_text(self, file_path):
        doc = docx.Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text
        return text

class TXTTextExtractor(TextExtractor):
    def extract_text(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

# --- Smart File Analyzer Class ---
class SmartFileAnalyzer:
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        self.text_extractor = None

    def set_extractor(self, file_type):
        if file_type == "pdf":
            self.text_extractor = PDFTextExtractor()
        elif file_type == "docx":
            self.text_extractor = DOCXTextExtractor()
        elif file_type == "txt":
            self.text_extractor = TXTTextExtractor()
        else:
            raise ValueError("Unsupported file type")

    def analyze_file(self, file_path):
        text = self.text_extractor.extract_text(file_path)
        sentiment, score = self.sentiment_analyzer.analyze(text)
        return text, sentiment, score

# --- Streamlit App ---
def main():
    st.title("📂 Smart File Analyzer with AI (OOP Version)")

    st.write("Upload a file (PDF, DOCX, TXT) to analyze its content using AI:")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1].lower()
        
        # Save the uploaded file temporarily
        temp_file_path = f"temp_file.{file_type}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            # Initialize the SmartFileAnalyzer and choose the extractor
            analyzer = SmartFileAnalyzer()
            analyzer.set_extractor(file_type)
            
            # Analyze the file
            text, sentiment, score = analyzer.analyze_file(temp_file_path)

            # Display Results
            st.subheader("File Content Preview")
            st.text_area("Extracted Text", text[:1500], height=300)  # Preview first 1500 chars

            st.subheader("Sentiment Analysis Result")
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"**Confidence Score:** {score:.2f}")

        except ValueError as e:
            st.error(str(e))
        
        # Clean up the temporary file
        os.remove(temp_file_path)

if __name__ == "__main__":
    main()
st.write("Made with ❤️ by [Tehreem Abdullah]")


