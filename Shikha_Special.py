import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="For Shikha ❤️", page_icon="🌹", layout="centered")

# Custom CSS for the "Romantic Interface"
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 40px;
        text-align: center;
        color: white;
    }
    .heart-anim {
        font-size: 100px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .apology-text {
        font-family: 'Georgia', serif;
        font-size: 20px;
        line-height: 1.6;
        color: #5c0a1a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    # Landing Screen
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='heart-anim'>💝</div>", unsafe_allow_html=True)
    st.title("Hey Shikha...")
    st.write("I've put my heart into this code just for you.")
    
    if st.button("Unlock My Message"):
        with st.spinner("One second..."):
            time.sleep(1)
            st.session_state.unlocked = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # The Main Surprise
    st.balloons() # Romantic entrance
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #d81b60;'>To My Dearest Shikha</h1>", unsafe_allow_html=True)
    
    # The Heartfelt Apology
    st.markdown(f"""
    <div class='apology-text'>
    <b>Shikha, I am very sorry.</b> <br><br>
    I know that due to my <u>overthinking</u>, you face many difficulties and stress. 
    It breaks my heart to know that my mind sometimes creates trouble for the person I love most. <br><br>
    But please believe me—<b>deep down, I love you a lot.</b> <br>
    You are my everything, my peace, and my home. <br><br>
    Can we please forgive the past and <b>start a new beginning</b> together?
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interaction
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("❤️ Click to forgive me ❤️"):
            st.snow()
            st.success("You are the best! I love you Shikha! 🥂")
            st.info("Let's make this Valentine's Day the best one yet.")
            
    st.markdown("</div>", unsafe_allow_html=True)