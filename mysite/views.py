from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

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
                ('MQTT & WebSockets', 94),
                ('UART / SPI / I2C Buses', 92),
                ('HTTP / HTTPS REST APIs', 95),
            ],
            'tags': ['C/C++', 'MicroPython', 'MODBUS', 'MQTT', 'UART', 'SPI', 'I2C', 'FreeRTOS']
        },
        {
            'category': 'Wireless & Networking',
            'icon': 'fa-solid fa-tower-broadcast',
            'skills': [
                ('LoRaWAN (The Things Network, ChirpStack)', 92),
                ('Cellular IoT (GPRS / LTE-M / NB-IoT)', 88),
                ('Bluetooth Low Energy (BLE)', 86),
                ('Wi-Fi Mesh & Station', 90),
                ('Sigfox', 80),
                ('CCNA Routing & Switching', 85),
            ],
            'tags': ['LoRaWAN', 'GPRS / 4G', 'BLE', 'Wi-Fi', 'Sigfox', 'CCNA', 'TCP/IP']
        },
        {
            'category': 'Backend & Cloud Infrastructure',
            'icon': 'fa-solid fa-cloud',
            'skills': [
                ('Python (Django / Django Channels / FastAPI)', 94),
                ('Node.js & Next.js', 82),
                ('Linux Server Administration (Ubuntu)', 88),
                ('AWS & Azure Cloud Services', 82),
                ('Redis In-Memory Caching & Queues', 85),
                ('RESTful API Design & OpenAPI', 92),
            ],
            'tags': ['Django', 'Python', 'Node.js', 'Redis', 'AWS', 'Azure', 'Ubuntu Linux', 'Gunicorn']
        },
        {
            'category': 'Databases & Time-Series',
            'icon': 'fa-solid fa-database',
            'skills': [
                ('InfluxDB (Time-series telemetry)', 92),
                ('ClickHouse (High-throughput analytics)', 86),
                ('PostgreSQL & PostGIS', 88),
                ('MySQL / MariaDB', 85),
                ('Data Normalization & Retention Policies', 90),
            ],
            'tags': ['InfluxDB', 'ClickHouse', 'PostgreSQL', 'MySQL', 'Time-Series', 'SQL Optimization']
        },
        {
            'category': 'Frontend, Mobile & Automation',
            'icon': 'fa-solid fa-laptop-code',
            'skills': [
                ('Node-RED Automation & Alerting', 95),
                ('Flutter & Flet Mobile Diagnostics', 85),
                ('Tailwind CSS & Modern HTML5', 90),
                ('JavaScript & HTMX', 88),
                ('Technical Leadership & Architecture', 92),
            ],
            'tags': ['Node-RED', 'Flutter', 'Tailwind CSS', 'HTMX', 'React', 'JavaScript', 'Technical Strategy']
        },
    ]

    experience = [
        {
            'title': 'Head of Technology',
            'company': 'Powerpay Africa Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Feb 2025 – Present',
            'current': True,
            'description': 'Leading technology vision, infrastructure scalability, and strategic IT planning across hardware and software engineering teams.',
            'highlights': [
                'Direct overall technology vision, infrastructure scaling, strategic IT planning, and architectural roadmaps across hardware & software.',
                'Lead engineering teams across firmware, cloud backend, and mobile apps to deliver smart energy metering and financing systems.',
                'Orchestrate tech stack decisions, cloud operations (AWS/Azure/Ubuntu), and technical delivery to align with company growth goals.',
                'Manage cross-functional hardware and software teams toward product milestones and enterprise client commitments.',
            ],
            'stack': ['Technology Strategy', 'Engineering Leadership', 'AWS/Azure', 'Django', 'IoT Infrastructure', 'System Architecture']
        },
        {
            'title': 'Head of IoT',
            'company': 'Powerpay Africa Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Feb 2023 – Jan 2025',
            'current': False,
            'description': 'Directed end-to-end IoT engineering, firmware architecture, smart energy telemetry, and cloud integration.',
            'highlights': [
                'Spearheaded firmware engineering using C++ and MicroPython for smart energy meters and edge telemetry controllers.',
                'Deployed multi-protocol communication pipelines utilizing MODBUS (RS485), GPRS, Wi-Fi, and BLE for continuous remote asset monitoring.',
                'Architected scalable backend services and REST APIs with Node.js, Django, ClickHouse, and PostgreSQL on Ubuntu AWS/Azure environments.',
                'Built real-time monitoring user interfaces and mobile diagnostics tools using React and Flutter.',
                'Automated data normalization and exception alerts via custom Node-RED workflows, eliminating manual intervention.',
            ],
            'stack': ['C++', 'MicroPython', 'MODBUS (RS485)', 'Django', 'ClickHouse', 'PostgreSQL', 'Node-RED', 'Flutter', 'AWS/Azure']
        },
        {
            'title': 'Head of IoT',
            'company': 'Upande Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Sep 2022 – Jan 2023',
            'current': False,
            'description': 'Managed product strategy and hardware delivery across municipal and agricultural IoT initiatives.',
            'highlights': [
                'Directed product strategy and hardware delivery roadmaps as Product Owner across municipal and agricultural remote sensing initiatives.',
                'Streamlined device testing and dispatch pipelines using Node-RED, reducing commissioning time across field deployments.',
                'Liaised with external enterprise stakeholders to translate complex monitoring requirements into scalable IoT architectures.',
            ],
            'stack': ['Product Ownership', 'Node-RED', 'LoRaWAN', 'Agricultural IoT', 'Stakeholder Management']
        },
        {
            'title': 'IoT Engineer',
            'company': 'Upande Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Apr 2021 – Aug 2022',
            'current': False,
            'description': 'Field deployment, sensor calibration, firmware maintenance, and time-series analytics.',
            'highlights': [
                'Assembled, calibrated, and deployed industrial sensor nodes (water level, ultrasonic, flow, weather) using LoRaWAN and GSM.',
                'Proactively maintained field device fleets, diagnosing power faults and issuing remote firmware updates to maximize uptime.',
                'Configured InfluxDB time-series instances for sensor data ingestion, enabling real-time analytics and client dashboard visualizations.',
            ],
            'stack': ['LoRaWAN', 'GSM/GPRS', 'InfluxDB', 'Ultrasonic Sensors', 'Firmware Flashing', 'Hardware Debugging']
        },
        {
            'title': 'Electrical Engineering Intern',
            'company': 'New Kenya Co-operative Creameries',
            'location': 'Nyeri, Kenya',
            'period': 'Mar 2016 – Aug 2016',
            'current': False,
            'description': 'Industrial plant electrical maintenance, motor control circuits, and automation troubleshooting.',
            'highlights': [
                'Carried out scheduled electrical preventive maintenance across industrial dairy processing plants, reducing machine downtime.',
                'Assisted senior engineers in troubleshooting motor control panels, relay boards, and industrial automation equipment.',
            ],
            'stack': ['Industrial Automation', 'Motor Control Panels', 'Relay Logic', 'Preventive Maintenance']
        },
    ]

    education = [
        {
            'degree': 'M.Sc. in Computer Science',
            'institution': 'Zetech University',
            'location': 'Ruiru, Kenya',
            'period': 'Aug 2026 – Dec 2027',
            'status': 'Enrolled / Upcoming',
            'details': 'Focusing on distributed systems, advanced algorithms, edge computing architectures, and cloud scalability.'
        },
        {
            'degree': 'B.Sc. in Electronics & Computer Engineering',
            'institution': 'Jomo Kenyatta University of Agriculture and Technology (JKUAT)',
            'location': 'Juja, Kiambu, Kenya',
            'period': 'Graduated 2021',
            'status': 'Completed',
            'details': 'Comprehensive foundation in microprocessors, digital signal processing, embedded systems, telecommunications, and software engineering.'
        }
    ]

    certifications = [
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

    portfolio = [
        {
            'id': 'svs-platform',
            'title': 'SVS Multi-Vendor Service Platform',
            'category': 'Full-Stack Web Platform',
            'description': (
                'A comprehensive full-stack Django enterprise platform enabling service providers and clients to connect, '
                'manage bookings, process secure payments, track service milestones with real-time updates, and monitor performance analytics.'
            ),
            'features': [
                'Dynamic provider verification & tiered access control',
                'Real-time booking status transitions via HTMX',
                'Integrated payments and financial transaction logging',
                'Comprehensive analytics reporting dashboard'
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
    <lastmod>2026-10-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://jefftarimo.co.ke/resume/</loc>
    <lastmod>2026-10-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""
    return HttpResponse(xml, content_type="application/xml")
