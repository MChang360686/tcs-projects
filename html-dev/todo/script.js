function addTask() {
    const taskInput = document.getElementById("taskInput");
    const taskList = document.getElementById("taskList");

    if (taskInput.value.trim() !== "") {
        const newTask = document.createElement("li");
        newTask.innerHTML = `
            <input type="checkbox" onchange="toggleTask(this)">
            <span>${taskInput.value}</span>
            <button onclick="removeTask(this)">Remove</button>
        `;
        taskList.appendChild(newTask);
        taskInput.value = "";
    }
}

function toggleTask(checkbox) {
    const taskText = checkbox.nextElementSibling;
    if (checkbox.checked) {
        taskText.classList.add("completed");
    } else {
        taskText.classList.remove("completed");
    }
}

function removeTask(button) {
    const taskItem = button.parentNode;
    taskItem.parentNode.removeChild(taskItem);
}
