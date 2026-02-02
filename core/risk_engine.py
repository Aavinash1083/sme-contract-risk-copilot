RISK_WEIGHTS = {
    "Penalty": 2,
    "Termination": 3,
    "Auto Renewal": 2,
    "IP Rights": 3,
    "Jurisdiction": 2
}

def calculate_risk(classified_clauses):
    score = 0
    risky = []

    for clause, category in classified_clauses:
        if category in RISK_WEIGHTS:
            score += RISK_WEIGHTS[category]
            risky.append((clause, category))

    if score >= 8:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return level, score, risky
