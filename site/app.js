let cart = [];
let currentImageIndex = 0;
let images = [];

function addToCart(productName, price) {
    cart.push({productName, price});
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById("cartItems");
    cartItems.innerHTML = "";
    cart.forEach((item, index) => {
        cartItems.innerHTML += `<p>${item.productName} - ${item.price} ₽ <button onclick="removeFromCart(${index})">Remove</button></p>`;
    });
}

function removeFromCart(index) {
    cart.splice(index, 1);
    updateCart();
}

function showImageGallery(imageArray) {
    images = imageArray;
    currentImageIndex = 0;
    document.getElementById("galleryImage").src = images[currentImageIndex];
    document.getElementById("imageGallery").style.display = "flex";
}

function closeImageGallery() {
    document.getElementById("imageGallery").style.display = "none";
}

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    document.getElementById("galleryImage").src = images[currentImageIndex];
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    document.getElementById("galleryImage").src = images[currentImageIndex];
}

function checkout() {
    const total = cart.reduce((sum, item) => sum + item.price, 0);
    alert(`Total: ${total} ₽. Pay with cryptocurrency.`);
    // Здесь можно добавить интеграцию с платежной системой.
}
