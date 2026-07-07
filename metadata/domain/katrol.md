---
id_domain: "katrol"
dependencies:
  - "Hukum_Newton_2"
required_parameters:
  - "massa_1"
  - "massa_2"
optional_parameters:
  - "gravitasi"
visual_hooks:
  scene_type: "katrol"
  vectors_template:
    - id: "T1"
      type: "arrow"
      direction_logic: "absolute_up"
      color: "PURPLE"
      label: "T_1"
      value_ref: "tegangan"
    - id: "T2"
      type: "arrow"
      direction_logic: "absolute_up"
      color: "PURPLE"
      label: "T_2"
      value_ref: "tegangan"
    - id: "W1"
      type: "arrow"
      direction_logic: "absolute_down"
      color: "RED"
      label: "W_1"
      value_ref: "W1"
    - id: "W2"
      type: "arrow"
      direction_logic: "absolute_down"
      color: "RED"
      label: "W_2"
      value_ref: "W2"
---
# Skenario: Katrol Sederhana (Atwood Machine)
Dua massa dihubungkan oleh tali melalui katrol licin tanpa massa.
Gunakan Hukum Newton II pada masing-masing massa untuk mencari percepatan sistem dan tegangan tali.

**Ketergantungan Fisika:**
[[Hukum_Newton_2]]
