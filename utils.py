import json
import random

from question import Question


# noinspection PyTypeChecker
def create_list_of_instances(filename: object) -> object:
    """
    создание списка экземпляров класса Question
    из фаила question.json
    в формате список вложенный в словарь
    """

    # список экзкмпляров класса
    questions = []
    with open(filename, 'r', encoding="utf-8") as file:
        json_file = json.load(file)
    for f in json_file:
        question = f['q']
        complexity = int(f['d'])
        correct_answer = f['a']
        question = Question(question, complexity, correct_answer)
        questions.append(question)
        random.shuffle(questions)
    return questions


def output_of_results(questions):
    """
    подсчёт и вывод результатов
    """
    number_correct_questions = 0
    points = 0
    for question in questions:
        if question.is_correct():
            number_correct_questions += 1
            points += question.points_per_question
    return f'Вот и всё!\nОтвечено {number_correct_questions} вопроса из {len(questions)}\nНабрано баллов: {points}'
