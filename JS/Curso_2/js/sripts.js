//funcao que adiciona tarefa
function addTask() {
    // Titulo
    const taskTitle = document.querySelector("#task-title").value;

    if (taskTitle) {
        //Clona template
        const template = document.querySelector(".template");

        const newTask = template.cloneNode(true);

        //Adiciona titulo
        newTask.querySelector(".task-title").textContent = taskTitle;

        //Remover as classes desnecessarias
        newTask.classList.remove("template");
        newTask.classList.remove("hide");

        //Adiciona tarefa na lista
        const list = document.querySelector("#task-list");

        list.appendChild(newTask);

        //adicionar evento de remover
        const removeBtn = newTask.querySelector(".remove-btn").addEventListener("click",function(){
            removeTask(this);
        })

        //adicionar evento de completar tarefa
        const doneBtn = newTask.querySelector(".done-btn").addEventListener("click",function(){
            completeTask(this);
        })

        //Limpar texto
        document.querySelector("#task-title").value = "";

    } else {

    }
}

//funcao de remover tarefa
function removeTask(task) {
    task.parentNode.remove(true);
}

//funcao de completar tarefa
function completeTask(task) {
    const taskToComplete = task.parentNode;

    taskToComplete.classList.toggle("done");
}

//Evento de adicionar tarefa
const addBtn = document.querySelector("#add-btn");

addBtn.addEventListener("click",function(e){
    e.preventDefault();
    
    addTask();
})