"""
HadithDisplay component with integrated payment system for audio features
"""

import streamlit as st
from gtts import gTTS
import tempfile
import os
import base64
from components.payment import Payment

class HadithDisplay:
    def __init__(self, hadiths):
        self.hadiths = hadiths
        self.payment = Payment()
        
        # CSS styling
        st.markdown("""
        <style>
            .arabic-text {
                font-family: 'Traditional Arabic', Arial, sans-serif;
                font-size: 24px;
                text-align: right;
                direction: rtl;
                margin: 20px 0;
            }
            .translation-text {
                font-size: 18px;
                margin: 15px 0;
                padding: 10px;
                border-radius: 5px;
            }
            .reference-text {
                font-style: italic;
                color: #666;
                margin-top: 10px;
            }
            .audio-button {
                margin: 5px;
                width: 100%;
            }
            .payment-required {
                background-color: #fff3cd;
                padding: 15px;
                border-radius: 5px;
                margin: 10px 0;
            }
        </style>
        """, unsafe_allow_html=True)

    def play_audio(self, text, language):
        """Play audio for the given text in the specified language."""
        # Check if user is logged in
        if 'user' not in st.session_state or not st.session_state.user:
            st.warning("Please sign in to access audio features")
            return
            
        # Get user email
        user_email = st.session_state.user.email
        
        # Check payment status first
        if not self.payment.check_payment_status(user_email):
            st.markdown('<div class="payment-required">', unsafe_allow_html=True)
            st.warning("Audio access requires a one-time payment of $10")
            if self.payment.handle_payment_flow(user_email):
                # If payment was successful, play the audio
                self._generate_and_play_audio(text, language)
            st.markdown('</div>', unsafe_allow_html=True)
            return
            
        # If payment is completed, play audio directly
        self._generate_and_play_audio(text, language)
            
    def _generate_and_play_audio(self, text, language):
        """Generate and play audio for the given text"""
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                temp_path = temp_file.name
                
            # Generate audio
            tts = gTTS(text=text, lang=language)
            tts.save(temp_path)
            
            # Play audio
            with open(temp_path, "rb") as f:
                audio_bytes = f.read()
            
            # Create audio player with autoplay
            audio_base64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
                <audio autoplay controls style="width:100%">
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
            
            # Clean up
            os.unlink(temp_path)
            
        except Exception as e:
            st.error(f"Error playing audio: {str(e)}")

    def display_hadith(self):
        """Display the hadith selection interface and content"""
        st.title("Hadith Explorer")
        
        # Collection selection
        collection = st.selectbox(
            "Select Hadith Collection",
            list(self.hadiths.keys()),
            key="hadith_collection"
        )
        
        if not collection:
            return
            
        # Book selection
        book = st.selectbox(
            "Select Book",
            list(self.hadiths[collection].keys()),
            key="hadith_book"
        )
        
        if not book:
            return
            
        # Hadith selection
        hadith_list = list(self.hadiths[collection][book].keys())
        hadith = st.selectbox(
            "Select Hadith",
            hadith_list,
            key="hadith_selection"
        )
        
        if not hadith:
            return
            
        # Display selected hadith
        hadith_data = self.hadiths[collection][book][hadith]
        
        # Arabic text
        st.markdown('<div class="arabic-text">' + hadith_data["arabic"] + '</div>', unsafe_allow_html=True)
        
        # Translations (always visible)
        st.subheader("English Translation")
        st.markdown('<div class="translation-text">' + hadith_data["english"] + '</div>', unsafe_allow_html=True)
        
        st.subheader("Urdu Translation")
        st.markdown('<div class="translation-text">' + hadith_data["urdu"] + '</div>', unsafe_allow_html=True)
        
        # Reference
        st.markdown('<div class="reference-text">Reference: ' + hadith_data["reference"] + '</div>', unsafe_allow_html=True)
        
        # Audio section with payment check
        st.subheader("Audio Features")
        
        # Check if user is logged in
        if 'user' not in st.session_state or not st.session_state.user:
            st.warning("Please sign in to access audio features")
            return
            
        # Get user email
        user_email = st.session_state.user.email
        
        # Check payment status
        has_paid = self.payment.check_payment_status(user_email)
        
        if has_paid:
            st.success("You have permanent access to audio features!")
        else:
            st.warning("One-time payment of $10 required for audio features")
        
        # Audio buttons in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔊 Arabic Audio", key="arabic_audio", use_container_width=True):
                self.play_audio(hadith_data["arabic"], "ar")
        with col2:
            if st.button("🔊 English Audio", key="english_audio", use_container_width=True):
                self.play_audio(hadith_data["english"], "en")
        with col3:
            if st.button("🔊 Urdu Audio", key="urdu_audio", use_container_width=True):
                self.play_audio(hadith_data["urdu"], "ur")

    def _add_to_favorites(self, user_email, collection, book, hadith):
        """Add hadith to user's favorites in Supabase"""
        try:
            self.supabase.table('favorites').insert({
                'user_email': user_email,
                'collection': collection,
                'book': book,
                'hadith': hadith,
                'timestamp': 'now()'
            }).execute()
        except Exception as e:
            st.error(f"Error adding to favorites: {str(e)}")