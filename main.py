import os
import sys
import json

from src.reader import read_all_problems
from src.analyzer import analyze_physics_problem
from src.retriever import retrieve_knowledge
from src.extractor_llm import extract_parameters

def process_one_problem(nama_file: str, problem_text: str, metadata_path: str, api_key: str, shared_dir: str) -> dict:
    """Proses satu soal, kembalikan dict status."""
    result = {"nama_file": nama_file, "status": "gagal", "alasan": ""}
    
    try:
        m2_data = analyze_physics_problem(problem_text)
        scene_type = m2_data["domain"]
        
        konteks_fisika, visual_hooks, required_params, optional_params = retrieve_knowledge(
            m2_data, repo_path=metadata_path
        )
        
        extracted = extract_parameters(
            problem_text, konteks_fisika, required_params, optional_params, scene_type, api_key
        )
        
        # Tulis ke shared folder dengan nama unik
        payload = {
            "scene_type": scene_type,
            "known": extracted["known"],
            "visual_hooks": visual_hooks,
            "soal": problem_text[:200]  # simpan cuplikan soal
        }
        os.makedirs(shared_dir, exist_ok=True)
        output_path = os.path.join(shared_dir, f"known_parameters_{nama_file}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4, ensure_ascii=False)
        
        result["status"] = "berhasil"
        result["scene_type"] = scene_type
        print(f"  [OK] {nama_file} -> {scene_type}")
        
    except Exception as e:
        result["alasan"] = str(e)
        print(f"  [GAGAL] {nama_file}: {e}")
    
    return result

def main():
    print("[SYSTEM] Axiom Knowledge Brain — MODE BATCH")
    
    problems = read_all_problems()
    print(f"[+] Ditemukan {len(problems)} soal di Docs/problems/")
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[-] FATAL: GEMINI_API_KEY tidak ditemukan.")
        sys.exit(1)
    
    metadata_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metadata")
    shared_dir = "/tmp/axiom_shared"
    
    ringkasan = []
    for nama_file, isi in problems:
        print(f"\n[PROSES] {nama_file}")
        res = process_one_problem(nama_file, isi, metadata_path, api_key, shared_dir)
        ringkasan.append(res)
    
    # Cetak ringkasan akhir
    print("\n" + "="*60)
    print("RINGKASAN BATCH BRAIN")
    print("="*60)
    berhasil = [r for r in ringkasan if r["status"] == "berhasil"]
    gagal = [r for r in ringkasan if r["status"] == "gagal"]
    print(f"Total: {len(ringkasan)} soal")
    print(f"Berhasil: {len(berhasil)}")
    print(f"Gagal: {len(gagal)}")
    for r in gagal:
        print(f"  - {r['nama_file']}: {r['alasan']}")
    print("="*60)

if __name__ == "__main__":
    main()
