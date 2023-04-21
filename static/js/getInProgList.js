$(document).ready(function(){
  console.log("getInProgList.js - begin");
  
  $.getJSON('/get_in_progs', function(data) {
    console.log("getInProgList.js - getJSON data function");
    var tasks = data.tasks;
    var list = $('#in_prog-list');
  
    for (var i = 0; i < tasks.length; i++) {
      var li = document.createElement('li');
      li.className = 'task in_prog draggable';
      li.draggable = true;
      li.innerHTML = tasks[i];
      li.id = i;
      li.dataset.status = 'in_prog';
      // console.log("getInProgList.js - JSON data ", i ,"added to DOM");
      list.append(li);
    }
  console.log("getInProgList.js - end");
  });
});