def final_decision(risk_level):
    if risk_level == "HIGH":
        return "AVOID OR RENEGOTIATE"
    elif risk_level == "MEDIUM":
        return "SIGN AFTER NEGOTIATION"
    else:
        return "SAFE TO SIGN"
