import streamlit as st
from components.data.hadith_data import HADITHS
from components.hadith_display import HadithDisplay
from components.auth import Auth

class HadithApp:
    def __init__(self):
        self.setup_page()
        self.auth = Auth()
        self.hadith_display = HadithDisplay(HADITHS)
        
    def setup_page(self):
        st.set_page_config(
            page_title="Hadith Explorer",
            page_icon="📖",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.title("📖 Hadith Explorer")
        st.markdown("""
        <style>
        .arabic-text {
            font-size: 24px;
            text-align: right;
            direction: rtl;
            padding: 15px;
            
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .translation-text {
            font-size: 18px;
            padding: 15px;
            
            border-radius: 8px;
            line-height: 1.6;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            margin: 5px 0;
        }
        .reference-text {
            color: #666;
            font-size: 14px;
            margin-bottom: 20px;
        }
        .blur {
            filter: blur(5px);
            pointer-events: none;
        }
        </style>
        """, unsafe_allow_html=True)
        
    def run(self):
        # Authentication
        if not self.auth.is_authenticated():
            tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
            with tab1:
                self.auth.signin()
            with tab2:
                self.auth.signup()
        else:
            # Show sign out button in sidebar
            self.auth.signout()
            
            # Display hadith content
            self.hadith_display.display_hadith()

if __name__ == "__main__":
    app = HadithApp()
    app.run() 