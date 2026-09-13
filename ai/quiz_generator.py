def generate_quiz(topic: str, count: int = 5):
    """Placeholder quiz generator."""
    return [
        {
            "question": f"Which statement best describes {topic}?",
            "options": ["Concept A", "Concept B", "Concept C", "Concept D"],
            "answer": "Concept A"
        }
        for _ in range(count)
    ]
