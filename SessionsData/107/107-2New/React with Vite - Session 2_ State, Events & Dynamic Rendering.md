## **React with Vite - Session 2: State, Events & Dynamic Rendering**

### **3-Hour Comprehensive Workshop**

### **Session Overview**

- **Duration**: 3 hours

- **Format**: Hands-on workshop with guided practice

- **Breaks**: 1 x 15-minute break at the halfway point.

- **Learning Objectives**: By the end of this session, students will be
  able to:

  - Create interactive, stateful components using the useState Hook.

  - Handle user events like button clicks.

  - Structure an application with page-level and reusable components.

  - Create a data service to manage application data.

  - Dynamically render lists of components from an array of data.

  - Pass data from a parent component to a child component using props.

  - Integrate a CSS framework like Bootstrap for rapid styling.

### **Prerequisites Checklist**

- Completion of \"React with Vite - Session 1\" or equivalent knowledge.

- A working React project created with Vite.

- Familiarity with creating and exporting/importing functional
  components.

### **Part 1: State and Interactivity (85 minutes)**

#### **1A: Creating the QuantityPicker Component (20 minutes)**

Let\'s build a reusable component to handle item quantities. This will
be the foundation for learning about state and events.

Step 1: Create the Component Files

In your terminal, create the component file and its corresponding CSS
file inside the src/components directory.

touch src/components/QuantityPicker.jsx\
touch src/components/QuantityPicker.css



Step 2: Implement the Basic QuantityPicker Component

Open src/components/QuantityPicker.jsx and add the following code to
create the structure with two buttons and a label.

import \'./QuantityPicker.css\';\
\
function QuantityPicker() {\
return (\
\<div className=\"quantity-picker\"\>\
\<button className=\"btn-minus\"\>-\</button\>\
\<label className=\"label-qty\"\>1\</label\>\
\<button className=\"btn-plus\"\>+\</button\>\
\</div\>\
);\
}\
\
export default QuantityPicker;



Step 3: Render it in App.jsx

For now, let\'s add the new component to App.jsx to see it on the
screen.

// In src/App.jsx\
import Navbar from \'./components/Navbar\';\
import Footer from \'./components/Footer\';\
import QuantityPicker from \'./components/QuantityPicker\'; // Import
the new component\
import \'./App.css\';\
\
function App() {\
return (\
\<div className=\"App\"\>\
\<Navbar /\>\
\<main className=\"main-content\"\>\
\<h1\>Welcome to My Online Store\</h1\>\
\<p\>Discover amazing products at incredible prices.\</p\>\
\<QuantityPicker /\> {/\* Add the component here \*/}\
\</main\>\
\<Footer /\>\
\</div\>\
);\
}\
\
export default App;



*You should now see the \"-\", \"1\", and \"+\" laid out on your page.*

#### **1B: Handling User Events with onClick (20 minutes)**

A component isn\'t interactive until it can respond to user input.
Let\'s make the buttons do something when clicked.

Step 1: Create Event Handler Functions In

src/components/QuantityPicker.jsx, add two functions inside the
QuantityPicker component, before the return statement.

function QuantityPicker() {\
function handleDecrease() {\
console.log(\"Decrease clicked!\"); //\
\
function handleIncrease() {\
console.log(\"Increase clicked\"); //\
}\
\
return (\
// \... JSX from before\
);\
}



Step 2: Attach Functions to Buttons

Use the onClick event attribute on your buttons to link them to your new
functions.

// In src/components/QuantityPicker.jsx\
\
function QuantityPicker() {\
// \... handleDecrease and handleIncrease functions\
\
return (\
\<div className=\"quantity-picker\"\>\
\<button className=\"btn-minus\" onClick={handleDecrease}\>-\</button\>

\<label className=\"label-qty\"\>1\</label\>\
\<button className=\"btn-plus\" onClick={handleIncrease}\>+\</button\>

\</div\>\
);\
}\
\
export default QuantityPicker;



*Now, open your browser\'s developer tools (F12), go to the Console, and
click the buttons. You should see your messages being logged.*

#### **1C: Managing State with the useState Hook (45 minutes)**

Logging to the console is great for debugging, but we need the component
to visually update. For that, we need **state**. React components will
\"react\" and re-render whenever their state changes. ^7^

Step 1: Import useState from React

The useState function is a \"Hook\" that lets you add state to
functional components. You must import it from the

// At the top of src/components/QuantityPicker.jsx\
import { useState } from \'react\'; //\
import \'./QuantityPicker.css\';

\
Step 2: Initialize a State Variable

Call useState inside your component to create the state. It returns a
pair: the current state value and a function that lets you update it.



// In src/components/QuantityPicker.jsx\
function QuantityPicker() {\
const \[quantity, setQuantity\] = useState(1); //\
\
function handleDecrease() {\
console.log(\"Decrease clicked!\");\
}\
//\...\
}



Step 3: Use the State Variable in Your JSX

Replace the hard-coded \"1\" in your label with the

quantity state variable. ^11^Remember to use curly braces {} to embed
JavaScript expressions in JSX.



// In the return() of src/components/QuantityPicker.jsx\
\<label className=\"label-qty\"\>{quantity}\</label\> //



Step 4: Update State in the Event Handlers

Now, modify your handleIncrease and handleDecrease functions to use the
setQuantity function. You should never modify state directly (e.g.,
quantity = quantity + 1).

// In src/components/QuantityPicker.jsx\
function QuantityPicker() {\
const \[quantity, setQuantity\] = useState(1);\
\
function handleDecrease() {\
let nextVal = quantity - 1; //\
if (nextVal \> 0) {\
setQuantity(nextVal);\
}\
}\
\
function handleIncrease() {\
let nextVal = quantity + 1; //\
setQuantity(nextVal); //\
}\
//\...\
}



Step 5: Add Conditional Logic

We don\'t want the quantity to go below 1. Let\'s also disable the \"-\"
button when the quantity is 1.

// In the return() of src/components/QuantityPicker.jsx\
\<button className=\"btn-minus\" onClick={handleDecrease}
disabled={quantity === 1}\>-\</button\> //



*Your QuantityPicker is now fully interactive!*

**Break (15 minutes)**

### **Part 2: Building with Dynamic Data (80 minutes)**

#### **2A: Creating a Product Component (20 minutes)**

Let\'s create a component to display a single product, which will
include our QuantityPicker.

**Step 1: Create the Component Files**

touch src/components/Product.jsx\
touch src/components/Product.css



Step 2: Implement the Product Component

Open src/components/Product.jsx and add the following. Notice we are
composing components by including \<QuantityPicker /\> inside our new
Product component.

import \'./Product.css\';\
import QuantityPicker from \'./QuantityPicker\'; //\
\
function Product() {\
return (\
\<div className=\"product\"\>

\<img src=\"https://picsum.photos/220/180\" alt=\"Product\" /\>

\<h5\>Product Title Goes Here\</h5\>\
\<div className=\"prices\"\>\
\<label\>Price\</label\>\
\<label\>Total\</label\>\
\</div\>\
\<QuantityPicker /\> \</div\>\
);\
}

export default Product; //



#### **2B: Creating the Catalog Page (25 minutes)**

The catalog will display all of our products. This is a \"page-level\"
component, so we will organize it in a separate pages folder.

**Step 1: Create the Page Files**

mkdir src/pages\
touch src/pages/Catalog.jsx\
touch src/pages/Catalog.css



Step 2: Implement the Catalog Page

Open src/pages/Catalog.jsx. We will import the Product component and
render it multiple times.

import \'./Catalog.css\';\
import Product from \'../components/Product\'; //\
function Catalog() {\
return (\
\<div className=\"catalog\"\>\
\<h1\>Check our amazing products\</h1\>\
\<Product /\>

\<Product /\>

\<Product /\>

\</div\>\
);\
}\
\
export default Catalog;



Step 3: Update App.jsx to Show the Catalog

Replace the test QuantityPicker in App.jsx with your new Catalog page.

// In src/App.jsx\
import Navbar from \'./components/Navbar\';\
import Footer from \'./components/Footer\';\
import Catalog from \'./pages/Catalog\'; // Import the new Catalog page\
import \'./App.css\';\
\
function App() {\
return (\
\<div className=\"App\"\>\
\<Navbar /\>\
\<Catalog /\> {/\* Render the Catalog page \*/}\
\<Footer /\>\
\</div\>\
);\
}\
\
export default App;



#### **2C: Rendering Data Dynamically (35 minutes)**

Hard-coding components is not practical. Let\'s create a \"data
service\" to provide our product information and then use JavaScript\'s
.map() function to render a component for each item in our data.

Step 1: Create a Data Service

This is a simple JavaScript file that exports our data. This keeps our
data separate from our display logic.

mkdir src/services\
touch src/services/dataService.js



Step 2: Add Product Data

Open src/services/dataService.js and add an array of product objects.

// In src/services/dataService.js\
const catalog = \[\
{\
\"title\": \"Orange\", //

\"category\": \"fruit\", //\
\"price\": 12.99, //\
\"image\": \"orange.jpg\",\
\"\_id\": \"1\"\
},\
{\
\"title\": \"Apple\",\
\"category\": \"fruit\",\
\"price\": 8.50,\
\"image\": \"apple.jpg\",\
\"\_id\": \"2\"\
},\
{\
\"title\": \"Banana\",\
\"category\": \"fruit\",\
\"price\": 10.00,\
\"image\": \"banana.jpg\",\
\"\_id\": \"3\"\
},\
{\
\"title\": \"Strawberries\",\
\"category\": \"berry\",\
\"price\": 15.25,\
\"image\": \"strawberry.jpg\",\
\"\_id\": \"4\"\
},\
{\
\"title\": \"Grapes\",\
\"category\": \"fruit\",\
\"price\": 11.99,\
\"image\": \"grapes.jpg\",\
\"\_id\": \"5\"\
}\
\];\
\
class DataService {\
getProducts() {\
return catalog;\
}\
}\
\
export default DataService;



*(Note: You will need to find your own images and place them in the
public/images/ folder for them to work).*

Step 3: Use the Data in Catalog.jsx

Now, let\'s import the data and use .map() to dynamically create our
\<Product /\> list.

// In src/pages/Catalog.jsx\
import { useEffect, useState } from \'react\';\
import \'./Catalog.css\';\
import Product from \'../components/Product\';\
import DataService from \'../services/dataService\';\
\
function Catalog() {\
const \[products, setProducts\] = useState(\[\]);\
\
useEffect(() =\> {\
// Load your data here\
let service = new DataService();\
let data = service.getProducts();\
setProducts(data);\
}, \[\]); // The empty array \[\] means this effect runs only ONCE\
\
return (\
\<div className=\"catalog\"\>\
\<h1\>Check our amazing products\</h1\>\
\<div className=\"product-list\"\>\
{products.map(prod =\> \<Product key={prod.\_id} /\>)}\
\</div\>\
\</div\>\
);\
}\
\
export default Catalog;



*Your app now renders five identical products because we are not yet
passing data down to them.*

### **Part 3: Props & Final Styling (15 minutes)**

#### **3A: Passing Data with Props**

**Props** (short for properties) are how you pass data from a parent
component to a child.

Step 1: Pass Props from Catalog.jsx

Modify the .map() function to pass the product data as props to the
Product component.

// In src/pages/Catalog.jsx\'s return()\
{products.map(prod =\> \<Product key={prod.\_id} data={prod} /\>)}



Step 2: Receive and Use Props in Product.jsx

Modify the Product component to accept the data prop and display its
information.

// In src/components/Product.jsx\
function Product(props) {\
return (\
\<div className=\"product\"\>\
\<img src={\'/images/\' + props.data.image} alt=\"Product\" /\>\
\<h5\>{props.data.title}\</h5\>\
\<div className=\"prices\"\>\
\<label\>\${props.data.price.toFixed(2)}\</label\>\
\<label\>Total\</label\>\
\</div\>\
\<QuantityPicker /\>\
\</div\>\
);\
}



*Your product catalog should now be displaying unique data for each
product!*

Debugging & Common Issues

- **Component Doesn\'t Update on Click?** Make sure you are using a
  state variable (useState) and updating it with the setter function
  (e.g., setQuantity()). Directly changing a variable will not cause a
  re-render.

- **Data Not Showing in Child Component?** Check the prop name you are
  passing from the parent (\<Product data={\...} /\>). Ensure it matches
  the name you are accessing in the child (props.data).

- **useState is not defined?** Ensure you have imported it at the top of
  your file: import { useState } from \'react\';.

- **Images Not Loading?** Place your images in the public folder. You
  can then reference them directly with a path starting from /, for
  example: /images/my-image.jpg.
