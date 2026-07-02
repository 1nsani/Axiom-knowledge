import json
import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# Skema Kontrak Baku
# Jika repo 'axiom' (Manim) butuh variabel lain, tambahkan HANYA di sini.
class ManimPhysicsData(BaseModel):
    massa: float = Field(description="Massa objek dalam kg")
    sudut_kemiringan: float = Field(description="Sudut bidang miring dalam derajat")
    gaya_tarik: float = Field(description="Gaya eksternal yang menarik objek dalam Newton")
    percepatan: float = Field(description="Hasil akhir percepatan dalam m/s^2")
    arah_gerak: str = Field(description="Arah pergerakan: 'ke_atas', 'ke_bawah', atau 'diam'")

def convert_to_manim_data(solver_output_text, api_key, output_filename="anim_input.json"):
    """
    M-6 Bridge: Memaksa teks dinamis menjadi data statis (JSON).
    File JSON ini adalah satu-satunya bentuk komunikasi dengan repo 'axiom'.
    """
    if not api_key:
        return None, {"error": "API Key tidak ditemukan."}

    client = genai.Client(api_key=api_key)
    
    system_instruction = """
    Anda adalah ekstraktor data deterministik. 
    Baca solusi fisika yang diberikan dan ekstrak nilai numeriknya ke dalam format JSON.
    Hanya ekstrak angkanya, jangan sertakan satuannya.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=solver_output_text,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.0,
                response_mime_type="application/json",
                response_schema=ManimPhysicsData,
            ),
        )
        
        manim_data = json.loads(response.text)
        
        # Eksekusi I/O: Menulis file ke disk
        # File ini akan terbuat di direktori di mana skrip utama (main.py) dijalankan
        with open(output_filename, "w") as f:
            json.dump(manim_data, f, indent=4)
            
        return output_filename, manim_data
        
    except Exception as e:
        return None, {"error": f"Ekstraksi M-6 gagal: {str(e)}"}
