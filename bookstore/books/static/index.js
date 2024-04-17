// Function to increment cart count and update UI
function addToCart() {
    // Increment cart count in localStorage
    let currentQuantity = localStorage.getItem("cartCount") || 0;
    currentQuantity = parseInt(currentQuantity) + 1;
    localStorage.setItem("cartCount", currentQuantity);

    // Update cart count in the UI
    document.getElementById("cart-count").textContent = currentQuantity;

    // Update cart count in checkout page if it exists
    let checkoutCartCount = document.getElementById("checkout-cart-count");
    if (checkoutCartCount) {
        checkoutCartCount.textContent = currentQuantity;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // This function will be executed when the DOM content is fully loaded
    // Add event listener to "Add to Cart" button
    let addToCartButtons = document.querySelectorAll('.addToCart');
    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', addToCart);
    });
});
