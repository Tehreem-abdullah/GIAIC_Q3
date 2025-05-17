"""
This module contains the authentication component.
"""

import streamlit as st
from supabase import create_client, Client
import os
from dotenv import load_dotenv

class Auth:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Get Supabase credentials from environment variables
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        
        # Initialize Supabase client
        self.supabase: Client = create_client(url, key)
        
        # Initialize session state for auth
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        if 'user' not in st.session_state:
            st.session_state.user = None
            
    def signup(self):
        """Handle user signup."""
        st.subheader("Create New Account")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
        
        if st.button("Sign Up", key="signup_button"):
            if password != confirm_password:
                st.error("Passwords do not match!")
                return
                
            try:
                # Create user in Supabase
                response = self.supabase.auth.sign_up({
                    "email": email,
                    "password": password
                })
                st.success("Account created successfully! Please check your email for verification.")
            except Exception as e:
                st.error(f"Error creating account: {str(e)}")
                
    def signin(self):
        """Handle user signin."""
        st.subheader("Sign In")
        email = st.text_input("Email", key="signin_email")
        password = st.text_input("Password", type="password", key="signin_password")
        
        if st.button("Sign In", key="signin_button"):
            try:
                # Sign in with Supabase
                response = self.supabase.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })
                st.session_state.authenticated = True
                st.session_state.user = response.user
                st.success("Signed in successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error signing in: {str(e)}")
                
    def signout(self):
        """Handle user signout."""
        if st.sidebar.button("Sign Out"):
            try:
                self.supabase.auth.sign_out()
                st.session_state.authenticated = False
                st.session_state.user = None
                st.rerun()
            except Exception as e:
                st.error(f"Error signing out: {str(e)}")
                
    def is_authenticated(self):
        """Check if user is authenticated."""
        return st.session_state.authenticated 