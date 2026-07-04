import os
import json
import sys
from google import genai
from google.genai import types

def extract_parameters(problem_text, context_text, visual_hooks, required_params, scene_type, api_key):
    if not api_key:
        raise ValueError("GEMINI_API_KEY tidak tersedia.")
    client = genai.Client(api_key=api_key)
    params_str = ", ".join(required_params)
    system_prompt = f"""
Anda adalah ekstraktor parameter fisika. 
Baca soal dan ekstrak nilai numerik untuk parameter yang diminta.
Jangan menghitung, menebak, atau menambahkan nilai yang tidak ada di soal.

Parameter yang WAJIB diekstrak (jika ada di soal):
{params_str}

Output harus berupa JSON dengan format:
{{
  "known": {{
    "nama_parameter": nilai,
    ...
  }}
}}
Hanya masukkan parameter yang benar-benar disebutkan dalam soal.
Gunakan satuan SI (kg, m, s, N, rad).
"""
    full_prompt = f"""
Konteks fisika (hanya sebagai panduan, bukan untuk menghitung):
{context_text}

Soal:
{problem_text}

Catatan: scene_type sudah ditentukan sebagai "{scene_type}", jangan ubah.
"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=full_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.0,
                response_mime_type="application/json",
            )
        )
        data = json.loads(response.text)
        if "known" not in data:
            raise ValueError("Output AI tidak memiliki field 'known'.")
        data["scene_type"] = scene_type
        data["visual_hooks"] = visual_hooks if visual_hooks else {}
        return data
    except Exception as e:
        raise RuntimeError(f"Ekstraksi gagal: {e}")
