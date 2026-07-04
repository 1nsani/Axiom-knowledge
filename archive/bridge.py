import json
from google import genai
from google.genai import types

def convert_to_manim_data(solver_output_text, visual_config, api_key, output_filename="anim_input.json"):
    """
    K-5 Bridge: Menerjemahkan angka hitungan ke dalam template visual dari Obsidian.
    Sistem ini agnostik. Tidak peduli bidang miring atau katrol.
    """
    if not api_key:
        return None, {"error": "API Key tidak ditemukan."}

    client = genai.Client(api_key=api_key)
    
    # Memaksa Gemini merakit JSON berdasarkan blueprint Obsidian
    blueprint_json = json.dumps(visual_config, indent=2)
    
    system_instruction = f"""
    Anda adalah mesin JSON formatter.
    Ekstrak nilai numerik dari teks solusi fisika, dan gabungkan dengan blueprint visual ini:
    
    BLUEPRINT OBSIDIAN:
    {blueprint_json}
    
    OUTPUT WAJIB BERUPA JSON DENGAN STRUKTUR INI:
    {{
        "scene_type": "<isi_dari_blueprint>",
        "parameters": {{
            "massa": <angka>,
            "percepatan": <angka>,
            "arah_gerak": "<ke_atas/ke_bawah/diam>"
        }},
        "vectors_to_render": [
            {{
                "id": "<id_dari_blueprint>",
                "type": "<type_dari_blueprint>",
                "direction_logic": "<direction_logic_dari_blueprint>",
                "color": "<color_dari_blueprint>",
                "label": "<label_dari_blueprint>"
            }}
            // ... masukkan SEMUA vektor yang ada di blueprint
        ]
    }}
    HANYA keluarkan JSON murni tanpa markdown formatter.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=solver_output_text,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.0,
                response_mime_type="application/json",
            ),
        )
        
        manim_data = json.loads(response.text)
        
        with open(output_filename, "w") as f:
            json.dump(manim_data, f, indent=4)
            
        return output_filename, manim_data
        
    except Exception as e:
        return None, {"error": f"Ekstraksi K-5 gagal: {str(e)}"}
        
