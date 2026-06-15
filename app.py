import streamlit as st
import time

from solver import HangmanAI

st.set_page_config(
    page_title="Hangman AI",
    page_icon="🎯",
    layout="wide"
)

solver = HangmanAI()

st.title("🎯 Hangman AI Solver")

word = st.text_input(
    "Enter a secret word"
).lower()

speed = st.slider(
    "Animation Speed",
    0.1,
    2.0,
    0.5
)

if st.button("Solve"):

    if not word.isalpha():

        st.error("Only letters allowed")
        st.stop()

    guessed = set()

    wrong_letters = set()

    lives = 6

    pattern = ["_"] * len(word)

    board = st.empty()

    metrics = st.empty()

    history_box = st.empty()

    history = []

    while "_" in pattern and lives > 0:

        guess, confidence = solver.choose_letter(
            "".join(pattern),
            guessed,
            wrong_letters
        )

        guessed.add(guess)

        if guess in word:

            for i, ch in enumerate(word):

                if ch == guess:
                    pattern[i] = ch

        else:

            wrong_letters.add(guess)
            lives -= 1

        history.append(
            (guess, confidence)
        )

        board.markdown(
            f"""
## Pattern

{' '.join(pattern)}

## Lives Remaining

{lives}

## Wrong Guesses

{', '.join(sorted(wrong_letters))}
"""
        )

        metrics.progress(
            min(confidence / 100, 1.0)
        )

        history_box.markdown(
            "\n".join(
                [
                    f"**{g.upper()}** → {c}%"
                    for g, c in history
                ]
            )
        )

        time.sleep(speed)

    st.divider()

    if "_" not in pattern:

        st.success(
            f"🎉 SOLVED: {word}"
        )

    else:

        st.error(
            f"💀 FAILED: {word}"
        )