/* jshint esversion: 11 */

document.addEventListener('click', function (e) {
    const btn = e.target.closest('[data-qty-btn]');
    if (!btn) return;

    const form = btn.closest('form');
    if (!form) return;

    const input = form.querySelector('input[name="qty"]');
    if (!input) return;

    const min = parseInt(input.min || '0', 10);
    const cur = parseInt(input.value || '0', 10);
    const next = btn.dataset.qtyBtn === 'inc' ? cur + 1 : cur - 1;

    input.value = Math.max(min, next);
    form.submit();
});

document.addEventListener('change', function (e) {
    if (e.target.matches('input[name="qty"]')) {
        const form = e.target.closest('form');
        if (form) form.submit();
    }
});