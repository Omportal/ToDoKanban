var csrfcookie = function () {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

function onDragStart(event) {
    event
        .dataTransfer
        .setData('text/plain', event.target.id);
}

function onDragOver(event) {
    event.preventDefault();
}

function onDrop(event) {
    const id = event
        .dataTransfer
        .getData('text');
    const draggableElement = document.getElementById(id);
    const dropzone = event.target;
    const progress = dropzone.getAttribute('name')
    dropzone.appendChild(draggableElement);
    var formData = new FormData();

    // добавить к пересылке ещё пару ключ - значение

    formData.append("progress_choice", `${progress}`);
    formData.append("id", `${id}`);

    // отослать
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/', true);
    // xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    xhr.setRequestHeader('X-CSRFToken', csrfcookie());
    xhr.send(formData);
    event
        .dataTransfer
        .clearData();
}