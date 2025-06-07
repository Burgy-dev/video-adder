import re
from pathlib import Path

mod_name = "Hildaremaster"
mod_root = Path("mods") / mod_name

subfolders = [f for f in mod_root.iterdir() if f.is_dir()]
if not subfolders:
    raise Exception(f"No subfolders found in {mod_root}")

for mod_dir in subfolders:
    print(f"\n🔍 Processing: {mod_dir.name}")

    config_dir = mod_dir / "config"
    notes_path = config_dir / "notes.cfg"
    keyframes_path = config_dir / "keyframes.cfg"
    video_dir = mod_dir / "video"

    if not notes_path.exists() or not keyframes_path.exists() or not video_dir.exists():
        print(f"⚠️ Missing expected files or folders in {mod_dir}, skipping...")
        continue

    # get ogv file
    ogv_files = list(video_dir.glob("*.ogv"))
    if not ogv_files:
        print(f"⚠️ No .ogv video file found in: {video_dir}, skipping...")
        continue
    video_filename = ogv_files[0].name

    # get when the last note happens
    last_timestamp = None
    with open(notes_path, "r", encoding="utf-8") as f:
        for line in reversed(f.readlines()):
            match = re.search(r'"timestamp"\s*:\s*([0-9.]+)', line)
            if match:
                last_timestamp = float(match.group(1))
                break

    if last_timestamp is None:
        print("⚠️ Could not find a timestamp in notes.cfg, skipping...")
        continue

    # read keyframes
    with open(keyframes_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # look for closing brace
    end_brace_index = next((i for i in range(len(lines)-1, -1, -1) if lines[i].strip() == "}"), None)
    if end_brace_index is None:
        print("⚠️ Could not find closing '}' in keyframes.cfg, skipping...")
        continue

    # find the last list closing line before }
    insert_index = None
    for j in range(end_brace_index - 1, -1, -1):
        if re.search(r"\],?\s*$", lines[j].strip()):  # matches ] or ],
            if not lines[j].strip().endswith("],"):
                lines[j] = lines[j].rstrip() + ",\n"  # add comma if missing
            insert_index = j + 1
            break

    if insert_index is None:
        print("⚠️ Could not find list-closing line before '}' in keyframes.cfg, skipping...")
        continue

    # shove the video in there
    video_block = f'"video": [{{\n"path": "{video_filename}",\n"timestamp": {last_timestamp}\n}}]\n'
    lines.insert(insert_index, video_block)

    # write it back to the file
    with open(keyframes_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"✅ Inserted video section for {video_filename} at timestamp {last_timestamp} in {mod_dir.name}")
