import os

def retrieve_knowledge(m2_output, repo_path="/content/Axiom-knowledge"):
    """
    Mesin M-3: Bertugas menarik aturan fisika dari database Obsidian
    berdasarkan peta JSON yang dihasilkan oleh M-2.
    """
    print("[SYSTEM] Mengaktifkan M-3 Retriever...\n")
    knowledge_context = ""
    
    # 1. Tarik Aturan Hukum Fundamental
    hukum_list = m2_output.get("hukum_terkait", [])
    for hukum in hukum_list:
        path = os.path.join(repo_path, "metadata", "hukum_dasar", f"{hukum}.md")
        if os.path.exists(path):
            print(f"[+] Menemukan node fundamental: {hukum}.md")
            with open(path, 'r') as f:
                knowledge_context += f"\n>>> [ATURAN FUNDAMENTAL: {hukum}] <<<\n"
                knowledge_context += f.read() + "\n"
        else:
            print(f"[-] PERINGATAN: Node {hukum}.md hilang dari database Obsidian!")

    # 2. Tarik Aturan Skenario/Domain
    domain = m2_output.get("domain", "")
    # Konversi string 'dinamika_translasi' menjadi nama file 'Translasi.md'
    if domain:
        domain_file = domain.split("_")[-1].capitalize() + ".md"
        domain_path = os.path.join(repo_path, "metadata", "dinamika", domain_file)
        
        if os.path.exists(domain_path):
            print(f"[+] Menemukan node skenario: {domain_file}")
            with open(domain_path, 'r') as f:
                knowledge_context += f"\n>>> [ATURAN SKENARIO: {domain}] <<<\n"
                knowledge_context += f.read() + "\n"
        else:
            print(f"[-] PERINGATAN: Node {domain_file} hilang dari database Obsidian!")
            
    return knowledge_context

# --- UJI COBA MESIN M-3 ---
# Ini adalah output M-2 yang kamu sebut "kosong" tadi
m2_data = {
    "domain": "dinamika_translasi",
    "entitas": ["Balok", "Bidang_Miring"],
    "hukum_terkait": ["Hukum_Newton_2"]
}

# M-3 beraksi menarik data
konteks_fisika = retrieve_knowledge(m2_data)

print("\n" + "="*50)
print("HASIL EKSTRAKSI PENGETAHUAN OBSIDIAN:")
print("="*50)
print(konteks_fisika)
