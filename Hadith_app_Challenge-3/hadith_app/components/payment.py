"""
This module handles payment processing using Stripe with Supabase integration for permanent access.
"""

import streamlit as st
import stripe
import os
from dotenv import load_dotenv
from supabase import create_client, Client

class Payment:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize Stripe with your secret key
        stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
        
        # Initialize Supabase
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)
        
        # Initialize payment status in session state
        if 'payment_completed' not in st.session_state:
            st.session_state.payment_completed = False
            
    def check_payment_status(self, email: str) -> bool:
        """Check if user has already paid"""
        try:
            if not email:
                return False
                
            # Check in Supabase
            response = self.supabase.table('payments').select('*').eq('user_email', email).execute()
            
            # If payment exists and is completed, update session state
            if len(response.data) > 0:
                st.session_state.payment_completed = True
                return True
            return False
        except Exception as e:
            st.error(f"Error checking payment status: {str(e)}")
            return False
            
    def create_checkout_session(self, email: str):
        """Create a Stripe checkout session"""
        try:
            # Get current URL for redirects
            current_url = st.query_params.get('_stcore_streamlit_url', [''])[0]
            if not current_url:
                current_url = "http://localhost:8501"  # Default for local dev
                
            success_url = f"{current_url}?payment=success"
            cancel_url = f"{current_url}?payment=cancelled"
            
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Permanent Audio Access',
                            'description': 'One-time payment for lifetime audio access',
                        },
                        'unit_amount': 1000,  # $10.00
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
                customer_email=email,
                metadata={'user_email': email}
            )
            return checkout_session.url
        except Exception as e:
            st.error(f"Error creating checkout session: {str(e)}")
            return None
            
    def record_payment(self, email: str):
        """Record successful payment in Supabase"""
        try:
            # First check if payment already exists
            existing = self.supabase.table('payments').select('*').eq('user_email', email).execute()
            if len(existing.data) > 0:
                return True
                
            # If no existing payment, record new payment
            self.supabase.table('payments').insert({
                'user_email': email,
                'payment_status': 'completed'
            }).execute()
            
            # Update session state
            st.session_state.payment_completed = True
            return True
        except Exception as e:
            st.error(f"Error recording payment: {str(e)}")
            return False
            
    def handle_payment_flow(self, email: str):
        """Handle the complete payment flow"""
        # Check if already paid
        if self.check_payment_status(email):
            return True
            
        # Check for payment success callback
        query_params = st.query_params
        if 'payment' in query_params:
            if query_params['payment'][0] == 'success':
                if self.record_payment(email):
                    st.success("Payment successful! You now have permanent audio access.")
                    st.rerun()
                return True
            elif query_params['payment'][0] == 'cancelled':
                st.warning("Payment was cancelled. Please try again.")
                return False
                
        # Show payment button if not paid
        st.warning("One-time payment of $10 required for audio features")
        checkout_url = self.create_checkout_session(email)
        if checkout_url:
            st.markdown(f"""
            <a href="{checkout_url}" target="_blank">
                <button style="
                    background-color: #4CAF50;
                    color: white;
                    padding: 14px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                ">
                    💳 Pay $10 for Permanent Access
                </button>
            </a>
            """, unsafe_allow_html=True)
        return False