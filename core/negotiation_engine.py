def negotiation_tip(category):
    tips = {
        "Termination": "Ask for mutual termination with notice period.",
        "Penalty": "Request penalty cap or grace period.",
        "Auto Renewal": "Ask to remove auto-renewal or reduce duration.",
        "IP Rights": "Request shared ownership or limited usage rights.",
        "Jurisdiction": "Request local jurisdiction."
    }
    return tips.get(category, "Ask for clarification or modification.")
