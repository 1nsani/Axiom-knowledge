import os
import yaml

def parse_obsidian_file(filepath):
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
    domain = m2_output.get("domain", "")
    dependencies = m2_output.get("hukum_terkait", [])
    domain_file_map = {
        "bidang_miring": "bidang_miring.md",
        "collision": "collision.md",
        "katrol": "katrol.md",
        "translasi": "translasi.md"
    }
    domain_file = domain_file_map.get(domain, f"{domain}.md")
    domain_path = os.path.join(repo_path, "domain", domain_file)
    if os.path.exists(domain_path):
        print(f"[+] Menemukan node domain: {domain_file}")
        frontmatter, body = parse_obsidian_file(domain_path)
        knowledge_context += f"
>>> [SKENARIO: {domain}] <<<
{body}
"
        visual_config = frontmatter.get("visual_hooks", {})
        yaml_deps = frontmatter.get("dependencies", [])
        for d in yaml_deps:
            if d not in dependencies:
                dependencies.append(d)
    else:
        print(f"[-] PERINGATAN: Skenario {domain_file} tidak ditemukan di {domain_path}")
    for hukum in dependencies:
        hukum_path = os.path.join(repo_path, "hukum_dasar", f"{hukum}.md")
        if os.path.exists(hukum_path):
            print(f"[+] Menemukan dependensi fundamental: {hukum}.md")
            _, body = parse_obsidian_file(hukum_path)
            knowledge_context += f"
>>> [FUNDAMENTAL: {hukum}] <<<
{body}
"
        else:
            print(f"[-] PERINGATAN: Dependensi {hukum}.md tidak ditemukan di {hukum_path}")
    if not visual_config:
        print("[!] PERINGATAN: visual_hooks kosong untuk domain ini.")
    return knowledge_context, visual_config
