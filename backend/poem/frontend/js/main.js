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

document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("copy-link-btn");
    const confirm = document.getElementById("copy-confirm");

    btn.addEventListener("click", function () {
        const url = window.location.href;
        navigator.clipboard.writeText(url).then(() => {
            confirm.classList.add("show");

            setTimeout(() => {
                confirm.classList.remove("show");
            }, 2000);
        }).catch(() => {
            alert("Не удалось скопировать ссылку.");
        });
    });
});
