from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "grkostas/greeklegalbert-v2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Your code using the model and tokenizer goes here
