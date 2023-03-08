@echo off
echo Starting GLAM Chatbot...
start python chat.py
timeout /t 5 /nobreak > NUL
start python sentiment_analysis.py
timeout /t 5 /nobreak > NUL
start python question_answering.py
timeout /t 5 /nobreak > NUL
start python ner.py
echo GLAM Chatbot started.
