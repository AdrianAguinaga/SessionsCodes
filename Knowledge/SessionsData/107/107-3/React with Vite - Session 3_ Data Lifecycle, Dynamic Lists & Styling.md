## **React with Vite - Session 3: Data Lifecycle, Dynamic Lists & Styling**

### **3-Hour Comprehensive Workshop**

### **Session Overview**

- **Duration**: 3 hours

- **Format**: Hands-on workshop with guided practice

- **Breaks**: 1 x 15-minute break at the halfway point.

- **Learning Objectives**: By the end of this session, students will be
  able to:

  - Use the useEffect Hook to fetch data when a component loads.

  - Store and manage data from an external source using the useState
    Hook.

  - Dynamically render a list of components from an array using the
    .map() method.

  - Understand and use the unique key prop in lists.

  - Pass entire data objects to child components via props.

  - Convert standard HTML into valid JSX.

  - Integrate and customize a complex UI component from a framework like
    Bootstrap.

### **Prerequisites Checklist**

- Completion of \"React with Vite - Session 2\" or equivalent knowledge.

- A working React project with Catalog and Product components.

- Basic understanding of useState and event handling.

### **Part 1: Component Lifecycle and Data Handling (85 minutes)**

#### **1A: The useEffect Hook for Data Fetching (30 minutes)**

So far, our data is available immediately. In a real application, you
need to fetch data from a server, which takes time. The useEffect Hook
lets us perform \"side effects,\" like fetching data, after the
component has rendered.

Step 1: Introduce useEffect in Catalog.jsx

First, import useEffect from React. Then, call it inside your Catalog
component. The function you pass to useEffect will run after the
component mounts (is displayed on screen).

// At the top of src/pages/Catalog.jsx\
import { useState, useEffect } from \'react\'; // Add useEffect\
import \'./Catalog.css\';\
import Product from \'../components/Product\';\
import DataService from \'../services/dataService\';\
\
function Catalog() {\
const \[products, setProducts\] = useState(\[\]);\
\
// useEffect runs when the component loads\
useEffect(function() {\
console.log(\"Component loaded!\");\
loadCatalog();\
}, \[\]); // The empty array \[\] means: \"run this function only
once\"\
\
function loadCatalog() {\
let service = new DataService();\
let data = service.getProducts();\
console.log(data);\
setProducts(data);\
}\
\
return (\
// \... your existing JSX\
);\
}\
\
export default Catalog;



*Your console should now show \"Component loaded!\" followed by the
array of products. This confirms your data is being loaded when the
component first appears.*

Step 2: A Note on StrictMode

In development, you might see the console.log from useEffect appear
twice. This is because of \<React.StrictMode\> in src/main.jsx, which
intentionally double-renders components to help you find bugs. For this
lesson, you can temporarily remove it to see the log only once.

// In src/main.jsx\
\
// Remove \<React.StrictMode\> wrappers\
root.render(\
\<App /\>\
);



#### **1B: Rendering Dynamic Lists with .map() (55 minutes)**

Instead of hard-coding \<Product /\> components, we will now render them
dynamically from our products state variable.

Step 1: Understanding Array.map()

The .map() method is a standard JavaScript function that transforms each
element of an array into something new. For us, we\'ll transform each
product object into a \<Product /\> component.

Step 2: Map Over the products State

In Catalog.jsx, replace the hard-coded \<Product /\> tags with a
JavaScript map expression.

// In the return() of src/pages/Catalog.jsx\
return (\
\<div className=\"catalog\"\>\
\<h1\>Check our amazing products\</h1\>\
\<h5\>We have {products.length} products ready for you!\</h5\>\
\
\<div className=\"product-list\"\>\
{products.map(prod =\> \<Product key={prod.\_id} /\>)}\
\</div\>\
\</div\>\
);



**Why the key prop?** React uses the key prop to identify which items in
a list have changed, been added, or been removed. It\'s crucial for
performance and must be a **unique string or number** for each item in
the list. Our product\'s \_id is perfect for this.

*You should now see a list of products rendered on the page, one for
each object in your data service.*

### **Break (15 minutes)**

### **Part 2: Advanced Props and UI Customization (80 minutes)**

#### **2A: Passing Full Objects as Props (30 minutes)**

Our products are rendering, but they are all identical because we
aren\'t passing any data to them yet. Let\'s send the entire product
object down to the Product component.

Step 1: Pass the Product Object in a data Prop

Modify the .map() function in Catalog.jsx to pass the entire prod object
in a single prop called data.

// In the map function of src/pages/Catalog.jsx\
{products.map(prod =\> \<Product key={prod.\_id} data={prod} /\>)}



Step 2: Receive and Use Props in Product.jsx

Now, update the Product component to accept props and use the
information from the data object to display the image, title, and price.

// In src/components/Product.jsx\
import \'./Product.css\';\
import QuantityPicker from \'./QuantityPicker\';\
\
function Product(props) {\
return (\
\<div className=\"product\"\>\
\<img src={\"/images/\" + props.data.image} alt=\"Product\" /\>\
\<h5\>{props.data.title}\</h5\>\
\
\<div className=\"prices\"\>\
\<label\>Total: \$0.00\</label\>\
\<label\>Price: \${props.data.price.toFixed(2)}\</label\>\
\</div\>\
\
\<QuantityPicker /\>\
\<button className=\"btn btn-sm btn-outline-primary\"\>Add\</button\>\
\</div\>\
);\
}\
export default Product;



*Your catalog page should now display a list of unique products, each
with its correct title, image, and price.*

#### **2B: Integrating a Bootstrap Navbar (50 minutes)**

Let\'s upgrade our basic navbar to a full-featured, responsive one from
the Bootstrap library. This is a common task in web development.

Step 1: Get the Navbar HTML from Bootstrap

Go to the official Bootstrap documentation website, find the \"Navbar\"
component, and copy the HTML for a navbar you like.

Step 2: Paste and Convert to JSX in Navbar.jsx

Replace the entire content of the return statement in
src/components/Navbar.jsx with the HTML you copied from Bootstrap. You
will immediately see errors. This is because HTML is not the same as
JSX.

Step 3: Fix JSX Errors

You need to make two main changes to convert the HTML to JSX:

1.  **class to className**: The class attribute is a reserved word in
    JavaScript. In JSX, you must use className. Use your code editor\'s
    **Find and Replace** feature (Ctrl+F or Cmd+F) to replace all
    instances of class= with className=.

2.  **Close All Tags**: JSX requires all tags to be closed. Tags like
    \<hr\> or \<input\> must be self-closing: \<hr /\>, \<input /\>.

// Example of a converted Bootstrap Navbar in
src/components/Navbar.jsx\
function Navbar() {\
return (\
\<nav className=\"navbar navbar-expand-lg navbar-dark bg-dark\"\>\
\<div className=\"container-fluid\"\>\
\<a className=\"navbar-brand\" href=\"#\"\>My Store\</a\>\
\<button className=\"navbar-toggler\" type=\"button\"
data-bs-toggle=\"collapse\" data-bs-target=\"#navbarNav\"
aria-controls=\"navbarNav\" aria-expanded=\"false\" aria-label=\"Toggle
navigation\"\>\
\<span className=\"navbar-toggler-icon\"\>\</span\>\
\</button\>\
\<div className=\"collapse navbar-collapse\" id=\"navbarNav\"\>\
\<ul className=\"navbar-nav\"\>\
\<li className=\"nav-item\"\>\
\<a className=\"nav-link active\" aria-current=\"page\"
href=\"#\"\>Home\</a\>\
\</li\>\
\<li className=\"nav-item\"\>\
\<a className=\"nav-link\" href=\"#\"\>Catalog\</a\>\
\</li\>\
\</ul\>\
\</div\>\
\</div\>\
\</nav\>\
);\
}\
\
export default Navbar;



*Your application now has a professional and responsive navigation bar.*

### **Debugging & Common Issues**

- **Infinite Loop of Loading**: If your component keeps re-rendering
  endlessly, make sure you have included the empty dependency array \[\]
  as the second argument to useEffect. Without it, useEffect runs after
  *every* render.

- **.map() is not a function**: This error usually means you are trying
  to map over something that isn\'t an array. Check that the initial
  value in your useState is \[\] and that your data service is returning
  an array.

- **\"Each child in a list should have a unique \'key\' prop\"**: This
  is a warning from React. Make sure to add a unique key prop to the
  top-level element inside your .map(), like \<Product key={prod.\_id}
  \... /\>.

- **Bootstrap Dropdowns or Toggles Don\'t Work**: The bootstrap npm
  package includes CSS and JavaScript. To enable JS features, you need
  to import it. A good place is at the top of your src/main.jsx file:
  import \'bootstrap/dist/js/bootstrap.bundle.min.js\';
