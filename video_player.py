import cv2
import os
import time

# ===== โฟลเดอร์ที่เก็บวิดีโอ =====
VIDEO_DIR = "sign_videos"

def play_gloss_sequence(gloss_text):
    """
    รับ Gloss string เช่น "สวัสดี ฉัน ต้องการ น้ำ"
    แล้วเล่น video clip ต่อกันเป็นประโยค
    """
    if not gloss_text:
        print("⚠️ ไม่มี Gloss สำหรับการเล่นวิดีโอ")
        return

    glosses = gloss_text.strip().split()
    print(f"\nกำลังเล่น: {' → '.join(glosses)}")
    
    clips = []
    for gloss in glosses:
        for ext in [".mp4", ".avi", ".mov"]:
            path = os.path.join(VIDEO_DIR, f"{gloss}{ext}")
            if os.path.exists(path):
                clips.append((gloss, path))
                break
        else:
            print(f"⚠️ ไม่พบวิดีโอสำหรับคำ: {gloss}")
    
    if not clips:
        print("❌ ไม่พบวิดีโอเลย กรุณาตรวจสอบโฟลเดอร์ sign_videos/")
        return
    
    window_name = "SignBridge - Sign Language Player"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 640, 480)
    
    for gloss, path in clips:
        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS) or 30
        
        print(f"▶ กำลังเล่น: {gloss}")
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            h, w = frame.shape[:2]
            cv2.rectangle(frame, (0, h-50), (w, h), (0, 0, 0), -1)
            cv2.putText(
                frame, gloss,
                (20, h-15),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                (255, 255, 255), 2
            )
            
            cv2.imshow(window_name, frame)
            
            if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return
        
        cap.release()
        time.sleep(0.2)
    
    print("✅ เล่นครบทุกคำแล้ว")
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

def run_full_pipeline(thai_text):
    try:
        from gloss_api import thai_to_gloss
        gloss = thai_to_gloss(thai_text)
        if gloss:
            play_gloss_sequence(gloss)
    except Exception as e:
        print(f"⚠️ เกิดข้อผิดพลาดในระบบ: {e}")

if __name__ == "__main__":
    os.makedirs(VIDEO_DIR, exist_ok=True)
    print("=" * 50)
    print("  SignBridge — Ready")
    print("=" * 50)
    
    thai_input = input("พิมพ์ประโยคไทย: ").strip()
    if thai_input:
        run_full_pipeline(thai_input)