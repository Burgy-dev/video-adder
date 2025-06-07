from pathlib import Path

mods_root = Path("mods")

if not mods_root.exists():
    raise Exception(f"No mods directory found at: {mods_root.resolve()}")

print("🔎 Scanning for existing 'video' sections in keyframes.cfg...\n")

for mod_dir in mods_root.iterdir():
    if not mod_dir.is_dir():
        continue

    for level_dir in mod_dir.iterdir():
        if not level_dir.is_dir():
            continue

        keyframes_path = level_dir / "config" / "keyframes.cfg"
        if keyframes_path.exists():
            with open(keyframes_path, "r", encoding="utf-8") as f:
                content = f.read()
                if '"video"' in content:
                    print(f"📼 Found 'video' section in: {mod_dir.name} → {level_dir.name}")

print("\n✅ Scan complete.")
 
