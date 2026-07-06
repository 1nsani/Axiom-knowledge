import os
import glob

def read_all_problems() -> list:
    """Kembalikan list of (nama_file, isi_teks) dari folder Docs/problems/"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    problems_dir = os.path.join(base_dir, "Docs", "problems")
    
    # Buat folder jika belum ada
    os.makedirs(problems_dir, exist_ok=True)
    
    # Jika folder kosong, buat soal default
    files = glob.glob(os.path.join(problems_dir, "*.md"))
    if not files:
        default_path = os.path.join(problems_dir, "soal_default.md")
        with open(default_path, "w", encoding="utf-8") as f:
            f.write("Sebuah balok bermassa 5 kg meluncur pada bidang miring 37 derajat tanpa gesekan. (g=10 m/s²)")
        files = [default_path]
    
    results = []
    for filepath in sorted(files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        nama_file = os.path.basename(filepath).replace(".md", "")
        results.append((nama_file, content))
    return results

if __name__ == "__main__":
    for nama, isi in read_all_problems():
        print(f"=== {nama} ===\n{isi}\n")
