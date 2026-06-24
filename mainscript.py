"""
Main script สำหรับ Exam Formatter
"""

import os
import time
import gdown

from .config import LOGO_CONFIG, PATHS
from .helpers import extract_text, parse_questions, extract_metadata
from .docx_generator import generate_docx

def download_all_logos():
    """ดาวน์โหลด Logo ทั้งหมดจาก Google Drive"""
    logo_paths = {}
    
    print("📥 กำลังดาวน์โหลด Logo ทั้งหมดจาก Google Drive...\n")
    
    for key, config in LOGO_CONFIG.items():
        file_id = config['file_id']
        logo_url = f"https://drive.google.com/uc?id={file_id}"
        local_path = f"{key}.png"
        
        print(f"🔄 [{config['label']}] กำลังดาวน์โหลด...")
        
        try:
            gdown.download(logo_url, local_path, quiet=True)
            
            if os.path.exists(local_path):
                logo_paths[key] = local_path
                print(f"   ✅ สำเร็จ: {local_path} ({os.path.getsize(local_path)} bytes)")
            else:
                print(f"   ❌ ดาวน์โหลดไม่สำเร็จ")
                logo_paths[key] = None
        except Exception as e:
            print(f"   ❌ Error: {e}")
            logo_paths[key] = None
    
    success_count = sum(1 for v in logo_paths.values() if v)
    print(f"\n✅ ดาวน์โหลด Logo สำเร็จ: {success_count}/{len(LOGO_CONFIG)} รูป")
    
    return logo_paths

def main():
    """Main function"""
    # ดาวน์โหลด Logo
    logo_paths = download_all_logos()
    
    print(f"\n📌 Logo ที่พร้อมใช้งาน:")
    for key, path in logo_paths.items():
        status = "✅" if path else "❌"
        print(f"   {status} {LOGO_CONFIG[key]['label']}: {path}")
    
    # สร้างโฟลเดอร์ output ถ้ายังไม่มี
    os.makedirs(PATHS['ready_dir'], exist_ok=True)
    
    print("\n📂 กำลังสแกนไฟล์...")
    
    if not os.path.exists(PATHS['raw_dir']):
        print(f"❌ ไม่พบโฟลเดอร์: {PATHS['raw_dir']}")
        print(f"   กรุณาสร้างโฟลเดอร์ '{PATHS['raw_dir']}' และใส่ไฟล์ข้อสอบลงไป")
        return
    
    all_files = [f for f in os.listdir(PATHS['raw_dir']) 
                 if f.lower().endswith(('.pdf', '.docx'))]
    
    print(f"พบ {len(all_files)} ไฟล์")
    
    if len(all_files) == 0:
        print("⚠️ ไม่พบไฟล์ PDF หรือ DOCX ในโฟลเดอร์ raw/")
        return
    
    # วัดเวลาทั้งหมด
    total_start_time = time.time()
    success_count = 0
    failed_count = 0
    file_times = []
    
    for i, filename in enumerate(all_files, 1):
        print(f"\n[{i}/{len(all_files)}] {filename}")
        
        file_start_time = time.time()
        
        raw_path = os.path.join(PATHS['raw_dir'], filename)
        is_docx = filename.lower().endswith('.docx')
        ready_path = os.path.join(
            PATHS['ready_dir'],
            f"Ready_{filename.replace('.pdf', '').replace('.docx', '')}.docx"
        )
        
        try:
            text = extract_text(raw_path, is_docx)
            
            if not text.strip():
                print("  ⚠️ ไม่พบข้อความ")
                failed_count += 1
                continue
            
            questions = parse_questions(text)
            print(f"   ✅ แยกได้ {len(questions)} ข้อ")
            
            metadata = extract_metadata(text)
            
            docx_data = {
                'unit': metadata['unit'] or DEFAULTS['unit'],
                'topic': metadata['topic'] or DEFAULTS['topic'],
                'grade': metadata['grade'] or DEFAULTS['grade'],
                'instruction': metadata['instruction'] or DEFAULTS['instruction'],
                'questions': questions
            }
            
            generate_docx(docx_data, ready_path, logo_paths)
            
            file_time = time.time() - file_start_time
            file_times.append(file_time)
            success_count += 1
            
            print(f"  ✅ สำเร็จ!")
            print(f"  ⏱️ ใช้เวลา: {file_time:.3f} วินาที")
            
        except Exception as e:
            file_time = time.time() - file_start_time
            file_times.append(file_time)
            failed_count += 1
            print(f"  ❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    # สรุปผลการประมวลผล
    total_time = time.time() - total_start_time
    
    print("\n" + "="*60)
    print("📊 สรุปผลการประมวลผล")
    print("="*60)
    print(f"🎉 เสร็จสิ้น!")
    print(f"✅ สำเร็จ: {success_count} ไฟล์")
    print(f"❌ ล้มเหลว: {failed_count} ไฟล์")
    print(f"\n⏱️ เวลาทั้งหมด: {total_time:.2f} วินาที ({total_time/60:.2f} นาที)")
    
    if file_times:
        avg_time = sum(file_times) / len(file_times)
        print(f"⏱️ เฉลี่ยต่อไฟล์: {avg_time:.3f} วินาที")
        print(f"⏱️ เร็วที่สุด: {min(file_times):.3f} วินาที")
        print(f"⏱️ ช้าที่สุด: {max(file_times):.3f} วินาที")
        
        estimated_10k = avg_time * 10000
        print(f"\n📈 ประเมินเวลาสำหรับ 10,000 ไฟล์:")
        print(f"   ⏱️ ประมาณ {estimated_10k:.0f} วินาที")
        print(f"   ⏱️ ประมาณ {estimated_10k/60:.1f} นาที")
        print(f"   ⏱️ ประมาณ {estimated_10k/3600:.2f} ชั่วโมง")
    
    print("="*60)

if __name__ == "__main__":
    main()
