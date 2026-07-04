---
id_domain: "bidang_miring"
dependencies:
  - "Hukum_Newton_2"
required_parameters:
  - "massa"
  - "sudut_permukaan"
optional_parameters:
  - "koefisien_gesek"
  - "gravitasi"
visual_hooks:
  scene_type: "bidang_miring"
  vectors_template:
    - id: "F_tarik"
      type: "arrow"
      direction_logic: "parallel_up"
      color: "GREEN"
      label: "\\vec{F}"
    - id: "N"
      type: "arrow"
      direction_logic: "perpendicular_up"
      color: "YELLOW"
      label: "\\vec{N}"
    - id: "W"
      type: "arrow"
      direction_logic: "absolute_down"
      color: "RED"
      label: "\\vec{W}"
---
# Skenario: Bidang Miring

**1. Analisis Geometri & Sistem Koordinat:**
Sistem koordinat wajib diputar searah dengan kemiringan bidang.
Gaya berat diuraikan menjadi komponen sejajar bidang (`W sin θ`) dan tegak lurus bidang (`W cos θ`).

**2. Ketergantungan Fisika:**
Wajib menguasai [[Hukum_Newton_2]] untuk resultan gaya sepanjang bidang.
