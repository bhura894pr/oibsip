document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('task-title').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            addTask();
        }
    });
    document.getElementById('task-desc').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            addTask();
        }
    });

    updatePendingTasksBackground();
});

function addTask() {
    const taskTitleInput = document.getElementById('task-title');
    const taskDescInput = document.getElementById('task-desc');
    const taskTitle = taskTitleInput.value.trim();
    const taskDesc = taskDescInput.value.trim();
    
    if (taskTitle === '' || taskDesc === '') {
        alert('Please enter both a title and a description.');
        return;
    }
    
    const taskItem = createTaskElement(taskTitle, taskDesc);
    document.getElementById('pending-tasks').appendChild(taskItem);
    
    taskTitleInput.value = '';
    taskDescInput.value = '';

    updatePendingTasksBackground();
}

function createTaskElement(taskTitle, taskDesc) {
    const taskItem = document.createElement('li');
    const taskContent = document.createElement('div');
    
    const taskTitleElem = document.createElement('h3');
    taskTitleElem.textContent = taskTitle;
    
    const taskDescElem = document.createElement('p');
    taskDescElem.textContent = taskDesc;
    
    taskContent.appendChild(taskTitleElem);
    taskContent.appendChild(taskDescElem);
    
    const actions = document.createElement('div');
    actions.className = 'task-actions';
    
    const completeButton = document.createElement('button');
    completeButton.className = 'complete';
    completeButton.onclick = () => completeTask(taskItem);
    
    const deleteButton = document.createElement('button');
    deleteButton.className = 'delete';
    deleteButton.onclick = () => deleteTask(taskItem);
    
    actions.appendChild(completeButton);
    actions.appendChild(deleteButton);
    
    taskItem.appendChild(taskContent);
    taskItem.appendChild(actions);
    
    return taskItem;
}

function completeTask(taskItem) {
    const completedTasksList = document.getElementById('completed-tasks');
    
    taskItem.querySelector('.task-actions').remove();
    taskItem.classList.add('completed');
    
    const completedTime = document.createElement('p');
    completedTime.className = 'completed-time';
    completedTime.textContent = `Completed at: ${new Date().toLocaleString()}`;
    taskItem.appendChild(completedTime);
    
    const actions = document.createElement('div');
    actions.className = 'task-actions';
    
    const removeButton = document.createElement('button');
    removeButton.className = 'remove';
    removeButton.onclick = () => removeTaskPermanently(taskItem);
    
    actions.appendChild(removeButton);
    taskItem.appendChild(actions);
    completedTasksList.appendChild(taskItem);
    
    updatePendingTasksBackground();
}

function deleteTask(taskItem) {
    taskItem.remove();
    
    updatePendingTasksBackground();
}

function removeTaskPermanently(taskItem) {
    if (confirm('Are you sure you want to Remove this Completed task Permanently?')) {
        taskItem.remove();
    }
}

function updatePendingTasksBackground() {
    const pendingTasks = document.getElementById('pending-tasks').children;
    
    for (let i = 0; i < pendingTasks.length; i++) {
        pendingTasks[i].style.backgroundColor = '#f57979';
    }
    
    const completedTasks = document.getElementById('completed-tasks').children;
    
    for (let i = 0; i < completedTasks.length; i++) {
        completedTasks[i].style.backgroundColor = '#83fca1';
    }
}
