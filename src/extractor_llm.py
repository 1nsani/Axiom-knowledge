import json
from google import genai
from google.genai import types


def extract_parameters(problem_text: str, context_text: str,
                        required_params: list, optional_params: list,
                        scene_type: str, api_key: str) -> dict:
    if not api_key:
        raise ValueError("GEMINI_API_KEY tidak tersedia.")
    if not required_params:
        raise ValueError(
            f"required_params kosong untuk scene_type '{scene_type}'. "
            f"Tidak boleh memanggil LLM tanpa skema parameter — risiko halusinasi."
        )

    client = genai.Client(api_key=api_key)

    wajib_str = "\n".join(f'- "{p}"  (WAJIB)' for p in required_params)
    opsional_str = "\n".join(f'- "{p}"  (opsional)' for p in optional_params)

    system_prompt = f"""Anda adalah ekstraktor parameter fisika. Tugas Anda SEMPIT dan KETAT:

1. Baca soal fisika di bawah.
2. Ekstrak HANYA nilai numerik yang SECARA EKSPLISIT tertulis di soal.
3. JANGAN menghitung, menurunkan, memperkirakan, atau membulatkan nilai apapun.
4. Gunakan PERSIS nama key berikut (case-sensitive, JANGAN diterjemahkan/diubah/disingkat):

Parameter WAJIB (jika tidak ada di soal, tetap tulis apa adanya — jangan menebak):
{wajib_str}

Parameter OPSIONAL (sertakan HANYA jika disebutkan eksplisit di soal):
{opsional_str if opsional_str else "(tidak ada)"}

5. Jika sebuah parameter WAJIB tidak disebutkan di soal, JANGAN sertakan key tersebut
   di output — jangan menebak nilainya. Validasi kelengkapan akan dilakukan di luar sistem ini.
6. Gunakan satuan SI (kg, m, s, N, derajat untuk sudut).
7. Output HANYA JSON dengan struktur:
{{"known": {{"<nama_key_persis>": <angka>, ...}}}}
Tidak ada teks lain selain JSON ini.
"""

    full_prompt = (
        f"Konteks fisika (referensi rumus untuk memahami istilah, BUKAN untuk dihitung olehmu):\n"
        f"{context_text}\n\nSoal:\n{problem_text}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.0,
            response_mime_type="application/json",
        ),
    )

    try:
        data = json.loads(response.text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Output LLM bukan JSON valid: {e}\nRaw: {response.text}")

    if "known" not in data:
        raise RuntimeError("Output LLM tidak punya field 'known'.")

    hilang = [p for p in required_params if p not in data["known"]]
    if hilang:
        raise RuntimeError(
            f"Parameter wajib tidak ditemukan di soal: {hilang}. "
            f"Soal mungkin tidak lengkap, atau ekstraksi gagal. "
            f"Pipeline dihentikan untuk mencegah data cacat/halusinasi."
        )

    data["scene_type"] = scene_type
    return data
