import streamlit as st
from streamlit_extras.let_it_rain import rain

# Page Configuration
st.set_page_config(page_title="For Shikha ❤️", page_icon="🌹", layout="centered")

# Custom Styles
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    .letter-box {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #ff4d6d;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        color: #333;
    }
    .shikha-title {
        font-family: 'Dancing Script', cursive;
        color: #c9184a;
        font-size: 45px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initial Screen
if 'opened' not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<div class='letter-box'>", unsafe_allow_html=True)
    st.header("Hey Shikha... 💌")
    st.write("I've been holding onto something I wanted to show you.")
    if st.button("Open the message"):
        st.session_state.opened = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # Falling Hearts Animation
    rain(emoji="❤️", font_size=40, falling_speed=5, animation_length="infinite")

    st.markdown("<div class='letter-box'>", unsafe_allow_html=True)
    st.markdown("<h1 class='shikha-title'>To My Dearest Shikha</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    **I am so deeply sorry.** I know that because of my **overthinking**, you've had to face many difficulties and stress that you didn't deserve. It hurts me to know that my mind sometimes creates walls between us.
    
    But please believe me—**deep down, I love you a lot.** You are my everything, and the last thing I ever want to do is make your life harder.
    
    Can we please leave the past behind and **start a new beginning today?** """)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("I Forgive You ❤️"):
        st.balloons()
        st.success("Thank you, Shikha. You just made me the luckiest person in the world.")
        st.snow()
    
    st.markdown("</div>", unsafe_allow_html=True)