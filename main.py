import os
import json
from src.analyzer import analyze_physics_problem
from src.retriever import retrieve_knowledge
from src.assembler import assemble_prompt
from src.solver import execute_solver
from src.bridge import convert_to_manim_data

def run_axiom_engine(soal_teks):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[-] FATAL: GEMINI_API_KEY tidak terdeteksi di Environment Variables.")
        return

    print("[1] Membedah Ontologi & Menarik Aturan...")
    m2_data = analyze_physics_problem(soal_teks)
    konteks = retrieve_knowledge(m2_data)

    print("[2] Kalkulasi M-5 Solver...")
    prompt = assemble_prompt(soal_teks, konteks)
    solusi_teks = execute_solver(prompt, api_key)

    print("[3] Konversi Data Visual (M-6 Bridge)...")
    json_file, ekstracted_data = convert_to_manim_data(solusi_teks, api_key)

    if json_file:
        print(f"[+] SUKSES: Payload siap di '{json_file}'")
        print(json.dumps(ekstracted_data, indent=4))
    else:
        print("[-] GAGAL membangun jembatan data.")

if __name__ == "__main__":
    soal = "Sebuah balok bermassa 4 kg ditarik ke atas bidang miring licin (sudut 30 derajat) dengan gaya 50 N. (g=10)"
    run_axiom_engine(soal)
