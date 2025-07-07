from transformers import pipeline
from functools import lru_cache


def get_pipeline():
    return pipeline("sentiment-analysis")

sentiment_pipeline = get_pipeline()

async def analyze_sentiment(text: str) -> str:
    try:
        result = sentiment_pipeline(text)[0]
        label = result["label"].lower()


        if label in ["positive", "negative", "neutral"]:
            return label
        elif label == "pos":
            return "positive"
        elif label == "neg":
            return "negative"
        else:
            return "neutral"
    except Exception as e:
        print(f"[Sentiment error] {e}")
        return "unknown"
