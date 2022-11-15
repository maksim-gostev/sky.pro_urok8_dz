class Question:
    def __init__(self, question, complexity, correct_answer):
        self.question = question
        self.complexity = complexity
        self.correct_answer = correct_answer
        self.is_question_asked = False
        self.user_answer = None
        self.points_per_question = self.complexity * 10

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points_per_question

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        self.is_question_asked = self.correct_answer == self.user_answer
        return self.is_question_asked

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question}\nСложность {self.complexity}/5'

    def build_feedback(self):
        """
        Возвращает :
        Ответ верный, получено __ баллов
        Возвращает :
        Ответ неверный, верный ответ __
        """
        if self.is_question_asked:
            return f'Ответ верный, получено {self.points_per_question} баллов'
        return f'Ответ неверный, верный ответ {self.correct_answer}'