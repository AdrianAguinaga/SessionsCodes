Here is the detailed guide for **Session 2**.

In this session, we breathe life into the application. We will move from
a static page to a dynamic one that can **Read** user input, **Render**
visual elements, and **Fetch** data from the cloud.

# 📅 Session 2: The DOM, Events & Reading Data

Duration: 3 Hours

Goal: Master DOM manipulation with jQuery, handle Form events, and
implement the first leg of Client-Server communication (GET).

### Part 2.1: Understanding the DOM (The Tree)

Before we write code, we must visualize what we are manipulating. The
**Document Object Model (DOM)** is a tree structure.

Original Visual: The DOM Tree

Use this diagram to explain how jQuery \"travels\" to find elements.

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
┌────────┴────────┐\
\<form\> \<div id=\"list\"\> ◄── THE TARGET\
│ │\
\<input\> ├── (We will inject Task 1 here)\
└── (We will inject Task 2 here)

**Explanation:**

1.  **Selection:** When we write \$(\"#list\"), jQuery starts at
    document and hunts down the tree until it finds the unique ID list.

2.  **Manipulation:** When we use .append(), we are programmatically
    growing new \"branches\" (HTML elements) onto that specific part of
    the tree.

### Part 2.2: Capturing Data (Input)

We need to extract what the user typed when they click \"Save\".

Code to Share (scripts/app.js):

In app.js, we write the saveTask function. Explain that .val() is a
jQuery method that grabs the current text inside an input field.

> JavaScript

function saveTask() {\
console.log(\"Saving task\...\");\
\
// 1. Get values from the DOM\
const title = \$(\"#txtTitle\").val();\
const desc = \$(\"#txtDescription\").val();\
const color = \$(\"#selColor\").val();\
const date = \$(\"#selDate\").val();\
const status = \$(\"#selStatus\").val();\
const budget = \$(\"#numBudget\").val();\
\
// 2. Create an Object using our Class (Model)\
const taskToSave = new Task(title, desc, color, date, status, budget);\
\
// 3. Log it to verify\
console.log(taskToSave);\
\
// 4. (Coming up next) Display it on screen\
displayTask(taskToSave);\
}

### Part 2.3: Rendering Data (Output)

Now we need to convert that Javascript Object back into HTML so the user
can see it. We use **Template Literals** (backticks \`\`) to mix HTML
strings with JavaScript variables \${var}.

**Code to Share (scripts/app.js):**

> JavaScript

function displayTask(task){\
// Create the HTML syntax using values from the task object\
// Note the style=\"border-color:\${task.color}\" -\> Dynamic Styling!\
let syntax = \`\
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
// Inject the new HTML into the DOM Tree\
\$(\".list\").append(syntax);\
}

**Activity:** Have students fill out the form and click save. They
should see the task appear instantly. This is called \"Local Echo\".

### Part 2.4: Asynchronous Data (AJAX GET)

The local echo is temporary. If they refresh, it disappears. We need to
load real data from the server.

Visual Concept: The AJAX \"Waiter\"

Explain that AJAX is like a waiter in a restaurant.

1.  **Request:** You (Client) tell the waiter (AJAX) \"Get me the
    menu\".

2.  **Async:** While the waiter goes to the kitchen (Server), you sit at
    the table. You don\'t freeze.

3.  **Response:** The waiter returns with the menu (JSON Data).

4.  **Callback:** You read the menu (success function).

Code to Share (scripts/app.js):

Define the API URL constant at the top of the file first.

> JavaScript

// This URL points to our Azure Function\
const API =
\"https://106api-b0bnggbsgnezbzcz.westus3-01.azurewebsites.net/api/tasks\";\
\
function loadTasks(){\
\$.ajax({\
type: \"GET\", // HTTP Verb: READ\
url: API, // Destination\
dataType: \"json\", // Expected format\
success: function(data) {\
console.log(\"Server responded with:\", data);\
\
// Clear the list to avoid duplicates\
\$(\".list\").empty();\
\
// Loop through the array of tasks\
for(let i=0; i \< data.length; i++) {\
displayTask(data\[i\]); // Reuse our display function!\
}\
},\
error: function(err) {\
console.error(\"Error fetching data\", err);\
}\
});\
}

### Part 2.5: Wiring it Up (Initialization)

Finally, we update our init function to hook up the button and load the
data when the app starts.

**Code to Share (scripts/app.js):**

> JavaScript

function init(){\
console.log(\"App initialized\");\
\
// Hook up the Save Button\
\$(\"#btnSave\").click(saveTask);\
\
// Load data from server immediately\
loadTasks();\
}\
\
window.onload = init;

### ✅ Session 2 Checklist

By the end of this session, students should have:

1.  **Form Functionality:** Clicking \"Save\" adds a visual card to the
    list immediately.

2.  **Server Connection:** When the page loads, they should see tasks
    that exist on the Server (verify by checking the Console for
    \"Server responded with\...\").

3.  **Visual Feedback:** The tasks should have different border colors
    based on the data received.

**Ready for Session 3 (POST, PUT & Server Logic)?**
