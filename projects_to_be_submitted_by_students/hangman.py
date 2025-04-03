import streamlit as st
import random

# Custom CSS for Full-Screen Background
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap');
        
        /* Full-screen gradient background */
        .stApp {
            background: linear-gradient(45deg, #FF9A8B, #FF6B6B, #4ECDC4, #556270);
            background-size: 400% 400%;
            animation: gradientBG 10s ease infinite;
            min-height: 100vh;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        /* Main content container */
        .main-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem auto;
            max-width: 800px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }

        .title {
            color: #FFD700;
            font-family: 'Comic Neue', cursive;
            font-size: 3.5rem !important;
            text-align: center;
            text-shadow: 2px 2px #4ECDC4;
            margin-bottom: 30px;
        }

        .scoreboard {
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            margin: 20px;
            color: white;
        }

        /* Keyboard buttons */
        .stButton>button {
            background: rgba(255, 255, 255, 0.9) !important;
            color: #4ECDC4 !important;
            border-radius: 10px !important;
            border: 2px solid #4ECDC4 !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
        }

        .stButton>button:disabled {
            background: rgba(255, 107, 107, 0.5) !important;
            color: white !important;
        }

        .stButton>button:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(78, 205, 196, 0.4);
        }

    </style>
""", unsafe_allow_html=True)

# Words for the game
words = ["ALPACIN", "PYTHON", "STREAMLIT", "DEVELOPER", "HANGMAN"]

# Initialize game state
if 'game' not in st.session_state:
    st.session_state.game = {
        'word': random.choice(words),
        'guessed': [],
        'attempts': 6,
        'wins': 0,
        'losses': 0
    }

# Function to update the game
def update_game(letter):
    game = st.session_state.game
    if letter not in game['word'].upper():
        game['attempts'] -= 1
    game['guessed'].append(letter)
    
    # Check win/lose conditions
    if all(c in game['guessed'] for c in game['word'].upper()):
        game['wins'] += 1
        st.balloons()
    elif game['attempts'] <= 0:
        game['losses'] += 1

# Main content container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title with Emoji
st.markdown('<h1 class="title">✨ Hangman (Word Game) 🎨</h1>', unsafe_allow_html=True)

# Display word
display_word = ' '.join([c if c in st.session_state.game['guessed'] else '_' for c in st.session_state.game['word'].upper()])
st.markdown(f'<h2 style="text-align:center; color:#FFD700; font-size:2rem;">{display_word}</h2>', unsafe_allow_html=True)

# Attempts left with emoji
attempts_visual = ' '.join(['🟢'] * st.session_state.game['attempts'] + ['🔴'] * (6 - st.session_state.game['attempts']))
st.markdown(f"### ❤️ Attempts Left: {attempts_visual}")

# 🎹 Keyboard (Horizontal layout)
cols = st.columns(13)
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    with cols[i % 13]:
        if letter not in st.session_state.game['guessed']:
            if st.button(letter, key=f"btn_{letter}"):
                update_game(letter)
        else:
            st.button(letter, disabled=True, key=f"disabled_{letter}")

# Scoreboard
st.markdown('<div class="scoreboard">', unsafe_allow_html=True)
st.markdown(f"🏆 Wins: {st.session_state.game['wins']}  |  💀 Losses: {st.session_state.game['losses']}", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Restart Button
if st.button('🔁 New Game'):
    st.session_state.game = {
        'word': random.choice(words),
        'guessed': [],
        'attempts': 6,
        'wins': st.session_state.game['wins'],
        'losses': st.session_state.game['losses']
    }

# Close main container
st.markdown('</div>', unsafe_allow_html=True)