def generate_study_plan(subjects, days, daily_minutes):
    """Rule-based starter planner; AI optimization can be added later."""
    plan = []
    if not subjects:
        return plan
    minutes_each = max(15, daily_minutes // len(subjects))
    for day in range(1, days + 1):
        plan.append({
            "day": day,
            "tasks": [{"subject": s, "minutes": minutes_each} for s in subjects]
        })
    return plan
