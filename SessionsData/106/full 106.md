# 🎓 Workshop: Full Stack Logic with jQuery & Azure Functions

Total Duration: 12 Hours (4 Sessions x 3 Hours)

Goal: Build a professional \"Task Manager\" application, moving from
static HTML to a dynamic, cloud-connected Full Stack application.

## 📅 Session 1: Architecture, Models & Styles

**Goal:** Setup the project structure, apply professional CSS design,
and create the Data Model.

### 1.1 Project Structure (Visual)

We define the \"Skeleton, Skin, and Brains\" of our application.

> Plaintext

📁 TaskManager/\
│\
├── 📄 index.html (The Skeleton - Structure)\
│\
├── 📁 style/\
│ └── 📄 app.css (The Skin - Visuals & Layout)\
│\
└── 📁 scripts/\
├── 📄 task.js (The DNA - Data Model)\
└── 📄 app.js (The Brains - Logic)

### 1.2 \"Simple but Elegant\" CSS

We use CSS Grid and shadows to create a modern \"Card\" interface.

**Code to Share (style/app.css):**

> CSS

body {\
font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto,
sans-serif;\
background-color: #f4f7f9; /\* Soft Gray Background \*/\
color: #333;\
padding: 20px;\
}\
\
.card {\
background-color: #ffffff;\
border-radius: 8px; /\* Smooth corners \*/\
box-shadow: 0 4px 8px rgba(0,0,0,0.1); /\* \"Floating\" effect \*/\
padding: 20px;\
margin-bottom: 20px;\
}\
\
/\* CSS Grid for Responsive Forms - No Media Queries needed! \*/\
.form-grid {\
display: grid;\
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\
gap: 15px;\
}\
\
.task {\
border-left: 5px solid #ffcc00; /\* Visual Status Indicator \*/\
display: flex;\
justify-content: space-between;\
align-items: center;\
/\* \... additional task styles \... \*/\
}

### 1.3 The Data Model (Class)

We define the blueprint for our data to ensure consistency.

**Code to Share (scripts/task.js):**

> JavaScript

class Task {\
constructor (title, description, color, date, status, budget) {\
this.title = title;\
this.desc = description;\
this.color = color;\
this.date = date;\
this.status = status;\
this.budget = budget;\
}\
}

## 📅 Session 2: The DOM, Events & Reading Data (GET)

**Goal:** Master DOM manipulation, capture user input, and fetch data
from the server.

### 2.1 Understanding the DOM (Visual)

Before coding, visualize the tree structure we are about to manipulate.

> Plaintext

🌳 THE DOM TREE (Document Object Model)\
=======================================\
\
\[ window \]\
│\
\[ document \]\
│\
\< html \>\
/ \\\
\<head\> \<body\>\
│\
┌─────────┼──────────────┐\
\<header\> \<main\> \<footer\>\
│\
\<section .card\>\
│\
\<div id=\"list\"\> ◄── jquery target: \$(\"#list\")\
│ We will APPEND children here\
├─ \<div .task\>\
└─ \<div .task\>

### 2.2 Capturing Input & Rendering

**Code to Share (scripts/app.js):**

> JavaScript

// Capturing input and creating an Object\
function saveTask() {\
const title = \$(\"#txtTitle\").val();\
const desc = \$(\"#txtDescription\").val();\
const color = \$(\"#selColor\").val();\
const date = \$(\"#selDate\").val();\
const status = \$(\"#selStatus\").val();\
const budget = \$(\"#numBudget\").val();\
\
const data = new Task(title, desc, color, date, status, budget);\
console.log(data); // Verify the object structure\
}\
\
// Rendering HTML using Template Literals\
function displayTask(task){\
const syntax = \`\
\<div class=\"task\" style=\"border-color:\${task.color}\"\>\
\<div class=\"info\"\>\
\<h4\>\${task.title}\</h4\>\
\<p\>\${task.desc}\</p\>\
\</div\>\
\<label class=\"status\"\>\${task.status}\</label\>\
\<div class=\"date-budget\"\>\
\<label\>Due: \${task.date}\</label\>\
\<label\>Budget: \$\${task.budget}\</label\>\
\</div\>\
\</div\>\`;\
\
\$(\".list\").append(syntax); // Add to the DOM Tree\
}

### 2.3 Fetching Data (AJAX GET)

**Code to Share (scripts/app.js):**

> JavaScript

const API =
\"https://106api-b0bnggbsgnezbzcz.westus3-01.azurewebsites.net/api/tasks\";\
\
function loadTasks(){\
\$.ajax({\
type: \"GET\",\
url: API,\
dataType: \"json\",\
success: function (tasks){\
\$(\".list\").empty(); // Clear old branches\
tasks.forEach(displayTask); // Create new branches for each task\
},\
error: function (err){\
console.error(\"GET error:\", err);\
}\
});\
}

## 📅 Session 3: Client-Server Communication (POST)

**Goal:** Send data to the Azure Function, understand JSON
Serialization, and handle server logic.

### 3.1 The Data Serialization Journey (Visual)

Explain the transformation of data from Client to Server.

> Plaintext

🔄 THE DATA SERIALIZATION JOURNEY\
=================================\
\
Browser (Client) Cloud (Azure Server)\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\
1. JS Object (RAM)\
{ title: \"Work\" }\
│\
▼\
2. JSON.stringify() ─── \[SERIALIZATION\]\
│\
▼\
3. JSON String ─────── \[ TRANSPORT \] ─────────▶ 4. Receive String\
\'{\"title\":\"Work\"}\' (HTTP POST) │\
▼\
5. JSON.parse()\
│\
▼\
Receipt (201 Created) ◀────── \[ RESPONSE \] ──── 6. JS Object + ID\
{ id: 99, \... } { id: 99, title: \"Work\"}

### 3.2 Implementing POST

**Code to Share (scripts/app.js):**

> JavaScript

function saveTask() {\
// \... (capture data logic) \...\
\
// Send data to server\
\$.ajax({\
type: \"POST\", // CREATE action\
url: API,\
data: JSON.stringify(data), // Step 2 in diagram\
contentType: \"application/json\", // Step 3 in diagram\
success: function(created){\
console.log(\"CREATED:\", created);\
displayTask(created); // Update screen with Server Data (contains ID)\
clearForm();\
},\
error: function(err){\
console.error(\"POST error:\", err.responseText \|\| err);\
alert(\"Task could not be saved.\");\
}\
});\
}

### 3.3 Server Logic Analysis

**Explanation:** The Azure Function receives the POST, assigns a unique
id using NEXT_ID++, adds it to the DB array using unshift, and returns
status 201.

## 📅 Session 4: Deletion & Advanced Logic

**Goal:** Implement Deletion, Client-Side Filtering, and understand
Event Delegation.

### 4.1 Event Delegation (Visual)

Why \$(\".btn-delete\").click() fails on dynamic elements.

> Plaintext

📡 EVENT DELEGATION VISUALIZED\
==============================\
\
USER CLICKS HERE ▼ (Trash Icon)\
\
\[ Trash Icon \] \-\--\> Does it have a listener? NO.\
│\
▼ (Bubbles Up)\
│\
\[ Task Div \] \-\--\> Does it have a listener? NO.\
│\
▼ (Bubbles Up)\
│\
\[ List Div \] \-\--\> YES! \"Listener: .on(\'click\',
\'.btn-delete\')\"\
│ Action: Check if source was \'.btn-delete\'.\
│ Result: EXECUTE deleteTask()

### 4.2 Implementing Delete

**Code to Share (scripts/app.js):**

1.  **Update Template:** Add the ID and Button.\
    JavaScript\
    // Inside displayTask:\
    // \<div class=\"task\" id=\"\${task.id}\"\> \... \<button
    class=\"btn-delete\"\>🗑️\</button\> \... \</div\>

2.  **Logic:**\
    JavaScript\
    function deleteTask() {\
    let taskDiv = \$(this).parents(\".task\");\
    let id = taskDiv.attr(\"id\");\
    \
    \$.ajax({\
    type: \"DELETE\",\
    url: API + \"/\" + id,\
    success: function() {\
    taskDiv.fadeOut(500, function(){ \$(this).remove(); });\
    }\
    });\
    }\
    \
    function init() {\
    // Event Delegation Registration\
    \$(\".list\").on(\"click\", \".btn-delete\", deleteTask);\
    }

### 4.3 Client-Side Filtering

**Code to Share (scripts/app.js):**

> JavaScript

function filterTasks(status) {\
if(status === \'All\') {\
\$(\".task\").show();\
} else {\
\$(\".task\").hide();\
// Show only tasks containing the specific text\
\$(\".task:contains(\'\" + status + \"\')\").show();\
}\
}
