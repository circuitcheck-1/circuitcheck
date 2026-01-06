from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(issues, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "CircuitCheck – Design Analysis Report")

    y -= 40
    c.setFont("Helvetica", 12)

    if not issues:
        c.drawString(50, y, "No issues detected. Design passed all checks.")
    else:
        for issue in issues:
            c.drawString(50, y, f"{issue['level']}: {issue['title']}")
            y -= 15
            c.drawString(60, y, issue["description"])
            y -= 15
            c.drawString(60, y, f"Fix: {issue['fix']}")
            y -= 30

            if y < 100:
                c.showPage()
                y = height - 50

    c.save()
