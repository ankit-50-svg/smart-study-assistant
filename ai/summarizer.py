def summarize_text(text: str) -> str:
    """Simple extractive starter; replace/extend with an AI model."""
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    return ". ".join(sentences[:5]) + ("." if sentences else "")
