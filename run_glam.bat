@echo off

start cmd /k python chat.py
start cmd /k python sentiment_analysis.py
start cmd /k python question_answering.py
start cmd /k python ner_model.py
start cmd /k python ner.py

pause
