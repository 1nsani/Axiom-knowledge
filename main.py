import os
import json
from src.analyzer import analyze_physics_problem
from src.retriever import retrieve_knowledge
from src.assembler import assemble_prompt
from src.solver import execute_solver
from src.bridge import convert_to_manim_data

def run_axiom_engine():
    print("[SYSTEM] Memulai Eksekusi Jalur DFS Axiom Engine...\n")
    
    # 1. Ambil API Key dari Environment Variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[-] FATAL ERROR: GEMINI_API_KEY tidak ditemukan di environment.")
        print("Pastikan kamu sudah menjalankan 'os.environ[\"GEMINI_API_KEY\"] = ...' di cell Colab.")
        return

    # 2. Input Soal
    soal = "Sebuah balok bermassa 4 kg ditarik ke atas bidang miring licin (sudut 30 derajat) dengan gaya 50 N. (g=10)"
    print(f"[+] Input Soal: {soal}")

    # 3. M-2: Analyzer (Lokal)
    print("[+] Menjalankan M-2 Analyzer...")
    m2_data = analyze_physics_problem(soal)
    print(f"    Output M-2: {json.dumps(m2_data)}")

    # 4. M-3: Retriever (Lokal - Membaca Obsidian)
    print("[+] Menjalankan M-3 Retriever...")
    # Sesuaikan path jika folder metadata kamu ada di lokasi berbeda
    repo_path = "./metadata" 
    konteks_fisika = retrieve_knowledge(m2_data, repo_path=repo_path)
    
    if not konteks_fisika.strip():
        print("    [!] Peringatan: Konteks fisika dari Obsidian kosong. Periksa path folder metadata kamu.")

    # 5. M-4: Assembler (Lokal)
    print("[+] Menjalankan M-4 Prompt Assembler...")
    final_prompt = assemble_prompt(soal, konteks_fisika)

    # 6. M-5: Solver (API Call - Menggunakan fungsi baru yang sudah steril)
    print("[+] Menjalankan M-5 Solver (Menghubungi Gemini 3.5 Flash)...")
    solusi_teks = execute_solver(final_prompt, api_key)
    
    print("\n================ HASIL EKSEKUSI M-5 ================")
    print(solusi_teks)
    print("====================================================\n")

    # 7. M-6: Bridge (API Call - Ekstraksi Terstruktur untuk Manim)
    print("[+] Menjalankan M-6 Bridge Adapter...")
    json_file, extracted_data = convert_to_manim_data(solusi_teks, api_key)

    if json_file:
        print(f"[SUCCESS] Rantai DFS Selesai! Payload visual siap di: '{json_file}'")
        print("Isi Data JSON untuk Manim:")
        print(json.dumps(extracted_data, indent=4))
    else:
        print(f"[-] Gagal di tahap akhir M-6: {extracted_data.get('error')}")

if __name__ == "__main__":
    run_axiom_engine()
