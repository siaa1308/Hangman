from collections import defaultdict, Counter
import math

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class HangmanAI:

    def __init__(self, corpus_file="corpus.txt"):

        with open(corpus_file, "r", encoding="utf-8") as f:
            self.words = [
                w.strip().lower()
                for w in f
                if w.strip().isalpha()
            ]

        self.words_by_length = defaultdict(list)

        for word in self.words:
            self.words_by_length[len(word)].append(word)

    def filter_candidates(
        self,
        pattern,
        wrong_letters
    ):

        candidates = self.words_by_length[len(pattern)]

        filtered = []

        for word in candidates:

            valid = True

            for i, ch in enumerate(pattern):

                if ch != "_" and word[i] != ch:
                    valid = False
                    break

            if not valid:
                continue

            if any(
                x in word
                for x in wrong_letters
            ):
                continue

            filtered.append(word)

        return filtered

    def entropy_score(
        self,
        candidates,
        guessed
    ):

        scores = {}

        total = len(candidates)

        for letter in ALPHABET:

            if letter in guessed:
                continue

            contain = sum(
                1
                for w in candidates
                if letter in w
            )

            p = contain / total if total else 0

            scores[letter] = p * (1 - p)

        return scores

    def positional_score(
        self,
        candidates,
        pattern,
        guessed
    ):

        score = Counter()

        for word in candidates:

            for i, ch in enumerate(word):

                if (
                    pattern[i] == "_"
                    and ch not in guessed
                ):
                    score[ch] += 1

        return score

    def choose_letter(
        self,
        pattern,
        guessed,
        wrong_letters
    ):

        candidates = self.filter_candidates(
            pattern,
            wrong_letters
        )

        if not candidates:

            remaining = [
                c
                for c in ALPHABET
                if c not in guessed
            ]

            return remaining[0], 0

        entropy = self.entropy_score(
            candidates,
            guessed
        )

        positional = self.positional_score(
            candidates,
            pattern,
            guessed
        )

        final_scores = {}

        for letter in ALPHABET:

            if letter in guessed:
                continue

            e = entropy.get(letter, 0)

            p = positional.get(letter, 0)

            final_scores[letter] = (
                0.6 * e
                +
                0.4 * (p / len(candidates))
            )

        best = max(
            final_scores,
            key=final_scores.get
        )

        confidence = (
            final_scores[best]
            /
            sum(final_scores.values())
        )

        return (
            best,
            round(confidence * 100, 2)
        )