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
