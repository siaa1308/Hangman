# Hangman AI Solver

An AI-powered Hangman solver that attempts to guess hidden words using probabilistic reasoning, candidate word filtering, and information-gain based letter selection.

This project was originally inspired by exploring how machine learning and search strategies can be applied to a classic word game. Rather than focusing on building a traditional playable Hangman game, the goal was to build an **AI agent capable of solving Hangman puzzles autonomously**.

<img width="1460" height="793" alt="Screenshot 2026-06-15 at 11 51 17 AM" src="https://github.com/user-attachments/assets/e9fd5ed3-5083-44b0-89e5-0ce6cdbc833b" />

---

# Project Goal

The objective of this project is not to achieve perfect Hangman performance.

Instead, the goal is to explore:

* Probabilistic decision making
* Candidate space reduction
* Information gain and entropy
* Language pattern recognition
* AI-assisted problem solving

The solver continuously narrows down possible words and selects letters that maximize the amount of information gained from each guess.

---

# How It Works

The solver follows a multi-step reasoning process:

### 1. Candidate Filtering

Given the current word pattern:

```text
a _ _ l e
```

the solver filters the corpus and keeps only words that:

* Match the known letters
* Match the word length
* Do not contain previously incorrect letters

---

### 2. Candidate Analysis

The remaining candidate words are analyzed to determine:

* Most common unseen letters
* Positional letter frequencies
* Information gain for future guesses

---

### 3. Letter Selection

The AI selects the letter that is expected to provide the most useful information while reducing uncertainty in the candidate set.

---

### 4. Iterative Solving

The process repeats until:

* The word is solved
* The AI runs out of lives

---

# Why Isn't The Accuracy Higher?

A common question is:

> "Why doesn't the AI solve every word?"

Hangman is fundamentally a game of incomplete information.

At the beginning of a game, the AI sees only:

```text
________
```

for an unknown 8-letter word.

Thousands of possible candidates may exist.

Some words contain rare letters such as:

```text
x
q
z
j
```

which are difficult to predict early.

Additionally:

* The AI only has a limited number of lives.
* The corpus may not contain every possible English word.
* Multiple candidate words can fit the same pattern.
* Early incorrect guesses can significantly reduce success rates.

Because of these constraints, even strong Hangman solvers are not guaranteed to achieve 100% accuracy.

The focus of this project is the reasoning process rather than perfect performance.

---

# Dataset Files

## corpus.txt

The training corpus used by the solver.

Contains approximately 50,000 English words.

Purpose:

* Candidate generation
* Letter frequency estimation
* Word pattern matching
* Statistical analysis

---

# User Interface

The project includes an interactive Streamlit interface that allows users to:

* Enter a secret word
* Watch the AI solve it in real time
* View confidence scores
* Track wrong guesses
* Monitor remaining lives
* Observe the solver's reasoning process

---

# Installation

Clone the repository:

```bash
git clone https://github.com/siaa1308/Hangman.git
cd Hangman
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running The Application

Launch the Streamlit interface:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# Tech Stack

### Language

* Python 3

### Libraries

* Streamlit
* NumPy
* Pandas
