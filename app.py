from flask import Flask, request, jsonify, render_template
from datetime import datetime
import random
import time
from named_entity_recognition.ner import get_named_entities
from question_answering.question_answering_model import get_answer
from sentiment_analysis.sentiment_model import get_sentiment_analysis
from utils.chat import create_chat_bubble
from utils.nlg import generate_response

app = Flask(__name__)
log_file = "logs/log.txt"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/glam', methods=['POST'])
def glam():
    user_input = request.form['text']
    user_chat_bubble = create_chat_bubble(user_input, "user")
    sentiment_score, sentiment_label = get_sentiment_analysis(user_input)
    sentiment_chat_bubble = create_chat_bubble(sentiment_label, "GLAM")
    if sentiment_label == "POSITIVE":
        named_entities = get_named_entities(user_input)
        if "?" in user_input:
            answer = get_answer(user_input, named_entities)
            if answer:
                answer_chat_bubble = create_chat_bubble(answer, "GLAM")
                return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, answer_chat_bubble]})
            else:
                error_chat_bubble = create_chat_bubble("I'm sorry, I don't know the answer to that.", "GLAM")
                return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, error_chat_bubble]})
        else:
            response = generate_response()
            response_chat_bubble = create_chat_bubble(response, "GLAM")
            return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, response_chat_bubble]})

    else:
        empathy_chat_bubble = create_chat_bubble("I'm sorry you feel that way. Would you like to know more about the law?", "GLAM")
        return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, empathy_chat_bubble]})

def log_message(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{current_time}] {message}\n")

if __name__ == '__main__':
    while True:
        try:
            app.run(debug=True)
        except Exception as e:
            log_message(f"ERROR: {str(e)}")
            log_message("Restarting in 5 seconds...")
            time.sleep(15)
