from PIL import Image, ImageDraw, ImageFont

# Canvas
w, h = 1200, 750
img = Image.new('RGB', (w, h), color='#070b14')
draw = ImageDraw.Draw(img)

# Card background
draw.rounded_rectangle([30, 30, w - 30, h - 30], radius=16, fill='#0f172a', outline='#334155', width=2)

# Header bar
draw.rectangle([30, 30, w - 30, 95], fill='#0b1120')
draw.line([30, 95, w - 30, 95], fill='#334155', width=2)

# Window control dots
draw.ellipse([50, 56, 64, 70], fill='#ef4444')
draw.ellipse([72, 56, 86, 70], fill='#f59e0b')
draw.ellipse([94, 56, 108, 70], fill='#10b981')

try:
    font_lg = ImageFont.truetype('arialbd.ttf', 22)
    font_md = ImageFont.truetype('arialbd.ttf', 15)
    font_sm = ImageFont.truetype('arial.ttf', 13)
    font_mono = ImageFont.truetype('consola.ttf', 12)
    font_mono_bold = ImageFont.truetype('consolab.ttf', 12)
except Exception:
    font_lg = font_md = font_sm = font_mono = font_mono_bold = ImageFont.load_default()

draw.text((130, 52), 'DL/T 645-2007 MQTT Meter Payload Workbench', fill='#f8fafc', font=font_lg)
draw.text((750, 55), 'Industrial Protocol Tool & Telemetry Engine', fill='#14b8a6', font=font_sm)

# Tabs
tabs = [('1. Command Encoder', True), ('2. Response Decoder', False), ('3. Telemetry Decoder', False), ('4. Protocol Reference', False)]
tx = 50
for tab_name, active in tabs:
    t_w = 160
    if active:
        draw.rounded_rectangle([tx, 115, tx + t_w, 150], radius=6, fill='#0d9488')
        draw.text((tx + 14, 124), tab_name, fill='#ffffff', font=font_md)
    else:
        draw.rounded_rectangle([tx, 115, tx + t_w, 150], radius=6, fill='#1e293b', outline='#334155')
        draw.text((tx + 12, 124), tab_name, fill='#94a3b8', font=font_sm)
    tx += t_w + 10

# Left Card: MQTT & Meter Settings
draw.rounded_rectangle([50, 168, 570, 420], radius=10, fill='#0b1120', outline='#1e293b', width=1)
draw.text((70, 182), '1. Meter & MQTT Configuration', fill='#14b8a6', font=font_md)

draw.text((70, 215), 'Meter Address (12-digit BCD):', fill='#94a3b8', font=font_sm)
draw.rounded_rectangle([70, 235, 290, 268], radius=6, fill='#1e293b', outline='#475569')
draw.text((85, 243), '002404018932', fill='#38bdf8', font=font_mono_bold)

draw.text((310, 215), 'Generated Msg ID:', fill='#94a3b8', font=font_sm)
draw.rounded_rectangle([310, 235, 550, 268], radius=6, fill='#1e293b', outline='#475569')
draw.text((325, 243), '1714478901234567', fill='#cbd5e1', font=font_mono)

draw.text((70, 280), 'MQTT Command Topic:', fill='#94a3b8', font=font_sm)
draw.rounded_rectangle([70, 300, 550, 333], radius=6, fill='#1e293b', outline='#475569')
draw.text((85, 308), '/v1/device/002404018932/cmd', fill='#38bdf8', font=font_mono)

draw.text((70, 345), 'Command / Data Identifier Preset:', fill='#94a3b8', font=font_sm)
draw.rounded_rectangle([70, 365, 550, 398], radius=6, fill='#1e293b', outline='#475569')
draw.text((85, 373), 'Read Combined Active Energy (DI = 00 01 00 00)', fill='#f8fafc', font=font_sm)

# Left Card 2: Raw 645 Frame & Checksum
draw.rounded_rectangle([50, 436, 570, 700], radius=10, fill='#0b1120', outline='#1e293b', width=1)
draw.text((70, 450), '2. Assembled DL/T 645-2007 Frame (Hex)', fill='#14b8a6', font=font_md)

hex_sample = 'FE FE FE FE 68 32 89 01 04 24 00 68 11 04 33 33 34 33 9E 16'
draw.rounded_rectangle([70, 480, 550, 545], radius=6, fill='#1e293b', outline='#475569')
draw.text((85, 495), hex_sample, fill='#34d399', font=font_mono_bold)
draw.text((85, 520), 'Wake: 4x0xFE | Control: 0x11 | Length: 0x04 | CS: 0x9E', fill='#94a3b8', font=font_mono)

draw.text((70, 560), 'Field Dissection & Verification:', fill='#cbd5e1', font=font_sm)
fields = [
    ('Frame Delimiters:', '0x68 ... 0x68 ... 0x16 (Compliant)'),
    ('Address (Reversed BCD):', '32 89 01 04 24 00 -> 002404018932'),
    ('DI Offset (+0x33):', '33 33 34 33 -> 00 00 01 00 (Active Total)'),
    ('Checksum Calculation:', 'Modulo 256 Validated (0x9E - OK)')
]
fy = 585
for k, v in fields:
    draw.text((70, fy), k, fill='#94a3b8', font=font_mono)
    draw.text((265, fy), v, fill='#f8fafc', font=font_mono)
    fy += 22

# Right Card: MQTT JSON Envelope & Payload
draw.rounded_rectangle([590, 168, 1150, 700], radius=10, fill='#0b1120', outline='#1e293b', width=1)
draw.text((610, 182), '3. Generated MQTT JSON Telemetry / Command Packet', fill='#38bdf8', font=font_md)

json_lines = [
    '{',
    '  "msg_id": "1714478901234567",',
    '  "timestamp": "2026-10-30T10:14:00Z",',
    '  "meter_id": "002404018932",',
    '  "protocol": "DLT_645_2007",',
    '  "command": "READ_ENERGY_TOTAL",',
    '  "raw_frame_hex": "FEFEFEFE68328901042400681104333334339E16",',
    '  "payload": {',
    '    "control_code": "0x11",',
    '    "di": "00010000",',
    '    "description": "Total Active Energy",',
    '    "unit": "kWh",',
    '    "status": "READY_TO_PUBLISH"',
    '  },',
    '  "qos": 1,',
    '  "retain": false',
    '}'
]
jy = 220
for line in json_lines:
    if ':' in line:
        parts = line.split(':', 1)
        draw.text((610, jy), parts[0] + ':', fill='#38bdf8', font=font_mono)
        val = parts[1]
        val_color = '#34d399' if '"' in val else '#f59e0b'
        draw.text((610 + int(font_mono.getlength(parts[0] + ': ')), jy), val, fill=val_color, font=font_mono)
    else:
        draw.text((610, jy), line, fill='#94a3b8', font=font_mono)
    jy += 25

# Action bar in right box
draw.rounded_rectangle([610, 638, 860, 678], radius=6, fill='#0d9488')
draw.text((645, 650), 'Live Interactive Tool', fill='#ffffff', font=font_md)

draw.rounded_rectangle([880, 638, 1120, 678], radius=6, fill='#1e293b', outline='#0d9488')
draw.text((915, 650), 'Decode Response Hex', fill='#14b8a6', font=font_md)

img.save(r'C:\Users\Admin\Desktop\mysites\mysite\static\images\dlt_workbench_1.png', 'PNG')
print('Generated image saved to static/images/dlt_workbench_1.png')
