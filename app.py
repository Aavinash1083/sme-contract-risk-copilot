import streamlit as st
from core.extractor import extract_text
from core.clause_splitter import split_clauses
from core.classifier import detect_contract_type, classify_clause
from core.risk_engine import calculate_risk
from core.decision_engine import final_decision
from core.explanation_engine import explain_clause
from core.negotiation_engine import negotiation_tip
from reports.pdf_report import generate_pdf

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="SME Contract Risk Copilot",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown("## 📄 SME Contract Risk Copilot")
st.caption("Decision-first contract clarity for small & medium businesses")

st.markdown("---")

# ---------- FILE UPLOAD ----------
file = st.file_uploader(
    "📤 Upload Contract",
    type=["txt", "pdf", "docx"]
)

if file:
    # ---------- PROCESS ----------
    text = extract_text(file)
    clauses = split_clauses(text)

    contract_type = detect_contract_type(text)
    classified = [(c, classify_clause(c)) for c in clauses]

    risk_level, score, risky = calculate_risk(classified)
    decision = final_decision(risk_level)

    # ---------- CONTRACT TYPE ----------
    st.markdown("### 📌 Contract Type")
    st.info(contract_type)

    # ---------- DECISION CARD ----------
    st.markdown("### ✅ Final Recommendation")

    if risk_level == "HIGH":
        st.error(decision)
    elif risk_level == "MEDIUM":
        st.warning(decision)
    else:
        st.success(decision)

    # ---------- RISK METER ----------
    st.markdown("### ⚠️ Overall Risk Level")

    max_score = 10
    progress_value = min(score / max_score, 1.0)

    st.progress(progress_value)

    st.caption(f"Risk Score: {score} / {max_score}")

    # ---------- SUMMARY FOR PDF ----------
    summary_lines = [
        f"Contract Type: {contract_type}",
        f"Final Decision: {decision}",
        f"Risk Level: {risk_level}",
        ""
    ]

    # ---------- RISKY CLAUSES ----------
    st.markdown("### 📑 Risky Clauses & Explanation")

    if not risky:
        st.success("No major risky clauses detected.")
    else:
        for idx, (clause, category) in enumerate(risky, start=1):
            with st.expander(f"{idx}. {category}"):
                st.write(clause)

                explanation = explain_clause(category)
                suggestion = negotiation_tip(category)

                st.markdown("**Why this matters:**")
                st.info(explanation)

                st.markdown("**What you can negotiate:**")
                st.warning(suggestion)

                summary_lines.append(f"{category}: {explanation}")
                summary_lines.append(f"Negotiation Tip: {suggestion}")
                summary_lines.append("")

    st.markdown("---")

    # ---------- PDF DOWNLOAD ----------
    st.markdown("### 📥 Download Report")

    if st.button("Generate PDF Report"):
        pdf_file = generate_pdf(summary_lines)
        st.success("PDF report generated")

        st.download_button(
            label="⬇️ Download Contract Risk Report",
            data=open(pdf_file, "rb"),
            file_name=pdf_file,
            mime="application/pdf"
        )

# ---------- FOOTER ----------
st.markdown("---")
st.caption("⚠️ Disclaimer: This tool provides business-level insights and is not legal advice.")
