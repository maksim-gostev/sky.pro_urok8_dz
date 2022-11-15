
from utils import create_list_of_instances, output_of_results

from config import FILENAME



if __name__ == '__main__':

    questions = create_list_of_instances(FILENAME)

    # цикл вопросов
    for question in questions:
        print(question.build_question())
        question.user_answer = input('Ваш ответ:\n')
        question.is_correct()
        print(question.build_feedback())
    print(output_of_results(questions))
