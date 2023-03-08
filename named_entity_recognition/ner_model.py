from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer_ner = AutoTokenizer.from_pretrained("C:/Users/delet/GLAv0.0.0.1/greekbert")
model_ner = AutoModelForSequenceClassification.from_pretrained("C:/Users/delet/GLAv0.0.0.1/greekbert")
