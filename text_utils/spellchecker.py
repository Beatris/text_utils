from typing import List, Optional
from numpy import sort

from pyxdameraulevenshtein import damerau_levenshtein_distance


class SpellChecker:

    def __init__(self, vocabulary: List[str], max_distance: int = 2) -> None:
        self.vocabulary = vocabulary
        self.max_distance = max_distance

    def correct(self, word: str) -> str:
        if word.isdigit():
            return word

        best_vocab_match = self._get_best_vocab_match(word)
        return best_vocab_match or word

    def _get_best_vocab_match(self, word: str) -> Optional[str]:
        candidates = []
        for vocab_word in self.vocabulary:
            distance = damerau_levenshtein_distance(word, vocab_word)
            if 0 < distance <= self.max_distance:
                candidates.append((vocab_word, distance))
        if not candidates:
            return None
        candidates.sort(key=lambda candidate: candidate[1])
        return candidates[0][0]
