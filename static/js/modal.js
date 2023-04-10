$(document).ready(function() {
  // Open modal on button click
  $('#open-modal-btn').click(function() {
    var unhide = document.getElementById("hide_it");
    unhide.style.display = "block";
  });

  // Close modal on click outside or on close button
  $('.modal-wrapper').click(function(e) {
    if (e.target == this || $(e.target).hasClass('close-btn')) {
      var hide = document.getElementById("hide_it");
      hide.style.display = "none";
    }
  });

  // Submit form data using AJAX
  $('#submit_form').submit(function(e) {
    e.preventDefault(); // Prevent page reload
    var formData = $(this).serialize(); // Get form data
    // check if form data is blank
    $.post('/add_task', formData, function(data) {
      // Handle response from server
      console.log(data);
      addTask();
      // Refresh page or update task list
    });

    // hide modal
    var hide = document.getElementById("hide_it");
    hide.style.display = "none";

    // display success/failed message 
  });
});

function addTask() {
    var taskName = $("#task-name").val();
    var taskDescription = $("#task-description").val();

    $.post("/add_task", { task_name: taskName, task_description: taskDescription }, function(response) {
        if (response.success) {
            // display success message to user
            alert(response.message);
        } else {
            // display error message to user
            alert(response.message);
        }
    });
}




