from typing import List

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer


class KeywordsExtractor:

    def __init__(self, vectorizer: TfidfVectorizer) -> None:
        self.vectorizer = vectorizer

    @classmethod
    def train(cls, corpus: List[str]) -> "KeywordsExtractor":
        vectorizer = TfidfVectorizer(stop_words='english')
        vectorizer.fit(corpus)
        return KeywordsExtractor(vectorizer)

    def get_keywords_from_text(self, text: str, max_words: int = 8) -> List[str]:
        tf_idf = self.vectorizer.transform([text])
        df = pd.DataFrame(
            tf_idf[0].T.todense(),
            index=self.vectorizer.get_feature_names_out(),
            columns=['tf-idf']
        )
        df = df[df['tf-idf'] != 0]
        df = df.sort_values('tf-idf', ascending=False).head(max_words)
        return list(df.index)
