# Phase 2: Fazoviy Geometriya va Kinematik Modellashtirish
## kuka-robotics-phase-2-kinematics-and-math

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20ros2--robotics%20%7C%20industrial--automation%20%7C%20samdu%20%7C%20tsu-blue.svg)](#)

---

### 📖 Bob Tavsifi
Rodrigues formulasi, so(3) Lie algebrasi, Eyler burchaklari (A, B, C), Kvaternionlar, DH parametrlari va To'g'ri/Teskari kinematika.

Bu repozitoriy **KUKA Industrial Robotics Course** o'quv dasturining bir qismi bo'lib, quyidagi darslarni o'z ichiga oladi:

### 📑 Darslar Mundarijasi
* [**05-rodrigues-rotation-formula**: Fazoviy burilishlar va Rodrigues aylantirish formulasi](./05-rodrigues-rotation-formula) — *so(3) Lie algebrasi, skew-symmetric operator [k]_x va Rodrigues formulasining geometrik hamda matritsaviy eksponensial (e^{theta K}) keltirib chiqarilishi.*
* [**06-rotation-matrices-and-quaternions**: Aylanish matritsalari, Eyler burchaklari va Kvaternionlar](./06-rotation-matrices-and-quaternions) — *KUKA Z-Y'-X'' (A, B, C) Eyler burchaklari, Gimbal Lock (B=+-90) muammosi va to'rt o'lchamli birlik kvaternionlar (H) orqali SLERP interpolyatsiyasi.*
* [**07-dh-parameters-modelling**: Denavit-Hartenberg (DH) parametrlari modellashtirishi](./07-dh-parameters-modelling) — *Standart va Modifikatsiyalangan DH konvensiyalari. KUKA KR 6 R900-2 uchun rasmiy DH koordinata jadvallarini noldan qurish.*
* [**08-forward-kinematics-solver**: To'g'ri kinematika (Forward Kinematics) solveri](./08-forward-kinematics-solver) — *SE(3) transformatsiya matritsalari zanjiri. Bo'g'in burchaklariga ko'ra flanetsning fazodagi yakuniy o'rnini hisoblash va $POS_ACT bilan tekshirish.*
* [**09-inverse-kinematics-analytical**: Analitik teskari kinematika (Pieper usuli)](./09-inverse-kinematics-analytical) — *Sferik bilak uchun Piper (Pieper) dekouplingi, 8 ta analitik yechim, KUKA Status (S) va Turn (T) butun sonli bitlarining fizik ma'nosi.*
* [**10-numerical-inverse-kinematics**: Raqamli (Numerical) teskari kinematika usullari](./10-numerical-inverse-kinematics) — *Nyuton-Rafson iteratsiyasi, Yakobian transponirlangan va Levenberg-Marquardt (Damped Least Squares) optimallashtirish algoritmlari.*

---

### 🏛️ Repozitoriya Tuzilishi
```
kuka-robotics-phase-2-kinematics-and-math/
├── 05-rodrigues-rotation-formula/
├── 06-rotation-matrices-and-quaternions/
├── 07-dh-parameters-modelling/
├── 08-forward-kinematics-solver/
├── 09-inverse-kinematics-analytical/
├── 10-numerical-inverse-kinematics/
```

---

### 👥 Hamkorlik va Mualliflik
* **Muallif:** Muzaffarbek Mustafayev (SamDU & TSU)
* 🔗 **[Bosh Kurs Mundarijasi (Master Navigator Hub)](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
