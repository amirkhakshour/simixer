import random
from itertools import combinations

question_format = """
    - {id}) {question}"""


def random_get_answer(answers, memory=None):
    if memory is None:
        memory = []
    while True:
        answer = random.choice(answers)
        if answer not in memory:
            memory.append(answer)
            return answer


def generate_combinations(dimensions):
    """
    Generate a list of two element items which each is a tuple of (dimenstion_name, answer)
    e.g:
    [[('Adaptive', 'I am a curious person'), ('Integrity', 'I am fair')], ...]
    :return:
    """
    questions = []
    memory = []
    for comb in combinations(range(len(dimensions)), 2):
        first_dimension_index, second_dimension_index = comb
        first_d = dimensions[first_dimension_index]
        second_d = dimensions[second_dimension_index]
        for i in range(2):
            a_1 = random_get_answer(first_d['answers'], memory)
            a_2 = random_get_answer(second_d['answers'], memory)
            questions.append([(first_d['name'], a_1), (second_d['name'], a_2)])
    random.shuffle(questions)
    return questions
