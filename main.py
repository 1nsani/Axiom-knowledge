    # ... (kode M-2 di atasnya tetap sama)

    # 4. M-3: Retriever (Lokal - Membaca Obsidian)
    print("[+] Menjalankan K-4 Retriever...")
    repo_path = "./metadata" 
    
    # PERUBAHAN DI SINI: Menerima 2 output
    konteks_fisika, visual_config = retrieve_knowledge(m2_data, repo_path=repo_path)
    
    if not konteks_fisika.strip():
        print("    [!] Peringatan: Konteks fisika kosong.")

    # 5. M-4: Assembler 
    print("[+] Menjalankan M-4 Prompt Assembler...")
    final_prompt = assemble_prompt(soal, konteks_fisika)

    # 6. M-5: Solver
    print("[+] Menjalankan M-5 Solver...")
    solusi_teks = execute_solver(final_prompt, api_key)
    print("\n--- HASIL M-5 ---\n", solusi_teks[:500], "...\n-----------------")

    # 7. M-6: Bridge 
    print("[+] Menjalankan K-5 Bridge Adapter...")
    
    # PERUBAHAN DI SINI: Menyuntikkan visual_config ke M-6
    json_file, extracted_data = convert_to_manim_data(solusi_teks, visual_config, api_key)

    if json_file:
        print(f"[SUCCESS] Payload universal siap di '{json_file}'")
    else:
        print(f"[-] FATAL ERROR pada K-5 Bridge.")
        
