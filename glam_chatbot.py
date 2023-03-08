from flask import Flask, request, jsonify, render_template
from datetime import datetime
import random
from chat import create_chat_bubble
from sentiment_analysis import get_sentiment_analysis
from question_answering import get_answer
from named_entity_recognition.ner import get_named_entities

app = Flask(__name__)

# Defining the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Defining the route for the chat page
@app.route('/glam', methods=['POST'])
def glam():
    # Getting the user input from the POST request
    user_input = request.form['text']

    # Creating a chat bubble for the user input
    user_chat_bubble = create_chat_bubble(user_input, "user")

    # Getting the sentiment analysis score and label for the user input
    sentiment_score, sentiment_label = get_sentiment_analysis(user_input)

    # Creating a chat bubble for the sentiment analysis label
    sentiment_chat_bubble = create_chat_bubble(sentiment_label, "GLAM")

    # Checking if the sentiment label is positive and processing the user input
    if sentiment_label == "POSITIVE":
        # Getting the named entities in the user input
        named_entities = get_named_entities(user_input)

        # Checking if the user input is a question and getting the answer
        if "?" in user_input:
            answer = get_answer(user_input, named_entities)
            if answer:
                # Creating a chat bubble for the answer
                answer_chat_bubble = create_chat_bubble(answer, "GLAM")
                return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, answer_chat_bubble]})
            else:
                # Creating a chat bubble for the error message
                error_chat_bubble = create_chat_bubble("I'm sorry, I don't know the answer to that.", "GLAM")
                return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, error_chat_bubble]})
        else:
            # Generating a random response
            response = generate_response()
            # Creating a chat bubble for the response
            response_chat_bubble = create_chat_bubble(response, "GLAM")
            return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, response_chat_bubble]})

    # If the sentiment label is negative or neutral, responding with a message of empathy
    else:
        # Creating a chat bubble for the empathy message
        empathy_chat_bubble = create_chat_bubble("I'm sorry you feel that way. Would you like to know more about the law?", "GLAM")
        return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, empathy_chat_bubble]})

# Helper function to generate a random response
def generate_response():
    responses = [
        "The Greek legal system is based on civil law and is heavily influenced by Roman law and ancient Greek law.",
        "The Hellenic Parliament is responsible for making the laws in Greece.",
        "The Greek legal system has three main branches: civil, criminal, and administrative law.",
        "The Greek Constitution is the supreme law of the land and provides the framework for the legal system.",
        "The Greek legal system has a long history, dating back to ancient Greece and the Roman Empire.",
        "The Greek legal system is a mixture of both civil and common law traditions."
    ]
    return random.choice(responses)

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
