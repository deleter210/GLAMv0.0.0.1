from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Loading the tokenizer and the model for named entity recognition
from named_entity_recognition.ner_model import model_ner, tokenizer_ner

def get_named_entities(text):
    # Tokenizing the input text
    inputs = tokenizer_ner(text, return_tensors="pt", truncation=True)

    # Getting the model prediction
    outputs = model_ner(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)

    # Converting the predicted labels back to the named entities
    labels = ['O', 'B-LOC', 'I-LOC', 'B-ORG', 'I-ORG', 'B-PER', 'I-PER']
    named_entities = []
    for i, label in enumerate(predictions.tolist()):
        if label != 0:
            if i == 0 or predictions.tolist()[i-1] == 0:
                named_entity = {"word": inputs.tokens()[0][i], "type": labels[label]}
                named_entities.append(named_entity)
            else:
                named_entity["word"] += f" {inputs.tokens()[0][i]}"
        else:
            named_entity = None

    return named_entities
