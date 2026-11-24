# ============================================================
# HIDDEN TESTS สำหรับครูเท่านั้น  (ห้าม push ขึ้น git page)
# วิธีใช้: เปิด notebook ที่เด็กส่ง > File > Save a copy in Drive
#          > Runtime > Run all > วาง cell ด้านล่างไว้ท้ายสุดแล้วรัน
# ใช้ข้อมูลคนละชุดกับในหน้าเว็บ ถ้าเด็ก hardcode คำตอบจะพังตรงนี้
# ============================================================

def check(name, fn):
    try:
        fn()
        print("✅", name)
    except NameError as e:
        print("⚪", name, "- ยังไม่ได้ทำ:", e)
    except Exception as e:
        print("❌", name, "-", type(e).__name__, e)

# ---------- W1 ----------
def _w1_avg():
    assert calculate_average([100, 50, 60]) == 70.0
    assert calculate_average([7]) == 7.0
check("W1 Quest 04 calculate_average", _w1_avg)

# ---------- S0 ----------
def _s0_grade():
    assert grade(100) == 4
    assert grade(79) == 3
    assert grade(69) == 2
    assert grade(59) == 1
    assert grade(0) == 0
check("S0 ข้อ 3 grade", _s0_grade)

# ---------- Mission ----------
hp = {"ชาไทย": 20, "ชาเขียว": 35, "โกโก้": 25, "นมชมพู": 15}
ho = [
    {"day": "เสาร์", "menu": "ชาเขียว", "qty": 2},
    {"day": "อาทิตย์", "menu": "นมชมพู", "qty": 7},
    {"day": "เสาร์", "menu": "โกโก้", "qty": 4},
    {"day": "อาทิตย์", "menu": "ชาเขียว", "qty": 1},
]

def _m1(): assert order_total(ho[0], hp) == 70
def _m2(): assert week_total(ho, hp) == 310
def _m3(): assert day_totals(ho, hp) == {"เสาร์": 170, "อาทิตย์": 140}
def _m4(): assert count_cups(ho) == {"ชาเขียว": 3, "นมชมพู": 7, "โกโก้": 4}
check("Mission L1 order_total", _m1)
check("Mission L2 week_total", _m2)
check("Mission L3 day_totals (วันไม่เรียงต่อกัน)", _m3)
check("Mission L4 count_cups", _m4)

def _bonus():
    t, k = clean_week_total(ho + [{"day": "เสาร์", "menu": "x", "qty": 1},
                                  {"day": "เสาร์", "menu": "ชาไทย", "qty": "3"},
                                  {"day": "เสาร์", "menu": "โกโก้", "qty": 0}], hp)
    assert (t, k) == (370, 2), f"ได้ {(t, k)} ควรได้ (370, 2)"
check("Mission Bonus clean_week_total", _bonus)

# ---------- เฉลย Level 5 (ข้อมูลในหน้าเว็บ) ----------
# ข้อ 1 ขึ้นราคาชาไทยเป็น 30: เพิ่ม 225 บาท (45 แก้ว x 5 บาท) รายได้ใหม่ 2700
# ข้อ 2 เลิกขายนมชมพู (15 แก้ว): รายได้หายไป 300 บาท เหลือ 2175
# สังเกต: ถ้าเด็กใช้ prices["ชาไทย"] = 30 แก้ของเดิมตรง ๆ Level 2-3 จะ assert ไม่ผ่านเมื่อ Run all

# ============================================================
# C1 NumPy  (ตารางคนละขนาด 5 วัน x 3 เมนู ถ้า hardcode 14 หรือ 4 จะพัง)
# ============================================================
import numpy as np
_c = np.array([[2, 1, 0], [5, 3, 2], [0, 4, 1], [3, 3, 3], [6, 0, 2]])
_p = np.array([20, 15, 40])
_m = np.array(["ก", "ข", "ค"])

def _c1_report():
    r = shop_report(_c, _p, _m, 100)
    assert list(r["menu_cups"]) == [16, 11, 8], f"menu_cups ได้ {list(r['menu_cups'])}"
    assert r["total"] == 805, f"total ได้ {r['total']}"
    assert r["hit_count"] == 4, f"hit_count ได้ {r['hit_count']} (เช็ค >= กับวันที่ได้ 100 พอดี)"
    assert r["best_menu"] == "ก", f"best_menu ได้ {r['best_menu']}"
check("C1 Level 5 shop_report", _c1_report)

# เฉลยคำถามเจ้าของร้าน C1 Level 5:
# สัปดาห์ 1 = 5,495 บาท, สัปดาห์ 2 = 6,130 บาท -> เพิ่มขึ้น 635 บาท (ประมาณ 11.6%)
# Human Verify Level 4: ชาเขียว 79 แก้ว = 2,370 บาท > นมชมพู 90 แก้ว = 1,800 บาท

# ============================================================
# C3 clean_orders  (ข้อมูลสกปรกชุดเล็กที่ไม่เคยเห็น)
# ============================================================
import pandas as pd
_raw = pd.DataFrame({
    "order_id": ["X1", "X2", "X2", "X3", "X4", "X5", "X6", "X7"],
    "date": ["2026-12-01"] * 8,
    "time": ["08:00", "08:10", "08:10", "09:00", "09:30", "10:00", "10:30", "11:00"],
    "branch": ["ตลาด", " หน้าวิทยาลัย", " หน้าวิทยาลัย", "ตลาด ", "ตลาด", "ตลาด", "หน้าวิทยาลัย", "ตลาด"],
    "menu": ["Thai Tea", "โกโก้ ", "โกโก้ ", "ชาเขียว", "นมชมพู", "ชาไทย", "ชาไทย", "โกโก้"],
    "qty": ["3", "2 แก้ว", "2 แก้ว", None, "50", "-1", "4", "1"],
    "price": [25, 30, 30, 30, 20, 25, 25, 30],
    "payment": ["โอน", None, None, "เงินสด", "โอน", "โอน", "เงินสด", None],
})
def _c3():
    before = _raw.copy()
    c = clean_orders(_raw)
    assert _raw.equals(before), "ฟังก์ชันไปแก้ข้อมูลดิบ"
    assert len(c) == 4, f"ควรเหลือ 4 แถว ได้ {len(c)}"
    assert sorted(c["order_id"]) == ["X1", "X2", "X6", "X7"], f"ได้ {sorted(c['order_id'])}"
    assert c["amount"].sum() == 75 + 60 + 100 + 30
    assert set(c["branch"]) == {"ตลาด", "หน้าวิทยาลัย"}
    assert (c["payment"] == "ไม่ระบุ").sum() == 2
    assert pd.api.types.is_datetime64_any_dtype(c["date"])
check("C3 Level 1 clean_orders", _c3)

# เฉลย C3:
# Part A ซ้ำ 12 -> 562 | Part B ลบ qty ว่าง 5 -> 557, payment ไม่ระบุ 11 | Part E ตัด 999,999,-1,-2,0 -> 552
# ยอดขายดิบ 94,065 (C2) -> หลัง clean 38,805 ; ส่วนใหญ่หายจาก qty=999 สองแถว (54,945 บาท)
# Level 3: หน้าวิทยาลัย 318, ตลาด 234, โอน 51.1%, ยอดตลาด 15,775
# Bonus: หน้าวิทยาลัย วันหยุด 35 / วันธรรมดา 283
# สังเกต: ถ้า X5 (qty 50) ยังอยู่ แปลว่าใช้เกณฑ์อื่น ไม่ใช่ <= 20 ให้ดูเหตุผลใน Text cell ก่อนหักคะแนน

# ============================================================
# S1 clean_borrows + ค่าปรับ
# ============================================================
_lib = pd.DataFrame({
    "borrow_id": ["L1", "L2", "L2", "L3", "L4", "L5", "L6"],
    "borrow_date": ["2026-12-01"] * 7,
    "department": ["ไอที", " AI", " AI", "บัญชี", "ช่างยนต์ ", "IT", "เทคโนโลยีสารสนเทศ"],
    "category": ["นิยาย", None, None, "ทั่วไป", "การ์ตูน", "นิยาย", "ทั่วไป"],
    "days": ["7", "10 วัน", "10 วัน", None, "40", "8", "0"],
})
def _s1():
    before = _lib.copy()
    c = clean_borrows(_lib)
    assert _lib.equals(before), "ฟังก์ชันไปแก้ข้อมูลดิบ"
    assert sorted(c["borrow_id"]) == ["L1", "L2", "L5"], f"ได้ {sorted(c['borrow_id'])}"
    assert sorted(c["department"]) == ["AI", "IT", "IT"]
    assert (c["category"] == "ไม่ระบุ").sum() == 1
check("S1 Step 2 clean_borrows", _s1)

# เฉลย S1: 439 แถว ซ้ำ 9 -> 430, days ว่าง 4 -> 426, days นอกช่วง 4 (365,180,-3,0) -> 422
# category ว่าง 14 แต่ 1 แถวอยู่ในแถวซ้ำ -> "ไม่ระบุ" 13
# คืนช้า 143 ครั้ง (33.9%) ค่าปรับรวม 2,790 บาท | ค่าปรับจากข้อมูลดิบ 7,210 บาท (แถว 365 กับ 180 วัน)
# Step 4: IT ยืมมากสุด, การบัญชีปรับ 795 บาท, IT ยืมหมวดคอมพิวเตอร์ 44.6%
# Human Verify Step 4: % คืนช้ารายแผนก การบัญชี 37.9% สูงสุดจริง (AI 35.1, IT 33.0, ไฟฟ้า 32.5, ยนต์ 30.4)
# Bonus: ศุกร์ยืมมากสุด
