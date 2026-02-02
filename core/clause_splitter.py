import re

def split_clauses(text):
    clauses = re.split(r"\n\s*\d+\.", text)
    return [c.strip() for c in clauses if len(c.strip()) > 30]
