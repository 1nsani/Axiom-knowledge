import re

def analyze_physics_problem(problem_text):
    text = problem_text.lower()
    entitas_ditemukan = []
    if "balok" in text: entitas_ditemukan.append("Balok")
    if "bidang miring" in text: entitas_ditemukan.append("Bidang_Miring")
    if "katrol" in text: entitas_ditemukan.append("Katrol")
    if "tumbukan" in text or "momentum" in text or "bertumbukan" in text:
        entitas_ditemukan.append("Tumbukan")
    if "bidang miring" in text:
        domain = "bidang_miring"
    elif "tumbukan" in text or "momentum" in text:
        domain = "collision"
    elif "katrol" in text:
        domain = "katrol"
    else:
        domain = "translasi"
    hukum_terkait = ["Hukum_Newton_2"]
    if domain == "collision":
        hukum_terkait.append("Hukum_Kekekalan_Momentum")
    return {
        "domain": domain,
        "entitas": entitas_ditemukan,
        "hukum_terkait": hukum_terkait
    }
