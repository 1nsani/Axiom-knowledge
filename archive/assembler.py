def assemble_prompt(problem_text, context_text):
    """
    Mesin M-4: Merakit Prompt Absolut.
    Mengikat soal dengan aturan ketat dari Obsidian.
    """
    
    prompt_template = f"""
Anda adalah mesin komputasi fisika numerik tingkat lanjut.
Tugas Anda adalah menyelesaikan soal fisika berikut HANYA dengan mematuhi aturan fundamental dan konstrain visual yang diberikan. 

=== ATURAN SISTEM OBSIDIAN (WAJIB DIPATUHI) ===
{context_text}
==============================================

=== SOAL FISIKA ===
{problem_text}
===================

INSTRUKSI EKSEKUSI (JALANKAN SECARA BERURUTAN):
1. DEKLARASI PARAMETER: Identifikasi semua angka dan satuan dari soal. Sesuaikan dengan `required_parameters` di aturan sistem.
2. ANALISIS GEOMETRI: Terapkan `visual_constraints`. Jika sistem koordinat miring (tilted), pecah vektor gaya (W, N, f) ke dalam komponen sumbu X sejajar bidang dan sumbu Y tegak lurus bidang.
3. PENURUNAN LOGIKA & SATUAN: Jangan gunakan hafalan rumus instan. Turunkan persamaan dari `rumus_utama` di aturan fundamental. Lakukan verifikasi analisis satuan (unit analysis) di setiap tahap.
4. KALKULASI NUMERIK: Masukkan angka ke dalam persamaan yang telah diturunkan dan hitung hasil akhirnya.

Jika ada informasi yang kurang untuk memenuhi parameter sistem, nyatakan dengan jelas variabel apa yang hilang. 
Gunakan format output yang rasional, objektif, dan tanpa basa-basi.
"""
    return prompt_template.strip()

# --- UJI COBA MESIN M-4 ---
# Kita gunakan variabel dari pengujian M-2 dan M-3 sebelumnya
soal_asli = "Sebuah balok bermassa 4 kg ditarik ke atas bidang miring licin (sudut 30 derajat) dengan gaya 50 N. (g = 10 m/s^2)"

# (Asumsi 'konteks_fisika' adalah output dari fungsi retrieve_knowledge di skrip M-3 sebelumnya)
# Jika kamu menjalankan ini di sel yang sama/berurutan di Colab, variabel 'konteks_fisika' masih tersimpan di memori.
try:
    final_prompt = assemble_prompt(soal_asli, konteks_fisika)
    print("[SYSTEM] Prompt berhasil dirakit. Berikut adalah peluru yang akan ditembakkan ke M-5 Solver:\n")
    print("="*60)
    print(final_prompt)
    print("="*60)
except NameError:
    print("[-] ERROR: Variabel 'konteks_fisika' tidak ditemukan. Pastikan kamu sudah menjalankan sel M-3 sebelumnya.")
