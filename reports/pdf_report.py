from fpdf import FPDF

def generate_pdf(lines, filename="contract_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in lines:
        safe_line = line.encode("latin-1", "ignore").decode("latin-1")
        pdf.multi_cell(0, 8, safe_line)

    pdf.output(filename)
    return filename
