import json
import re

def analyze_physics_problem_local(problem_text):
    """
    Mesin M-2 tanpa API. Menggunakan pencocokan pola deterministik
    untuk mengekstrak struktur ontologi fisika.
    0% Halusinasi, 0 Limit Kuota.
    """
    text = problem_text.lower()
    
    # 1. Pindai Entitas Fisika
    entitas_ditemukan = []
    kamus_entitas = ["balok", "bidang miring", "katrol", "pegas", "tali", "partikel", "mobil", "bola"]
    for entitas in kamus_entitas:
        if re.search(r'\b' + entitas + r'\b', text):
            # Format output agar rapi (cth: "Bidang_Miring")
            entitas_ditemukan.append(entitas.replace(" ", "_").title())
            
    # 2. Logika Klasifikasi Domain & Hukum
    domain = "tidak_diketahui"
    hukum = []
    
    # Cek Termodinamika
    if any(kata in text for kata in ["suhu", "kalor", "termodinamika", "gas", "ideal", "isobarik"]):
        domain = "termodinamika"
        hukum.append("Hukum_Termodinamika_1")
        
    # Cek Dinamika Rotasi
    elif any(kata in text for kata in ["torsi", "momen inersia", "menggelinding", "silinder pejal"]):
        domain = "dinamika_rotasi"
        hukum.append("Hukum_Newton_2_Rotasi")
        
    # Cek Dinamika Translasi (Gaya, Massa, Gesekan)
    elif any(kata in text for kata in ["gaya", "ditarik", "didorong", "gesek", "licin", "massa"]):
        domain = "dinamika_translasi"
        # Jika ada indikasi keseimbangan
        if any(kata in text for kata in ["diam", "konstan", "seimbang"]):
            hukum.append("Hukum_Newton_1")
        else:
            hukum.append("Hukum_Newton_2")
            
    # Cek Kinematika (Gerak tanpa penyebab gaya)
    elif any(kata in text for kata in ["kecepatan", "percepatan", "waktu", "jarak"]):
        domain = "kinematika"
        hukum.append("Persamaan_GLBB")

    # 3. Rakit Output JSON
    hasil = {
        "domain": domain,
        "entitas": entitas_ditemukan,
        "hukum_terkait": hukum
    }
    
    return hasil

# --- UJI COBA MESIN M-2 LOKAL ---
soal_dummy = "Sebuah balok bermassa 4 kg ditarik ke atas bidang miring licin (sudut 30 derajat) dengan gaya 50 N."
hasil_analisis = analyze_physics_problem_local(soal_dummy)

print("INPUT SOAL:", soal_dummy)
print("-" * 40)
print("OUTPUT M-2 (JSON MURNI - TANPA API):")
print(json.dumps(hasil_analisis, indent=4))
