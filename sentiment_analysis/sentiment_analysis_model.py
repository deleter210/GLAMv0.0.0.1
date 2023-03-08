from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Loading the sentiment analysis model
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
sentiment_analyzer = pipeline('sentiment-analysis', model=model_name)

class SentimentAnalyzer:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
    def get_sentiment(self, text):
        # Analyzing the sentiment of the text
        result = sentiment_analyzer(text)[0]
        score = round(result['score'], 2)
        label = result['label'].upper()
        return score, label
