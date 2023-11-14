$(document).ready(function(){
  console.log("getTodoList.js - begin");
  
  $.getJSON('/get_todos', function(data) {
    console.log("getTodoList.js - getJSON data function");
    var tasks = data.tasks;
    var list = $('#todo-list');
  
    for (var i = 0; i < tasks.length; i++) {
      var li = document.createElement('li');
      li.className = 'task todo draggable';
      li.draggable = true;
      li.innerHTML = tasks[i].title;
      li.id = i;
      li.dataset.status = tasks[i].status;
      list.append(li);
    }
  console.log("getTodoList.js - end");
  });
});

