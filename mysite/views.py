from django.shortcuts import render

def home(request):
    skills = [
        ('DJANGO', 90),
        ('WIRELESS COMMUNICATION: LORAWAN, LORA, CELLULAR, SIGFOX, BLUETOOTH', 85),
        ('MICROCONTROLLERS: RASPBERRY PI, ARDUINO, STM32', 85),
        ('HTML, CSS (TAILWIND/BOOTSTRAP), DAISYUI', 80),
        ('DATABASES: MYSQL, POSTGRESQL, INFLUXDB', 75),
        ('LINUX, BASH, REDIS CACHING, DEVOPS (AZURE/AWS)', 70),
        ('TYPESCRIPT / JAVASCRIPT', 70),
    ]
    portfolio = [
        ('SVS (E-Commerce)', 'SVS is a full-stack Django web application that allows users to register as service providers or clients, manage payments, view provider profiles, and track service progress with rich UI and analytics.', ['Django', 'Postgres', 'HTML', 'CSS', 'HTMX', 'Javascript', 'DaisyUI'], ['svs_1.png', 'svs_2.png', 'svs_3.png', 'svs_4.png', 'svs_5.png', 'svs_6.png']),
        ('Chat Application', 'A chat application that allows users of the app to communicate in real time and view each other profle and is soon to be expanded to allow sharing of photos and media', ['Django', 'Django Channels', 'Websockets', 'HTML', 'CSS', 'JS', 'Flowbite'], ['chat_1.jpeg', 'chat_2.jpeg']),
        ('Analytics Mobile App', 'A mobile app that pulls energy data on IoT devices, provides insightful analytics and allows you to remotely switch off and switch on whatever device is connected to the IoT device.', ['Python', 'Flet', 'Flutter', 'Firebase', 'InfluxDB'], ['flet_1.jpeg', 'flet_2.jpeg', 'flet_3.jpeg', 'flet_4.jpeg']),
    ]
    context = {
        'skills': skills,
        'portfolio': portfolio
    }
    return render(request, "index.html",  context)
