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
        background-color: #1E90FF;
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
    for i in range(5):
        if i == 2:
            st.markdown("""
            <div class="balloon">
                <div class="button-container">
                    <form action="#">
                        <button type="submit" id="click-here">🎁 Click Here</button>
                    </form>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="balloon"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# First button to open the image
    if st.button('Click here'):
        st.image('saggi.jpg', caption='Here is your surprise!')


    # Streamlit button to display the image
    if st.button('🎁 Click to see your surprise'):
        st.image('saggi.jpg', use_column_width=True)  # Replace with your image path

    st.markdown(f'<div class="signature">With lots of love, <br> Komalpreet</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

show()
