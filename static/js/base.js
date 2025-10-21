//** Dismisses alert messages automatically after a delay */ 
document.addEventListener("DOMContentLoaded", function () {
    const messageBox = document.getElementById('messages');
    if (messageBox) {
        setTimeout(() => {
            messageBox.style.display = 'none';
        }, 4000);
    }
});