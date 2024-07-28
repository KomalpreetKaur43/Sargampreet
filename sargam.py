import streamlit as st

def show():
    st.markdown("""
    <style>
    .container {
        text-align: center;
        color: #FFD700;
        background-color: #1E1E1E;
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
    }
    .header {
        font-size: 60px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 40px;
        margin-bottom: 20px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .message {
        font-size: 25px;
        margin-bottom: 30px;
        font-style: italic;
    }
    .signature {
        font-size: 20px;
        margin-top: 50px;
        font-style: normal;
        color: #FF69B4;
    }
    .gift-box {
        margin: 20px auto;
        width: 150px;
        height: 150px;
        background-color: #FF4500;
        border-radius: 10%;
        position: relative;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
    }
    .gift-box::before, .gift-box::after {
        content: '';
        position: absolute;
        background-color: #FFD700;
    }
    .gift-box::before {
        top: 50%;
        left: 0;
        width: 100%;
        height: 20px;
        transform: translateY(-50%);
    }
    .gift-box::after {
        top: 0;
        left: 50%;
        width: 20px;
        height: 100%;
        transform: translateX(-50%);
    }
    .balloons {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    .balloon {
        width: 60px;
        height: 80px;
        margin: 10px;
        border-radius: 50%;
        background-color: #1E90FF; /* Blue color */
        position: relative;
        animation: float 3s ease-in-out infinite;
    }
    .balloon::before {
        content: '';
        position: absolute;
        bottom: -15px;
        left: 50%;
        width: 2px;
        height: 30px;
        background: white;
        transform: translateX(-50%);
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<div class="header">🎂 Happy Birthday, Sargam! 🎈</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">To the Best Little Brother Ever!</div>', unsafe_allow_html=True)
    st.markdown('<div class="message">On your special day, I just want to say how much you mean to me. You bring so much joy and happiness into our lives, and I am so lucky to have a brother like you. Enjoy every moment, have fun, and make this day as amazing as you are!</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="balloons">', unsafe_allow_html=True)
    for _ in range(5):
        st.markdown('<div class="balloon"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button('🎁 Click here!'):
        st.image('saggi.jpg', use_column_width=True)  # Replace with your image path


    if st.button('🎁 Click to Open Your Gift!'):
        st.image('bullet.jpg', use_column_width=True)  # Replace with your image path

    st.markdown(f'<div class="signature">With lots of love, <br> Komalpreet</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

show()
