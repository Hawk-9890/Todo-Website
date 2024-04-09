let todoInput = document.getElementById("todoInput");
let todoSubmit = document.getElementById("todoSubmit");
let todoList = document.getElementById("todoList");
let editTodoContainer = document.getElementById("container")
let overlay = document.getElementById("overlay")
let editInput = document.getElementById("editInput")
let editSubmit = document.getElementById("editSubmit")

todoSubmit.addEventListener("click", function(event) {
    event.preventDefault();

    const todoListElement = document.createElement("li");
    const deleteButton = document.createElement("button");
    const editButton = document.createElement("button");

    if (todoInput.value !== ""){
        todoListElement.textContent = todoInput.value.trim();

        deleteButton.innerHTML = '<span>&#10006;</span>';
        deleteButton.id = "deleteButton";

        editButton.innerHTML = '<span>&#9998;</span>';
        editButton.id = "editButton"

        deleteButton.addEventListener("click", function() {
            todoList.removeChild(todoListElement);
        })

        editButton.addEventListener("click", function() {
            editTodoContainer.style.display = "block"
            overlay.style.display = "block"

            editSubmit.addEventListener("click", function(event) {
                event.preventDefault();

                if (editInput.value !== ""){
                    todoListElement.textContent = editInput.value.trim()
                    
                    todoListElement.appendChild(deleteButton);
                    todoListElement.appendChild(editButton);
                }

                editTodoContainer.style.display = "none"
                overlay.style.display = "none"
            })

        })

        todoList.appendChild(todoListElement);
        todoListElement.appendChild(deleteButton);
        todoListElement.appendChild(editButton);
    } 
})
