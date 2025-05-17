# Hadith Audio Access App

## Overview
A Streamlit-based web application that provides authenticated access to Hadith collections in Arabic, Urdu, and English text formats. Users can unlock audio versions (using gTTS) of the Hadith by making a one-time $10 payment via Stripe.

## Key Features
- User authentication (Signup/Login) via Supabase
- Free access to Hadith texts in Arabic, Urdu, and English
- Premium audio access after one-time $10 payment
- Text-to-speech functionality using gTTS for Arabic/Urdu/English
- Payment processing via Stripe integration
- Data storage and user management with Supabase

## Business Logic

### 1. User Flow
1. **Signup/Login**: Users must create an account or login to access content
2. **Free Access**: All authenticated users can read Hadith in text format
3. **Premium Upgrade**: 
   - Users can pay $10 one-time fee for audio access
   - Payment processed via Stripe
   - On successful payment, user's `has_premium_access` flag is set to True in Supabase
4. **Audio Access**: Premium users can listen to Hadith in their preferred language

### 2. Revenue Model
- One-time payment of $10 for lifetime audio access
- No subscriptions or recurring charges
- Entire payment goes to platform owner (minus Stripe processing fees)

### 3. Value Proposition
- Free access to authentic Hadith texts
- Convenient audio access for on-the-go learning
- Multi-language support (Arabic/Urdu/English)
- One-time payment model (no subscriptions)

## Technology Stack
- **Frontend**: Streamlit (Python)
- **Authentication/Database**: Supabase
- **Payment Processing**: Stripe
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Hosting**: Streamlit 
