import re
from pathlib import Path

# Mods to skip because they already have video sections
SKIP_MODS = {

}

mods_root = Path("mods")

if not mods_root.exists():
    raise Exception(f"No 'mods' directory found at: {mods_root.resolve()}")

print("🔁 Processing all mods (except known ones with video sections)...\n")

for mod_dir in mods_root.iterdir():
    if not mod_dir.is_dir() or mod_dir.name in SKIP_MODS:
        continue

    print(f"📂 Mod: {mod_dir.name}")

    subfolders = [f for f in mod_dir.iterdir() if f.is_dir()]
    if not subfolders:
        print(f"❌ No subfolders found in {mod_dir}, skipping...")
        continue

    for level_dir in subfolders:
        print(f"  ➤ Processing level: {level_dir.name}")

        try:
            config_dir = level_dir / "config"
            notes_path = config_dir / "notes.cfg"
            keyframes_path = config_dir / "keyframes.cfg"
            video_dir = level_dir / "video"

            if not notes_path.exists():
                print(f"    ⚠️ Missing notes.cfg in {config_dir}")
                continue
            if not keyframes_path.exists():
                print(f"    ⚠️ Missing keyframes.cfg in {config_dir}")
                continue
            if not video_dir.exists():
                print(f"    ⚠️ Missing video folder in {level_dir}")
                continue

            ogv_files = list(video_dir.glob("*.ogv"))

            if not ogv_files:
                # Check if the folder has other video-like files
                other_files = list(video_dir.glob("*"))
                if other_files:
                    print(f"    ❗ ERROR: NO .OGV FILE FOUND BUT OTHER FILES EXIST IN {video_dir}")
                else:
                    print(f"    ❌ No .ogv file found in {video_dir}")
                continue

            video_filename = ogv_files[0].name

            # Get the last timestamp from notes.cfg
            last_timestamp = None
            with open(notes_path, "r", encoding="utf-8") as f:
                for line in reversed(f.readlines()):
                    match = re.search(r'"timestamp"\s*:\s*([0-9.]+)', line)
                    if match:
                        last_timestamp = float(match.group(1))
                        break

            if last_timestamp is None:
                print(f"    ❌ Could not find timestamp in notes.cfg")
                continue

            # Read keyframes.cfg
            with open(keyframes_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Find where to insert
            end_brace_index = next((i for i in range(len(lines)-1, -1, -1) if lines[i].strip() == "}"), None)
            if end_brace_index is None:
                print(f"    ❌ No closing brace in keyframes.cfg")
                continue

            insert_index = None
            for j in range(end_brace_index - 1, -1, -1):
                if re.search(r"\],?\s*$", lines[j].strip()):
                    if not lines[j].strip().endswith("],"):
                        lines[j] = lines[j].rstrip() + ",\n"
                    insert_index = j + 1
                    break

            if insert_index is None:
                print(f"    ❌ Could not find insert location in keyframes.cfg")
                continue

            # Insert video section
            video_block = f'"video": [{{\n"path": "{video_filename}",\n"timestamp": {last_timestamp}\n}}]\n'
            lines.insert(insert_index, video_block)

            with open(keyframes_path, "w", encoding="utf-8") as f:
                f.writelines(lines)

            print(f"    ✅ Inserted video section for {video_filename} at timestamp {last_timestamp}")

        except Exception as e:
            print(f"    ❌ Exception while processing {level_dir.name}: {e}")

print("\n✅ Done.")
 
