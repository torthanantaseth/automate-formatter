# 📖 Setup Guide - คู่มือติดตั้ง

## 🚀 วิธีที่ 1: Google Colab (แนะนำ - ง่ายที่สุด)

### ขั้นตอน:

1. **เปิด Notebook**
   - คลิกปุ่ม "Open in Colab" ใน README
   - หรือไปที่: https://colab.research.google.com/

2. **อัปโหลด Notebook**
   - คลิก File → Upload notebook
   - เลือกไฟล์ `notebooks/exam_formatter.ipynb`

3. **รัน Cell แรก**
   - กด Shift+Enter หรือคลิกปุ่ม ▶️
   - รอให้ติดตั้ง libraries เสร็จ

4. **ตั้งค่าโฟลเดอร์**
   - แก้ไข `raw_dir` และ `ready_dir` ให้ตรงกับโฟลเดอร์ของคุณ
   - ถ้าใช้ Google Drive ให้ mount ก่อน:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   raw_dir = '/content/drive/MyDrive/your-folder/raw'
   ready_dir = '/content/drive/MyDrive/your-folder/ready'
