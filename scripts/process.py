import re
import os
from datetime import datetime

zoom_data_file = r"C:\SDGKU\SessionsCodes\ZoomData\107.md"
templates_dir = r"C:\SDGKU\SessionsCodes\Templates\107"
output_dir = r"C:\SDGKU\SessionsCodes\Output\107_Cohort69"
email_out = r"C:\SDGKU\SessionsCodes\EmailTemplates\107_Cohort69_Email.txt"

with open(zoom_data_file, 'r', encoding='utf-8') as f:
    zoom_text = f.read()

sessions = []
parts = zoom_text.split("Topic: ")[1:]
for part in parts:
    s = {}
    time_m = re.search(r"Time:\s*(.*?)(?=\n\n|\r\n\r\n|\n|\r)", part)
    link_m = re.search(r"https://us02web\.zoom\.us/j/.*?(?=\n|\r|\s)", part)
    chat_m = re.search(r"https://us02web\.zoom\.us/launch/jc/.*?(?=\n|\r|\s)", part)
    insights_m = re.search(r"https://us02web\.zoom\.us/launch/edl\?muid=.*?(?=\n|\r|\s)", part)
    id_m = re.search(r"Meeting ID:\s*(.*?)(?=\n|\r)", part)
    pwd_m = re.search(r"Passcode:\s*(.*?)(?=\n|\r)", part)

    if time_m: s['time'] = time_m.group(1).strip()
    if link_m: s['link'] = link_m.group(0).strip()
    if chat_m: s['chat'] = chat_m.group(0).strip()
    if insights_m: s['insights'] = insights_m.group(0).strip()
    if id_m: s['id'] = id_m.group(1).strip()
    if pwd_m: s['passcode'] = pwd_m.group(1).strip()
    
    date_str = re.sub(r' Pacific Time.*', '', s['time']).strip()
    try:
        dt = datetime.strptime(date_str, "%b %d, %Y %I:%M %p")
        s['time_session'] = s['time'] 
        s['time_ann'] = dt.strftime("%a, %b %d, %Y @ %I:%M %p PT").replace(' 0', ' ')
    except Exception as e:
        print("Date parse error:", e)
        s['time_session'] = s['time']
        s['time_ann'] = s['time']
    
    sessions.append(s)

cohort = "69"
course = "107"

os.makedirs(output_dir, exist_ok=True)
os.makedirs(r"C:\SDGKU\SessionsCodes\EmailTemplates", exist_ok=True)

# 2. Update Templates
for i, session in enumerate(sessions):
    session_num = i + 1
    template_path = os.path.join(templates_dir, f"session{session_num}.txt")
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'Cohort \d+', f'Cohort {cohort}', content)
        content = re.sub(r'⏰ <strong>Time:</strong>.*?</li>', f'⏰ <strong>Time:</strong> {session["time"]}</li>', content)
        content = re.sub(r'🔑 <strong>Meeting ID:</strong>.*?</li>', f'🔑 <strong>Meeting ID:</strong> {session["id"]}</li>', content)
        content = re.sub(r'🔐 <strong>Passcode:</strong>.*?</li>', f'🔐 <strong>Passcode:</strong> {session["passcode"]}</li>', content)
        content = re.sub(r'href="https://us02web\.zoom\.us/j/[^"]+"', f'href="{session["link"]}"', content)
        if 'chat' in session:
            content = re.sub(r'href="https://us02web\.zoom\.us/launch/jc/[^"]+"', f'href="{session["chat"]}"', content)
        if 'insights' in session:
            content = re.sub(r'href="https://us02web\.zoom\.us/launch/edl\?muid=[^"]+"', f'href="{session["insights"]}"', content)

        out_path = os.path.join(output_dir, f"session{session_num}.txt")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Update announcements
ann_path = os.path.join(templates_dir, "announcements.txt")
if os.path.exists(ann_path):
    with open(ann_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'Cohort \d+', f'Cohort {cohort}', content)
    content = re.sub(r'https://github\.com/[^/]+/[^"]+\.git', 'Pending', content)
    
    links = [s['link'] for s in sessions]
    passcodes = [s['passcode'] for s in sessions]
    dates = [s['time_ann'] for s in sessions]
    
    def repl_link(m):
        if links: return f'href="{links.pop(0)}"'
        return m.group(0)
    
    def repl_pass(m):
        if passcodes: return f'>{passcodes.pop(0)}<'
        return m.group(0)

    def repl_date(m):
        # We only want to replace dates in the table. The table rows have dates starting with 📅 <Day>
        if dates: return f'📅 {dates.pop(0)}</span>'
        return m.group(0)

    # replace dates but carefully avoiding "4 Sessions". The regex for dates in the table: 📅 [A-Z][a-z]{2}, [A-Z][a-z]{2} \d{1,2}, \d{4} @ \d{1,2}:\d{2} [AP]M PT
    content = re.sub(r'📅 (Mon|Tue|Wed|Thu|Fri|Sat|Sun)[^<]+</span>', repl_date, content)
    
    content = re.sub(r'href="https://us02web\.zoom\.us/j/[^"]+"', repl_link, content)
    content = re.sub(r'>\d{6}<', repl_pass, content)
    content = re.sub(r'<a href="https://us02web\.zoom\.us/rec/share/[^"]+">[^<]+</a>', 'Pending', content)
    
    out_path = os.path.join(output_dir, "announcements.txt")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)


# 3. Create Email
email_content = f"""Subject: Zoom Details for Cohort {cohort} - Course {course}

Hello everyone,

Welcome to the FSDI {course} course! Below you will find the Zoom details for our upcoming live sessions.

"""

for i, session in enumerate(sessions):
    email_content += f"""Session {i+1}:
Date/Time: {session.get('time', 'N/A')}
Zoom Link: {session.get('link', 'N/A')}
Meeting ID: {session.get('id', 'N/A')}
Passcode: {session.get('passcode', 'N/A')}

"""

email_content += """Please keep this email for your records. The session recordings and the code repository will be shared in Canva once they are available.

Best regards,
Adrian Aguinaga
"""

with open(email_out, 'w', encoding='utf-8') as f:
    f.write(email_content)

print("Done generating output for 107 Cohort 69")
