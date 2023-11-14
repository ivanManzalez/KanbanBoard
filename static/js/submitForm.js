function submitForm(event, endpoint) {
  event.preventDefault(); // Prevent the default form submission
  console.log(event)

  var formData = {};
  
  $("#submit_form").serializeArray().forEach(function (field) {
    formData[field.name] = field.value;
  });
  

  $.ajax({
    type: "POST",
    url: endpoint,
    data: JSON.stringify(formData),
    contentType: "application/json",
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.error(error);
    },
  });
}

function handleAddTaskSubmission(event) {
  console.log("handleAddTaskSubmission - Loaded")
  submitForm(event, "/add_task"); // Specify your endpoint here
  }

export { handleAddTaskSubmission };
