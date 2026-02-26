from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.core.mail import EmailMessage

def generate_pdf_report(analysis):

    filename = f"report_{analysis.id}.pdf"
    c = canvas.Canvas(filename,pagesize=letter)

    y=750

    c.drawString(50,y,f"Readiness Score: {analysis.readiness_score}%")
    y-=30

    c.drawString(50,y,"Matched Skills:")
    y-=20
    for s in analysis.matched_skills:
        c.drawString(70,y,str(s))
        y-=15

    y-=10
    c.drawString(50,y,"Missing Skills:")
    y-=20
    for s in analysis.missing_skills:
        c.drawString(70,y,str(s))
        y-=15

    c.save()

    return filename


def send_analysis_report(email,analysis):

    file = generate_pdf_report(analysis)

    mail = EmailMessage(
        "Skill Gap Analysis Report",
        "Attached is your AI Readiness Analysis Report",
        "your_email@gmail.com",
        [email]
    )

    mail.attach_file(file)
    mail.send()