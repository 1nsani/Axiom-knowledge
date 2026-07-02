import os
import json
from src.analyzer import analyze_physics_problem
from src.retriever import retrieve_knowledge
from src.assembler import assemble_prompt
from src.solver import execute_solver
from src.bridge import convert_to_manim_data

def run_axiom_engine():
    print("[SYSTEM] Memulai Eksekusi Jalur DFS Axiom Engine...\n")
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[-] FATAL ERROR: GEMINI_API_KEY tidak ditemukan.")
        return

    soal = "Sebuah balok bermassa 4 kg ditarik ke atas bidang miring licin (sudut 30 derajat) dengan gaya 50 N. (g=10)"
    print(f"[+] Input Soal: {soal}")

    # 1. M-2 Analyzer
    print("[+] Menjalankan M-2 Analyzer...")
    m2_data = analyze_physics_problem(soal)

    # 2. M-3 Retriever (K-4 Universal)
    print("[+] Menjalankan K-4 Retriever...")
    repo_path = "./metadata" 
    konteks_fisika, visual_config = retrieve_knowledge(m2_data, repo_path=repo_path)
    
    if not konteks_fisika.strip():
        print("    [!] Peringatan: Konteks fisika kosong.")

    # 3. M-4 Assembler
    print("[+] Menjalankan M-4 Prompt Assembler...")
    final_prompt = assemble_prompt(soal, konteks_fisika)

    # 4. M-5 Solver
    print("[+] Menjalankan M-5 Solver...")
    solusi_teks = execute_solver(final_prompt, api_key)
    print("\n--- HASIL M-5 ---\n", solusi_teks[:300], "...\n-----------------")

    # 5. M-6 Bridge (K-5 Universal)
    print("[+] Menjalankan K-5 Bridge Adapter...")
    json_file, extracted_data = convert_to_manim_data(solusi_teks, visual_config, api_key)

    if json_file:
        print(f"[SUCCESS] Payload universal siap di '{json_file}'")
    else:
        print(f"[-] FATAL ERROR pada K-5 Bridge: {extracted_data.get('error')}")

if __name__ == "__main__":
    run_axiom_engine()
    
