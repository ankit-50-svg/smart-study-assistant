from ai.study_planner import generate_study_plan

def test_planner():
    plan = generate_study_plan(["Python", "DBMS"], 2, 120)
    assert len(plan) == 2
