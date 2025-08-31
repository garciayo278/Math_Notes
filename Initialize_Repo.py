import os

# Base path (change if needed)
base_path = r"C:\Users\garci\Math_Notes"

# Folder structure (relative to base_path)
folders = [
    "notes/raw/geometry_analysis",
    "notes/raw/computational_math",
    "notes/processed/html",
    "notes/processed/pdf",
    "scripts",
    ".github/workflows"
]

def create_structure(base, folders):
    for folder in folders:
        path = os.path.join(base, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")

if __name__ == "__main__":
    create_structure(base_path, folders)
    print("\n✅ Folder structure ready at:", base_path)