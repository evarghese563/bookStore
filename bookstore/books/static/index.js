function addToCheckout(imageUrl) {
    
    // Increment cart count in localStorage
    let currentQuantity = localStorage.getItem("cartCount") || 0;
    currentQuantity = parseInt(currentQuantity);
    localStorage.setItem("cartCount", currentQuantity);

    document.getElementById("cart-count").textContent = currentQuantity;

    // Get item details
    let itemName = "Dragon Ball (Vizbig Edition), Vol. 1";

    // Create a new row for the item
    let newRow = document.createElement("tr");

    // Populate the row with item details
    newRow.innerHTML = `
        <td>${itemName}</td>
        <td>1</td>
        <td><img src="${imageUrl}" alt="${itemName}" width="100"></td>
        <td><span style="color: orange;" id="cart-count">${currentQuantity}</span></td>
        `;

    // Add the new row to the table
    let cartItems = document.getElementById("cart-items");
    cartItems.appendChild(newRow);
}

document.addEventListener('DOMContentLoaded', function() {
    // This function will be executed when the DOM content is fully loaded
    addToCheckout(imageUrl);
});



function addToCart() {
    // Increment cart count in localStorage
    let currentQuantity = localStorage.getItem("cartCount") || 0;
    currentQuantity = parseInt(currentQuantity) + 1;
    localStorage.setItem("cartCount", currentQuantity);

    document.getElementById("cart-count").textContent = currentQuantity;
}