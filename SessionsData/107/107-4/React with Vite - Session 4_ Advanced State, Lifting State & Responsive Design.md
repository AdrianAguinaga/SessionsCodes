## **React with Vite - Session 4: Advanced State, Lifting State & Responsive Design**

### **3-Hour Comprehensive Workshop**

### **Session Overview**

- **Duration**: 3 hours

- **Format**: Hands-on workshop with guided practice

- **Breaks**: 1 x 15-minute break at the halfway point.

- **Learning Objectives**: By the end of this session, students will be
  able to:

  - Implement client-side filtering logic to display a subset of data.

  - Manage multiple, related state variables within a single component.

  - Communicate data from a child component back up to a parent
    (**Lifting State Up**).

  - Pass functions as props to handle child-to-parent data flow.

  - Calculate and display derived data (e.g., a total price) based on
    state and props.

  - Apply responsive CSS using media queries to adapt the layout for
    mobile devices.

### **Prerequisites Checklist**

- Completion of \"React with Vite - Session 3\" or equivalent knowledge.

- A working React project that dynamically renders a list of products
  from a data service.

- Familiarity with useState, useEffect, and passing props.

### **Part 1: Client-Side Filtering (85 minutes)**

#### **1A: Setting Up State for Filtering (25 minutes)**

To filter our products, we need to manage several pieces of information:
the complete list of all products, the list of products we are
*currently showing*, and the list of available categories.

Step 1: Create State for Categories and Displayed Products

In src/pages/Catalog.jsx, we\'ll add two new state variables. One will
hold our filter categories, and the other will hold the products that
should be rendered on the screen.

// In src/pages/Catalog.jsx\
\
function Catalog() {\
const \[products, setProducts\] = useState(\[\]);\
const \[categories, setCategories\] = useState(\[\]); // To hold the
category list\
const \[prodsToDisplay, setProdsToDisplay\] = useState(\[\]); // To hold
the products to show\
\
// \... useEffect and other functions\
}



Step 2: Populate All State Variables on Load

Update the loadCatalog function to populate all our state variables when
the component first loads. We\'ll set the master product list, the
initial list to display (which is all products at first), and a
hard-coded list of categories.



// In src/pages/Catalog.jsx\
\
function loadCatalog() {\
let service = new DataService();\
let data = service.getProducts();\
setProducts(data);\
setProdsToDisplay(data); // Initially, display all products\
\
// TODO: Move this to a service later\
let cats = \[\"Fruit\", \"Vegetable\", \"Dairy & Eggs\",
\"Beverages\"\];\
setCategories(cats);\
}



Step 3: Render from the Correct State

Change the .map() function in your JSX to render from the prodsToDisplay
state variable, not the original products state.

// In the return() of src/pages/Catalog.jsx\
\<div className=\"product-list\"\>\
{prodsToDisplay.map(prod =\> \<Product key={prod.\_id} data={prod}
/\>)}\
\</div\>



#### **1B: Implementing the Filter Logic (60 minutes)**

Now we\'ll create the UI and the functions needed to perform the
filtering.

Step 1: Render the Category Filter Buttons

In Catalog.jsx, add a section above your product list that maps over the
categories array to create a filter button for each one. We\'ll also add
an \"All\" button to clear the filter.

// In the return() of src/pages/Catalog.jsx, before the product-list
div\
\
\<div className=\"filters\"\>\
\<button onClick={clearFilter} className=\"btn btn-dark
btn-filter\"\>All\</button\>\
{categories.map(cat =\> \<button key={cat} onClick={() =\> filter(cat)}
className=\"btn btn-primary btn-filter\"\>{cat}\</button\>)}\
\</div\>\
\<hr /\>



Step 2: Create the filter and clearFilter Functions

Now, let\'s create the functions that our buttons will call.

- clearFilter: This will simply reset the prodsToDisplay back to the
  original, full list of products.

- filter: This function will receive a category, loop through the master
  products list, and create a new list containing only the products that
  match the selected category.

// In src/pages/Catalog.jsx, before the return() statement\
\
function clearFilter() {\
setProdsToDisplay(products);\
}\
\
function filter(category) {\
let list = \[\];\
// Find the products that match the category\
for (let i = 0; i \< products.length; i++) {\
let prod = products\[i\];\
if (prod.category === category) {\
list.push(prod);\
}\
}\
setProdsToDisplay(list);\
}



*Your catalog should now be fully filterable! Clicking a category button
will show only those products, and clicking \"All\" will reset the
view.*

### **Break (15 minutes)**

### **Part 2: State Lifting & Derived Data (80 minutes)**

#### **2A: The Challenge: Child-to-Parent Communication (15 minutes)**

We have a new requirement: the Product component needs to calculate a
**total price** (price \* quantity). However, the quantity is managed
inside the QuantityPicker component. How does the parent Product get the
quantity from its child QuantityPicker?

This is a classic React challenge. The solution is called **\"lifting
state up,\"** which involves passing a function from the parent down to
the child as a prop.

#### **2B: Passing Functions as Props (35 minutes)**

We will give the QuantityPicker a function it can call whenever its
quantity changes, effectively sending the new quantity value \"up\" to
the Product parent.

Step 1: Create a Handler Function in Product.jsx

In the Product component, create a function that will receive the new
quantity. For now, it will just log the value.

// In src/components/Product.jsx\
function Product(props) {\
function handleQuantityChange(qty) {\
console.log(\"New value:\", qty);\
}\
\
return (\
// \...\
);\
}



Step 2: Pass the Handler as a Prop

Pass the new handleQuantityChange function to the QuantityPicker
component as a prop. A common name for such a prop is onChange.



// In the return() of src/components/Product.jsx\
\<QuantityPicker onChange={handleQuantityChange} /\>



Step 3: Call the Prop Function from the Child

Now, in src/components/QuantityPicker.jsx, we need to receive this prop
and call it.

First, accept props in the function definition.

// In src/components/QuantityPicker.jsx\
function QuantityPicker(props) {\
// \...\
}



Next, in your handleDecrease and handleIncrease functions, call the
function from props *after* you set the state. This notifies the parent
of the change.

// Inside handleDecrease in QuantityPicker.jsx\
let nextVal = quantity - 1;\
if (nextVal \> 0) {\
setQuantity(nextVal);\
props.onChange(nextVal); // Notify the parent\
}\
\
// Inside handleIncrease in QuantityPicker.jsx\
let nextVal = quantity + 1;\
setQuantity(nextVal);\
props.onChange(nextVal); // Notify the parent



*Now when you click the +/- buttons, you should see the \"New value\"
message logged in the console from the Product component!*

#### **2C: Calculating the Total Price (30 minutes)**

Now that the Product component receives the quantity, it can store it in
its own state and calculate the total.

Step 1: Create State for Quantity in Product.jsx

Add a state variable to the Product component to store the quantity.



// At the top of src/components/Product.jsx\
import { useState } from \'react\';\
// \...\
function Product(props) {\
const \[quantity, setQuantity\] = useState(1);\
\
function handleQuantityChange(qty) {\
setQuantity(qty);\
}\
// \...\
}



Step 2: Create a getTotal Helper Function

It\'s good practice to create a small function for calculations instead
of putting logic directly in the JSX. This function will use the
quantity from state and the price from props.

// In src/components/Product.jsx, before the return()\
function getTotal() {\
let total = props.data.price \* quantity;\
return total.toFixed(2);\
}



Step 3: Display the Total

Finally, call your new getTotal() function in the JSX to display the
calculated total price.

// In the return() of src/components/Product.jsx\
\<div className=\"prices\"\>\
\<label\>Total: \${getTotal()}\</label\>\
\<label\>Price: \${props.data.price.toFixed(2)}\</label\>\
\</div\>



*Your product cards should now show a total price that updates in
real-time as you change the quantity!*

### **Debugging & Common Issues**

- **Filter Clears but Doesn\'t Show Anything?** Make sure you are
  filtering from the master products list, not from prodsToDisplay. If
  you filter the already-filtered list, you\'ll end up with an empty
  array.

- **props.onChange is not a function?** This means the QuantityPicker
  was rendered without an onChange prop. Ensure you are passing the
  handler function from the Product component: \<QuantityPicker
  onChange={\...} /\>.

- **Total is NaN (Not a Number)?** This happens if you try to multiply a
  number by undefined. Check that props.data.price and the quantity
  state variable both have valid number values.

- **Layout Looks Bad on Mobile?** Add a \@media query to your CSS file.
  A common starting point is \@media (max-width: 768px) { \... } to
  target tablet and mobile screen sizes. Inside, you can change
  properties like width, display, and margin to re-flow your layout.
