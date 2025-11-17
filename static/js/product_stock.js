/* jshint esversion: 11 */

/** Handle product variant stock warnings and dynamic price display. */
document.addEventListener("DOMContentLoaded", function () {
    const select = document.getElementById("variant");
    const warning = document.getElementById("stock-warning");
    const priceDisplay = document.getElementById("price-display");
    const quantityInput = document.getElementById("qty");

    if (!select) return;

    /** Update the low stock / out of stock warning message. */
    function updateWarning() {
        const option = select.options[select.selectedIndex];
        if (!option || !warning) return;

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

    if (!priceDisplay) return;

    // Determine the minimum unit price from all variant options as a fallback.
    let minPrice = null;
    for (let i = 0; i < select.options.length; i++) {
        const opt = select.options[i];
        const priceAttr = opt.getAttribute("data-price");
        if (!priceAttr) continue;

        const val = Number(priceAttr);
        if (!Number.isNaN(val)) {
            if (minPrice === null || val < minPrice) {
                minPrice = val;
            }
        }
    }

    // Get the current quantity, defaulting to 1 if the input is invalid.
    function getQty() {
        if (!quantityInput) return 1;
        const q = Number(quantityInput.value || "1");
        if (Number.isNaN(q) || q <= 0) return 1;
        return q;
    }

    /** Update displayed price based on selected variant and quantity. */
    function updatePrice() {
        let unitPrice = null;
        const option = select.options[select.selectedIndex];

        if (option && option.value) {
            const priceAttr = option.getAttribute("data-price");
            if (priceAttr) {
                const v = Number(priceAttr);
                if (!Number.isNaN(v)) {
                    unitPrice = v;
                }
            }
        } else if (minPrice !== null) {
            unitPrice = minPrice;
        }

        if (unitPrice === null) {
            priceDisplay.textContent = "";
            return;
        }

        const lineTotal = unitPrice * getQty();
        priceDisplay.textContent = "£" + lineTotal.toFixed(2);
    }

    if (minPrice !== null) {
        updatePrice();
    }

    // Recalculate price when variant or quantity changes.
    select.addEventListener("change", updatePrice);
    if (quantityInput) {
        quantityInput.addEventListener("input", updatePrice);
        quantityInput.addEventListener("change", updatePrice);
    }
});