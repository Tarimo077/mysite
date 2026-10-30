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
            },
            'projects': [
                {
                    'id': 'chomsky-hierarchy',
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
                    'spec_title': 'Formal Hierarchy Breakdown',
                    'spec_icon': 'fa-solid fa-cubes',
                    'specs': [
                        {'label': 'Type 3 (Regular):', 'text': 'DFA / NFA / RegEx • No memory • O(n) time • Fully Decidable'},
                        {'label': 'Type 2 (Context-Free):', 'text': 'Pushdown Automata (PDA) • LIFO Stack memory • O(n³) CYK'},
                        {'label': 'Type 1 (Context-Sensitive):', 'text': 'Linear Bounded Automata (LBA) • Tape ≤ n • PSPACE-complete'},
                        {'label': 'Type 0 (Unrestricted):', 'text': 'Turing Machine • Infinite Tape • Turing-Complete (Undecidable)'},
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
                },
                {
                    'id': 'security-smells-iac',
                    'badge': 'Graduate Security Presentation (Week 1)',
                    'type': 'ICS 6140 Seminar Presentation',
                    'unit': 'ICS 6140: Computer Systems Security (Secure Software Development)',
                    'title': 'The Seven Sins: Security Smells in Infrastructure as Code Scripts',
                    'subtitle': 'Empirical Analysis of DevSecOps Anti-Patterns, Static Linting (SLIC), and CWE Weaknesses in Production IaC',
                    'summary': (
                        'Critical security presentation examining recurring insecure coding patterns ("security smells") across 15,232 production '
                        'Infrastructure as Code (Puppet) scripts mined from 293 open-source repositories (GitHub, Mozilla, OpenStack, and Wikimedia). '
                        'Evaluates the SLIC static analysis rule engine, maps seven core configuration anti-patterns to MITRE Common Weakness Enumerations (CWE), '
                        'and analyzes smell persistence (up to 98 months) alongside developer remediation feedback.'
                    ),
                    'highlights': [
                        'Taxonomy of the "Seven Sins" mapped to CWEs: Hard-coded Secrets, Admin by Default, Invalid IP (0.0.0.0) Binding, HTTP without TLS, Weak Crypto, Empty Passwords, and Suspicious Comments',
                        'SLIC Static Analyzer Architecture: Lexical token vectorization + AST boolean rule predicates achieving 0.99 Precision and 0.99 Recall',
                        'Empirical Findings: 21,201 security smells identified across 15,232 scripts, including 16,952 hard-coded secrets persisting up to 98 months (~8.1 years)',
                        'DevSecOps Shift-Left Mitigation: Pre-commit AST linting gates, centralized secret vaulting (HashiCorp Vault), and zero-trust configuration defaults'
                    ],
                    'spec_title': 'The Seven IaC Security Sins (CWE Mapping)',
                    'spec_icon': 'fa-solid fa-shield-halved',
                    'specs': [
                        {'label': 'Hard-Coded Secrets (CWE-798):', 'text': '16,952 occurrences (~80% of all smells) • Keys, usernames & 1,326 passwords'},
                        {'label': 'Invalid IP & Cleartext (CWE-284/319):', 'text': '0.0.0.0 wildcard bindings & unencrypted HTTP endpoints susceptible to MITM'},
                        {'label': 'Weak Crypto & Privs (CWE-327/250):', 'text': 'Broken MD5/SHA-1 password hashing & default root/admin user provisioning'},
                        {'label': 'Empirical Longevity & Acceptance:', 'text': 'Up to 98 months persistence in Git • 64.4% practitioner bug acceptance rate'},
                    ],
                    'tags': [
                        'Secure Software Development',
                        'DevSecOps',
                        'Infrastructure as Code (IaC)',
                        'Static Analysis (SLIC)',
                        'MITRE CWE',
                        'Secret Management'
                    ],
                    'downloads': [
                        {
                            'name': 'Presentation Slides (.pptx)',
                            'file_url': 'documents/ICS_6140_Tarimo_Jeff_Security_Smells_Presentation.pptx',
                            'file_name': 'ICS_6140_Tarimo_Jeff_Security_Smells_Presentation.pptx',
                            'icon': 'fa-solid fa-file-powerpoint',
                            'btn_class': 'edu-btn--slides'
                        },
                        {
                            'name': 'Reference Paper (ICSE 2019 PDF)',
                            'url': 'https://akondrahman.github.io/files/papers/icse19_slic.pdf',
                            'external': True,
                            'icon': 'fa-solid fa-arrow-up-right-from-square',
                            'btn_class': 'edu-btn--pdf'
                        }
                    ]
                },
                {
                    'id': 'biometric-security-systems',
                    'badge': 'Graduate Security Presentation (Week 2)',
                    'type': 'ICS 6140 Seminar Presentation',
                    'unit': 'ICS 6140: Computer Systems Security (Biometric Security Systems)',
                    'title': 'A Survey of Biometrics Security Systems: Technologies, Architectures & Challenges',
                    'subtitle': 'Comparative Analysis of Physiological & Behavioral Modalities, Access Control Middleware, and Anti-Spoofing Defenses',
                    'summary': (
                        'Comprehensive evaluation of biometric authentication architectures across physical and logical access control domains. '
                        'Examines the seven foundational biometric criteria (uniqueness, universality, permanence, collectability, performance, acceptability, '
                        'and circumvention), compares physiological and behavioral feature extraction pipelines, and proposes modern defense-in-depth '
                        'mitigations against presentation attacks, AI deepfakes, and template irrevocability.'
                    ),
                    'highlights': [
                        'Modality Feature Extraction: Fingerprint minutiae (Loops 60%, Whorls 34%), 200+ point Iris textural mapping, and subcutaneous Near-IR Palm Vein scanning (0.5s verification)',
                        'Access Control & Middleware: Bridging edge biometric sensors with centralized cryptographic verification servers across physical and logical domains',
                        'Privacy & Threat Analysis: Addressing the Irrevocability Dilemma of biological templates, function creep, covert surveillance, and FAR/FRR trade-offs',
                        'Resilient Engineering Defenses: Multi-modal sensor fusion, hardware liveness detection (pulse/thermal), and cancelable homomorphic templates'
                    ],
                    'spec_title': 'Biometric Modalities & Defense Architecture',
                    'spec_icon': 'fa-solid fa-fingerprint',
                    'specs': [
                        {'label': 'Iris & Subcutaneous Vein:', 'text': '99.9% accuracy • 200+ iris points • 0.5s Near-IR vascular scan • Spoof-resistant'},
                        {'label': 'Fingerprint & Facial Geometry:', 'text': 'Ridge endings/bifurcations & nodal facial distances • Contactless & edge-ready'},
                        {'label': 'Voice & DNA Profiling:', 'text': 'Vocal tract + behavioral pitch challenges • VNTR tandem repeat genetic loci'},
                        {'label': 'Modern Hardening:', 'text': 'Multi-modal fusion • Hardware liveness anti-spoofing • Cancelable fuzzy vaults'},
                    ],
                    'tags': [
                        'Biometric Security',
                        'Access Control',
                        'Iris & Vein Recognition',
                        'Minutiae Matching',
                        'Liveness Detection',
                        'Cancelable Biometrics'
                    ],
                    'downloads': [
                        {
                            'name': 'Presentation Slides (.pptx)',
                            'file_url': 'documents/ICS_6140_Jeff_TARIMO_Biometric_Security_Presentation.pptx',
                            'file_name': 'ICS_6140_Jeff_TARIMO_Biometric_Security_Presentation.pptx',
                            'icon': 'fa-solid fa-file-powerpoint',
                            'btn_class': 'edu-btn--slides'
                        },
                        {
                            'name': 'Reference Survey Paper (WUSTL)',
                            'url': 'https://classes.engineering.wustl.edu/~jain/cse571-11/ftp/biomet/',
                            'external': True,
                            'icon': 'fa-solid fa-arrow-up-right-from-square',
                            'btn_class': 'edu-btn--pdf'
                        }
                    ]
                }
            ]
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
        'email': 'business@jefftarimo.co.ke',
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
            'title': 'Head of Technology',
            'company': 'Powerpay Africa Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Feb 2025 – Present',
            'current': True,
            'description': 'Directing overall technology vision, infrastructure scaling, strategic IT planning, and architectural roadmaps across hardware & software.',
            'highlights': [
                'Direct overall technology vision, infrastructure scaling, strategic IT planning, and architectural roadmaps across hardware & software.',
                'Lead engineering teams across firmware, cloud backend, and mobile apps to deliver smart energy metering and financing systems.',
                'Orchestrate tech stack decisions, cloud operations (AWS/Azure/Ubuntu), and technical delivery to align with company growth goals.'
            ],
            'stack': ['Technical Leadership', 'System Architecture', 'AWS/Azure', 'Ubuntu Linux', 'Django', 'IoT Infrastructure']
        },
        {
            'title': 'Head of IoT',
            'company': 'Powerpay Africa Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Feb 2023 – Jan 2025',
            'current': False,
            'description': 'Spearheaded firmware engineering, multi-protocol telemetry, and backend cloud architecture for smart energy meters.',
            'highlights': [
                'Spearheaded firmware engineering using C++ and MicroPython for smart energy meters and edge telemetry controllers.',
                'Deployed multi-protocol communication pipelines (MODBUS RS485, GPRS, Wi-Fi, BLE) for continuous remote asset monitoring.',
                'Architected scalable backend services and REST APIs with Node.js, Django, ClickHouse, and PostgreSQL on Ubuntu cloud servers.',
                'Automated data normalization and exception alerts via custom Node-RED workflows, eliminating manual intervention.'
            ],
            'stack': ['C++', 'MicroPython', 'MODBUS RS485', 'LoRaWAN', 'Cellular GPRS', 'Django', 'ClickHouse', 'PostgreSQL', 'Node-RED', 'Flutter']
        },
        {
            'title': 'Head of IoT',
            'company': 'Upande Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Sep 2022 – Jan 2023',
            'current': False,
            'description': 'Managed product strategy and hardware delivery roadmaps as Product Owner across municipal and agricultural remote sensing initiatives.',
            'highlights': [
                'Directed product strategy and hardware delivery roadmaps as Product Owner across municipal and agricultural remote sensing initiatives.',
                'Streamlined device testing and dispatch pipelines using Node-RED, reducing commissioning time across field deployments.',
                'Liaised with external enterprise stakeholders to translate complex monitoring requirements into scalable IoT architectures.'
            ],
            'stack': ['Product Ownership', 'Node-RED', 'LoRaWAN', 'Agricultural IoT', 'Stakeholder Management', 'System Design']
        },
        {
            'title': 'IoT Engineer',
            'company': 'Upande Limited',
            'location': 'Nairobi, Kenya',
            'period': 'Apr 2021 – Aug 2022',
            'current': False,
            'description': 'Assembled, calibrated, and maintained industrial sensor node fleets and time-series telemetry pipelines.',
            'highlights': [
                'Assembled, calibrated, and deployed industrial sensor nodes (water level, ultrasonic, flow, weather) using LoRaWAN and GSM.',
                'Proactively maintained field device fleets, diagnosing power faults and issuing remote firmware updates to maximize uptime.',
                'Configured InfluxDB time-series instances for sensor data ingestion, enabling real-time analytics and client dashboard visualizations.'
            ],
            'stack': ['LoRaWAN', 'GSM/Cellular', 'InfluxDB', 'Ultrasonic Sensors', 'Firmware Flashing', 'Hardware Diagnostics']
        },
        {
            'title': 'Electrical Engineering Intern',
            'company': 'New Kenya Co-operative Creameries',
            'location': 'Nyeri, Kenya',
            'period': 'Mar 2016 – Aug 2016',
            'current': False,
            'description': 'Industrial plant electrical preventive maintenance, motor control circuits, and automation troubleshooting.',
            'highlights': [
                'Carried out scheduled electrical preventive maintenance across industrial dairy processing plants, reducing machine downtime.',
                'Assisted senior engineers in troubleshooting motor control panels, relay boards, and industrial automation equipment.'
            ],
            'stack': ['Industrial Automation', 'Motor Control Panels', 'Relay Logic', 'Preventive Maintenance']
        },
    ]

    education = get_education_data()
    certifications = get_certifications_data()

    portfolio = [
        {
            'id': 'dlt-workbench',
            'title': 'DL/T 645-2007 MQTT Smart Meter Encoder & Decoder Workbench',
            'category': 'IoT & Smart Metering Protocol Tool',
            'url': '/tools/dlt-encoder-decoder/',
            'url_display': 'jefftarimo.co.ke/tools/dlt-encoder-decoder/',
            'description': (
                'Industrial-grade DL/T 645-2007 telemetry & command engineering workbench for smart energy meters. '
                'Enables bidirectional translation between raw serial RS485 / optical frames (BCD + 0x33 byte offset, modulo-256 CS) '
                'and structured MQTT JSON command and response packets for edge gateways and IoT cloud platforms.'
            ),
            'features': [
                'Bidirectional Encoding & Decoding: Generates raw 645 frames with automatic 0xFE preamble bytes, control codes (0x11 Read, 0x14 Write, 0x08 Broadcast), and reverse BCD addresses',
                'MQTT Payload Synthesizer: Packages hex frames into structured JSON envelopes (`/cmd` & `/response`) with automated 16-digit unique message IDs, timestamps, and QoS settings',
                'Comprehensive DI Catalog: Built-in decoding presets for active/reactive energy, tariff schedules, voltage, current, power factor, frequency, and meter clock synchronization',
                'Edge Telemetry Verification: Live protocol parser that inspects checksum integrity, extracts engineering units, and validates exception/error status flags in real-time'
            ],
            'tech': ['DL/T 645-2007', 'MQTT', 'RS485', 'JavaScript', 'Hex/BCD Encoding', 'Smart Metering', 'IoT Telemetry'],
            'images': ['dlt_workbench_1.png'],
            'icon': 'fa-solid fa-bolt-lightning'
        },
        {
            'id': 'jt-erp',
            'title': 'JT ERP — Enterprise Resource Planning Suite',
            'category': 'Enterprise Operations & Finance ERP',
            'url': 'https://erp.jefftarimo.co.ke',
            'url_display': 'erp.jefftarimo.co.ke',
            'description': (
                'End-to-end cloud ERP platform engineered for multi-department operations, project & task tracking, '
                'procurement workflows, payment vouchers, inventory & petty cash controls, HR leave/timesheets, and internal team messaging.'
            ),
            'features': [
                'Multi-stage approval pipelines for Payment Vouchers & Item Requisitions with PDF/Word/Excel exports',
                'Interactive project boards, employee timesheets, leave management, and role-based access control',
                'Real-time internal team chat channels, direct messaging, and instant activity notifications',
                'Serverless cloud architecture backed by managed PostgreSQL, OTP 2FA security, and automated SMTP alerts'
            ],
            'tech': ['Django', 'PostgreSQL', 'Tailwind CSS', 'DaisyUI', 'ReportLab PDF', 'OpenPyXL', 'Vercel'],
            'images': ['jterp_1.png', 'jterp_2.png', 'jterp_3.png', 'jterp_4.png'],
            'icon': 'fa-solid fa-sitemap'
        },
        {
            'id': 'qiksearch-platform',
            'title': 'Qiksearch Agricultural E-Commerce Platform',
            'category': 'E-Commerce & Live CMS Platform',
            'url': 'https://qiksearch.jefftarimo.co.ke',
            'url_display': 'qiksearch.jefftarimo.co.ke',
            'description': (
                'High-performance mobile-first agricultural machinery and farm supplies storefront engineered to replace legacy WooCommerce '
                'with sub-200ms responses, multi-faceted catalog filtering, 1-click WhatsApp ordering, and a real-time Superadmin Live Editor.'
            ),
            'features': [
                'Superadmin Live Editor (`/superadmin/live-editor/`) with instant in-memory component preview across Desktop/Tablet/Mobile viewports',
                'Multi-faceted filtering, debounced typeahead search, dynamic discount badges, and Grid/List view toggles',
                'Direct pre-formatted WhatsApp order routing (`wa.me`) and stateless signed-cookie cart & wishlist sessions',
                'Automated Schema.org JSON-LD product metadata, dynamic XML sitemaps, and live Google Shopping Merchant feeds'
            ],
            'tech': ['Django 5.2', 'Tailwind CSS', 'Vanilla JS', 'WhiteNoise', 'JSON-LD SEO', 'Google Merchant XML'],
            'images': ['qiksearch_1.png', 'qiksearch_2.png', 'qiksearch_3.png', 'qiksearch_4.png'],
            'icon': 'fa-solid fa-wheat-awn'
        },
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


def dlt_workbench_view(request):
    """Interactive DL/T 645-2007 MQTT Meter Payload Workbench."""
    return render(request, "tools/dlt_workbench.html")


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
    <loc>https://jefftarimo.co.ke/tools/dlt-encoder-decoder/</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
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
