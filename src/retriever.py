import os
import yaml


def parse_obsidian_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return frontmatter, body
            except yaml.YAMLError as e:
                raise RuntimeError(f"YAML rusak di {filepath}: {e}")
    return {}, content


def retrieve_knowledge(m2_output: dict, repo_path: str = "./metadata"):
    """
    Return: (knowledge_context, visual_hooks, required_params, optional_params)
    """
    print("[SYSTEM] Mengaktifkan Retriever...")
    domain = m2_output.get("domain", "")
    dependencies = list(m2_output.get("hukum_terkait", []))

    domain_path = os.path.join(repo_path, "domain", f"{domain}.md")
    if not os.path.exists(domain_path):
        raise RuntimeError(
            f"[FATAL] Domain '{domain}' tidak punya metadata di {domain_path}. "
            f"Pipeline dihentikan untuk mencegah ekstraksi tanpa skema (anti-halusinasi)."
        )

    print(f"[+] Domain node ditemukan: {domain}.md")
    frontmatter, body = parse_obsidian_file(domain_path)
    knowledge_context = f"\n>>> [SKENARIO: {domain}] <<<\n{body}\n"
    visual_hooks = frontmatter.get("visual_hooks", {})
    required_params = frontmatter.get("required_parameters", [])
    optional_params = frontmatter.get("optional_parameters", [])

    for extra_dep in frontmatter.get("dependencies", []):
        if extra_dep not in dependencies:
            dependencies.append(extra_dep)

    for hukum in dependencies:
        hukum_path = os.path.join(repo_path, "hukum_dasar", f"{hukum}.md")
        if os.path.exists(hukum_path):
            print(f"[+] Dependensi fundamental ditemukan: {hukum}.md")
            _, hukum_body = parse_obsidian_file(hukum_path)
            knowledge_context += f"\n>>> [FUNDAMENTAL: {hukum}] <<<\n{hukum_body}\n"
        else:
            print(f"[!] Peringatan (non-fatal): dependensi {hukum}.md tidak ditemukan.")

    if not visual_hooks:
        print(f"[!] Peringatan: visual_hooks kosong untuk domain '{domain}'.")
    if not required_params:
        print(f"[!] Peringatan: required_parameters kosong untuk domain '{domain}'.")

    return knowledge_context, visual_hooks, required_params, optional_params
