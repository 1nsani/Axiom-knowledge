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
  - "gaya_eksternal"
visual_hooks:
  scene_type: "bidang_miring"
  vectors_template:
    - id: "W"
      type: "arrow"
      direction_logic: "absolute_down"
      color: "RED"
      label: "\\vec{W}"
    - id: "W_sin"
      type: "arrow"
      direction_logic: "parallel_down"
      color: "ORANGE"
      label: "W\\sin\\theta"
    - id: "W_cos"
      type: "arrow"
      direction_logic: "perpendicular_down"
      color: "ORANGE"
      label: "W\\cos\\theta"
    - id: "N"
      type: "arrow"
      direction_logic: "perpendicular_up"
      color: "YELLOW"
      label: "\\vec{N}"
    - id: "F_ext"
      type: "arrow"
      direction_logic: "parallel_up"
      color: "GREEN"
      label: "F_{\\text{tarik}}"
---
# Skenario: Bidang Miring

**1. Analisis Geometri & Sistem Koordinat:**
Sistem koordinat wajib diputar searah dengan kemiringan bidang.
Gaya berat diuraikan menjadi komponen sejajar bidang (`W sin θ`) dan tegak lurus bidang (`W cos θ`).

**2. Ketergantungan Fisika:**
Wajib menguasai [[Hukum_Newton_2]] untuk resultan gaya sepanjang bidang.
