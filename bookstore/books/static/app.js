<<<<<<< HEAD
$(document).ready(function() {
    $('.addToCart').click(function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Retrieve product information from the button's data attributes
        var productName = $(this).data('loc-name');
        var productPrice = $(this).data('loc-price');
        var imageUrl = $(this).data('loc-image');
=======

$(document).ready(function() {
    // alert("jQuery is working!");


    $('.addToCart').click(function() {

        var productName = $(this).data('loc-name');
        var productPrice = $(this).data('loc-price');

>>>>>>> upstream/main

        console.log("Adding to cart:");
        console.log("Product Name: " + productName);
        console.log("Product Price: $" + productPrice);
<<<<<<< HEAD
        console.log("Image URL: " + imageUrl);

        // Check if any of the variables are undefined
        if (productName === undefined || productPrice === undefined || imageUrl === undefined) {
            console.error("One or more product details are missing.");
            return;
        }

        // Construct the URL for the checkout page
        var checkoutUrl = "/books/fullmetal/checkout/?name=" + encodeURIComponent(productName) + "&price=" + encodeURIComponent(productPrice) + "&image_url=" + encodeURIComponent(imageUrl);

        // Add any additional actions here, such as updating the UI or making AJAX requests
        
        // Redirect to the checkout page
        window.location.href = checkoutUrl;
    });
});
=======
        
        alert("You added "+productName+" to the cart")
    });

});


>>>>>>> upstream/main
