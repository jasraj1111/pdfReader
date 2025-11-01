import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)

STOPWORDS = set(stopwords.words("english"))

def preprocess_text(text: str) -> str:
    """Lowercase, remove special chars, extra spaces, and stopwords."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s.]", "", text)
    words = [w for w in text.split() if w not in STOPWORDS]
    return " ".join(words)

def extract_keywords(text: str, top_n: int = 10):
    """Return top keywords by frequency."""
    words = text.split()
    freq = Counter(words)
    return [word for word, _ in freq.most_common(top_n)]

def summarize_text(text: str, max_sentences: int = 3):
    """Simple frequency-based summarizer."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    if len(sentences) <= max_sentences:
        return text

    word_freq = Counter([w for w in text.split() if w not in STOPWORDS])
    sentence_scores = {}
    for sent in sentences:
        for word in sent.lower().split():
            if word in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]
    ranked = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary = " ".join([s for s, _ in ranked[:max_sentences]])
    return summary
