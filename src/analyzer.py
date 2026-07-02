import re

def analyze_physics_problem(problem_text):
    text = problem_text.lower()
    entitas_ditemukan = []
    
    # Deteksi entitas spesifik
    if "balok" in text: entitas_ditemukan.append("Balok")
    if "bidang miring" in text: entitas_ditemukan.append("Bidang_Miring")
    if "katrol" in text: entitas_ditemukan.append("Katrol")
            
    # LOGIKA PEMETAAN DOMAIN (Dinamis K-Series)
    if "bidang miring" in text:
        domain = "bidang_miring"
    elif "katrol" in text:
        domain = "katrol"
    else:
        domain = "translasi"
    
    return {
        "domain": domain,
        "entitas": entitas_ditemukan,
        "hukum_terkait": ["Hukum_Newton_2"]
    }
# PASTIKAN TIDAK ADA SATU BARIS PUN KODE ATAU PRINT DI BAWAH INI
