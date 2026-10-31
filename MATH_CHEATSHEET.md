# Mathematical Cheatsheet & Rigorous Kinematic Foundations
## KUKA KR 6 R900-2 Industrial Robotics Course

This cheatsheet provides the unified mathematical standard, notation conventions, closed-form derivations, and algorithmic formulations referenced across all 13 modular lesson repositories.

---

## 📑 Table of Contents
1. [Coordinate Frames & Vector Notation](#1-coordinate-frames--vector-notation)
2. [Skew-Symmetric Operators & Lie Algebra $\mathfrak{so}(3)$](#2-skew-symmetric-operators--lie-algebra-mathfrakso3)
3. [The Rodrigues Rotation Formula (Forward Derivation)](#3-the-rodrigues-rotation-formula-forward-derivation)
4. [Inverse Rodrigues Formula (Logarithmic Map)](#4-inverse-rodrigues-formula-logarithmic-map)
5. [KUKA Euler Convention: $Z-Y'-X''$ ($A, B, C$)](#5-kuka-euler-convention-z-y-x-a-b-c)
6. [Unit Quaternions ($\mathbb{H}$) & Conversion Triad](#6-unit-quaternions-mathbbh--conversion-triad)
7. [KUKA KR 6 R900-2 Denavit-Hartenberg (DH) Model](#7-kuka-kr-6-r900-2-denavit-hartenberg-dh-model)
8. [Forward & Inverse Kinematics (Pieper's Decoupling)](#8-forward--inverse-kinematics-piepers-decoupling)
9. [Geometric Jacobian & Singularity Analysis](#9-geometric-jacobian--singularity-analysis)
10. [Computer Vision & Hand-Eye Calibration ($AX = XB$)](#10-computer-vision--hand-eye-calibration-ax--xb)

---

## 1. Coordinate Frames & Vector Notation

* Let $\{W\}$ be the World reference frame.
* Let $\{B\}$ be the Robot Base frame (`$BASE`).
* Let $\{F\}$ be the Robot Tool Flange frame (`$FLANGE`).
* Let $\{T\}$ be the Tool Center Point frame (`$TOOL`).
* Let $\{C\}$ be the Camera optical frame.

A homogeneous coordinate transformation matrix $T_B^A \in SE(3)$ maps a point $P^B$ in frame $\{B\}$ to frame $\{A\}$:
$$P^A = T_B^A P^B = \begin{bmatrix} R_B^A & \vec{p}_B^A \\ \vec{0}^T & 1 \end{bmatrix} \begin{bmatrix} P^B \\ 1 \end{bmatrix}$$
where:
* $R_B^A \in SO(3)$ is the $3\times 3$ rotation matrix ($R^T R = I$, $\det(R) = +1$).
* $\vec{p}_B^A \in \mathbb{R}^3$ is the translation vector pointing from the origin of $\{A\}$ to the origin of $\{B\}$, expressed in $\{A\}$ coordinates.

---

## 2. Skew-Symmetric Operators & Lie Algebra $\mathfrak{so}(3)$

For any vector $\vec{k} = [k_x, k_y, k_z]^T \in \mathbb{R}^3$, the cross product operator $\vec{k} \times \vec{v}$ can be represented by matrix multiplication:
$$\vec{k} \times \vec{v} = [\vec{k}]_\times \vec{v} = K \vec{v}$$

where the skew-symmetric matrix $K = [\vec{k}]_\times \in \mathfrak{so}(3)$ is defined as:
$$K = [\vec{k}]_\times = \begin{bmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{bmatrix}$$

### Fundamental Algebraic Properties:
1. **Skew-symmetry:** $K^T = -K$.
2. **Nilpotent-like cyclic power relation:** If $\|\vec{k}\| = 1$, then:
   $$K^2 = \vec{k}\vec{k}^T - I = \begin{bmatrix} k_x^2 - 1 & k_x k_y & k_x k_z \\ k_x k_y & k_y^2 - 1 & k_y k_z \\ k_x k_z & k_y k_z & k_z^2 - 1 \end{bmatrix}$$
   $$K^3 = -K, \quad K^4 = -K^2, \quad K^5 = K, \quad \dots$$
   $$\forall n \ge 1: \quad K^{2n+1} = (-1)^n K, \quad K^{2n} = (-1)^{n-1} K^2$$

---

## 3. The Rodrigues Rotation Formula (Forward Derivation)

### 3.1 Geometric Vector Derivation
Let $\vec{v} \in \mathbb{R}^3$ be rotated about a unit axis $\vec{k}$ ($\|\vec{k}\|=1$) by an angle $\theta$ to produce $\vec{v}_{rot}$.

1. Decompose $\vec{v}$ into parallel and perpendicular components to $\vec{k}$:
   $$\vec{v}_\parallel = (\vec{k} \cdot \vec{v})\vec{k}$$
   $$\vec{v}_\perp = \vec{v} - \vec{v}_\parallel = \vec{v} - (\vec{k} \cdot \vec{v})\vec{k}$$

2. Construct an orthogonal basis in the rotation plane:
   * First basis vector: $\vec{v}_\perp$
   * Second basis vector (rotated by $+90^\circ$ around $\vec{k}$): $\vec{w} = \vec{k} \times \vec{v}_\perp = \vec{k} \times \vec{v}$

3. The rotated perpendicular component $\vec{v}_{\perp, rot}$ is:
   $$\vec{v}_{\perp, rot} = \vec{v}_\perp \cos\theta + (\vec{k} \times \vec{v}) \sin\theta$$

4. The parallel component is invariant under rotation ($\vec{v}_{\parallel, rot} = \vec{v}_\parallel$):
   $$\begin{aligned}
   \vec{v}_{rot} &= \vec{v}_{\parallel, rot} + \vec{v}_{\perp, rot} \\
   &= (\vec{k} \cdot \vec{v})\vec{k} + [\vec{v} - (\vec{k} \cdot \vec{v})\vec{k}]\cos\theta + (\vec{k} \times \vec{v})\sin\theta \\
   &= \vec{v}\cos\theta + (\vec{k} \times \vec{v})\sin\theta + \vec{k}(\vec{k} \cdot \vec{v})(1 - \cos\theta)
   \end{aligned}$$

### 3.2 Matrix Exponential Derivation ($e^{\theta K}$)
Using the Taylor series expansion of the matrix exponential $R = \exp(\theta K)$:
$$R = \sum_{n=0}^{\infty} \frac{(\theta K)^n}{n!} = I + \theta K + \frac{\theta^2 K^2}{2!} + \frac{\theta^3 K^3}{3!} + \frac{\theta^4 K^4}{4!} + \dots$$

Grouping terms using $K^3 = -K$ and $K^4 = -K^2$:
$$R = I + \left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots\right) K + \left(\frac{\theta^2}{2!} - \frac{\theta^4}{4!} + \frac{\theta^6}{6!} - \dots\right) K^2$$

Substituting the Maclaurin series for $\sin\theta$ and $1 - \cos\theta$:
$$\mathbf{R}(\vec{k}, \theta) = \mathbf{I} + \sin(\theta)\mathbf{K} + (1 - \cos(\theta))\mathbf{K}^2$$

---

## 4. Inverse Rodrigues Formula (Logarithmic Map)

Given an arbitrary rotation matrix $R \in SO(3)$, determine the rotation angle $\theta \in [0, \pi]$ and unit axis $\vec{k} = [k_x, k_y, k_z]^T$.

### 4.1 Trace Formula for Rotation Angle $\theta$
The trace of $R$ is invariant under change of basis:
$$\text{tr}(R) = R_{11} + R_{22} + R_{33} = 1 + 2\cos\theta$$
$$\theta = \arccos\left(\frac{\text{tr}(R) - 1}{2}\right) = \arccos\left(\frac{R_{11} + R_{22} + R_{33} - 1}{2}\right)$$

### 4.2 General Case ($\theta \in (0, \pi)$)
Subtracting $R^T$ from $R$:
$$R - R^T = 2\sin(\theta) K$$
$$\begin{bmatrix} 0 & R_{12}-R_{21} & R_{13}-R_{31} \\ R_{21}-R_{12} & 0 & R_{23}-R_{32} \\ R_{31}-R_{13} & R_{32}-R_{23} & 0 \end{bmatrix} = 2\sin\theta \begin{bmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{bmatrix}$$

Solving for $\vec{k}$:
$$\vec{k} = \frac{1}{2\sin\theta} \begin{bmatrix} R_{32} - R_{23} \\ R_{13} - R_{31} \\ R_{21} - R_{12} \end{bmatrix}$$

### 4.3 Singular Boundary Cases
* **Case 1 ($\theta \to 0$):** Identity rotation ($R \to I$). The axis $\vec{k}$ is arbitrary (conventionally $\vec{k} = [1, 0, 0]^T$), and $\vec{r} = \theta \vec{k} = [0, 0, 0]^T$.
* **Case 2 ($\theta \to \pi$):** $\sin\theta = 0$, so $\frac{1}{2\sin\theta}$ diverges.
  Since $\cos\pi = -1$, Rodrigues gives:
  $$R = I + 2K^2 = I + 2(\vec{k}\vec{k}^T - I) = 2\vec{k}\vec{k}^T - I \implies \vec{k}\vec{k}^T = \frac{R + I}{2}$$
  Therefore:
  $$k_x = \sqrt{\max\left(0, \frac{R_{11}+1}{2}\right)}, \quad k_y = \text{sgn}(R_{12}) \sqrt{\max\left(0, \frac{R_{22}+1}{2}\right)}, \quad k_z = \text{sgn}(R_{13}) \sqrt{\max\left(0, \frac{R_{33}+1}{2}\right)}$$

---

## 5. KUKA Euler Convention: $Z-Y'-X''$ ($A, B, C$)

KUKA controllers represent orientation using three intrinsic Tait-Bryan angles:
* **$A$ (Yaw):** Rotation around the current $Z$ axis.
* **$B$ (Pitch):** Rotation around the new $Y'$ axis.
* **$C$ (Roll):** Rotation around the final $X''$ axis.

### 5.1 Forward Matrix Composition
$$R_{KUKA}(A, B, C) = R_z(A) \cdot R_y(B) \cdot R_x(C)$$

$$\begin{aligned}
R_{KUKA} &= \begin{bmatrix} \cos A & -\sin A & 0 \\ \sin A & \cos A & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \cos B & 0 & \sin B \\ 0 & 1 & 0 \\ -\sin B & 0 & \cos B \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos C & -\sin C \\ 0 & \sin C & \cos C \end{bmatrix} \\
&= \begin{bmatrix}
\cos A \cos B & \cos A \sin B \sin C - \sin A \cos C & \cos A \sin B \cos C + \sin A \sin C \\
\sin A \cos B & \sin A \sin B \sin C + \cos A \cos C & \sin A \sin B \cos C - \cos A \sin C \\
-\sin B & \cos B \sin C & \cos B \cos C
\end{bmatrix}
\end{aligned}$$

### 5.2 Inverse Extraction ($R \to A, B, C$)
From $R_{31} = -\sin B$:
$$B = \text{atan2}\left(-R_{31}, \sqrt{R_{11}^2 + R_{21}^2}\right)$$

Assuming $\cos B \neq 0$ ($B \neq \pm 90^\circ$):
$$A = \text{atan2}\left(\frac{R_{21}}{\cos B}, \frac{R_{11}}{\cos B}\right) = \text{atan2}(R_{21}, R_{11})$$
$$C = \text{atan2}\left(\frac{R_{32}}{\cos B}, \frac{R_{33}}{\cos B}\right) = \text{atan2}(R_{32}, R_{33})$$

### 5.3 Gimbal Lock Singularity ($B = \pm 90^\circ$)
When $B = +90^\circ$ ($\cos B = 0, \sin B = 1$):
$$R = \begin{bmatrix} 0 & \sin(C-A) & \cos(C-A) \\ 0 & \cos(C-A) & -\sin(C-A) \\ -1 & 0 & 0 \end{bmatrix}$$
Only the difference or sum $(C - A)$ is measurable. In KRL controllers, set $C = 0$ and solve for $A = \text{atan2}(-R_{12}, R_{22})$.

---

## 6. Unit Quaternions ($\mathbb{H}$) & Conversion Triad

A unit quaternion $q \in \mathbb{S}^3 \subset \mathbb{H}$ represents orientation without singularities:
$$\mathbf{q} = w + x\mathbf{i} + y\mathbf{j} + z\mathbf{k} = [w, \vec{v}] = [w, x, y, z]^T, \quad w^2 + x^2 + y^2 + z^2 = 1$$

### 6.1 Axis-Angle / Rodrigues $\longleftrightarrow$ Quaternion
Given unit axis $\vec{k}$ and angle $\theta$:
$$w = \cos\left(\frac{\theta}{2}\right), \quad \vec{v} = \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \vec{k} \sin\left(\frac{\theta}{2}\right)$$

Conversely, given unit quaternion $\mathbf{q}$:
$$\theta = 2 \arccos(w) = 2 \text{atan2}(\|\vec{v}\|, w)$$
$$\vec{k} = \begin{cases} \frac{\vec{v}}{\|\vec{v}\|}, & \text{if } \|\vec{v}\| \neq 0 \\ [1, 0, 0]^T, & \text{otherwise} \end{cases}$$

### 6.2 Quaternion $\longrightarrow$ Rotation Matrix
$$R(\mathbf{q}) = \begin{bmatrix}
1 - 2(y^2 + z^2) & 2(xy - wz) & 2(xz + wy) \\
2(xy + wz) & 1 - 2(x^2 + z^2) & 2(yz - wx) \\
2(xz - wy) & 2(yz + wx) & 1 - 2(x^2 + y^2)
\end{bmatrix}$$

---

## 7. KUKA KR 6 R900-2 Denavit-Hartenberg (DH) Model

The KUKA KR 6 R900-2 (KR AGILUS-2) is a 6-axis vertically articulated robot with a spherical wrist intersecting at $A_4, A_5, A_6$.

### Standard DH Transformation Matrix:
$$A_i = \text{Rot}(z, \theta_i) \cdot \text{Trans}(z, d_i) \cdot \text{Trans}(x, a_i) \cdot \text{Rot}(x, \alpha_i)$$

$$A_i = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\
\sin\theta_i & \cos\theta_i \cos\alpha_i & -\cos\theta_i \sin\alpha_i & a_i \sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}$$

### Standard DH Parameter Table for KUKA KR 6 R900-2:

| Link $i$ | Joint Angle $\theta_i$ | Offset $d_i\text{ [mm]}$ | Link Length $a_i\text{ [mm]}$ | Twist Angle $\alpha_i\text{ [rad]}$ | Joint Range |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $q_1$ | $d_1 = 400.0$ | $a_1 = 25.0$ | $-\pi/2$ ($-90^\circ$) | $\pm 170^\circ$ |
| **2** | $q_2 - \pi/2$ | $0.0$ | $a_2 = 455.0$ | $0$ ($0^\circ$) | $-190^\circ / +45^\circ$ |
| **3** | $q_3$ | $0.0$ | $a_3 = 35.0$ | $+\pi/2$ ($+90^\circ$) | $-120^\circ / +156^\circ$ |
| **4** | $q_4$ | $d_4 = 420.0$ | $0.0$ | $-\pi/2$ ($-90^\circ$) | $\pm 185^\circ$ |
| **5** | $q_5$ | $0.0$ | $0.0$ | $+\pi/2$ ($+90^\circ$) | $\pm 120^\circ$ |
| **6** | $q_6 + \pi$ | $d_6 = 80.0$ | $0.0$ | $\pi$ ($180^\circ$) | $\pm 350^\circ$ |

*Note: In Link 6, $d_6 = 80.0\text{ mm}$ is the distance from the intersection of axes 4, 5, 6 to the mechanical tool flange.*

---

## 8. Forward & Inverse Kinematics (Pieper's Decoupling)

### 8.1 Forward Kinematics Chain
$$T_0^6(\vec{q}) = A_1(q_1) \cdot A_2(q_2) \cdot A_3(q_3) \cdot A_4(q_4) \cdot A_5(q_5) \cdot A_6(q_6) = \begin{bmatrix} R_0^6(\vec{q}) & \vec{p}_0^6(\vec{q}) \\ \vec{0}^T & 1 \end{bmatrix}$$

### 8.2 Analytical Inverse Kinematics (Pieper's Solution)
Because axes 4, 5, and 6 intersect at a single point (the **Wrist Center** $\vec{p}_{wc}$), the 6-DoF inverse kinematics decouples into:
1. **Position Decoupling:** Solve $(q_1, q_2, q_3)$ for the wrist center position.
2. **Orientation Decoupling:** Solve $(q_4, q_5, q_6)$ from $R_3^6 = (R_0^3)^T \cdot R_{target}$.

#### Step 1: Wrist Center Computation
Given target end-effector position $\vec{p}_e$ and approach orientation vector $\vec{a} = R_{target}[:, 2]$ (third column):
$$\vec{p}_{wc} = \vec{p}_e - d_6 \vec{a}$$

#### Step 2: Regional Angles ($q_1, q_2, q_3$)
* $q_1 = \text{atan2}(p_{wc, y}, p_{wc, x}) \pm \text{atan2}(\dots)$
* Planar 2-link trigonometry on links $a_2$ and $d_4$ gives 2 solutions for $q_3$ (Elbow Up / Elbow Down) and 2 corresponding solutions for $q_2$.

#### Step 3: Spherical Wrist Angles ($q_4, q_5, q_6$)
$$R_3^6 = (R_0^3(q_1, q_2, q_3))^T \cdot R_{target}$$
Since axes 4, 5, 6 form an Euler $Z-Y-Z$ or $X-Y-X$ equivalent wrist:
* $q_5 = \pm \arccos(R_{33}^{36})$
* $q_4 = \text{atan2}(R_{23}^{36}, R_{13}^{36})$
* $q_6 = \text{atan2}(R_{32}^{36}, -R_{31}^{36})$

Total distinct kinematic configurations: $2 (\text{arm}) \times 2 (\text{elbow}) \times 2 (\text{wrist}) = 8\text{ solutions}$. In KRL, these are resolved by the **Status ($S$)** and **Turn ($T$)** integers.

---

## 9. Geometric Jacobian & Singularity Analysis

### 9.1 Geometric Jacobian Matrix
The geometric Jacobian $J(\vec{q}) \in \mathbb{R}^{6\times 6}$ relates joint velocities $\dot{\vec{q}}$ to end-effector spatial twist $\vec{V} = [\vec{v}_e^T, \vec{\omega}_e^T]^T$:
$$\begin{bmatrix} \vec{v}_e \\ \vec{\omega}_e \end{bmatrix} = J(\vec{q}) \dot{\vec{q}} = \begin{bmatrix} \vec{J}_{v1} & \vec{J}_{v2} & \dots & \vec{J}_{v6} \\ \vec{J}_{\omega 1} & \vec{J}_{\omega 2} & \dots & \vec{J}_{\omega 6} \end{bmatrix} \begin{bmatrix} \dot{q}_1 \\ \vdots \\ \dot{q}_6 \end{bmatrix}$$

For revolute joints $i \in \{1, \dots, 6\}$:
$$\vec{J}_{\omega i} = \vec{z}_{i-1}, \quad \vec{J}_{v i} = \vec{z}_{i-1} \times (\vec{p}_e - \vec{p}_{i-1})$$

### 9.2 Singularities ($\det(J(\vec{q})) = 0$)
Using the spherical wrist decoupling, the determinant factors into:
$$\det(J(\vec{q})) = \det(J_{11}(\vec{q})) \cdot \det(J_{22}(\vec{q})) = 0$$

1. **Wrist Singularity:** Occurs when axis 4 and axis 6 become collinear:
   $$q_5 = 0^\circ \implies \sin(q_5) = 0$$
   *Consequence:* Infinite joint speeds $\dot{q}_4, \dot{q}_6$ required to maintain Cartesian orientation during linear motion.

2. **Shoulder / Overhead Singularity:** Occurs when the wrist center lies directly on the axis of rotation of joint 1:
   $$p_{wc, x}^2 + p_{wc, y}^2 = 0$$

3. **Elbow / Boundary Singularity:** Occurs when the arm is fully extended or folded on itself:
   $$q_3 \in \{0^\circ, \text{boundary limit}\}$$

---

## 10. Computer Vision & Hand-Eye Calibration ($AX = XB$)

### 10.1 Pinhole Camera Model & Perspective-$n$-Point (PnP)
A 3D point $P_w = [X_w, Y_w, Z_w, 1]^T$ is projected onto image coordinates $p = [u, v, 1]^T$ via:
$$s \begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = \mathbf{K} \cdot [R_{c}^w \mid \vec{t}_c^w] \begin{bmatrix} X_w \\ Y_w \\ Z_w \\ 1 \end{bmatrix}$$
where:
$$\mathbf{K} = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix}$$

In OpenCV `cv2.solvePnP`, the estimated pose is returned as:
* `rvec`: The Rodrigues rotation vector $\vec{r} = \theta \vec{k} \in \mathbb{R}^3$.
* `tvec`: The translation vector $\vec{t} \in \mathbb{R}^3$.

### 10.2 Hand-Eye Calibration: $AX = XB$
When matching robot flange movements with camera movements across $N$ poses:

* **For Eye-in-Hand** (Camera mounted on robot flange):
  $$A_i = (T_{\text{base}}^{\text{flange}, i+1})^{-1} \cdot T_{\text{base}}^{\text{flange}, i}$$
  $$B_i = T_{\text{cam}, i+1}^{\text{target}} \cdot (T_{\text{cam}, i}^{\text{target}})^{-1}$$
  $$A_i X = X B_i \quad \text{where } X = T_{\text{flange}}^{\text{cam}}$$

* **Tsai-Lenz Method (Axis-Angle Separation):**
  Decomposing $A = (R_A, \vec{t}_A)$, $B = (R_B, \vec{t}_B)$, and $X = (R_X, \vec{t}_X)$:
  1. Solve rotation using modified Rodrigues vectors $\vec{P}$:
     $$\text{skew}(\vec{P}_A + \vec{P}_B) \cdot \vec{P}_X = \vec{P}_B - \vec{P}_A$$
  2. Solve translation via linear least squares:
     $$(R_A - I) \vec{t}_X = R_X \vec{t}_B - \vec{t}_A$$
