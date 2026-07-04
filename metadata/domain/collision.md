---
id_domain: "collision"
dependencies: 
  - "Hukum_Kekekalan_Momentum"
required_parameters: 
  - "massa_1"
  - "massa_2"
  - "v1_awal"
  - "v2_awal"
  - "koefisien_restitusi"
visual_hooks:
  scene_type: "collision"
  vectors_template:
    - id: "p1_before"
      type: "arrow"
      direction_logic: "horizontal_right"
      color: "GREEN"
      label: "\vec{p_1}"
    - id: "p2_before"
      type: "arrow"
      direction_logic: "horizontal_left"
      color: "RED"
      label: "\vec{p_2}"
    - id: "p1_after"
      type: "arrow"
      direction_logic: "horizontal_right"
      color: "GREEN"
      label: "\vec{p_1}'"
    - id: "p2_after"
      type: "arrow"
      direction_logic: "horizontal_left"
      color: "RED"
      label: "\vec{p_2}'"
---
# Skenario: Tumbukan 1D

**1. Analisis Sistem:**
Dua benda bergerak sepanjang garis lurus. Gunakan hukum kekekalan momentum dan koefisien restitusi.

**2. Rumus:**
- Kekekalan momentum: m1 v1 + m2 v2 = m1 v1' + m2 v2'
- Koefisien restitusi: e = (v2' - v1') / (v1 - v2)

**3. Kasus khusus:**
- e=1: elastis sempurna
- e=0: inelastis sempurna (v1' = v2')

**4. Validasi:**
Pastikan v1 > v2 (benda 1 mendekati benda 2) untuk tumbukan valid.
