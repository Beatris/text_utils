from sklearn.feature_extraction.text import TfidfVectorizer

from text_utils.keywords_extractor import KeywordsExtractor


TEST_CORPUS = [
    'I enjoy reading about Machine Learning and Machine Learning is my PhD subject',
    'I would enjoy a walk in the park',
    'I was reading in the library'
]


def test_train():
    keywords_extractor = KeywordsExtractor.train(TEST_CORPUS)
    assert isinstance(keywords_extractor, KeywordsExtractor)
    assert isinstance(keywords_extractor.vectorizer, TfidfVectorizer)


def test_get_keywords_from_text():
    keywords_extractor = KeywordsExtractor.train(TEST_CORPUS)
    test_text = 'I study Machine Learning and some other stuff that does not matter'
    keywords = keywords_extractor.get_keywords_from_text(test_text)
    assert ['learning', 'machine'] == keywords
