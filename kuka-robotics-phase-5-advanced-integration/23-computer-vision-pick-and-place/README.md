# Computer Vision va Hand-Eye kalibratsiyasi (Pick-and-Place)
## 23-computer-vision-pick-and-place | Phase 5: Tashqi Interfeyslar, ROS2 va Sun'iy Intellekt

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot](https://img.shields.io/badge/KUKA-KR%206%20R900--2-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 📖 Dars Haqida (Overview)
Pinhole kamera modeli, OpenCV cv2.solvePnP, cv2.Rodrigues, Hand-Eye AX=XB (Tsai-Lenz) kalibratsiyasi va robotlashtirilgan saralash.

* **Texnologiyalar:** `OpenCV, PnP, Hand-Eye Calibration (AX=XB), Pick-and-Place`
* **Asosiy Manipulyator:** KUKA KR 6 R900-2 (KR AGILUS-2)

---

### 🗂️ Jild Tuzilishi (Mandatory Boilerplate)
```
23-computer-vision-pick-and-place/
├── src/
│   ├── krl/            # KRL (.src, .dat) dasturlari
│   └── scripts/        # Python / MATLAB skriptlari
├── sim/                # KUKA.Sim Pro (.vcmx) va URDF simulyatsiya fayllari
├── docs/               # Matematik hisob-kitoblar va grafiklar
├── CLAUDE.md           # AI dasturchi ko'rsatmalari
└── README.md           # Ushbu to'liq dars qo'llanmasi
```

---

### 🎯 Laboratoriya Topshirig'i (Lab Assignment)
1. Nazariy qismdagi formulalar va algoritmlarni tahlil qilish.
2. `src/scripts/` jildidagi Python algoritmini ishga tushirib, hisob-kitoblarni tekshirish.
3. `src/krl/` jildidagi KRL dasturini KUKA.Sim Pro yoki OfficeLite virtual kontrolleriga yuklab simulyatsiya qilish.

---
🔗 **[Bosh Kurs Mundarijasiga Qaytish (Master Syllabus)](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**


---

## 🧮 Matematik Apparat, Teoremalar va Keltirib Chiqarilishi

### 📌 Asosiy Teorema: Tsai-Lenz Hand-Eye Calibration Theorem (AX = XB) & Modified Rodrigues Vector
$$A_i X = X B_i \quad \text{where } A_i = T_{F_{i+1}}^{F_i}, \quad B_i = T_{C_{i+1}}^{C_i}, \quad X = T_{FLANGE}^{CAMERA}$$

Batafsil qadam-baqadam matematik isboti va formulalarning geometrik chiqarilishi uchun:
👉 [**docs/derivations.md**](./docs/derivations.md) fayliga qarang.


### 1. Nazariy Asos va Teorema (Hand-Eye Kalibratsiyasi: $AX = XB$)
Kamerani sanoat roboti flanetsiga o'rnatilganda (Eye-in-Hand), kameraning flanetsga nisbatan aniq 6D fazoviy transformatsiyasini $X = T_{FLANGE}^{CAM}$ aniqlash talab qilinadi.

> **Teorema (Tsai-Lenz Hand-Eye Teoremasi):**
> Robot flanetsi $i$-holatdan $i+1$-holatga harakatlanganda ($A_i$), kamera ham nishonga (ChArUco/shaxmat doskasi) nisbatan mos $B_i$ harakatni amalga oshiradi:
> $$A_i X = X B_i$$
> Matritsaviy ko'rinishda:
> $$\begin{bmatrix} R_A & \vec{t}_A \\ \vec{0}^T & 1 \end{bmatrix} \begin{bmatrix} R_X & \vec{t}_X \\ \vec{0}^T & 1 \end{bmatrix} = \begin{bmatrix} R_X & \vec{t}_X \\ \vec{0}^T & 1 \end{bmatrix} \begin{bmatrix} R_B & \vec{t}_B \\ \vec{0}^T & 1 \end{bmatrix}$$
> Bu ikkita mustaqil tenglamaga ajraladi:
> 1. Aylanish tenglamasi: $R_A R_X = R_X R_B$
> 2. Siljish tenglamasi: $(R_A - I) \vec{t}_X = R_X \vec{t}_B - \vec{t}_A$

### 2. Modifikatsiyalangan Rodrig Vektori Orqali Yechish (Tsai-Lenz Algoritmi)
1. Har bir $A_i$ va $B_i$ burilish matritsalari uchun Rodrigues o'qi $\vec{k}$ va burchagi $\theta$ topiladi.
2. Modifikatsiyalangan Rodrigues vektori yasaladi:
   $$\vec{P} = 2 \tan\left(\frac{\theta}{2}\right) \vec{k}$$
3. Aylanish tenglamasi chiziqli ko'rinishga keladi:
   $$\text{skew}(\vec{P}_A + \vec{P}_B) \cdot \vec{P}_X' = \vec{P}_B - \vec{P}_A$$
4. Eng kichik kvadratlar usuli (SVD / Least Squares) orqali $\vec{P}_X$ topiladi va $R_X$ tiklanadi.
5. $R_X$ ma'lum bo'lgach, siljish $\vec{t}_X$ to'g'ridan-to'g'ri chiziqli tenglamalar tizimidan topiladi:
   $$(R_A - I) \vec{t}_X = R_X \vec{t}_B - \vec{t}_A \quad \blacksquare$$

