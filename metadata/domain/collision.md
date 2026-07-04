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
optional_parameters: []
visual_hooks:
  scene_type: "collision"
  vectors_template:
    - id: "v1_before"
      type: "velocity_arrow"
      value_ref: "v1_awal"
      phase: "before"
      target: "balok1"
      color: "GREEN"
      label: "v_1"
    - id: "v2_before"
      type: "velocity_arrow"
      value_ref: "v2_awal"
      phase: "before"
      target: "balok2"
      color: "RED"
      label: "v_2"
    - id: "v1_after"
      type: "velocity_arrow"
      value_ref: "v1_akhir"
      phase: "after"
      target: "balok1"
      color: "GREEN"
      label: "v_1'"
    - id: "v2_after"
      type: "velocity_arrow"
      value_ref: "v2_akhir"
      phase: "after"
      target: "balok2"
      color: "RED"
      label: "v_2'"
---
# Skenario: Tumbukan 1D

**1. Analisis Sistem:**
Dua benda bergerak sepanjang garis lurus. Gunakan hukum kekekalan momentum dan koefisien restitusi.

**2. Rumus:**
- Kekekalan momentum: `m1*v1 + m2*v2 = m1*v1' + m2*v2'`
- Koefisien restitusi: `e = (v2' - v1') / (v1 - v2)`

**3. Kasus khusus:** `e=1` elastis sempurna. `e=0` inelastis sempurna (v1' = v2').

**4. Validasi:** `v1 > v2` (benda 1 mendekati benda 2) untuk tumbukan valid.

**Ketergantungan Fisika:**
[[Hukum_Kekekalan_Momentum]]
