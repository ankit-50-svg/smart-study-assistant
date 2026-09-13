from ai.quiz_generator import generate_quiz

def test_quiz():
    quiz = generate_quiz("Python", 3)
    assert len(quiz) == 3
