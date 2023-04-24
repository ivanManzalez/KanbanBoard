$(document).ready(function(){
  console.log("getDoneList.js - begin");
  
  $.getJSON('/get_dones', function(data) {
    console.log("getInProgList.js - getJSON data function");
    var tasks = data.tasks;
    var list = $('#done-list');
  
    for (var i = 0; i < tasks.length; i++) {
      var li = document.createElement('li');
      li.className = 'task done draggable';
      li.draggable = true;
      li.innerHTML = tasks[i].title;
      li.id = i;
      li.dataset.status = tasks[i].status;
      // console.log("getInProgList.js - JSON data ", i ,"added to DOM");
      list.append(li);
    }
  console.log("getDoneList.js - end");
  });
});
