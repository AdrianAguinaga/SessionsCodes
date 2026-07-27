## **React with Vite - Session 1: Environment Setup + Basic Components**

### **3-Hour Comprehensive Workshop**

### **Session Overview**

- **Duration:** 3 hours

- **Format:** Hands-on workshop with guided practice

- **Breaks:** 1 x 15-minute break at the halfway point.

- **Learning Objectives:** By the end of this session, students will be
  able to:

  - Set up a modern React development environment using Vite from
    scratch.

  - Navigate and understand the project structure and configuration
    files.

  - Create, export, and import functional React components.

  - Implement component composition patterns.

  - Apply basic, modular CSS styling to components.

  - Debug common setup issues.

### Prerequisites Checklist

Ensure you have the following installed and ready:

- Install Node.js (version 16.0.0 or higher)

- Required Software:

  - Visual Studio Code (latest version)

  - Git (for version control)

  - A modern web browser (Chrome, Firefox, etc)

- Knowledge Prerequisites:

  - Basic understanding of HTML structure.

  - Fundamental JavaScript concepts (variables, functions, objects).

  - Basic command line/terminal usage.

## **Part 1: Getting Started (85 minutes)**

### 

### **1A: Terminal Mastery (20 minutes)**

The terminal is crucial for modern web development. It\'s your primary
interface for running tools, managing packages, and building your
project.

- **Navigation Commands:**

  - cd foldername: Navigate into a folder.

  - cd ..: Go back one level.

  - pwd: Show the current directory path.

- **File/Folder Management:**

  - mkdir foldername: Create a new folder.

  - ls -la (or dir on Windows): List folder contents.

- **Development-Specific Commands:**

  - npm run dev: Run the development server.

  - npm install: Install packages from package.json.

  - node -v: Check your Node.js version.

### **1B: VS Code Productivity Shortcuts (15 minutes)**

Mastering shortcuts will dramatically improve your speed.

- Ctrl+P / Cmd+P: Quickly find and open any file.

- Ctrl+B / Cmd+B: Toggle the sidebar.

- Ctrl+\\\`\` / Cmd+\`\`: Toggle the integrated terminal.

- Alt+Up/Down / Option+Up/Down: Move the current line up or down.

- Shift+Alt+Down / Shift+Option+Down: Copy the current line down.

### **1C: Creating Your First React Project with Vite (25 minutes)**

Let\'s create our React app using Vite for a faster development
experience.

Step 1: Initialize the Project

Run this command in your terminal to create a new React project in a
folder named my-react-store.

# Create a new React project with Vite\
npm create vite@latest my-react-store \--template react



Step 2: Navigate and Install

Move into the new directory and install the necessary packages.

# Enter the project directory\
cd my-react-store\
\
\# Install all required packages\
npm install



Step 3: Start the Development Server

Launch the application.

# Launch the development server\
npm run dev



You can now see your app running at

http://localhost:5173/.

## **Break (15 minutes)**

Take a break! When you return, we\'ll dive into the project structure
and start building components.

## **Part 2: Building & Styling (80 minutes)**

### **2A: Understanding the Project Architecture (15 minutes)**

Let\'s examine the project structure Vite has created.

- public/: Static assets that are served directly.

- src/: Your application\'s source code.

- src/main.jsx: The entry point of your application.

- index.html: The main HTML template for your app.

- package.json: Contains project metadata and dependencies.

- vite.config.js: Configuration file for the Vite build tool.

### **2B: Creating the Components Directory Structure (10 minutes)**

Let\'s organize our project by creating a proper directory structure for
our code.

# Create the components directory\
mkdir src/components\
\
\# Create additional directories for better organization\
mkdir src/pages src/services src/utils



This structure follows React best practices, separating reusable UI (

components), page-level components (pages), data logic (services), and
helper functions (utils).

### **2C: Creating Your First Custom Component (25 minutes)**

Let\'s create Navbar and Footer components.

Step 1: Create the Component Files

Use the terminal to create the files.

npm install touch-cli -g



touch src/components/Navbar.jsx\
touch src/components/Footer.jsx



**Step 2: Implement the Navbar Component (src/components/Navbar.jsx)**

function Navbar() {\
return (\
\<nav className=\"navbar\"\>\
\<div className=\"navbar-container\"\>\
\<div className=\"navbar-brand\"\>\
\<h1\>My Online Store\</h1\>\
\</div\>\
\<div className=\"navbar-menu\"\>\
\<ul className=\"navbar-nav\"\>\
\<li className=\"nav-item\"\>\<a href=\"#home\"
className=\"nav-link\"\>Home\</a\>\</li\>\
\<li className=\"nav-item\"\>\<a href=\"#catalog\"
className=\"nav-link\"\>Catalog\</a\>\</li\>\
\<li className=\"nav-item\"\>\<a href=\"#about\"
className=\"nav-link\"\>About\</a\>\</li\>\
\</ul\>\
\</div\>\
\</div\>\
\</nav\>\
);\
}\
export default Navbar;



**Step 3: Implement the Footer Component (src/components/Footer.jsx)**

function Footer() {\
return (\
\<footer className=\"footer\"\>\
\<div className=\"footer-container\"\>\
\<div className=\"footer-bottom\"\>\
\<p\>© 2025 My Online Store. All rights reserved.\</p\>\
\</div\>\
\</div\>\
\</footer\>\
);\
}\
export default Footer;



### **3A: Component Integration and Composition (20 minutes)**

Now, let\'s integrate our new components into the main

App component.

**Update src/App.jsx:**

// UPDATED CODE: Import our custom components\
import Navbar from \'./components/Navbar\';\
import Footer from \'./components/Footer\';\
import \'./App.css\';\
\
function App() {\
return (\
\<div className=\"App\"\>\
\<Navbar /\>\
\<main className=\"main-content\"\>\
\<h1\>Welcome to My Online Store\</h1\>\
\<p\>Discover amazing products at incredible prices.\</p\>\
\</main\>\
\<Footer /\>\
\</div\>\
);\
}\
export default App;



### **3B: Modular & Simplified CSS Styling (20 minutes)**

Instead of one large CSS file, we\'ll create separate, simple
stylesheets for each component. This keeps our styling organized and
easy to manage.

**Step 1: Create Component CSS Files**

touch src/components/Navbar.css\
touch src/components/Footer.css



Step 2: Add Imports to Components

Import the CSS file at the top of its corresponding component file.

- In src/components/Navbar.jsx, add: import \'./Navbar.css\';

- In src/components/Footer.jsx, add: import \'./Footer.css\';

Step 3: Discontinued





**Step 4: Add Component & App Styles**

**src/components/Navbar.css:**

.navbar {\
background-color: #333;\
color: white;\
padding: 1rem;\
}\
.navbar-container {\
display: flex;\
justify-content: space-between;\
align-items: center;\
max-width: 1200px;\
margin: 0 auto;\
}\
.navbar-nav {\
list-style: none;\
display: flex;\
gap: 1rem;\
}\
.nav-link {\
color: white;\
text-decoration: none;\
}

src/components/Footer.css:



.footer {\
background-color: #333;\
color: white;\
text-align: center;\
padding: 1rem;\
margin-top: auto; /\* Pushes footer to the bottom \*/\
}

src/App.css:

/\* App container layout \*/\
.App {\
min-height: 100vh;\
display: flex;\
flex-direction: column;\
}\
.main-content {\
flex: 1; /\* Ensures this area grows to push the footer down \*/\
padding: 2rem;\
max-width: 1200px;\
margin: 0 auto;\
width: 100%;\
}



### **3C: Testing and Debugging (5 minutes)**

- **Visual Testing:** Refresh your browser to see the changes.

- **Console Testing:** Open Developer Tools (F12) and check the Console
  tab for errors.

- **Common Issues:**

  - **Component not displaying?** Check that you have an export default
    statement in your component file.

  - **CSS not applying?** Ensure you have imported the .css file into
    the correct .jsx component.

  - **JSX Error?** Remember to use className instead of class for CSS
    classes in your JSX.
