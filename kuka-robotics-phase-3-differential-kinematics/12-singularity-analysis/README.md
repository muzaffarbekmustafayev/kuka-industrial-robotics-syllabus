# Singulyarlik tahlili va manipulyativlik ellipsoidi
## 12-singularity-analysis | Phase 3: Differensial Kinematika, Yakobian va Dinamika

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-3-differential-kinematics-blue.svg)](#)
[![Robot](https://img.shields.io/badge/KUKA-KR%206%20R900--2-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 📖 Dars Haqida (Overview)
det(J)=0 tahlili: Bilak (Wrist A5=0), Yelka (Shoulder) va Chegara singulyarliklari, Yoshikawa manipulyativlik indeksi va singulyarlikdan qochish.

* **Texnologiyalar:** `Singularity Avoidance, Yoshikawa Ellipsoid, Damped Inversion`
* **Asosiy Manipulyator:** KUKA KR 6 R900-2 (KR AGILUS-2)

---

### 🗂️ Jild Tuzilishi (Mandatory Boilerplate)
```
12-singularity-analysis/
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

### 📌 Asosiy Teorema: Kinematic Singularity Theorem, Determinant Decoupling & Yoshikawa Manipulability
$$\det(J(\vec{q})) = 0 \iff \text{rank}(J) < 6, \quad w = \sqrt{\det(J J^T)}$$

Batafsil qadam-baqadam matematik isboti va formulalarning geometrik chiqarilishi uchun:
👉 [**docs/derivations.md**](./docs/derivations.md) fayliga qarang.


### 1. Nazariy Asos va Teorema (Kinematik Singulyarlik Teoremasi)
Differensial kinematikada singulyarlik robotning fazodagi ma'lum bir yo'nalishlarda harakatlanish imkoniyatini yo'qotishidir.

> **Teorema (Singulyarlik Kriteriyasi):**
> Manipulyator Yakobiani $J(\vec{q}) \in \mathbb{R}^{6 \times 6}$ bo'lsin. Singulyarlik sharti uning determinanti nolga teng bo'lishi bilan aniqlanadi:
> $$\det(J(\vec{q})) = 0 \iff \text{rank}(J(\vec{q})) < 6$$
> Sferik bilakka ega KR 6 R900-2 uchun determinant ikkita alohida ko'paytuvchiga ajraladi:
> $$\det(J(\vec{q})) = \det(J_{arm}(q_1, q_2, q_3)) \cdot \sin(q_5) = 0$$

### 2. KUKA KR 6 R900-2 dagi 3 Ta Kritik Singulyarlik Holati
#### 2.1 Bilak Singulyarligi (Wrist Singularity):
* **Matematik sharti:** $q_5 = 0^\circ \implies \sin(q_5) = 0$.
* **Fizik ma'nosi:** $A_4$ va $A_6$ motorlarining aylanish o'qlari to'g'ri chiziq bo'ylab ustma-ust (kollinear) tushib qoladi.
* **Xavfi:** Agar robot chiziqli harakatda (LIN) ushbu nuqtadan o'tishga harakat qilsa, $A_4$ va $A_6$ motorlari cheksiz katta burchak tezlikka intiladi (kontroller `A4/A6 dynamic overload` xatosini beradi).

#### 2.2 Yelka Singulyarligi (Shoulder / Overhead Singularity):
* **Matematik sharti:** $p_{wc, x}^2 + p_{wc, y}^2 = 0$.
* **Fizik ma'nosi:** Bilak markazi $A_1$ o'qining to'g'ridan-to'g'ri ustiga (vertikal o'q chizig'iga) tushib qoladi.

#### 2.3 Chegara Singulyarligi (Elbow / Boundary Singularity):
* **Matematik sharti:** Robot qo'li to'liq cho'zilgan ($q_3$ burchak chegarasida) yoki to'liq bukilgan. Effektor ishchi sferaning eng chekka chegarasiga yetib borgan.

### 3. Yoshikawa Manipulyativlik Ko'rsatkichi (Manipulability Measure)
Manipulyatorning singulyarlikdan qanchalik uzoqligi Yoshikawa indeksi orqali baholanadi:
$$w(\vec{q}) = \sqrt{\det(J(\vec{q}) J(\vec{q})^T)} = |\det(J(\vec{q}))|$$
* $w = 0$ bo'lsa: robot qulflangan (singulyar).
* $w$ maksimal bo'lsa: robot barcha yo'nalishlarda teng erkinlik bilan eng samarali harakatlana oladi.

