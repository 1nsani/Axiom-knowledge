import json, os

def export_known_parameters(scene_type: str, known: dict, visual_hooks: dict,
                             shared_dir: str = "/tmp/axiom_shared",
                             problem_mode: str = None) -> str:
    payload = {
        "scene_type": scene_type,
        "known": known,
        "visual_hooks": visual_hooks,
    }
    if problem_mode:
        payload["problem_mode"] = problem_mode
    os.makedirs(shared_dir, exist_ok=True)
    output_path = os.path.join(shared_dir, "known_parameters.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=4, ensure_ascii=False)
    print(f"[+] known_parameters.json ditulis ke {output_path}")
    return output_path
