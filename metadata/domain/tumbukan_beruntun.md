---
id_domain: "tumbukan_beruntun"
dependencies:
  - "Hukum_Kekekalan_Momentum"
modes:
  simulasi:
    required_parameters:
      - "massa_kiri"
      - "massa_tengah"
      - "massa_kanan"
      - "kecepatan_tengah"
    optional_parameters: []
  cari_kritis:
    required_parameters:
      - "jumlah_benda"
      - "target_jumlah_tumbukan"
    optional_parameters: ["massa_banding"]
visual_hooks:
  scene_type: "tumbukan_beruntun"
  vectors_template: []
---
# Skenario: Tumbukan Beruntun Tiga Benda

**Mode "simulasi"**:
Diberikan massa dan kecepatan awal, hitung jumlah tumbukan dan animasikan.

**Mode "cari_kritis"**:
Cari nilai maksimum massa (alpha) agar terjadi tepat N kali tumbukan,
lalu animasikan skenario di bawah batas kritis.

**Ketergantungan Fisika:**
[[Hukum_Kekekalan_Momentum]]
