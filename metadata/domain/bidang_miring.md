---
id_domain: "bidang_miring"
dependencies: 
  - "Hukum_Newton_2"
required_parameters: 
  - "massa"
  - "sudut_permukaan"
visual_hooks:
  scene_type: "inclined_plane"
  vectors_template:
    - id: "F_tarik"
      type: "arrow"
      direction_logic: "parallel_up"
      color: "GREEN"
      label: "\vec{F}"
    - id: "N"
      type: "arrow"
      direction_logic: "perpendicular_up"
      color: "YELLOW"
      label: "\vec{N}"
    - id: "W"
      type: "arrow"
      direction_logic: "absolute_down"
      color: "RED"
      label: "\vec{W}"
---
# Skenario: Bidang Miring

**1. Analisis Geometri & Sistem Koordinat:**
Sistem koordinat wajib diputar searah dengan kemiringan bidang. 
Sumbu X sejajar permukaan bidang. Sumbu Y tegak lurus permukaan bidang.
Dekomposisi gaya berat ($W$):
- $W_x = -m \cdot g \cdot \sin(\theta)$
- $W_y = -m \cdot g \cdot \cos(\theta)$

**2. Penurunan Logika Translasi:**
Tidak ada pergerakan menembus bidang ($a_y = 0$). Selesaikan gaya normal ($N$) melalui $\Sigma F_y = 0$.
Pergerakan translasi hanya terjadi di sumbu X. Gunakan hukum fundamental untuk mencari $a_x$.

**3. Validasi Satuan:**
Semua hasil akhir gaya harus memiliki satuan turunan $\text{kg} \cdot \text{m/s}^2$. Percepatan harus $\text{m/s}^2$. Evaluasi satuan secara eksplisit.
