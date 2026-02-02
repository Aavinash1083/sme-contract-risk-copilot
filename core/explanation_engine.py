def explain_clause(category):
    explanations = {
        "Termination": "The other party can end the contract easily, but you may not have the same right.",
        "Penalty": "You may have to pay extra money if there is any delay or issue.",
        "Auto Renewal": "The contract will continue automatically unless cancelled early.",
        "IP Rights": "Any work or ideas you create may not belong to you.",
        "Jurisdiction": "Legal disputes may need to be handled in another location."
    }
    return explanations.get(category, "This clause may affect your responsibilities.")
