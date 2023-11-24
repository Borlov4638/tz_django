from django.db import models
import requests
import json
from datetime import datetime

#Model "Question" for data base 
class Question(models.Model):
    category = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.CharField(max_length=255)


class Test:
    def __init__(self, x, y):
        self.validate_arguments(x, y)
        self.x = x
        self.y = y

    def validate_arguments(self, x, y):
        if not isinstance(x, (int, float)):
            raise ValueError("x must be a number")
        if not isinstance(y, (int, float)):
            raise ValueError("y must be a number")

    def get_quiz_questions(self):
        response = requests.get(f"https://jservice.io/api/clues?count={self.x}")
        questions = response.json()

        # Saving questions in data base
        for question_data in questions:
            Question.objects.create(
                category=question_data['category'],
                question=question_data['question'],
                answer=question_data['answer']
            )

        return questions

    def get_records_in_category(self, category):
        # Get count of questions in passed throug category
        record_count = Question.objects.filter(category=category).count()
        return record_count

    def get_and_save_records(self):
        # get "y" amount of question from data base
        records = Question.objects.all()[:self.y]

        # Saving quesions to JSON file
        current_date = datetime.now().strftime("%Y-%m-%d")
        file_name = f"records_{current_date}.json"
        records_data = [{'category': record.category, 'question': record.question, 'answer': record.answer}
                        for record in records]
        with open(file_name, 'w') as file:
            json.dump(records_data, file)
