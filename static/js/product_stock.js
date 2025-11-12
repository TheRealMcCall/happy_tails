document.addEventListener("DOMContentLoaded", function () {
    const select = document.getElementById("variant");
    const warning = document.getElementById("stock-warning");
    if (!select || !warning) return;

    function updateWarning() {
        const option = select.options[select.selectedIndex];
        if (!option) return;

        const stock = parseInt(option.dataset.stock || "0", 10);
        const threshold = parseInt(option.dataset.threshold || "0", 10);

        if (threshold > 0 && stock > 0 && stock <= threshold) {
            warning.textContent = `Hurry! Only ${stock} left in stock.`;
        } else if (stock === 0) {
            warning.textContent = "Sorry, this variant is currently out of stock.";
        } else {
            warning.textContent = "";
        }
    }

    select.addEventListener("change", updateWarning);
    updateWarning();
});