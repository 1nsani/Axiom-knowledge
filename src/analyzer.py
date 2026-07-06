DOMAIN_KEYWORDS = {
    "bidang_miring": ["bidang miring"],
    "collision": ["tumbukan", "bertumbukan", "momentum", "restitusi"],
    "katrol": ["katrol", "pulley", "atwood"],
    "gerak_parabola": ["parabola", "peluru", "proyektil", "elevasi"],
}

DEFAULT_DOMAIN = "translasi"

ENTITY_KEYWORDS = {
    "Balok": ["balok"],
    "Bidang_Miring": ["bidang miring"],
    "Katrol": ["katrol"],
    "Tumbukan": ["tumbukan", "momentum", "bertumbukan"],
    "Proyektil": ["parabola", "peluru", "proyektil"],
}

def analyze_physics_problem(problem_text: str) -> dict:
    text = problem_text.lower()
    entitas_ditemukan = [
        nama for nama, kw_list in ENTITY_KEYWORDS.items()
        if any(kw in text for kw in kw_list)
    ]
    domain = DEFAULT_DOMAIN
    for domain_name, kw_list in DOMAIN_KEYWORDS.items():
        if any(kw in text for kw in kw_list):
            domain = domain_name
            break
    hukum_terkait = ["Hukum_Newton_2"]
    if domain == "collision":
        hukum_terkait.append("Hukum_Kekekalan_Momentum")
    return {
        "domain": domain,
        "entitas": entitas_ditemukan,
        "hukum_terkait": hukum_terkait,
    }
