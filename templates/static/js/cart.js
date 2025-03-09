let cart = [];

function addToCart(id, name, price) {
    cart.push({ id, name, price });
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Added to cart!");
}

window.onload = function () {
    cart = JSON.parse(localStorage.getItem("cart")) || [];
    let cartItems = document.getElementById("cart-items");
    let total = 0;

    if (cartItems) {
        cart.forEach(item => {
            let li = document.createElement("li");
            li.innerText = `${item.name} - $${item.price}`;
            cartItems.appendChild(li);
            total += item.price;
        });

        document.getElementById("cart-total").innerText = total;
    }
};
