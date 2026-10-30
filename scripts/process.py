"""Generate Canvas material (session pages + announcements + email) for a cohort.

Usage:  python scripts/process.py --course 106 --cohort 70

Reads   ZoomData/<course>.md          (Zoom invitations pasted as-is)
        Templates/<course>/*.txt      (previous cohort's Canvas HTML)
Writes  Output/<course>_Cohort<n>/*.txt
        EmailTemplates/<course>_Cohort<n>_Email.txt
"""
import argparse
import os
import re
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

parser = argparse.ArgumentParser()
parser.add_argument("--course", required=True)
parser.add_argument("--cohort", required=True)
args = parser.parse_args()
course, cohort = args.course, args.cohort

zoom_data_file = os.path.join(ROOT, "ZoomData", f"{course}.md")
templates_dir = os.path.join(ROOT, "Templates", course)
output_dir = os.path.join(ROOT, "Output", f"{course}_Cohort{cohort}")
email_out = os.path.join(ROOT, "EmailTemplates", f"{course}_Cohort{cohort}_Email.txt")

with open(zoom_data_file, "r", encoding="utf-8") as f:
    # Invitations copied as Markdown arrive escaped ("https\://", "\&", "\-").
    zoom_text = re.sub(r"\\([^\w\s])", r"\1", f.read())

sessions = []
for part in zoom_text.split("Topic: ")[1:]:
    s = {}
    time_m = re.search(r"Time:\s*(.*?)(?=\n|\r)", part)
    link_m = re.search(r"https://us02web\.zoom\.us/j/.*?(?=\n|\r|\s)", part)
    chat_m = re.search(r"https://us02web\.zoom\.us/launch/jc/.*?(?=\n|\r|\s)", part)
    insights_m = re.search(r"https://us02web\.zoom\.us/launch/edl\?muid=.*?(?=\n|\r|\s)", part)
    id_m = re.search(r"Meeting ID:\s*(.*?)(?=\n|\r)", part)
    pwd_m = re.search(r"Passcode:\s*(.*?)(?=\n|\r)", part)

    if time_m: s["time"] = time_m.group(1).strip()
    if link_m: s["link"] = link_m.group(0).strip()
    if chat_m: s["chat"] = chat_m.group(0).strip()
    if insights_m: s["insights"] = insights_m.group(0).strip()
    if id_m: s["id"] = id_m.group(1).strip()
    if pwd_m: s["passcode"] = pwd_m.group(1).strip()

    date_str = re.sub(r" Pacific Time.*", "", s["time"]).strip()
    try:
        dt = datetime.strptime(date_str, "%b %d, %Y %I:%M %p")
        # "Saturday, August 22, 2026 &mdash; 9:00 AM Pacific Time (US &amp; Canada)"
        s["time_full"] = "{} &mdash; {} Pacific Time (US &amp; Canada)".format(
            dt.strftime("%A, %B %d, %Y").replace(" 0", " "),
            dt.strftime("%I:%M %p").lstrip("0"),
        )
        # "Sat, Aug 22, 2026 @ 9:00 AM PT"
        s["time_ann"] = "{} @ {} PT".format(
            dt.strftime("%a, %b %d, %Y").replace(" 0", " "),
            dt.strftime("%I:%M %p").lstrip("0"),
        )
    except ValueError as e:
        print("Date parse error:", e)
        s["time_full"] = s["time_ann"] = s["time"]

    sessions.append(s)

os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.dirname(email_out), exist_ok=True)

# --- Session pages -----------------------------------------------------------
for i, session in enumerate(sessions):
    n = i + 1
    # Templates/106 ships session 1 with a typo in the filename.
    template_path = next(
        (p for p in (os.path.join(templates_dir, f"session{n}.txt"),
                     os.path.join(templates_dir, f"sesssion{n}.txt"))
         if os.path.exists(p)), None)
    if not template_path:
        print(f"No template for session {n}, skipping")
        continue

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(r"Cohort \d+", f"Cohort {cohort}", content)
    # 107-style list markup
    content = re.sub(r"⏰ <strong>Time:</strong>.*?</li>", f'⏰ <strong>Time:</strong> {session["time"]}</li>', content)
    content = re.sub(r"🔑 <strong>Meeting ID:</strong>.*?</li>", f'🔑 <strong>Meeting ID:</strong> {session["id"]}</li>', content)
    content = re.sub(r"🔐 <strong>Passcode:</strong>.*?</li>", f'🔐 <strong>Passcode:</strong> {session["passcode"]}</li>', content)
    # 106-style hero date + monospace table
    content = re.sub(r"📅 [^<]*?Pacific Time \(US &amp; Canada\)", f'📅 {session["time_full"]}', content)
    content = re.sub(r">\d{3} \d{4} \d{4}<", f'>{session["id"]}<', content)
    content = re.sub(r">\d{6}<", f'>{session["passcode"]}<', content)
    # Links (both styles)
    content = re.sub(r'href="https://us02web\.zoom\.us/j/[^"]+"', f'href="{session["link"]}"', content)
    if "chat" in session:
        content = re.sub(r'href="https://us02web\.zoom\.us/launch/jc/[^"]+"', f'href="{session["chat"]}"', content)
    if "insights" in session:
        content = re.sub(r'href="https://us02web\.zoom\.us/launch/edl\?muid=[^"]+"', f'href="{session["insights"]}"', content)

    with open(os.path.join(output_dir, f"session{n}.txt"), "w", encoding="utf-8") as f:
        f.write(content)

# --- Announcements -----------------------------------------------------------
ann_path = os.path.join(templates_dir, "announcements.txt")
if os.path.exists(ann_path):
    with open(ann_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(r"Cohort \d+", f"Cohort {cohort}", content)

    links = [s["link"] for s in sessions]
    passcodes = [s["passcode"] for s in sessions]
    dates = [s["time_ann"] for s in sessions]

    def pop_into(values, template):
        def repl(m):
            return template.format(values.pop(0)) if values else m.group(0)
        return repl

    content = re.sub(r"📅 (Mon|Tue|Wed|Thu|Fri|Sat|Sun)[^<]+</span>", pop_into(dates, "📅 {}</span>"), content)
    content = re.sub(r'href="https://us02web\.zoom\.us/j/[^"]+"', pop_into(links, 'href="{}"'), content)
    content = re.sub(r">\d{6}<", pop_into(passcodes, ">{}<"), content)
    # Recordings and repo start the cohort empty.
    content = re.sub(r'<a href="https://us02web\.zoom\.us/rec/share/[^"]+">\s*([^<]*)</a>', "Pending", content)
    content = re.sub(r'<a href="https://github\.com/[^"]+">\s*([^<]*)</a>', "Pending", content)
    content = re.sub(r'https://github\.com/[^/]+/[^"]+\.git', "Pending", content)

    with open(os.path.join(output_dir, "announcements.txt"), "w", encoding="utf-8") as f:
        f.write(content)

# --- Email -------------------------------------------------------------------
email = f"""Subject: Zoom Details for Cohort {cohort} - Course {course}

Hello everyone,

Welcome to the FSDI {course} course! Below you will find the Zoom details for our upcoming live sessions.

"""
for i, session in enumerate(sessions):
    email += f"""Session {i+1}:
Date/Time: {session.get('time', 'N/A')}
Zoom Link: {session.get('link', 'N/A')}
Meeting ID: {session.get('id', 'N/A')}
Passcode: {session.get('passcode', 'N/A')}

"""
email += """Please keep this email for your records. The session recordings and the code repository will be shared in Canvas once they are available.

Best regards,
Adrian Aguinaga
"""

with open(email_out, "w", encoding="utf-8") as f:
    f.write(email)

print(f"Done generating output for {course} Cohort {cohort} ({len(sessions)} sessions)")
