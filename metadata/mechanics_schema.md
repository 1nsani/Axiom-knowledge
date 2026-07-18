# Skema JSON untuk Sistem Mekanika

## Struktur Umum
```json
{
  "sistem_id": "string",
  "koordinat_umum": ["q1"],
  "benda": [
    {
      "id": "string",
      "massa_simbol": "m1",
      "arah_gerak": {
        "tipe": "sepanjang_bidang_miring" | "vertikal",
        "parameter": {"sudut": 30},
        "tanda": 1 | -1
      },
      "koefisien_koordinat": "q1"
    }
  ],
  "gaya": [
    {
      "tipe": "gravitasi" | "gesekan_kinetis",
      "benda": "string",
      "parameter": {"g": 10, "mu": 0.2}
    }
  ]
}
