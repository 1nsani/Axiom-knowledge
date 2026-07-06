---
id_domain: "gerak_parabola"
dependencies:
  - "Hukum_Newton_2"
required_parameters:
  - "v0"
  - "sudut_elevasi"
optional_parameters:
  - "gravitasi"
  - "tinggi_awal"
visual_hooks:
  scene_type: "gerak_parabola"
  vectors_template: []
---
# Skenario: Gerak Parabola (Proyektil)

**1. Analisis:**
Gerak parabola adalah perpaduan GLB (horizontal) dan GLBB (vertikal).
Kecepatan awal diuraikan menjadi komponen horizontal dan vertikal.

**2. Rumus Utama:**
- Waktu di udara: `t = (v0 sin θ + √((v0 sin θ)² + 2gh)) / g`
- Jarak horizontal maksimum: `R = v0 cos θ × t`
- Tinggi maksimum: `h_max = h0 + (v0 sin θ)² / (2g)`

**Ketergantungan Fisika:**
[[Hukum_Newton_2]]
