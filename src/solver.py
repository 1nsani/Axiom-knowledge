def execute_solver(final_prompt):
    """
    Mesin M-5: Eksekutor akhir.
    Menembakkan prompt terstruktur ke model untuk mendapatkan solusi fisika.
    """
    try:
        # Menggunakan model yang sudah teruji di Colab kamu
        model = client.models.generate_content(
            model='gemini-1.5-flash', 
            contents=final_prompt,
            config=types.GenerateContentConfig(
                temperature=0.0, # Memaksa logika absolut, bukan kreatif
            ),
        )
        return model.text
    except Exception as e:
        return f"[-] M-5 FAILED: {str(e)}"

# --- EKSEKUSI FINAL ---
solusi = execute_solver(final_prompt)

print("="*60)
print("HASIL EKSEKUSI M-5 (SOLVER ENGINE):")
print("="*60)
print(solusi)
