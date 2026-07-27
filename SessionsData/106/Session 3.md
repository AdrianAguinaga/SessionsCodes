# 📅 Session 3: Client-Server Communication (POST)

Duration: 3 Hours

Goal: Implement the \"Create\" (POST) and \"Update\" (PUT)
functionality, understand JSON Serialization, and analyze the backend
logic.

### Part 3.1: The Data Journey (Theory)

Before writing code, students must understand that they cannot simply
\"send an object\" across the internet. It must be converted.

Visual: The Serialization Journey

Use this text-based diagram to illustrate the flow.

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

**Key Concepts to Explain:**

- **Serialization:** Converting a living object (RAM) into a text string
  (JSON) so it can travel through the wire.

- **Content-Type:** The \"Shipping Label\" on the packet that tells the
  server: \"This string is actually JSON data, please parse it.\"

### Part 3.2: Implementing POST (The Code)

We now refactor our saveTask function. In Session 2, it was just a local
echo. Now, it will be a real network request.

**Code to Share (scripts/app.js):**

> JavaScript

function saveTask() {\
// 1. Capture Data (Same as Session 2)\
const title = \$(\"#txtTitle\").val();\
const desc = \$(\"#txtDescription\").val();\
const color = \$(\"#selColor\").val();\
const date = \$(\"#selDate\").val();\
const status = \$(\"#selStatus\").val();\
const budget = \$(\"#numBudget\").val();\
\
// 2. Create the Object\
const data = new Task(title, desc, color, date, status, budget);\
console.log(\"DATA before POST:\", data);\
\
// 3. Send to Server\
\$.ajax({\
type: \"POST\", // HTTP Verb: CREATE\
url: API,\
data: JSON.stringify(data), // Step 2 in diagram: Convert to String\
contentType: \"application/json\", // Step 3 in diagram: The Label\
\
success: function(created){\
console.log(\"CREATED:\", created);\
\
// 4. Update UI with the SERVER\'S version\
// Important: \'created\' contains the new ID assigned by the server!\
displayTask(created);\
\
// 5. Cleanup\
clearForm();\
},\
error: function(err){\
console.error(\"POST error:\", err.responseText \|\| err);\
alert(\"Task could not be saved.\");\
}\
});\
}\
\
function clearForm() {\
\$(\"#txtTitle\").val(\"\");\
\$(\"#txtDescription\").val(\"\");\
\$(\"#numBudget\").val(\"\");\
// We can reset the whole form using DOM method:\
// \$(\"#taskForm\")\[0\].reset();\
}

Crucial Discussion: Ask students: \"Why do we pass created to
displayTask instead of data?\"

Answer: Because created is the \"receipt\" from the server. It contains
the ID (e.g., id: 104) that the server generated. We need this ID later
to delete or edit the task.

### Part 3.3: Analyzing Server Logic

We switch roles to \"Backend Developer\" to understand what happens on
the other side.

Code Analysis (Azure Function):

Walk through this logic with the students.

> JavaScript

// This is what runs inside the Azure Function\
if (method === \"POST\") {\
const body = req.body \|\| {};\
\
// 1. Validation Check\
if (!body.title) {\
context.res.status = 400; // Bad Request\
context.res.body = { error: \"title is required\" };\
return;\
}\
\
// 2. ID Generation & Storage\
// The server adds the ID here. The client cannot guess this number.\
const created = { \...body, id: NEXT_ID++ };\
\
// 3. Add to Database (Array)\
DB.unshift(created); // \'unshift\' adds it to the TOP of the list\
\
// 4. Send Response\
context.res.status = 201; // HTTP 201 = \"Created\"\
context.res.body = created;\
return;\
}

### Part 3.4: Updating Data (PUT)

While we won\'t build a full \"Edit Mode\" UI (which requires filling
the form back up with data), we will teach the **PUT** method.

**Concept:** POST is for *New* things. PUT is for *Existing* things. You
MUST have an ID to use PUT.

Activity: Console Hacking

Since we don\'t have an Edit UI, we will update a task using the Browser
Console to prove the server works.

1.  Refresh the page and find a task. note its visual details.

2.  Open the Network Tab or Console and find the **ID** of that task
    (e.g., \"1\").

3.  Run this code in the Console:

> JavaScript

// Replace \'1\' with a real ID from your list\
\$.ajax({\
type: \"PUT\",\
url: \"https://\[YOUR-API-URL\]/api/tasks/1\",\
data: JSON.stringify({\
title: \"I Hacked the Mainframe\",\
budget: 999999\
}),\
contentType: \"application/json\",\
success: function(response) {\
console.log(\"Update Success!\", response);\
alert(\"Refresh the page to see the change!\");\
}\
});

**Discussion:**

- **Result:** When they refresh, the task title will change permanently.

- **Logic:** The server looks for ID \"1\", finds it, and *merges* the
  new data (req.body) into the old object using the Spread syntax
  (\...).

### ✅ Session 3 Checklist

By the end of this session, students should have:

1.  **Persistence:** Tasks added via the form survive a page refresh.

2.  **Network Proficiency:** They can see the POST request in the Chrome
    Network tab with status 201 Created.

3.  **Data Integrity:** They understand that if they don\'t send
    contentType: application/json, the server will reject the data (try
    it!).

**Ready for Session 4 (Delete, Filter & Polish)?**
