document.addEventListener('DOMContentLoaded', function() {
    const messageBox = document.getElementById('custom-message-box');
    const closeButton = messageBox.querySelector('.message-box-close');
    
    closeButton.addEventListener('click', function() {
        messageBox.classList.add('fade-out');
        
        messageBox.addEventListener('transitionend', function() {
            messageBox.remove();
        });
    });
});