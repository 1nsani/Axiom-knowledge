import json
import os

def export_known_parameters(data, shared_dir="/content/drive/MyDrive/axiom_shared"):
    os.makedirs(shared_dir, exist_ok=True)
    output_path = os.path.join(shared_dir, "known_parameters.json")
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] known_parameters.json ditulis ke {output_path}")
    return output_path
