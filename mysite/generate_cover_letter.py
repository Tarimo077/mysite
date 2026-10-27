import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_cover_letter(output_path):
    # Printable area: 552 x 742 pt (Margins: 30pt L/R, 25pt T/B)
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
        fontSize=8.4,
        leading=11.8,
        alignment=TA_JUSTIFY,
        textColor=TEXT_DARK,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'CoverBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.4,
        textColor=TEXT_DARK,
        leftIndent=11,
        firstLineIndent=-11,
        spaceAfter=3
    )

    signoff_style = ParagraphStyle(
        'CoverSignoff',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.4,
        leading=11.8,
        textColor=TEXT_DARK
    )

    story = []

    # ==================== HEADER ====================
    left_header = [
        Paragraph("JEFF TARIMO", name_style),
        Spacer(1, 1.5),
        Paragraph("Head of Technology &bull; Lead Full-Stack &amp; Systems Architect", subtitle_style),
    ]

    contact_html = (
        "Nairobi, Kenya &bull; <a href='tel:+254790024489' color='#0f766e'><b>+254 790 024 489</b></a><br/>"
        "<a href='mailto:tarimojeff@gmail.com' color='#0f766e'>tarimojeff@gmail.com</a> &bull; "
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
        "Kutuma Kenya Limited<br/>"
        "Nairobi County, Kenya<br/>"
        "Email: <font color='#0d9488'>recruitment@kutuma.co.ke</font>"
    )
    date_text = "<b>Date:</b> October 19, 2026"
    meta_table = Table([[Paragraph(recip_text, recipient_style), Paragraph(date_text, date_style)]], colWidths=[370, 174])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 7))

    # Subject
    story.append(Paragraph("<b>APPLICATION:</b> Senior Lead Full-Stack Engineer &amp; Head of Technology (Job ID: 4477701018)", subject_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=BORDER_COLOR, spaceBefore=3, spaceAfter=7))

    # Body Paragraph 1: Intro & Player-Coach Alignment
    p1 = (
        "Dear Kutuma Recruitment Team,<br/>"
        "I am writing to express my strong interest in the <b>Senior Lead Full-Stack Engineer &amp; Head of Technology</b> "
        "role at Kutuma Kenya Limited. As a technical player-coach currently serving as Head of Technology at Powerpay Africa "
        "with an academic background in Electronics &amp; Computer Engineering (JKUAT) and an ongoing M.Sc. in Computer Science "
        "(Zetech University), I bridge executive technology strategy with deep, hands-on software engineering."
    )
    story.append(Paragraph(p1, body_style))

    # Body Paragraph 2: Complex Multi-Market Case Study (Explicit Requirement)
    p2 = (
        "<b>Multi-Market Technical Project Execution &amp; Architecture:</b><br/>"
        "To address your specific requirement, at Powerpay Africa I architected and currently lead the rollout of our "
        "<b>Multi-Region Smart Energy Telemetry &amp; Asset Financing Platform</b> across Kenya and regional operating hubs. "
        "The project required engineering a unified platform capable of ingesting high-frequency telemetry from thousands of "
        "distributed IoT edge controllers while supporting regional cellular networks, currency gateways, and differing localized business models:"
    )
    story.append(Paragraph(p2, body_style))

    # Key Architecture Highlights
    b1 = (
        "<font color='#0d9488'>&bull;</font> <b>Core Backend &amp; Concurrency:</b> Engineered production-grade Python/Django REST "
        "microservices and async pipelines utilizing Celery and Redis. Scaled multi-tenant database architectures across PostgreSQL "
        "and ClickHouse/InfluxDB for ultra-low-latency analytics, sustaining 99.9% uptime across municipal and commercial customer deployments."
    )
    story.append(Paragraph(b1, bullet_style))

    b2 = (
        "<font color='#0d9488'>&bull;</font> <b>Real-Time Web &amp; Frontend:</b> Built bi-directional event systems and operational control "
        "dashboards leveraging Django Channels/WebSockets, modern JavaScript/React, and Flutter/Flet for field diagnostics. Integrated automated "
        "Node-RED exception handling that eliminated manual dispatch interventions across field operations."
    )
    story.append(Paragraph(b2, bullet_style))

    b3 = (
        "<font color='#0d9488'>&bull;</font> <b>AI &amp; Data Pipeline Oversight:</b> Developed a non-intrusive load monitoring solution using "
        "AI by building data pipelines, training APIs and defining necessary data structures."
    )
    story.append(Paragraph(b3, bullet_style))

    b4 = (
        "<font color='#0d9488'>&bull;</font> <b>DevOps, Security &amp; Compliance:</b> Orchestrated containerized deployment workflows using "
        "Docker on Ubuntu AWS/Azure environments, implementing automated CI/CD pipelines, robust unit/integration testing, strict secret management, "
        "and data privacy adherence for sensitive customer and transaction records."
    )
    story.append(Paragraph(b4, bullet_style))

    # Body Paragraph 3: Leadership & Business Impact
    p3 = (
        "<b>Engineering Leadership &amp; Team Growth:</b><br/>"
        "As a leader, I manage cross-functional software and hardware engineers through structured agile sprints, pragmatic code reviews, "
        "and clear career progression tracks. I collaborate directly with executive stakeholders, operations leads, and client partners "
        "to translate ambitious business targets into crisp engineering roadmaps, minimizing technical debt while ensuring timely delivery "
        "within tight capital allocations."
    )
    story.append(Paragraph(p3, body_style))

    # Body Paragraph 4: Conclusion & Links
    p4 = (
        "Kutuma’s rapid expansion across African logistics demands technical rigor, operational empathy, and an anchor engineer who thrives "
        "in both the codebase and the boardroom. I welcome the opportunity to discuss how my hands-on full-stack mastery, AI integration capabilities, "
        "and proven technology leadership will drive Kutuma’s next chapter of market leadership. You can inspect my live builds, repositories, "
        "and interactive portfolio at <a href='https://jefftarimo.co.ke' color='#0f766e'><b>jefftarimo.co.ke</b></a> and "
        "<a href='https://github.com/Tarimo077' color='#0f766e'><b>github.com/Tarimo077</b></a>."
    )
    story.append(Paragraph(p4, body_style))
    story.append(Spacer(1, 4))

    # Signoff
    signoff_text = (
        "Sincerely,<br/>"
        "<b>Jeff Tarimo</b><br/>"
        "<font color='#475569'>Head of Technology &bull; Full-Stack &amp; IoT Systems Architect</font><br/>"
        "<font color='#64748b'>+254 790 024 489 &bull; tarimojeff@gmail.com &bull; Nairobi, Kenya</font>"
    )
    story.append(Paragraph(signoff_text, signoff_style))

    doc.build(story)
    print(f"Cover letter PDF successfully built at: {output_path}")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(base_dir, 'static', 'documents', 'Jeff_Tarimo_Cover_Letter_Kutuma.pdf')
    build_cover_letter(target_path)
