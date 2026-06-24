"""
Helper functions สำหรับ Exam Formatter
"""

import re
import pdfplumber
from docx import Document as DocxDocument

def extract_text(path, is_docx):
    """
    ดึงข้อความจากไฟล์ PDF หรือ DOCX
    
    Parameters:
    - path: path ของไฟล์
    - is_docx: True ถ้าเป็นไฟล์ DOCX, False ถ้าเป็น PDF
    
    Returns:
    - text: ข้อความทั้งหมดในไฟล์
    """
    if is_docx:
        return "\n".join([p.text for p in DocxDocument(path).paragraphs])
    
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

def clean_thai_question(text):
    """
    ทำความสะอาดข้อความโจทย์
    - ลบช่องว่างเกิน
    - ลบเครื่องหมาย ? ท้ายข้อ
    """
    text = text.strip()
    if text.endswith('?') or text.endswith(' ?'):
        text = text.rstrip('? ').rstrip()
    return text

def sort_choices_by_length(choices):
    """
    เรียงตัวเลือกตามความยาว (สั้น → ยาว)
    
    Parameters:
    - choices: dict ของตัวเลือก {'ก': '...', 'ข': '...', ...}
    
    Returns:
    - sorted_choices: dict ที่เรียงแล้ว
    """
    sorted_choices = {}
    letters = ['ก', 'ข', 'ค', 'ง']
    sorted_letters = sorted(letters, key=lambda x: len(choices.get(x, '')))
    
    for letter in sorted_letters:
        sorted_choices[letter] = choices[letter]
    
    return sorted_choices

def parse_questions(text):
    """
    แยกข้อสอบและตัวเลือกจากข้อความ
    
    Parameters:
    - text: ข้อความทั้งหมด
    
    Returns:
    - questions: list ของ dict [{'no': '1', 'text': '...', 'choices': {...}}, ...]
    """
    # ลบ URLs
    text = re.sub(r'https?://[^\s)]+\)?', '', text)
    
    # หาข้อสอบทั้งหมด
    blocks = re.findall(r'(\d{1,2})\.\s+(.*?)(?=\n\s*\d{1,2}\.\s|\Z)', text, re.DOTALL)
    
    questions = []
    for num, content in blocks:
        # ดึงตัวเลือก
        choices = {}
        for l in ['ก', 'ข', 'ค', 'ง']:
            m = re.search(rf'{l}\.\s+([^\n]+)', content)
            if m:
                choices[l] = m.group(1).strip()
        
        # ดึงข้อความโจทย์ (ลบตัวเลือกออก)
        q_text = re.sub(r'\s+', ' ', re.sub(r'\s*[กขคง]\.\s+[^\n]+', '', content).strip())
        q_text = clean_thai_question(q_text)
        
        # เพิ่มเฉพาะข้อที่มีโจทย์และมีตัวเลือกอย่างน้อย 2 ข้อ
        if q_text and len(choices) >= 2:
            sorted_choices = sort_choices_by_length(choices)
            questions.append({
                'no': num,
                'text': q_text,
                'choices': sorted_choices
            })
    
    return questions

def extract_metadata(text):
    """
    ดึงข้อมูล metadata จากข้อความ
    
    Parameters:
    - text: ข้อความทั้งหมด
    
    Returns:
    - dict ของ metadata
    """
    unit = re.search(r'หน่วยการเรียนรู้[ที่\s]*(\d+|[^\n]+)', text)
    topic = re.search(r'เรื่อง\s*[:\s]*([^\n]+)', text)
    grade = re.search(r'ระดับชั้น\s*[:\s]*([^\n]+)', text)
    inst = re.search(r'คำชี้แจง\s*[:\s]+([^\n]+)', text)
    
    return {
        'unit': unit.group(1).strip() if unit else None,
        'topic': topic.group(1).strip() if topic else None,
        'grade': grade.group(1).strip() if grade else None,
        'instruction': inst.group(1).strip() if inst else None,
    }
