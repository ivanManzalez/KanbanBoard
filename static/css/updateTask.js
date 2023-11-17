$(document).ready(function() {
  // Event listener for form submission
  $('#submit_form').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Check if the task has an ID (retrieved from the database)
    var taskId = $('.task li').data('id');
    
    // Set the form action based on the task ID existence
    var formAction = taskId ? '/update_task' : '/add_task'; // Update if task ID exists, otherwise create

    // Set the form action dynamically
    $(this).attr('action', formAction);

    // Submit the form
    $(this)[0].submit();
  });

  // Event listener to open #hide_it on link click
  $('ul').on('click', 'a', function(event) {
    event.preventDefault();
    $('#hide_it').show(); // Display the #hide_it element

    // Populate form with data based on the clicked link's dataset values
    $('#title').val($(this).data('id'));
    $('#description').val($(this).data('description'));
    // Add other dataset values to respective form fields

    // Set the task ID in a data attribute of the form
    $('#submit_form').data('task-id', $(this).data('id'));

    // Optionally, scroll to the #hide_it element
    $('#hide_it')[0].scrollIntoView();
  });

  // Other code for populating lists and handling drag and drop functionality
});
