
#Grid System
GRID_CM = 0.32  # 1 Grid = 0.32 cm

GRID_SPACING = {
    'between_question_and_choice': 1,  # ระยะจากโจทย์ถึงตัวเลือกแรก
    'between_choices': 1,               # ระยะระหว่างตัวเลือก
    'after_last_choice': 4,             # ระยะหลังตัวเลือกสุดท้าย
    'choice_indent': 3,                 # เยื้องตัวเลือกจากซ้าย
    'question_number_gap': 2,           # ระยะจากเลขข้อถึงโจทย์
}
##Color adjust
COLOR_CONFIG = {
    'primary': '2E5C8A',           # สีน้ำเงินหลัก (Hex code)
    'primary_rgb': RGBColor(46, 92, 138),
    'text_black': RGBColor(0, 0, 0),
    'red': RGBColor(204, 0, 0),    # สีแดง (สำหรับข้อที่มีรูป)
    # เพิ่มสีอื่นๆ ได้ที่นี่
}

#Margin setup
PAGE_CONFIG = {
    'height_cm': 29.7,      # A4 height
    'width_cm': 21.0,       # A4 width
    'top_margin_cm': 3.8,
    'bottom_margin_cm': 1.78,
    'left_margin_cm': 1.78,
    'right_margin_cm': 1.78,
}



# automate INFO SECTION
info_items = [
    ("หน่วยการเรียนรู้", data.get('unit', DEFAULTS['unit'])),
    ("เรื่อง", data.get('topic', DEFAULTS['topic'])),
    ("ระดับชั้น", data.get('grade', DEFAULTS['grade'])),
    ("ชื่อ", "................................................................................."),
    ("วันที่", "..........................................."),  # ← เพิ่มฟิลด์ใหม่
]
