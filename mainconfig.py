"""
Configuration file สำหรับ Exam Formatter
แก้ไขค่าต่างๆ ที่นี่เพื่อปรับแต่งระบบ
"""

from docx.shared import RGBColor

# =====================================================
# LOGO CONFIGURATION
# =====================================================
# เพิ่ม/ลบ/แก้ไข Logo ได้ง่ายที่นี่
# วิธีหา File ID: เปิดไฟล์ใน Google Drive → Share → Copy link
# ลิงก์จะเป็น: https://drive.google.com/file/d/FILE_ID/view

LOGO_CONFIG = {
    'sptlogo': {
        'label': 'Logo สพฐ',
        'file_id': '1GJfXRACPNaOJ4_OP7-0zty4mxbeo1Cwu',
        'width_cm': 1.8,
        'height_cm': 1.8,
        'h_pos_cm': 15.87,
        'v_pos_cm': -0.34,
        'location': 'header',
        'behind_doc': True,
    },
    'header-01': {
        'label': 'แบบทดสอบก่อนเรียน',
        'file_id': '1B0zy5nxvdqvX8wLer9BCDBl-18breCfQ',
        'width_cm': 7.13,
        'height_cm': 1.25,
        'h_pos_cm': -0.04,
        'v_pos_cm': 0.19,
        'location': 'header',
        'behind_doc': True,
    },
    'header-02': {
        'label': 'คะแนน',
        'file_id': '1-ze1WTDn9vo9JXjaDWYkkYGTLxr7fkGw',
        'width_cm': 4.76,
        'height_cm': 1.25,
        'h_pos_cm': 3.66,
        'v_pos_cm': -0.06,
        'location': 'header',
        'behind_doc': True,
    },
    'scilogo': {
        'label': 'กลุ่มสาระ',
        'file_id': '1Y0_aa3Bncqy_2NFQOiFh-FZ1yzcIHfLf',
        'width_cm': 4.14,
        'height_cm': 1.0,
        'h_pos_cm': 15.08,
        'v_pos_cm': -0.34,
        'location': 'header',
        'behind_doc': True,
    },
    'page': {
        'label': 'Footer',
        'file_id': '1KFS0A4sQY0DIqNYZLRZH1KjZLLBMSlA6',
        'width_cm': 1.19,
        'height_cm': 0.45,
        'h_pos_cm': 1.78,
        'v_pos_cm': 28.5,
        'location': 'footer',
        'behind_doc': True,
    }
}

# =====================================================
# PAGE CONFIGURATION
# =====================================================
PAGE_CONFIG = {
    'height_cm': 29.7,      # A4 height
    'width_cm': 21.0,       # A4 width
    'top_margin_cm': 3.8,
    'bottom_margin_cm': 1.78,
    'left_margin_cm': 1.78,
    'right_margin_cm': 1.78,
}

# =====================================================
# GRID SYSTEM
# =====================================================
# 1 Grid = 0.32 cm (มาตรฐานของโรงเรียน)
GRID_CM = 0.32

GRID_SPACING = {
    'between_question_and_choice': 1,    # 1 Grid
    'between_choices': 1,                 # 1 Grid
    'after_last_choice': 4,               # 4 Grids
    'choice_indent': 3,                   # 3 Grids
    'question_number_gap': 2,             # 2 Grids (Tab stop)
}

# =====================================================
# FONT CONFIGURATION
# =====================================================
FONT_CONFIG = {
    'main': 'Sarabun',
    'button': 'Noto Sans Thai',
    'size': {
        'question': 11,
        'choice': 11,
        'header': 10,
        'button': 16,
        'subject': 18,
        'info_label': 11,
        'info_value': 11,
    }
}

# =====================================================
# COLOR CONFIGURATION
# =====================================================
COLOR_CONFIG = {
    'primary': '2E5C8A',           # สีน้ำเงินหลัก
    'primary_rgb': RGBColor(46, 92, 138),
    'text_black': RGBColor(0, 0, 0),
    'text_gray': RGBColor(100, 100, 100),
    'text_light_gray': RGBColor(128, 128, 128),
    'text_logo_gray': RGBColor(150, 150, 150),
    'white': RGBColor(255, 255, 255),
    'red': RGBColor(204, 0, 0),    # สำหรับข้อที่มีรูปภาพ
    'blue': RGBColor(0, 102, 204), # สำหรับข้อที่มีสมการ
}

# =====================================================
# DEFAULT VALUES
# =====================================================
DEFAULTS = {
    'unit': 'หน่วยการเรียนรู้ที่ 7 โครงสร้างและการเจริญเติบโตของพืชดอก',
    'topic': 'โครงสร้างภายใน',
    'grade': 'มัธยมศึกษาปีที่ 4-6',
    'instruction': 'ข้อสอบตัวชี้วัดปลายทางฉบับนี้ มีข้อสอบทั้งสิ้นจำนวน 40 ข้อ ข้อละ 1 คะแนน ใช้เวลา 40 นาที โดยเลือกคำตอบที่ถูกต้องที่สุด',
    'footer_text': 'เรียนดี มีความสุข',
}

# =====================================================
# FILE PATHS
# =====================================================
PATHS = {
    'raw_dir': 'raw',              # โฟลเดอร์ไฟล์ต้นฉบับ
    'ready_dir': 'ready',          # โฟลเดอร์ไฟล์ผลลัพธ์
    'logo_dir': '.',               # โฟลเดอร์เก็บ Logo (ดาวน์โหลดมา)
}

# =====================================================
# PERFORMANCE SETTINGS
# =====================================================
PERFORMANCE = {
    'batch_size': 100,             # จำนวนไฟล์ต่อ batch
    'max_workers': 4,              # จำนวน CPU cores สำหรับ multiprocessing
    'enable_progress_bar': True,   # แสดง progress bar
    'log_level': 'INFO',           # DEBUG, INFO, WARNING, ERROR
}
