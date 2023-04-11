
$(document).ready(function(){
  $.getJSON('/get_tasks', function(data) {
    var names = data.names;
    var list = $('#names-list');

    for (var i = 0; i < names.length; i++) {
      var li = $('<li>').text(names[i]);
      list.append(li);
            }
        });
      });
