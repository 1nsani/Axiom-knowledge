import os

def read_problem_file() -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, "Docs", "Problem.md")

    if not os.path.exists(input_file):
        print(f"[-] Warning: {input_file} tidak ditemukan. Memakai prompt cadangan.")
        return "Sebuah balok bermassa 4 kg ditarik ke atas bidang miring licin (sudut 30 derajat) dengan gaya 50 N. (g=10)"

    with open(input_file, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    print(read_problem_file())
