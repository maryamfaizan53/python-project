import streamlit as st
import random

# Initialize session state for score tracking
if 'score' not in st.session_state:
    st.session_state.score = {'wins': 0, 'losses': 0, 'ties': 0}

# Function to determine the winner
def is_win(player, opponent):
    """Determines if the player wins against the opponent."""
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

# Main game logic
def play(user_choice):
    """Plays a game of Rock, Paper, Scissors."""
    computer_choice = random.choice(['r', 'p', 's'])

    # Map choices to emojis for better visualization
    choices = {'r': '✊ Rock', 'p': '✋ Paper', 's': '✌️ Scissors'}

    st.session_state.user_choice = choices[user_choice]
    st.session_state.computer_choice = choices[computer_choice]

    if user_choice == computer_choice:
        st.session_state.result = "It's a tie! 😐"
        st.session_state.score['ties'] += 1
    elif is_win(user_choice, computer_choice):
        st.session_state.result = "You Won! 🎉"
        st.session_state.score['wins'] += 1
    else:
        st.session_state.result = "You Lost! 😢"
        st.session_state.score['losses'] += 1

# Streamlit app
def main():
    st.title("Rock, Paper, Scissors Game 🎮")
    st.write("Welcome to the game! Choose your move below:")

    # Display score
    st.subheader("Score 🏆")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Wins", st.session_state.score['wins'])
    with col2:
        st.metric("Losses", st.session_state.score['losses'])
    with col3:
        st.metric("Ties", st.session_state.score['ties'])

    # Buttons for user choice
    st.subheader("Make Your Move ✨")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✊ Rock"):
            play('r')
    with col2:
        if st.button("✋ Paper"):
            play('p')
    with col3:
        if st.button("✌️ Scissors"):
            play('s')

    # Display results
    if 'result' in st.session_state:
        st.subheader("Result 🎲")
        st.write(f"**You chose:** {st.session_state.user_choice}")
        st.write(f"**Computer chose:** {st.session_state.computer_choice}")
        if "Won" in st.session_state.result:
            st.success(st.session_state.result)
        elif "Lost" in st.session_state.result:
            st.error(st.session_state.result)
        else:
            st.warning(st.session_state.result)

    # Progress bars for score visualization
    st.subheader("Progress 📊")
    total_games = sum(st.session_state.score.values())
    if total_games > 0:
        win_rate = st.session_state.score['wins'] / total_games
        loss_rate = st.session_state.score['losses'] / total_games
        tie_rate = st.session_state.score['ties'] / total_games
        st.progress(win_rate, text=f"Wins: {st.session_state.score['wins']}")
        st.progress(loss_rate, text=f"Losses: {st.session_state.score['losses']}")
        st.progress(tie_rate, text=f"Ties: {st.session_state.score['ties']}")
    else:
        st.write("No games played yet. Make your move!")

# Run the app
if __name__ == "__main__":
    main()