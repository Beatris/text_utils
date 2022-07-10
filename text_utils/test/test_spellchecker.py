import pytest

from text_utils.spellchecker import SpellChecker


TEST_VOCABULARY = ["language", "programming", "functional", "function"]


@pytest.mark.parametrize("input_word,expected_correction",
    [
        ("langauge", "language"),
        ("programing", "programming"),
        ("functionall", "functional"),
        ("funcion", "function"),
        ("func1ion", "function"),
        ("missing", "missing"),
        ("banana", "banana"),
        ("lang", "lang"),
        ("123", "123")
    ])
def test_correct(input_word, expected_correction):
    spellchecker = SpellChecker(TEST_VOCABULARY)
    assert expected_correction == spellchecker.correct(input_word)
