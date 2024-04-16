
$(document).ready(function() {
    // alert("jQuery is working!");


    $('.addToCart').click(function() {

        var productName = $(this).data('loc-name');
        var productPrice = $(this).data('loc-price');


        console.log("Adding to cart:");
        console.log("Product Name: " + productName);
        console.log("Product Price: $" + productPrice);


        var items = {
            Name: productName,
            Price: productPrice
        };

        alert("You added "+productName+" to the cart")
    });

});

function toCartDB(items){
    const FileSystem = require("fs");
    FileSystem.writeFile('cart.json', JSON.stringify(items), (error) => {
       if (error) throw error;
     });
};

