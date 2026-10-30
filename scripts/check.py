"""Read-only consistency check for courses, templates, outputs and live labs.

Usage:  python scripts/check.py

For every courses/<course>.json it verifies:
  - referenced ZoomData / Templates / Knowledge paths exist
  - every lab listed for a session has labs/<id>/index.html and is embedded
    in that session's template
  - Output/<course>_Cohort<last_generated_cohort> mentions only that cohort and
    only Zoom meetings present in the current ZoomData (no leftovers from the
    previous cohort's template)
Exits 1 if anything fails. Never writes files.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_BASE = "https://adrianaguinaga.github.io/SessionsCodes/"

problems = []


def read(path):
    with open(os.path.join(ROOT, path), "r", encoding="utf-8") as f:
        return f.read()


def session_template(templates, n):
    # Templates/106 ships session 1 with a typo in the filename.
    for name in (f"session{n}.txt", f"sesssion{n}.txt"):
        path = os.path.join(templates, name)
        if os.path.exists(os.path.join(ROOT, path)):
            return path
    return None


for manifest in sorted(glob.glob(os.path.join(ROOT, "courses", "*.json"))):
    with open(manifest, "r", encoding="utf-8") as f:
        c = json.load(f)
    course = c["course"]

    for key in ("zoom_data", "templates", "knowledge"):
        if not os.path.exists(os.path.join(ROOT, c[key])):
            problems.append(f"{course}: {key} not found: {c[key]}")

    for s in c["sessions"]:
        for lab in s["labs"]:
            if not os.path.exists(os.path.join(ROOT, "labs", lab, "index.html")):
                problems.append(f"{course} S{s['n']}: labs/{lab}/index.html missing")
            tpl = session_template(c["templates"], s["n"])
            if not tpl:
                problems.append(f"{course} S{s['n']}: no template to embed lab {lab}")
            elif f"{PAGES_BASE}{lab}/" not in read(tpl):
                problems.append(f"{course} S{s['n']}: lab {lab} not embedded in {tpl}")

    cohort = c["last_generated_cohort"]
    # Finished cohorts are archived under Output/old/.
    out_dir = next((d for d in (os.path.join("Output", f"{course}_Cohort{cohort}"),
                                os.path.join("Output", "old", f"{course}_Cohort{cohort}"))
                    if os.path.isdir(os.path.join(ROOT, d))), None)
    if not out_dir:
        out_dir = os.path.join("Output", f"{course}_Cohort{cohort}")
        problems.append(f"{course}: {out_dir} missing")
        continue
    zoom = read(c["zoom_data"])
    for path in sorted(glob.glob(os.path.join(ROOT, out_dir, "*.txt"))):
        name = os.path.relpath(path, ROOT)
        text = read(name)
        for other in sorted(set(re.findall(r"Cohort (\d+)", text)) - {cohort}):
            problems.append(f"{name}: mentions Cohort {other}")
        for meeting in sorted(set(re.findall(r"zoom\.us/j/(\d+)", text))):
            if meeting not in zoom:
                problems.append(f"{name}: Zoom meeting {meeting} not in {c['zoom_data']}")

for p in problems:
    print("FAIL", p)
print("OK" if not problems else f"{len(problems)} problem(s)")
sys.exit(1 if problems else 0)
