

$(document).ready(function() {
  // Open modal on button click
  $('#open-modal-btn').click(function() {
    var unhide = document.getElementById("hide_it");
    unhide.style.display = "block";
  });

  // Close modal on click outside or on close button
  $('.modal-wrapper').click(function(e) {
    if (e.target == this || $(e.target).hasClass('close-btn') || e.target== $('#close-btn-icon')[0]) {
      var hide = document.getElementById("hide_it");
      hide.style.display = "none";
      $('#submit_new_task').text('Create New Task');
      $('#delete-task-btn').hide()
      $('#submit_form').attr('action', '/add_task');
      $('#submit_form').attr('method', 'POST');
      $('#submit_form')[0].reset();
    }
  });

  // Submit form data using AJAX
  $(document).on('submit', '#submit_form', function (e) {
  // $('#submit_form').on('click', '#submit_new_task', function (e) {
  // $('#submit_form').submit(function(e) {
    e.preventDefault(); // Prevent page reload
    
    var identifierValue = $('#identifier').val();
    if(identifierValue){
      console.log(identifierValue, " Must not send create req")
      return 
    }

    var formData = $(this).find(':input').not('[name="identifier"]').serialize(); // Get form data, excluding identifier
      
    $.post('/add_task', formData, function(data) {
      // Handle data response from server
      var data = JSON.parse(data);
      console.log(data)
      var msgDiv = $("#message");

      if (data.success) {
            // display success message to user
            msgDiv.addClass("success");
        } else {
            // display error message to user
            msgDiv.addClass("failed");
        }
      msgDiv.html(data.message);
      msgDiv.css("display", "block");

      // hide the message after 3 seconds
      setTimeout(function() {
      msgDiv.removeClass("success");
      msgDiv.html("");
      msgDiv.css("display", "none");
      }, showMessage);
      setTimeout(function() {
      location.reload();
      }, refreshTime);

      // Refresh page or update task list
      
      // Clear the form fields
    $('#submit_form')[0].reset();
    });

    // hide modal
    var hide = document.getElementById("hide_it");
    hide.style.display = "none";

    // display success/failed message 
    
  });
});



