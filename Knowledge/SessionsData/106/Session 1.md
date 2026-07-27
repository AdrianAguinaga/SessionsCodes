# 📅 Session 1: Architecture, Models & Styles

Duration: 3 Hours

Goal: Setup the project, apply professional styles using CSS Grid, and
create the JavaScript Data Model.

### Part 1.1: Visualizing the Project Structure

Start by explaining to the students that we are moving away from writing
everything in a single file. We are separating concerns.

The Architecture Tree (Text Visual):

Use this diagram to show where files live.

> Plaintext

📁 TaskManager/ \<\-- Root Folder\
│\
├── 📄 index.html (The Skeleton: Structure)\
│\
├── 📁 style/ (The Skin: Visuals)\
│ └── 📄 app.css\
│\
└── 📁 scripts/ (The Brains: Logic & Data)\
├── 📄 task.js \<\-- Data Model (Class)\
└── 📄 app.js \<\-- Controller (Logic)

**Activity:** Have students create this folder structure and empty files
in VS Code.

### Part 1.2: The Skeleton (HTML) & The DOM

Before pasting the code, explain the **Document Object Model (DOM)**
using the HTML structure.

**Concept:** The browser reads the HTML and builds a tree of objects. We
will later use jQuery to \"climb\" this tree.

Code to Share (index.html):

Key points to highlight:

- The \<link\> to our CSS file.

- The \<script\> tags at the bottom (jQuery first, then our scripts).

- The id attributes (e.g., txtTitle), which act as \"hooks\" for us to
  grab these elements later.

HTML

\<!doctype **html**\>\
\<html lang=\"en\"\>\
\<head\>\
\<meta charset=\"utf-8\" /\>\
\<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"
/\>\
\<title\>My Task Manager\</title\>\
\<link rel=\"stylesheet\" href=\"/style/app.css\" /\>\
\</head\>\
\<body\>\
\<header\>\
\<h1\>My Tasks\</h1\>\
\<p\>A simple task manager application\</p\>\
\</header\>\
\
\<main\>\
\<section class=\"card\"\>\
\<h2\>New Task\</h2\>\
\<form id=\"taskForm\"\>\
\<div class=\"form-grid\"\>\
\<label\>Title \<input id=\"txtTitle\" required placeholder=\"Pay the
bills\" /\>\</label\>\
\<label\>Description \<input id=\"txtDescription\"
placeholder=\"Electricity and water\" /\>\</label\>\
\<label\>Color \<input id=\"selColor\" type=\"color\" value=\"#ffcc00\"
/\>\</label\>\
\<label\>Date \<input id=\"selDate\" type=\"date\" /\>\</label\>\
\<label\>Status\
\<select id=\"selStatus\"\>\
\<option value=\"New\"\>New\</option\>\
\<option value=\"In Progress\"\>In Progress\</option\>\
\<option value=\"Completed\"\>Completed\</option\>\
\</select\>\
\</label\>\
\<label\>Budget \<input id=\"numBudget\" type=\"number\" step=\"0.01\"
placeholder=\"100.00\" /\>\</label\>\
\</div\>\
\<button type=\"button\" id=\"btnSave\"\>Save Task\</button\>\
\</form\>\
\</section\>\
\
\<section class=\"card\"\>\
\<h2\>Task List\</h2\>\
\<div id=\"list\" class=\"list\"\>\</div\>\
\</section\>\
\</main\>\
\
\<script
src=\"https://code.jquery.com/jquery-3.7.1.min.js\"\>\</script\>\
\<script src=\"/scripts/task.js\"\>\</script\>\
\<script src=\"/scripts/app.js\"\>\</script\>\
\</body\>\
\</html\>

### Part 1.3: \"Simple but Elegant\" CSS

Now we style the skeleton. We want a modern \"Material Design\" look
without using heavy libraries like Bootstrap.

Visual Concept: The Card Metaphor

Explain that we use shadows and borders to mimic physical cards on a
desk.

> Plaintext

┌──────────────────────────────┐ \<\-- .card\
│ Shadow: 0 4px 8px (Depth) │\
│ Radius: 8px (Soft Corners) │\
│ │\
│ \[ Input \] \[ Input \] │ \<\-- .form-grid\
│ \[ Input \] \[ Input \] │ (Auto-responsive)\
│ │\
└──────────────────────────────┘

Code to Share (style/app.css):

Key points to highlight:

- box-shadow: Creates the 3D lifting effect.

- .form-grid: Uses repeat(auto-fit, minmax(200px, 1fr)) which
  automatically makes the form responsive on mobile without writing
  media queries.

> CSS

body {\
font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto,
Helvetica, Arial, sans-serif;\
background-color: #f4f7f9; /\* Soft background \*/\
color: #333;\
margin: 0;\
padding: 20px;\
}\
\
/\* The Card Container \*/\
.card {\
background-color: #ffffff;\
border-radius: 8px;\
box-shadow: 0 4px 8px rgba(0,0,0,0.1);\
padding: 20px;\
margin-bottom: 20px;\
}\
\
/\* Modern Responsive Grid \*/\
.form-grid {\
display: grid;\
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\
gap: 15px;\
margin-bottom: 20px;\
}\
\
input, select, button {\
padding: 10px;\
border: 1px solid #ccc;\
border-radius: 4px;\
font-size: 1em;\
margin-top: 5px;\
}\
\
button {\
background-color: #303f9f;\
color: white;\
border: none;\
cursor: pointer;\
transition: background-color 0.3s;\
}\
\
button:hover {\
background-color: #1a237e;\
}

### Part 1.4: The Data Model (DNA)

We don\'t want to pass loose variables around. We create a blueprint for
what a \"Task\" looks like using a JavaScript Class.

**Code to Share (scripts/task.js):**

> JavaScript

class Task {\
constructor (title, description, color, date, status, budget) {\
this.title = title;\
this.desc = description; // Note: mapped to \'desc\' internally\
this.color = color;\
this.date = date;\
this.status = status;\
this.budget = budget;\
}\
}

### Part 1.5: Initialization

Finally, we ensure our logic starts only when the browser is ready.

**Code to Share (scripts/app.js):**

> JavaScript

function init(){\
console.log(\"App initialized\");\
// We will attach events here in the next session\
}\
\
window.onload = init;

### ✅ Session 1 Checklist

By the end of this session, students should have:

1.  A beautiful UI rendering in the browser (Inputs inside a white card
    on a gray background).

2.  No errors in the Chrome Console.

3.  The text \"App initialized\" visible in the Console.

**Ready for Session 2 (DOM Manipulation & GET Requests)?**
