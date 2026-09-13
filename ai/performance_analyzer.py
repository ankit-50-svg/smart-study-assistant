def analyze_performance(results):
    if not results:
        return {"average": 0, "status": "No quiz data yet."}
    scores = [float(r.get("percentage", 0)) for r in results]
    avg = sum(scores) / len(scores)
    status = "Strong performance" if avg >= 75 else "Needs more revision"
    return {"average": round(avg, 2), "status": status}
