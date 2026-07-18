"""
Jembatan antara output mesin mekanika umum dan format hasil_fisika
yang dipahami oleh renderer.py / bridge.py.
"""

def mechanics_result_ke_hasil_fisika(skema: dict, percepatan_numerik: float,
                                      gaya_constraint: dict = None) -> dict:
    """
    Konversi output mesin mekanika ke format hasil_fisika standar.
    
    Args:
        skema: dict definisi sistem (skema JSON)
        percepatan_numerik: float percepatan dalam koordinat umum q
        gaya_constraint: dict gaya constraint (tegangan, normal, dll.)
    
    Returns:
        dict dengan format standar hasil_fisika
    """
    a = percepatan_numerik
    
    # Tentukan arah gerak dari tanda percepatan
    if abs(a) < 1e-9:
        arah_gerak = "diam"
    elif a > 0:
        arah_gerak = "ke_bawah"
    else:
        arah_gerak = "ke_atas"
    
    hasil = {
        "percepatan": round(a, 4),
        "arah_gerak": arah_gerak,
    }
    
    # Tambahkan gaya constraint jika ada
    if gaya_constraint:
        hasil.update(gaya_constraint)
    
    # Tambahkan tegangan tali untuk domain katrol/gabungan
    sistem_id = skema.get("sistem_id", "")
    if "katrol" in sistem_id or "gabungan" in sistem_id:
        # Hitung tegangan dari percepatan dan massa
        for benda in skema["benda"]:
            if benda["arah_gerak"]["tanda"] == 1:
                # Benda ini naik jika a > 0, turun jika a < 0
                # T = m*(g + a) untuk benda yang naik, T = m*(g - a) untuk benda yang turun
                # Untuk koordinat umum q, kita gunakan rumus dari solver katrol
                pass
        # Untuk kasus gabungan, tegangan = m2*(g - a)
        # Tapi kita perlu nilai g dari skema
        g = 10.0
        for gaya in skema.get("gaya", []):
            if "g" in gaya.get("parameter", {}):
                g = gaya["parameter"]["g"]
        # Cari massa beban (benda dengan arah vertikal)
        for benda in skema["benda"]:
            if benda["arah_gerak"]["tipe"] == "vertikal":
                m_beban = benda.get("massa", 1.0)
                hasil["tegangan"] = round(m_beban * (g - abs(a)), 2)
                break
    
    return hasil


def build_vectors_from_skema(skema: dict) -> list:
    """
    Bangun daftar vektor (vectors_template) dari skema JSON untuk renderer.
    
    Returns:
        list of dict dengan format yang dipahami renderer.py
    """
    vectors = []
    
    for benda in skema["benda"]:
        if benda["arah_gerak"]["tipe"] == "sepanjang_bidang_miring":
            # Untuk benda di bidang miring: W, N, dan jika ada gesekan
            vectors.append({
                "id": f"W_{benda['id']}",
                "direction_logic": "absolute_down",
                "color": "RED",
                "label": f"W_{{{benda['id']}}}",
                "value_ref": f"W_{benda['id']}",
            })
            vectors.append({
                "id": f"N_{benda['id']}",
                "direction_logic": "perpendicular_up",
                "color": "YELLOW",
                "label": "N",
            })
        elif benda["arah_gerak"]["tipe"] == "vertikal":
            vectors.append({
                "id": f"T_{benda['id']}",
                "direction_logic": "absolute_up",
                "color": "PURPLE",
                "label": "T",
                "value_ref": "tegangan",
            })
            vectors.append({
                "id": f"W_{benda['id']}",
                "direction_logic": "absolute_down",
                "color": "RED",
                "label": f"W_{{{benda['id']}}}",
            })
    
    return vectors
