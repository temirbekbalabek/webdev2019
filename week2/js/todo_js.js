function button_clicked() {

    const input_text = document.getElementById('task_id');
    const text = input_text.value;
    if (!text) {
      alert('Please type something to add');
      return;
    }
  
    const task = document.createElement('div');
    task.className = 'task';
  
    const divbox = document.createElement('div');
    divbox.className = 'check';
    const box = document.createElement('input');
    box.type = 'checkbox';
    box.onchange = tickTask;
  
    divbox.appendChild(box);
    task.appendChild(divbox);
    
  
    const divbin = document.createElement('div');
    divbin.className = 'delete';
    const bin = document.createElement('input');
    bin.type = 'image';
    bin.src = 'korzina.jpg';
    bin.onclick = deleteTask;
  
    divbin.appendChild(bin);
    task.appendChild(divbin);
  
    const taskText = document.createElement('p');
    taskText.innerHTML = text;
  
    task.appendChild(taskText);
  
    document.getElementById('tasks').appendChild(task);
    input.value = '';
  }
  
  function deleteTask(e) {
    const task = e.target.parentElement.parentElement;
    const tasks = task.parentElement;
    tasks.removeChild(task);
  }

function tickTask(e) {
  const checkbox = e.target;
  const text = checkbox.parentElement.parentElement.childNodes[2];
  if (checkbox.checked) {
    text.style.textDecoration = 'line-through';
  }
  else {
    text.style.textDecoration = 'none';
  }
}