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
    
    $.post('/add_task', formData, function(data) {
      // Handle data response from server
      var data = JSON.parse(data);
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
        msgDiv.removeClass("failed");
        msgDiv.html("");
        msgDiv.css("display", "none");
      }, 3000);

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



