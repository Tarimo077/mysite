import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT

def build_m365_cover_letter(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=34,
        rightMargin=34,
        topMargin=26,
        bottomMargin=24
    )

    PRIMARY = colors.HexColor('#0f172a')      # Slate 900
    ACCENT = colors.HexColor('#0d9488')       # Teal 600
    ACCENT_DARK = colors.HexColor('#0f766e')  # Teal 700
    TEXT_DARK = colors.HexColor('#1e293b')    # Slate 800
    TEXT_MUTED = colors.HexColor('#475569')   # Slate 600
    TEXT_LIGHT = colors.HexColor('#64748b')   # Slate 500
    BORDER_COLOR = colors.HexColor('#cbd5e1') # Slate 300

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        'CoverName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=21,
        textColor=PRIMARY
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=ACCENT
    )

    contact_right_style = ParagraphStyle(
        'CoverContactRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        alignment=TA_RIGHT,
        textColor=TEXT_MUTED
    )

    date_style = ParagraphStyle(
        'CoverDate',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=TEXT_LIGHT
    )

    recipient_style = ParagraphStyle(
        'CoverRecipient',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK
    )

    subject_style = ParagraphStyle(
        'CoverSubject',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=12,
        textColor=PRIMARY
    )

    body_style = ParagraphStyle(
        'CoverBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.3,
        leading=11.5,
        alignment=TA_JUSTIFY,
        textColor=TEXT_DARK,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'CoverBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.3,
        textColor=TEXT_DARK,
        leftIndent=11,
        firstLineIndent=-11,
        spaceAfter=3
    )

    signoff_style = ParagraphStyle(
        'CoverSignoff',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.3,
        leading=11.5,
        textColor=TEXT_DARK
    )

    story = []

    # ==================== HEADER ====================
    left_header = [
        Paragraph("JEFF TARIMO", name_style),
        Spacer(1, 1.5),
        Paragraph("Head of Technology &bull; Full-Stack &amp; AI Systems Engineer", subtitle_style),
    ]

    contact_html = (
        "Nairobi, Kenya &bull; <a href='tel:+254790024489' color='#0f766e'><b>+254 790 024 489</b></a><br/>"
        "<a href='mailto:business@jefftarimo.co.ke' color='#0f766e'>business@jefftarimo.co.ke</a> &bull; "
        "<a href='https://jefftarimo.co.ke' color='#0f766e'><b>jefftarimo.co.ke</b></a><br/>"
        "<a href='https://linkedin.com/in/jeff-tarimo-043515151' color='#0f766e'>linkedin.com/in/jeff-tarimo</a> &bull; "
        "<a href='https://github.com/Tarimo077' color='#0f766e'>github.com/Tarimo077</a>"
    )
    right_header = Paragraph(contact_html, contact_right_style)

    header_table = Table([[left_header, right_header]], colWidths=[314, 230])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(header_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=2, spaceAfter=8))

    # ==================== DATE & RECIPIENT ====================
    recip_text = (
        "<b>Hiring Team</b><br/>"
        "M365Consult<br/>"
        "Remote / Global Talent Acquisition"
    )
    date_text = "<b>Date:</b> October 20, 2026"
    meta_table = Table([[Paragraph(recip_text, recipient_style), Paragraph(date_text, date_style)]], colWidths=[370, 174])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # Subject
    story.append(Paragraph("<b>APPLICATION:</b> Senior AI &amp; Full-Stack Engineer - DevOps &amp; Technical Leadership", subject_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=BORDER_COLOR, spaceBefore=3, spaceAfter=6))

    # Body Paragraph 1: Intro & Fit
    p1 = (
        "Dear Hiring Team,<br/>"
        "I am writing to express my enthusiastic interest in the <b>Senior AI &amp; Full-Stack Engineer (DevOps &amp; Technical Leadership)</b> "
        "role at M365Consult. As a hands-on technical player-coach currently serving as Head of Technology at Powerpay Africa, "
        "I combine senior full-stack development (Python/Django, Node.js, React) with practical AI/agentic integration, "
        "Linux/Docker DevOps, and distributed team leadership. Your emphasis on agile startup execution, human-reviewed AI agent workflows, "
        "and ownership across both internal and outsourced contributors closely matches my day-to-day operating model."
    )
    story.append(Paragraph(p1, body_style))

    # Body Paragraph 2: Targeted Answers to Job Post Questions
    p2 = "<b>Key Qualifications &amp; Application Overview:</b>"
    story.append(Paragraph(p2, body_style))

    b1 = (
        "<font color='#0d9488'>&bull;</font> <b>Full-Stack Delivery:</b> Architected and shipped multi-tier production platforms, "
        "including an enterprise SaaS platform (Django, PostgreSQL, HTMX/React, REST APIs) and real-time operational portals. "
        "I independently handle backend business logic, database migrations, caching layers (Redis), and responsive frontend interfaces."
    )
    story.append(Paragraph(b1, bullet_style))

    b2 = (
        "<font color='#0d9488'>&bull;</font> <b>AI &amp; Agentic Workflows:</b> Designed non-intrusive load monitoring (NILM) and anomaly "
        "detection pipelines using AI models, structured training APIs, and telemetry data. I leverage AI coding assistants and autonomous "
        "agents daily to accelerate velocity, always enforcing rigorous unit/integration test suites, syntax validation, and human code reviews."
    )
    story.append(Paragraph(b2, bullet_style))

    b3 = (
        "<font color='#0d9488'>&bull;</font> <b>Linux, Docker &amp; Cloud DevOps:</b> Direct end-to-end infrastructure management across "
        "Ubuntu Linux, AWS, and Azure. Proficient in Docker containerization, multi-stage builds, reverse proxies (Nginx/TLS), DNS routing, "
        "and automated CI/CD pipelines via GitHub Actions with automated rollback procedures and 99.9% telemetry uptime."
    )
    story.append(Paragraph(b3, bullet_style))

    b4 = (
        "<font color='#0d9488'>&bull;</font> <b>Leadership, Mentoring &amp; Outsourced Delivery:</b> Led cross-functional teams of software and "
        "hardware engineers, establishing PR review standards, architectural guardrails, and mentoring paths that elevated mid/junior contributors. "
        "Experienced coordinating external contractors, translating ambiguous business goals into verifiable acceptance criteria, and vetting deliverables for security and long-term maintainability."
    )
    story.append(Paragraph(b4, bullet_style))

    # Body Paragraph 3: Logistics, Availability & Salary Alignment
    p3 = (
        "<b>Availability &amp; Working Alignment:</b><br/>"
        "I am fully available to start <b>immediately</b> (or within 2 weeks of agreement) in a full-time, 100% remote capacity. "
        "I am entirely comfortable with startup-aligned tracking setups, milestone deliverables, and transparent time-tracking tools. "
        "My starting compensation expectations are <b>$2,500 – $3,500 / month (or equivalent in KES / agreed currency)</b>, "
        "structured with milestone-based progression as company initiatives grow and deliver impact."
    )
    story.append(Paragraph(p3, body_style))

    # Body Paragraph 4: Portfolio Links & Close
    p4 = (
        "I invite you to review my live builds, repositories, and technical portfolio at "
        "<a href='https://jefftarimo.co.ke' color='#0f766e'><b>jefftarimo.co.ke</b></a> and "
        "<a href='https://github.com/Tarimo077' color='#0f766e'><b>github.com/Tarimo077</b></a>. "
        "I look forward to discussing how my full-stack capabilities, pragmatic AI implementation, and startup technical leadership can accelerate M365Consult’s engineering vision."
    )
    story.append(Paragraph(p4, body_style))
    story.append(Spacer(1, 3))

    # Signoff
    signoff_text = (
        "Sincerely,<br/>"
        "<b>Jeff Tarimo</b><br/>"
        "<font color='#475569'>Head of Technology &bull; Full-Stack &amp; AI Systems Engineer</font><br/>"
        "<font color='#64748b'>+254 790 024 489 &bull; business@jefftarimo.co.ke &bull; Nairobi, Kenya</font>"
    )
    story.append(Paragraph(signoff_text, signoff_style))

    doc.build(story)
    print(f"Cover letter PDF successfully built at: {output_path}")

if __name__ == '__main__':
    base_dir = r"C:\Users\Admin\Desktop\mysites\mysite"
    target_path = os.path.join(base_dir, 'static', 'documents', 'Jeff_Tarimo_Cover_Letter_M365Consult.pdf')
    build_m365_cover_letter(target_path)
