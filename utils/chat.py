from flask import Flask, request, jsonify, render_template
from datetime import datetime

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
        # Checking if the user input is a question and getting the answer
        if "?" in user_input:
            answer = get_answer(user_input)
            if answer:
                # Creating a chat bubble for the answer
                answer_chat_bubble = create_chat_bubble(answer, "GLAM")
                return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, answer_chat_bubble]})
            else:
                # Creating a chat bubble for the error message
                error_chat_bubble = create_chat_bubble("I'm sorry, I don't know the answer to that.", "GLAM")
                return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, error_chat_bubble]})
        else:
            # Generating a random response using SimpleNLG
            response = generate_response()
            # Creating a chat bubble for the response
            response_chat_bubble = create_chat_bubble(response, "GLAM")
            return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, response_chat_bubble]})

    # If the sentiment label is negative or neutral, responding with a message of empathy
    else:
        # Creating a chat bubble for the empathy message
        empathy_chat_bubble = create_chat_bubble("I'm sorry you feel that way. Would you like to know more about the law?", "GLAM")
        return jsonify({"chat_bubbles": [user_chat_bubble, sentiment_chat_bubble, empathy_chat_bubble]})

# Helper function to create a chat bubble
def create_chat_bubble(text, sender):
    time = datetime.now().strftime("%H:%M")
    return {"text": text, "sender": sender, "time": time}

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
