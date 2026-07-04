from google import genai
from google.genai import types

def execute_solver(final_prompt, api_key):
    """
    Mesin M-5: Eksekutor akhir (Modul Pasif).
    Hanya berjalan jika dipanggil oleh main.py dengan menyertakan prompt dan api_key.
    """
    try:
        # Inisialisasi client di dalam fungsi agar terisolasi dan aman
        client = genai.Client(api_key=api_key)
        
        response = client.models.generate_content(
            model='models/gemini-3.5-flash', 
            contents=final_prompt,
            config=types.GenerateContentConfig(
                temperature=0.0, # Memaksa logika absolut, bukan kreatif
            ),
        )
        return response.text
    except Exception as e:
        return f"[-] M-5 FAILED: {str(e)}"
