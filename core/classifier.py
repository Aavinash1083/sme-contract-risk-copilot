def detect_contract_type(text):
    t = text.lower()
    if "employment" in t:
        return "Employment Contract"
    if "vendor" in t or "service" in t:
        return "Vendor Agreement"
    if "lease" in t or "rent" in t:
        return "Lease Agreement"
    return "General Business Contract"


def classify_clause(clause):
    c = clause.lower()
    if "terminate" in c:
        return "Termination"
    if "penalty" in c or "fine" in c:
        return "Penalty"
    if "auto-renew" in c:
        return "Auto Renewal"
    if "intellectual property" in c:
        return "IP Rights"
    if "jurisdiction" in c or "arbitration" in c:
        return "Jurisdiction"
    return "General"
