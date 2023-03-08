from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Loading the tokenizer and the model for question answering
model_qa = AutoModelForQuestionAnswering.from_pretrained("C:/Users/delet/GLAv0.0.0.1/greekbert")
tokenizer_qa = AutoTokenizer.from_pretrained("C:/Users/delet/GLAv0.0.0.1/greekbert")

# Helper function to get an answer for a given question
def get_answer(question):
    # Tokenizing the question and getting the answer
    input_ids = tokenizer_qa.encode(question, return_tensors='pt')
    start_scores, end_scores = model_qa(input_ids)
    answer_start = torch.argmax(start_scores)
    answer_end = torch.argmax(end_scores) + 1
    answer = tokenizer_qa.convert_tokens_to_string(tokenizer_qa.convert_ids_to_tokens(input_ids[0][answer_start:answer_end]))
    if answer == '[CLS]':
        answer = None
    return answer
