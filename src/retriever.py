import os
import yaml # Gunakan pyyaml untuk membaca frontmatter secara presisi

def parse_obsidian_file(filepath):
    """Membelah YAML Frontmatter dan Markdown Body"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2].strip()
                return frontmatter, body
            except Exception as e:
                print(f"[-] ERROR Parsing YAML di {filepath}: {e}")
    return {}, content

def retrieve_knowledge(m2_output, repo_path="./metadata"):
    print("[SYSTEM] Mengaktifkan K-4 Retriever (Universal)...")
    knowledge_context = ""
    visual_config = {}
    
    # 1. Ambil Aturan Skenario (Domain) Terlebih Dahulu
    domain = m2_output.get("domain", "")
    dependencies = []
    
    if domain:
        domain_file = domain.replace("dinamika_", "") + ".md" # misal: bidang_miring.md
        domain_path = os.path.join(repo_path, "domain", domain_file)
        
        if os.path.exists(domain_path):
            print(f"[+] Menemukan node domain: {domain_file}")
            frontmatter, body = parse_obsidian_file(domain_path)
            
            knowledge_context += f"\n>>> [SKENARIO: {domain}] <<<\n{body}\n"
            visual_config = frontmatter.get("visual_hooks", {})
            dependencies = frontmatter.get("dependencies", [])
        else:
            print(f"[-] PERINGATAN: Skenario {domain_file} tidak ditemukan di {domain_path}")

    # 2. Ambil Hukum Fundamental (Dari Dependencies YAML, BUKAN dari M-2)
    for hukum in dependencies:
        path = os.path.join(repo_path, "hukum_dasar", f"{hukum}.md")
        if os.path.exists(path):
            print(f"[+] Menemukan dependensi fundamental: {hukum}.md")
            _, body = parse_obsidian_file(path)
            knowledge_context += f"\n>>> [FUNDAMENTAL: {hukum}] <<<\n{body}\n"
        else:
            print(f"[-] PERINGATAN: Dependensi {hukum}.md tidak ditemukan.")

    return knowledge_context, visual_config
    
