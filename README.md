## การติดตั้ง

1. Clone repository
2. ติดตั้ง library
```
python -m pip install -r requirements.txt
```
3. สร้างไฟล์ `.env` แล้วใส่ API Key
```
API_KEY=your_gemini_api_key_here
```
4. วางไฟล์วิดีโอภาษามือในโฟลเดอร์ `sign_videos/` ตั้งชื่อตามคำ เช่น `สวัสดี.mp4`

## การใช้งาน

```
python video_player.py
```

แล้วพิมพ์ประโยคภาษาไทย ระบบจะแปลเป็น Gloss และเล่นวิดีโอให้อัตโนมัติ

## โครงสร้างไฟล์

```
signbridge/
    gloss_api.py        ← แปลภาษาไทยเป็น Gloss ผ่าน Gemini
    video_player.py     ← เล่นวิดีโอภาษามือ
    requirements.txt    ← library ที่ต้องติดตั้ง
    .env                ← API Key (ไม่อยู่ใน GitHub)
    sign_videos/        ← วิดีโอภาษามือ
```

## หมายเหตุ

- ต้องขอ Gemini API Key ที่ aistudio.google.com
- ไฟล์ `.env` ต้องสร้างเองไม่มีใน GitHub