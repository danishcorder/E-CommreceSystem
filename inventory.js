const products = {};

document.addEventListener("DOMContentLoaded", function () {
    const productForm = document.getElementById("productForm");
    const sellForm = document.getElementById("sellForm");

    productForm.onsubmit = function (e) {
        e.preventDefault();

        const name = document.getElementById("name").value;
        const product_id = document.getElementById("product_id").value;
        const price = parseFloat(document.getElementById("price").value);
        const quantity = parseInt(document.getElementById("quantity").value);
        const category = document.getElementById("category").value;
        const manufacturer = document.getElementById("manufacturer").value;

        if (products[product_id]) {
            alert("Product ID already exists.");
            return;
        }

        products[product_id] = { name, price, quantity, category, manufacturer };
        updateTable();
        productForm.reset();
    };

    sellForm.onsubmit = function (e) {
        e.preventDefault();

        const id = document.getElementById("sell_id").value;
        const qty = parseInt(document.getElementById("sell_quantity").value);

        if (products[id]) {
            if (products[id].quantity >= qty) {
                products[id].quantity -= qty;
                const total = (qty * products[id].price).toFixed(2);
                document.getElementById("invoiceOutput").textContent =
                    `Invoice: Sold ${qty} x ${products[id].name} = $${total}`;
                updateTable();
            } else {
                alert("Not enough stock!");
            }
        } else {
            alert("Product ID not found.");
        }
    };
});

function updateTable() {
    const tbody = document.getElementById("productTable").querySelector("tbody");
    tbody.innerHTML = "";

    for (let id in products) {
        const p = products[id];
        const row = `<tr>
            <td>${p.name}</td>
            <td>${id}</td>
            <td>$${p.price.toFixed(2)}</td>
            <td>${p.quantity}</td>
            <td>${p.category}</td>
            <td>${p.manufacturer}</td>
        </tr>`;
        tbody.innerHTML += row;
    }
}
