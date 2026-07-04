import os
import sys

from src.reader import read_problem_file
from src.analyzer import analyze_physics_problem
from src.retriever import retrieve_knowledge
from src.extractor_llm import extract_parameters
from src.bridge_export import export_known_parameters


def main():
    print("[SYSTEM] Axiom Knowledge Brain")

    problem_text = read_problem_file()
    print(f"[+] Soal: {problem_text[:120]}...")

    m2_data = analyze_physics_problem(problem_text)
    scene_type = m2_data["domain"]
    print(f"[+] Domain terdeteksi: {scene_type}")

    metadata_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metadata")

    try:
        konteks_fisika, visual_hooks, required_params, optional_params = retrieve_knowledge(
            m2_data, repo_path=metadata_path
        )
    except RuntimeError as e:
        print(f"[-] FATAL: {e}")
        sys.exit(1)

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[-] FATAL: GEMINI_API_KEY tidak ditemukan di environment.")
        sys.exit(1)

    try:
        extracted = extract_parameters(
            problem_text, konteks_fisika, required_params, optional_params, scene_type, api_key
        )
    except (RuntimeError, ValueError) as e:
        print(f"[-] FATAL ekstraksi: {e}")
        sys.exit(1)

    export_known_parameters(scene_type, extracted["known"], visual_hooks)
    print("[SYSTEM] Selesai.")


if __name__ == "__main__":
    main()
