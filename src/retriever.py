import os

def retrieve_knowledge(m2_output, repo_path="./metadata"):
    """
    Mesin M-3: Mengambil data dari Obsidian dengan kalkulasi path yang presisi.
    Tanpa penumpukan folder.
    """
    print("[SYSTEM] Mengaktifkan M-3 Retriever...")
    knowledge_context = ""
    
    # 1. Ambil Aturan Hukum Fundamental
    hukum_list = m2_output.get("hukum_terkait", [])
    for hukum in hukum_list:
        # Perbaikan: repo_path langsung digabung dengan sub-folder target
        path = os.path.join(repo_path, "hukum_dasar", f"{hukum}.md")
        if os.path.exists(path):
            print(f"[+] Menemukan node fundamental: {hukum}.md")
            with open(path, 'r') as f:
                knowledge_context += f"\n>>> [ATURAN FUNDAMENTAL: {hukum}] <<<\n" + f.read() + "\n"
        else:
            print(f"[-] PERINGATAN: File tidak ditemukan di rute: {path}")

    # 2. Ambil Aturan Skenario / Domain
    domain = m2_output.get("domain", "")
    if domain:
        domain_file = domain.split("_")[-1].capitalize() + ".md" # Contoh: 'Translasi.md'
        domain_path = os.path.join(repo_path, "dinamika", domain_file)
        
        if os.path.exists(domain_path):
            print(f"[+] Menemukan node skenario: {domain_file}")
            with open(domain_path, 'r') as f:
                knowledge_context += f"\n>>> [ATURAN SKENARIO: {domain}] <<<\n" + f.read() + "\n"
        else:
            print(f"[-] PERINGATAN: File tidak ditemukan di rute: {domain_path}")
            
    return knowledge_context
