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
      li.id = tasks[i].id;
      li.dataset.status = tasks[i].status;

      var link = document.createElement('a');
      link.href = '#' // Set the link destination
      link.innerHTML = tasks[i].title;
      
      // console.log("getInProgList.js - JSON data ", i ,"added to DOM");
      li.append(link);
      list.append(li);
    }
  console.log("getDoneList.js - end");
  });
});
