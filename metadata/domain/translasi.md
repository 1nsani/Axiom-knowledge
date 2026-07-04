---
id_domain: "translasi"
dependencies:
  - "Hukum_Newton_2"
required_parameters:
  - "massa"
optional_parameters:
  - "gaya"
  - "koefisien_gesek"
visual_hooks:
  scene_type: "translasi"
  vectors_template:
    - id: "F"
      type: "arrow"
      direction_logic: "parallel_up"
      color: "GREEN"
      label: "\\vec{F}"
---
# Skenario Dinamika Translasi (Fallback Umum)
Domain ini menampung soal gerak translasi generik yang tidak cocok domain spesifik manapun (bidang miring, tumbukan, katrol).
Solver untuk domain ini BELUM diimplementasikan secara sengaja — jika soal jatuh ke sini, sistem akan berhenti dengan pesan jelas alih-alih menebak jawaban.

**Ketergantungan Fisika:**
[[Hukum_Newton_2]]
