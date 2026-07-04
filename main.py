import os
import sys
from src.reader import read_problem_file
from src.analyzer import analyze_physics_problem
from src.retriever import retrieve_knowledge
from src.extractor_llm import extract_parameters
from src.bridge_export import export_known_parameters
import yaml

def main():
    print("[SYSTEM] Axiom Knowledge Brain - Ekstraksi Parameter")
    problem_text = read_problem_file()
    if not problem_text:
        print("[-] Gagal membaca soal.")
        sys.exit(1)
    print(f"[+] Soal: {problem_text[:100]}...")
    m2_data = analyze_physics_problem(problem_text)
    scene_type = m2_data["domain"]
    print(f"[+] Domain terdeteksi: {scene_type}")
    repo_path = "./metadata"
    konteks_fisika, visual_hooks = retrieve_knowledge(m2_data, repo_path=repo_path)
    if not konteks_fisika.strip():
        print("[!] Peringatan: Konteks fisika kosong.")
    domain_file = os.path.join(repo_path, "domain", f"{scene_type}.md")
    required_params = []
    if os.path.exists(domain_file):
        with open(domain_file, "r") as f:
            content = f.read()
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                required_params = frontmatter.get("required_parameters", [])
    if not required_params:
        required_params = ["massa", "sudut", "gaya", "kecepatan", "gravitasi"]
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[-] FATAL: GEMINI_API_KEY tidak ditemukan.")
        sys.exit(1)
    try:
        extracted = extract_parameters(
            problem_text, 
            konteks_fisika, 
            visual_hooks, 
            required_params, 
            scene_type, 
            api_key
        )
        print("[+] Ekstraksi berhasil.")
        assert "scene_type" in extracted
        assert "known" in extracted
        export_known_parameters(extracted)
    except Exception as e:
        print(f"[-] Gagal ekstraksi: {e}")
        sys.exit(1)
    print("[SYSTEM] Selesai.")

if __name__ == "__main__":
    main()
