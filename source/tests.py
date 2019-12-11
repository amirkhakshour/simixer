import pytest
from collections import Counter

from .utils import generate_combinations
from .data import dimensions


@pytest.fixture
def combined_questions():
    return generate_combinations(dimensions)


def test_combinations_len(combined_questions):
    assert len(combined_questions) == 30


def test_each_question_has_2_answer(combined_questions):
    assert all([len(pair) == 2 for pair in combined_questions])


def test_combination_items_uniqueness(combined_questions):
    question_items = [q[1] for pair in combined_questions for q in pair]
    assert len(set(question_items)) == len(question_items)


def test_match_each_dimension_pair_twice(combined_questions):
    question_items_types = [(pair[0][0], pair[1][0]) for pair in combined_questions]
    countered = Counter(question_items_types)
    assert all([c == 2 for c in countered.values()])
