document.addEventListener('DOMContentLoaded', function() {
    function addToCart() {
        // Get's product data from the html form
        var productName = this.getAttribute('data-loc-name');
        var productPrice = this.getAttribute('data-loc-price');

        console.log("Adding to cart:");
        console.log("Product Name: " + productName);
        console.log("Product Price: $" + productPrice);

        // Increcments the cart count in the local storage
        let cartCount = parseInt(localStorage.getItem("cartCount")) || 0;
        cartCount++;
        localStorage.setItem("cartCount", cartCount);

        // Updates the cart count in the UI
        document.getElementById("cart-count").textContent = cartCount;

        // Show confirmation message
        alert("You added " + productName + " to the cart");
    }

    // Every time the add to cart button is clicked, the addToCart function is activated
    var addToCartButtons = document.querySelectorAll('.addToCart');
    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', addToCart);
    });

    // gets cartcount from local storage and sets to initialized count
    var initializedCount = parseInt(localStorage.getItem("cartCount")) || 0;
    // sets all html elements with id cart-count to the value of initializedCount
    document.getElementById("cart-count").textContent = initializedCount;
});
// ----------------------------------------------------------------------------------
function clearCart() {
    // Removes cartCount from local storage
    localStorage.removeItem("cartCount"); 
    // sets all html elements with id cart-count to 0
    document.getElementById("cart-count").textContent = "0"; 
    //alerts user that cart was cleared
    alert("Cart cleared successfully");
}

// Add event listener to clear cart button
var clearCartB = document.getElementById("clear-cart-btn");
// If the user clicks on the clear cart button on the checkout page
// The if statement will activate the clearCart function
if (clearCartB) {
    clearCartB.addEventListener('On click', clearCart);
}

