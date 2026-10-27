from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


def get_education_data():
    """Returns structured educational history, graduate research, and capstone engineering projects."""
    return [
        {
            'id': 'msc-cs',
            'degree': 'M.Sc. in Computer Science',
            'institution': 'Zetech University',
            'location': 'Ruiru, Kenya',
            'period': 'Aug 2026 – Dec 2027',
            'status': 'Enrolled / Active Graduate Candidate',
            'details': (
                'Graduate coursework and research specializing in computability theory, distributed systems, '
                'advanced automata, edge cloud computing architectures, and data engineering.'
            ),
            'project': {
                'badge': 'Graduate Seminar Paper & Presentation',
                'type': 'M.Sc. Research Seminar Paper (Topic 3)',
                'unit': 'Advanced Theory of Computation (Computability and Formal Models)',
                'title': 'The Chomsky Hierarchy & The Relative Power of Formal Language Models',
                'subtitle': 'Theoretical Foundations, Machine Separations, Complexity Limits, and Contemporary Computing Applications',
                'summary': (
                    'Comprehensive graduate research investigation into the four classical tiers of formal language theory: '
                    'Regular (Type 3), Context-Free (Type 2), Context-Sensitive (Type 1), and Unrestricted (Type 0). '
                    'Establishes how memory topologies (none, LIFO stack, linearly bounded tape, and infinite tape) govern computational expressivity, '
                    'provides adversarial Pumping Lemma separation proofs, analyzes decidability boundaries, and demonstrates practical impacts '
                    'on compiler pipelines, Language-Theoretic Security (LangSec), and Transformer expressivity limits.'
                ),
                'highlights': [
                    'Rigorous non-pumping adversarial proofs separating Level 3 (0ⁿ1ⁿ ∉ REG) and Level 2 (aⁿbⁿcⁿ ∉ CFL)',
                    'Linear Bounded Automata (LBA) space-bounded configuration analysis & Immerman-Szelepcsényi complementation',
                    'Language-Theoretic Security (LangSec): Formal analysis of why ad-hoc parsing creates exploitable "weird machines"',
                    'Diagnostic evaluation of Transformer soft-attention circuit bounds (TC⁰) against formal language recognition'
                ],
                'tags': [
                    'Automata Theory',
                    'Chomsky Hierarchy',
                    'Pumping Lemmas',
                    'LangSec',
                    'Compiler Design',
                    'Decidability'
                ],
                'downloads': [
                    {
                        'name': 'Research Paper (PDF)',
                        'file_url': 'documents/The_Chomsky_Hierarchy_Research_Paper_Jeff_Tarimo.pdf',
                        'file_name': 'The_Chomsky_Hierarchy_Research_Paper_Jeff_Tarimo.pdf',
                        'icon': 'fa-solid fa-file-pdf',
                        'btn_class': 'edu-btn--pdf'
                    },
                    {
                        'name': 'Word Document (.docx)',
                        'file_url': 'documents/The_Chomsky_Hierarchy_Research_Paper_Jeff_Tarimo.docx',
                        'file_name': 'The_Chomsky_Hierarchy_Research_Paper_Jeff_Tarimo.docx',
                        'icon': 'fa-solid fa-file-word',
                        'btn_class': 'edu-btn--word'
                    },
                    {
                        'name': 'Presentation Slides (.pptx)',
                        'file_url': 'documents/The_Chomsky_Hierarchy_Presentation_Jeff_Tarimo.pptx',
                        'file_name': 'The_Chomsky_Hierarchy_Presentation_Jeff_Tarimo.pptx',
                        'icon': 'fa-solid fa-file-powerpoint',
                        'btn_class': 'edu-btn--slides'
                    }
                ]
            }
        },
        {
            'id': 'bsc-ece',
            'degree': 'B.Sc. in Electronics & Computer Engineering',
            'institution': 'Jomo Kenyatta University of Agriculture and Technology (JKUAT)',
            'location': 'Juja, Kiambu, Kenya',
            'period': 'Graduated 2021',
            'status': 'Completed (Second Class Honours)',
            'details': (
                'Comprehensive 5-year engineering foundation covering microprocessors, digital signal processing, '
                'embedded systems, telecommunications, control systems, circuit design, and software engineering.'
            ),
            'project': {
                'badge': 'Undergraduate Capstone Engineering Project',
                'type': 'B.Sc. Final Year Engineering Capstone Project',
                'unit': 'Department of Telecommunication & Information Engineering',
                'title': 'Smart Gate Controller: IoT & Automated Facial Recognition Access Control System',
                'subtitle': 'Edge-Deployed Computer Vision with Hardware Actuation on Raspberry Pi 4',
                'github': 'https://github.com/Tarimo077/smartGateController',
                'summary': (
                    'Designed, prototyped, and bench-tested an automated intelligent gate access control system deployed on a '
                    'Raspberry Pi 4 Model B single-board computer. Utilizes OpenCV Haar cascades and deep 128-dimensional metric facial embeddings '
                    'to identify registered occupants in real-time and trigger physical gate relay mechanisms via 50Hz PWM signals, '
                    'with automated intruder image capture and SMTP email security dispatch.'
                ),
                'highlights': [
                    'Edge-deployed real-time face detection with Haar cascades & 128-d deep metric facial embeddings via dlib',
                    'Hardware-level PWM servo & relay actuation via Raspberry Pi GPIO pin 12 to drive physical gate locks',
                    'Automated unknown-visitor snapshot capture with instant security alert email notifications via SMTP',
                    'Lightweight embedded Python architecture optimized for low-latency inference on single-board Linux'
                ],
                'images': [
                    {
                        'src': 'images/smart_gate_hardware.jpg',
                        'caption': 'Raspberry Pi 4 Model B Hardware Prototype & Peripheral Setup'
                    },
                    {
                        'src': 'images/smart_gate_screenshot.png',
                        'caption': 'Real-Time Live Facial Recognition Detection Stream & Recognition Output'
                    }
                ],
                'video': {
                    'src': 'videos/smart_gate_demo.mp4',
                    'title': 'Live Operational Demonstration & Gate Actuation',
                    'caption': 'Live hardware video showing real-time face detection, occupant recognition, and servo gate actuation on Raspberry Pi 4.'
                },
                'tags': [
                    'Raspberry Pi 4',
                    'Python',
                    'OpenCV',
                    'Computer Vision',
                    'Face Recognition (dlib)',
                    'GPIO Relay',
                    'IoT Security'
                ],
                'downloads': [
                    {
                        'name': 'Download Final Report (PDF)',
                        'file_url': 'documents/Smart_Gate_Controller_Final_Report_Jeff_Tarimo.pdf',
                        'file_name': 'Smart_Gate_Controller_Final_Report_Jeff_Tarimo.pdf',
                        'icon': 'fa-solid fa-file-pdf',
                        'btn_class': 'edu-btn--pdf'
                    },
                    {
                        'name': 'View Source on GitHub',
                        'url': 'https://github.com/Tarimo077/smartGateController',
                        'external': True,
                        'icon': 'fa-brands fa-github',
                        'btn_class': 'edu-btn--github'
                    }
                ]
            }
        }
    ]


def get_certifications_data():
    return [
        {
            'title': 'CCNA (Routing & Switching)',
            'issuer': 'AFRALTI',
            'year': '2018',
            'badge': 'Networking',
            'icon': 'fa-solid fa-network-wired'
        },
        {
            'title': 'Python & Web Development',
            'issuer': 'Institute of Software Technology (IST)',
            'year': '2020',
            'badge': 'Software',
            'icon': 'fa-brands fa-python'
        },
        {
            'title': 'Android App Development',
            'issuer': 'Institute of Software Technology (IST)',
            'year': '2020',
            'badge': 'Mobile',
            'icon': 'fa-brands fa-android'
        },
    ]


def home(request):
    profile = {
        'name': 'Jeff Tarimo',
        'headline': 'Head of Technology • IoT Systems Engineer • Full-Stack Cloud',
        'location': 'Nairobi, Kenya',
        'email': 'tarimojeff@gmail.com',
        'phone': '+254790024489',
        'phone_display': '+254 790 024 489',
        'website': 'https://jefftarimo.co.ke',
        'website_display': 'jefftarimo.co.ke',
        'linkedin': 'https://linkedin.com/in/jeff-tarimo-043515151',
        'github': 'https://github.com/Tarimo077',
        'twitter': 'https://x.com/JeffTarimo',
        'summary': (
            'Multidisciplinary Head of Technology & IoT Systems Engineer with over 4 years of proven expertise '
            'designing, bench-testing, and deploying industrial-grade edge-to-cloud architectures. '
            'Specialized in technical leadership, microcontrollers (STM32, ESP32), low-power wireless networks (LoRaWAN, Cellular, BLE), '
            'and scalable backend pipelines (Python/Django, Node.js, AWS/Azure).'
        ),
        'years_exp': '4+',
        'devices_count': '1,000+',
        'uptime_stat': '99.9%',
    }

    skill_categories = [
        {
            'category': 'Microcontrollers & Hardware',
            'icon': 'fa-solid fa-microchip',
            'skills': [
                ('STM32 & ARM Cortex', 90),
                ('ESP32 / ESP8266 (Wi-Fi/BLE)', 92),
                ('Raspberry Pi & SBCs', 88),
                ('Arduino Prototyping', 95),
                ('Circuit Design & PCB Layout', 82),
                ('Sensor Integration & Calibration', 90),
            ],
            'tags': ['STM32', 'ESP32', 'Raspberry Pi', 'Arduino', 'Sensors', 'KiCad', 'Oscilloscopes']
        },
        {
            'category': 'Firmware & Protocols',
            'icon': 'fa-solid fa-code',
            'skills': [
                ('C / C++ Embedded', 88),
                ('MicroPython / CircuitPython', 92),
                ('MODBUS (RS485 / RTU / TCP)', 90),
                ('MQTT & CoAP', 94),
                ('UART, SPI, I2C Buses', 92),
                ('TCP/IP, HTTP/REST, WebSockets', 95),
            ],
            'tags': ['C/C++', 'MicroPython', 'MODBUS RS485', 'MQTT', 'SPI', 'I2C', 'UART', 'LoRaWAN MAC']
        },
        {
            'category': 'Wireless & Networking',
            'icon': 'fa-solid fa-tower-broadcast',
            'skills': [
                ('LoRaWAN (ChirpStack / TTN)', 94),
                ('Cellular IoT (GPRS / 2G / LTE-M)', 90),
                ('Sigfox LPWAN', 80),
                ('Bluetooth Low Energy (BLE)', 86),
                ('Network Routing & Switching (CCNA)', 88),
                ('Field Antenna Tuning & RF Tests', 84),
            ],
            'tags': ['LoRaWAN', 'ChirpStack', 'Cellular GPRS', 'BLE', 'Wi-Fi', 'CCNA', 'Antenna Tuning']
        },
        {
            'category': 'Backend, Cloud & Databases',
            'icon': 'fa-solid fa-server',
            'skills': [
                ('Python (Django, DRF, Flask)', 94),
                ('Node.js & Express / NestJS', 88),
                ('Next.js & React Frameworks', 86),
                ('Time-Series DBs (InfluxDB, ClickHouse)', 92),
                ('Relational DBs (PostgreSQL, MySQL)', 90),
                ('Cloud Infrastructure (AWS, Azure, VPS)', 86),
            ],
            'tags': ['Django', 'Python', 'Node.js', 'Next.js', 'ClickHouse', 'InfluxDB', 'PostgreSQL', 'AWS', 'Redis']
        },
        {
            'category': 'Data Pipelines & Automation',
            'icon': 'fa-solid fa-diagram-project',
            'skills': [
                ('Node-RED Event Flow Pipelines', 95),
                ('Redis In-Memory Caching & Queues', 88),
                ('Linux Server Admin (Ubuntu/Debian)', 90),
                ('Docker Containerization', 82),
                ('Automated Anomaly Detection', 86),
                ('System Diagnostics & Benchmarking', 90),
            ],
            'tags': ['Node-RED', 'Docker', 'Linux', 'Systemd', 'Cron', 'Nginx', 'SSL/TLS', 'Bash']
        },
        {
            'category': 'Frontend & Engineering Tools',
            'icon': 'fa-solid fa-laptop-code',
            'skills': [
                ('Flutter & Cross-Platform UI', 82),
                ('Tailwind CSS, DaisyUI & HTML5', 92),
                ('Git Version Control & CI/CD', 90),
                ('Technical Strategy & Team Mentorship', 92),
                ('Bench Hardware Testing & QA', 94),
                ('Product Architecture & Roadmapping', 90),
            ],
            'tags': ['Flutter', 'Tailwind CSS', 'HTML5', 'Git', 'HTMX', 'Leadership', 'Hardware QA']
        },
    ]

    experience = [
        {
            'role': 'Head of Technology',
            'company': 'Powerpay Africa Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Nov 2024 – Present',
            'type': 'Full-Time Leadership',
            'summary': (
                'Leading the technology strategy, engineering direction, edge-to-cloud architecture, '
                'and technical roadmap for an industrial IoT smart metering company operating across East Africa.'
            ),
            'highlights': [
                'Directing end-to-end design and roll-out of smart prepayment and post-payment energy metering devices utilizing STM32 microcontrollers, MODBUS communication, and wireless telemetry.',
                'Architected high-throughput ingestion backends on Django, Node.js, and ClickHouse time-series data storage, processing thousands of telemetry messages per hour with 99.9% uptime.',
                'Leading hardware QA, firmware validation, and bench testing to guarantee fail-safe over-the-air performance across remote industrial sites.',
                'Supervising multidisciplinary engineering teams covering embedded firmware, hardware circuit design, cloud APIs, and field operations.'
            ],
            'stack': ['Technical Leadership', 'STM32', 'LoRaWAN', 'MODBUS', 'ClickHouse', 'Django', 'Node.js', 'System Architecture']
        },
        {
            'role': 'IoT Systems Engineer',
            'company': 'Powerpay Africa Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Mar 2024 – Nov 2024',
            'type': 'Full-Time Engineering',
            'summary': (
                'Engineered core firmware and communication stacks for smart electricity metering nodes deployed in commercial and residential properties.'
            ),
            'highlights': [
                'Wrote production-grade MicroPython and C firmware for ESP32 and STM32 chips interfacing with digital energy meters via MODBUS RS485.',
                'Designed cellular GPRS and LoRaWAN fallback pipelines ensuring zero data loss during network dropouts through localized SQLite buffer queues.',
                'Integrated Node-RED automation workflows with InfluxDB and Grafana for real-time electrical load visualization and automated overload trip detection.',
                'Conducted extensive field trials, RF path-loss measurements, and hardware reliability assessments in demanding electrical environments.'
            ],
            'stack': ['MicroPython', 'ESP32', 'MODBUS RS485', 'LoRaWAN', 'Cellular GPRS', 'InfluxDB', 'Node-RED', 'Grafana']
        },
        {
            'role': 'IoT Engineer',
            'company': 'Silvanus Telematics',
            'location': 'Nairobi, Kenya',
            'period': 'Jan 2022 – Aug 2023',
            'type': 'Full-Time Engineering',
            'summary': (
                'Designed, bench-tested, and deployed remote telematics and GPS fleet tracking hardware integrated with onboard vehicle CAN bus diagnostics.'
            ),
            'highlights': [
                'Engineered asset tracking devices using cellular SIMCom modules, GPS receivers, and low-power microcontrollers.',
                'Created Python backend services to decode proprietary binary telematics protocols and stream coordinates to real-time maps via WebSockets.',
                'Developed driver behavior scoring algorithms monitoring harsh braking, speeding, and excessive idling.',
                'Optimized device battery consumption with sleep-state power management routines, extending field battery endurance by 40%.'
            ],
            'stack': ['Embedded C', 'Python', 'SIMCom Modules', 'GPS / Telematics', 'CAN Bus', 'WebSockets', 'Power Optimization']
        },
        {
            'role': 'Graduate Engineering Intern',
            'company': 'New Kenya Planters Cooperative Union (New KPCU)',
            'location': 'Dandora, Nairobi, Kenya',
            'period': 'May 2021 – Sep 2021',
            'type': 'Engineering Internship',
            'summary': (
                'Assisted in industrial electrical engineering maintenance, power distribution, and motor control panels in heavy manufacturing plants.'
            ),
            'highlights': [
                'Carried out scheduled electrical preventive maintenance across industrial processing plants, reducing machine downtime.',
                'Assisted senior engineers in troubleshooting motor control panels, relay boards, and industrial automation equipment.',
            ],
            'stack': ['Industrial Automation', 'Motor Control Panels', 'Relay Logic', 'Preventive Maintenance']
        },
    ]

    education = get_education_data()
    certifications = get_certifications_data()

    portfolio = [
        {
            'id': 'svs-platform',
            'title': 'SVS Multi-Vendor Service Platform',
            'category': 'Full-Stack Web & E-Commerce',
            'description': (
                'A multi-vendor e-commerce and automotive service directory connecting service providers, vendors, and clients. '
                'Features vendor onboarding workflows, service booking calendars, automated invoicing, and a reactive UI.'
            ),
            'features': [
                'Multi-tenant vendor architecture with isolated service catalogs',
                'Real-time booking and calendar management powered by HTMX',
                'Automated PDF invoice generation and transaction receipts',
                'Responsive design with DaisyUI, Tailwind CSS, and custom dark/light palettes'
            ],
            'tech': ['Django', 'PostgreSQL', 'HTMX', 'DaisyUI', 'Tailwind CSS', 'JavaScript', 'Docker'],
            'images': ['svs_1.png', 'svs_2.png', 'svs_3.png', 'svs_4.png', 'svs_5.png', 'svs_6.png'],
            'icon': 'fa-solid fa-bag-shopping'
        },
        {
            'id': 'realtime-chat',
            'title': 'Real-Time WebSocket Communication Suite',
            'category': 'Real-Time Web & Messaging',
            'description': (
                'High-concurrency chat and messaging application built on Django Channels and WebSockets. '
                'Features instant messaging, user presence indicators, rich user profiles, and media sharing pipelines.'
            ),
            'features': [
                'Bi-directional WebSocket communication with Daphne ASGI',
                'User presence and typing state synchronization',
                'Responsive UI with modern drawer layouts and modal views',
                'Secure session authentication and channel layers with Redis'
            ],
            'tech': ['Django', 'Django Channels', 'ASGI / Daphne', 'Redis', 'WebSockets', 'Flowbite', 'JS'],
            'images': ['chat_1.jpeg', 'chat_2.jpeg'],
            'icon': 'fa-solid fa-comments'
        },
        {
            'id': 'iot-analytics-app',
            'title': 'IoT Energy Analytics & Remote Telemetry App',
            'category': 'IoT & Mobile Diagnostics',
            'description': (
                'Cross-platform mobile and desktop analytics tool that ingests real-time power metrics from field energy meters, '
                'visualizes high-frequency time-series data, and provides low-latency remote relay switching controls.'
            ),
            'features': [
                'Live time-series metric streaming from InfluxDB',
                'Remote bidirectional relay control and telemetry status',
                'Anomaly detection alerts and automated threshold triggers',
                'Lightweight cross-platform client built with Python Flet & Flutter'
            ],
            'tech': ['Python', 'Flet', 'Flutter', 'InfluxDB', 'Firebase', 'MQTT', 'MODBUS'],
            'images': ['flet_1.jpeg', 'flet_2.jpeg', 'flet_3.jpeg', 'flet_4.jpeg'],
            'icon': 'fa-solid fa-bolt'
        },
    ]

    pillars = [
        {
            'step': '01',
            'title': 'Edge Firmware & Sensors',
            'desc': 'Low-level C/C++ and MicroPython firmware engineered for STM32 and ESP32 with power optimization and sensor calibration.',
            'icon': 'fa-solid fa-microchip'
        },
        {
            'step': '02',
            'title': 'Telemetry & Protocols',
            'desc': 'Reliable multi-protocol field communication spanning LoRaWAN, Cellular (GPRS/LTE-M), MODBUS RS485, and MQTT.',
            'icon': 'fa-solid fa-tower-cell'
        },
        {
            'step': '03',
            'title': 'Cloud & Time-Series DBs',
            'desc': 'High-throughput ingestion pipelines powered by Django, Node.js, ClickHouse, and InfluxDB on robust Linux infrastructure.',
            'icon': 'fa-solid fa-database'
        },
        {
            'step': '04',
            'title': 'Dashboards & Control',
            'desc': 'Responsive dashboards, real-time alerting via Node-RED, and cross-platform mobile diagnostics built with Flutter & React.',
            'icon': 'fa-solid fa-chart-line'
        }
    ]

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'experience': experience,
        'education': education,
        'certifications': certifications,
        'portfolio': portfolio,
        'pillars': pillars,
    }
    return render(request, "index.html", context)


def education_view(request):
    """Dedicated Education, Graduate Research & Capstone Engineering Portal."""
    context = {
        'education': get_education_data(),
        'certifications': get_certifications_data(),
    }
    return render(request, "education.html", context)


def resume_view(request):
    """Dedicated interactive resume page with print & download capabilities."""
    return render(request, "resume.html")


@require_POST
@csrf_exempt
def contact_submit(request):
    """Handles contact form submissions via HTMX or standard POST."""
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip() or 'Portfolio Inquiry'
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        return render(request, 'partials/contact_response.html', {
            'success': False,
            'message': 'Please fill in all required fields (Name, Email, and Message).'
        })

    return render(request, 'partials/contact_response.html', {
        'success': True,
        'name': name,
        'message': f"Thank you, {name}! Your message has been received. Jeff will reach out to you shortly at {email}."
    })


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://jefftarimo.co.ke/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def sitemap_xml(request):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://jefftarimo.co.ke/</loc>
    <lastmod>2026-10-27</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://jefftarimo.co.ke/education/</loc>
    <lastmod>2026-10-27</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://jefftarimo.co.ke/resume/</loc>
    <lastmod>2026-10-27</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""
    return HttpResponse(xml, content_type="application/xml")
