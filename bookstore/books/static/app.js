function addToCart() {
    // Get's product data from the html form
    var productName = this.getAttribute('data-loc-name');
    var productPrice = this.getAttribute('data-loc-price');

    console.log("Adding to cart:");
    console.log("Product Name: " + productName);
    console.log("Product Price: $" + productPrice);
    alert("Item added to cart");

    // Increcments the cart count in the local storage
    var itemsInCart = parseInt(localStorage.getItem("cartCount")) || 0;
    itemsInCart++;
    localStorage.setItem("cartCount", itemsInCart);

    // Updates the cart count in the UI
    document.getElementById("cart-count").textContent = itemsInCart;
}

// Every time the add to cart button is clicked, the addToCart function is activated
document.addEventListener('DOMContentLoaded', function() {
    var addToCartButtons = document.querySelectorAll('.addToCart');
    for (var i = 0; i < addToCartButtons.length; i++)  
        addToCartButtons[i].addEventListener('click', addToCart);  
});

// gets cartcount from local storage and sets to initialized count
var count = parseInt(localStorage.getItem("cartCount")) || 0;
// sets all html elements with id cart-count to the value of initializedCount
document.getElementById("cart-count").textContent = count;

// ----------------------------------------------------------------------------------
// clears the data in the cart
function cartClear() {
// Removes cartCount from local storage
localStorage.removeItem("cartCount"); 
// sets all html elements with id cart-count to 0
document.getElementById("cart-count").textContent = '0'; 
}

function checkOut(){
    let total = document.getElementById("total-price").textContent;
    console.log(total);
    localStorage.removeItem("cartCount"); 
    document.getElementById("cart-count").textContent = '0'; 
    alert("Thank you for your purchase, your total was: " + total)
}


// Add event listener to clear cart button
var cartClearB = document.getElementById("clearcart");
// If the user clicks on the clear cart button on the checkout page
// The if statement will activate the cartClear function
if (cartClearB === true) cartClearB.addEventListener('On click', cartClear);

