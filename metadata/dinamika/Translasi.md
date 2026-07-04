---
domain: "dinamika_translasi"
required_parameters:
  - "massa"
  - "sudut_permukaan"
  - "gravitasi"
  - "koefisien_gesek"
visual_constraints:
  coordinate_system: "tilted_on_theta"
  object_alignment: "surface_contact_bottom"
  render_vectors:
    - "W"
    - "N"
    - "f"
---

# Skenario Dinamika Translasi
Domain ini mendikte aturan bagi objek yang bergeser atau meluncur (balok, kotak, partikel).

**Ketergantungan Fisika:**
Untuk menyelesaikan sistem ini, wajib menguasai [[Hukum_Newton_2]].
Sistem koordinat visual WAJIB diputar negatif sebesar `sudut_permukaan`.
