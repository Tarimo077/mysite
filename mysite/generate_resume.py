import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

def build_resume(output_path):
    """
    Builds a high-impact, single-page, ATS-optimized vector PDF resume for Jeff Tarimo,
    including Head of Technology & Head of IoT roles at Powerpay Africa.
    """
    # Letter size: 612 x 792 pt
    # Printable area: 552 x 748 pt
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=30,
        rightMargin=30,
        topMargin=22,
        bottomMargin=20
    )

    PRIMARY = colors.HexColor('#0f172a')      # Slate 900
    ACCENT = colors.HexColor('#0d9488')       # Teal 600
    ACCENT_DARK = colors.HexColor('#0f766e')  # Teal 700
    TEXT_DARK = colors.HexColor('#1e293b')    # Slate 800
    TEXT_MUTED = colors.HexColor('#475569')   # Slate 600
    TEXT_LIGHT = colors.HexColor('#64748b')   # Slate 500
    BG_LIGHT = colors.HexColor('#f8fafc')     # Slate 50
    BORDER_COLOR = colors.HexColor('#cbd5e1') # Slate 300

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        'ResumeName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=21,
        textColor=PRIMARY
    )

    subtitle_style = ParagraphStyle(
        'ResumeSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=ACCENT
    )

    contact_right_style = ParagraphStyle(
        'ResumeContactRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        alignment=TA_RIGHT,
        textColor=TEXT_MUTED
    )

    section_heading_style = ParagraphStyle(
        'ResumeSectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=PRIMARY,
        spaceAfter=0,
        textTransform='uppercase'
    )

    summary_style = ParagraphStyle(
        'ResumeSummary',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        alignment=TA_JUSTIFY,
        textColor=TEXT_DARK
    )

    skill_desc_style = ParagraphStyle(
        'ResumeSkillDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.8,
        textColor=TEXT_DARK
    )

    job_title_style = ParagraphStyle(
        'ResumeJobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10.2,
        textColor=PRIMARY
    )

    job_date_style = ParagraphStyle(
        'ResumeJobDate',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=10.2,
        alignment=TA_RIGHT,
        textColor=TEXT_LIGHT
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.7,
        leading=10.2,
        textColor=TEXT_DARK,
        leftIndent=10,
        firstLineIndent=-10,
        spaceAfter=1
    )

    edu_title_style = ParagraphStyle(
        'ResumeEduTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=9.8,
        textColor=PRIMARY
    )

    edu_sub_style = ParagraphStyle(
        'ResumeEduSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=ACCENT_DARK
    )

    edu_meta_style = ParagraphStyle(
        'ResumeEduMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9,
        textColor=TEXT_LIGHT
    )

    cert_item_style = ParagraphStyle(
        'ResumeCertItem',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.8,
        textColor=TEXT_DARK,
        leftIndent=7,
        firstLineIndent=-7
    )

    footer_style = ParagraphStyle(
        'ResumeFooter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8,
        alignment=TA_CENTER,
        textColor=TEXT_LIGHT
    )

    story = []

    # ==================== HEADER ====================
    left_header = [
        Paragraph("JEFF TARIMO", name_style),
        Spacer(1, 1.5),
        Paragraph("Head of Technology &bull; IoT Systems Engineer &bull; Full-Stack Cloud", subtitle_style),
    ]

    contact_html = (
        "Nairobi, Kenya &bull; <a href='tel:+254790024489' color='#0f766e'><b>+254 790 024 489</b></a><br/>"
        "<a href='mailto:tarimojeff@gmail.com' color='#0f766e'>tarimojeff@gmail.com</a> &bull; "
        "<a href='https://jefftarimo.co.ke' color='#0f766e'><b>jefftarimo.co.ke</b></a><br/>"
        "<a href='https://linkedin.com/in/jeff-tarimo-043515151' color='#0f766e'>linkedin.com/in/jeff-tarimo</a> &bull; "
        "<a href='https://github.com/Tarimo077' color='#0f766e'>github.com/Tarimo077</a>"
    )
    right_header = Paragraph(contact_html, contact_right_style)

    header_table = Table([[left_header, right_header]], colWidths=[312, 240])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(header_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=2, spaceAfter=4))

    def make_section_heading(title_text):
        content = [[
            Paragraph(f"<font color='#0d9488'>&#9632;</font> {title_text}", section_heading_style)
        ]]
        t = Table(content, colWidths=[552])
        t.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
            ('LINEBELOW', (0, 0), (-1, -1), 0.75, BORDER_COLOR),
        ]))
        return t

    # ==================== PROFESSIONAL SUMMARY ====================
    story.append(make_section_heading("Professional Summary"))
    story.append(Spacer(1, 2))
    summary_p = Paragraph(
        "Multidisciplinary <b>Head of Technology &amp; IoT Systems Engineer</b> with over 4 years of proven expertise designing, bench-testing, and deploying industrial-grade edge-to-cloud architectures. Specialized in technical leadership, microcontrollers (STM32, ESP32), low-power wireless networks (LoRaWAN, Cellular, BLE), and scalable backend pipelines (Python, Django, Node.js, AWS/Azure). Experienced in directing cross-functional engineering teams, architecting smart energy metering platforms, and delivering fault-tolerant telemetry infrastructure.",
        summary_style
    )
    story.append(summary_p)
    story.append(Spacer(1, 4))

    # ==================== TECHNICAL EXPERTISE ====================
    story.append(make_section_heading("Technical Expertise"))
    story.append(Spacer(1, 2))

    skills_data = [
        [
            Paragraph("<b>Microcontrollers &amp; Hardware:</b> STM32, ESP32, Raspberry Pi, Arduino, Circuit Design, Sensor Integration", skill_desc_style),
            Paragraph("<b>Firmware &amp; Protocols:</b> C/C++, MicroPython, MODBUS (RS485), MQTT, HTTP/S, UART, SPI, I2C", skill_desc_style)
        ],
        [
            Paragraph("<b>Wireless &amp; Networking:</b> LoRaWAN, Cellular (GPRS/LTE-M), Sigfox, BLE, Wi-Fi, CCNA R&amp;S", skill_desc_style),
            Paragraph("<b>Backend &amp; Cloud:</b> Node.js, Python (Django), Next.js, Redis, AWS, Azure, Linux (Ubuntu), REST APIs", skill_desc_style)
        ],
        [
            Paragraph("<b>Databases &amp; Time-Series:</b> ClickHouse, PostgreSQL, MySQL, InfluxDB (Time-series optimization)", skill_desc_style),
            Paragraph("<b>Frontend &amp; Leadership:</b> React, Flutter, Tailwind CSS, HTML5, Node-RED Automation, Technical Strategy", skill_desc_style)
        ]
    ]

    skills_table = Table(skills_data, colWidths=[273, 273])
    skills_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('BOX', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))

    # ==================== WORK EXPERIENCE ====================
    story.append(make_section_heading("Work Experience"))
    story.append(Spacer(1, 2))

    def make_job_header(title, company, date_location):
        header_p = Paragraph(f"<b>{title}</b> &mdash; <font color='#0d9488'><b>{company}</b></font>", job_title_style)
        date_p = Paragraph(date_location, job_date_style)
        t = Table([[header_p, date_p]], colWidths=[382, 170])
        t.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        return t

    # Job 1: Head of Technology
    story.append(make_job_header("Head of Technology", "Powerpay Africa Limited", "Feb 2025 – Present | Nairobi, Kenya"))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Direct overall technology vision, infrastructure scaling, strategic IT planning, and architectural roadmaps across hardware &amp; software.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Lead engineering teams across firmware, cloud backend, and mobile apps to deliver smart energy metering and financing systems.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Orchestrate tech stack decisions, cloud operations (AWS/Azure/Ubuntu), and technical delivery to align with company growth goals.", bullet_style))
    story.append(Spacer(1, 2.5))

    # Job 2: Head of IoT
    story.append(make_job_header("Head of IoT", "Powerpay Africa Limited", "Feb 2023 – Jan 2025 | Nairobi, Kenya"))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Spearheaded firmware engineering using C++ and MicroPython for smart energy meters and edge telemetry controllers.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Deployed multi-protocol communication pipelines (MODBUS RS485, GPRS, Wi-Fi, BLE) for continuous remote asset monitoring.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Architected scalable backend services and REST APIs with Node.js, Django, ClickHouse, and PostgreSQL on Ubuntu cloud servers.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Automated data normalization and exception alerts via custom Node-RED workflows, eliminating manual intervention.", bullet_style))
    story.append(Spacer(1, 2.5))

    # Job 3: Head of IoT - Upande
    story.append(make_job_header("Head of IoT", "Upande Limited", "Sep 2022 – Jan 2023 | Nairobi, Kenya"))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Directed product strategy and hardware delivery roadmaps as Product Owner across municipal and agricultural IoT initiatives.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Streamlined device testing and dispatch pipelines using Node-RED, reducing commissioning time across field deployments.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Liaised with enterprise stakeholders to translate complex monitoring requirements into scalable IoT architectures.", bullet_style))
    story.append(Spacer(1, 2.5))

    # Job 4: IoT Engineer - Upande
    story.append(make_job_header("IoT Engineer", "Upande Limited", "Apr 2021 – Aug 2022 | Nairobi, Kenya"))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Assembled, calibrated, and deployed industrial sensor nodes (water level, ultrasonic, flow, weather) using LoRaWAN and GSM.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Maintained field device fleets, diagnosing power faults and issuing remote firmware updates to maximize uptime.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Configured InfluxDB time-series instances for sensor data ingestion, enabling real-time analytics and client dashboards.", bullet_style))
    story.append(Spacer(1, 2.5))

    # Job 5: Electrical Engineering Intern - NKCC
    story.append(make_job_header("Electrical Engineering Intern", "New Kenya Co-operative Creameries", "Mar 2016 – Aug 2016 | Nyeri, Kenya"))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Carried out scheduled electrical preventive maintenance across industrial dairy processing plants, reducing machine downtime.", bullet_style))
    story.append(Paragraph("<font color='#0d9488'>&bull;</font> Assisted senior engineers in troubleshooting motor control panels, relay boards, and industrial automation equipment.", bullet_style))
    story.append(Spacer(1, 4))

    # ==================== DUAL COLUMNS: EDUCATION & CERTIFICATIONS ====================
    edu_content = [
        Paragraph("<font color='#0d9488'>&#9632;</font> <b>EDUCATION</b>", section_heading_style),
        HRFlowable(width="100%", thickness=0.75, color=BORDER_COLOR, spaceBefore=1, spaceAfter=2.5),
        Paragraph("<b>M.Sc. in Computer Science</b>", edu_title_style),
        Paragraph("<font color='#0d9488'>Zetech University</font>", edu_sub_style),
        Paragraph("Ruiru, Kenya &bull; Aug 2026 &ndash; Dec 2027", edu_meta_style),
        Spacer(1, 2.5),
        Paragraph("<b>B.Sc. in Electronics &amp; Computer Engineering</b>", edu_title_style),
        Paragraph("<font color='#0d9488'>Jomo Kenyatta Univ. of Agriculture &amp; Tech. (JKUAT)</font>", edu_sub_style),
        Paragraph("Juja, Kiambu &bull; Graduated 2021", edu_meta_style),
    ]

    cert_content = [
        Paragraph("<font color='#0d9488'>&#9632;</font> <b>CERTIFICATIONS &amp; TRAINING</b>", section_heading_style),
        HRFlowable(width="100%", thickness=0.75, color=BORDER_COLOR, spaceBefore=1, spaceAfter=2.5),
        Paragraph("<font color='#0d9488'>&bull;</font> <b>CCNA (Routing &amp; Switching):</b> AFRALTI (2018)", cert_item_style),
        Spacer(1, 1),
        Paragraph("<font color='#0d9488'>&bull;</font> <b>Python &amp; Web Development:</b> IST (2020)", cert_item_style),
        Spacer(1, 1),
        Paragraph("<font color='#0d9488'>&bull;</font> <b>Android App Development:</b> IST (2020)", cert_item_style),
        Spacer(1, 1),
        Paragraph("<font color='#0d9488'>&bull;</font> <b>Languages:</b> English (Fluent), Swahili (Fluent)", cert_item_style),
    ]

    dual_table = Table([[edu_content, cert_content]], colWidths=[280, 266])
    dual_table.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(dual_table)
    story.append(Spacer(1, 4))

    # ==================== FOOTER ====================
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceBefore=1, spaceAfter=2.5))
    footer_p = Paragraph(
        "Jeff Tarimo &bull; Curriculum Vitae &bull; Portfolio: <a href='https://jefftarimo.co.ke' color='#0d9488'><b>jefftarimo.co.ke</b></a> &bull; Confidential &bull; Single-Page Format",
        footer_style
    )
    story.append(footer_p)

    doc.build(story)
    print(f"Resume generated successfully at: {output_path}")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(base_dir, 'static', 'documents', 'Jeff_Tarimo_Resume.pdf')
    build_resume(target_path)
