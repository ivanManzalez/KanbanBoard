const second = 1000; //ms
var showMessage = 120*second; //ms
var refreshTime = 120*second; //ms


$(document).ready(function () {
    function createTaskLink(task) {
        var link = document.createElement('a');
        link.href = '#';
        link.innerHTML = task.title;
        link.dataset.description = task.description;
        link.dataset.identifier = task.task_id;
        link.dataset.urgency = task.urgency;
        link.dataset.importance = task.importance;
        link.dataset.status = task.status;
        link.classList.add('task-link');
        return link;
    }
    function createDescription(task) {
        var description = document.createElement('p');
        const maxLength = 50;
        description.innerHTML = task.description.substring(0, maxLength) + (task.description.length > maxLength ? '...' : '');;
        description.classList.add('task-desc');
        return description;
    }

    function determineColor(endpoint){
        if(endpoint =="/get_dones"){
            return "metallic_done"

        }else if(endpoint=="/get_todos"){
            return "metallic_todo"

        }else if(endpoint=="/get_in_progs"){
            return "metallic_in_prog"

        }else{
            return ""
        }
    }

    function populateList(endpoint, className, listId) {
        console.log(endpoint + " - begin");

        return new Promise((resolve, reject) => {
            $.getJSON(endpoint, function (data) {
                console.log(endpoint + " - getJSON data function");
                var color = determineColor(endpoint)
                var tasks = data.tasks;
                var list = $('#' + listId);

                tasks.forEach(function (task) {
                    var li = document.createElement('li');
                    li.className = color+ ' task ' + className + ' draggable border-silver';
                    li.draggable = true;
                    li.id = task.task_id;
                    li.dataset.status = task.status;

                    var link = createTaskLink(task);
                    var desc = createDescription(task)
                    li.appendChild(link);
                    li.appendChild(desc);
                    list.append(li);
                });

                console.log(endpoint + " - end");
                resolve();
            });
        });
    }

    function handleTaskLinkClick(event, task) {
        event.preventDefault();
        console.log("Clicked task link");
        $('#submit_new_task').text('Update Task');
        $('#hide_it').show();

        // Populate form with data
        $('#title').val(task.title);
        $('#description').val(task.description);
        $('#urgency').val(task.urgency);
        $('#importance').val(task.importance);
        $('#status').val(task.status);
        $('#identifier').val(task.identifier);

        // Update form action and method
        $('#submit_form').attr('action', '/update_task');
        $('#submit_form').attr('method', 'PUT');

        // Optionally, scroll to the #hide_it element
        $('#hide_it')[0].scrollIntoView();
    }

    // Usage examples and loading of dnd.js after API calls
    Promise.all([
        populateList('/get_dones', 'done', 'done-list'),
        populateList('/get_in_progs', 'in_prog', 'in_prog-list'),
        populateList('/get_todos', 'todo', 'todo-list')
    ]).then(() => {
        console.log('All API calls completed loading data');

        // Dynamically load dnd.js after API calls are done
        var dndScript = document.createElement('script');
        dndScript.src = '/static/js/dnd.js';
        document.body.appendChild(dndScript);
    });

    // EVENT HANDLERS
    $(document).on('click', '.task-link', function (event) {
        var task = {
            title: $(this).text(),
            description: $(this).data('description'),
            urgency: $(this).data('urgency'),
            importance: $(this).data('importance'),
            status: $(this).data('status'),
            identifier: $(this).data('identifier')
        };
        console.log("task", task)
        handleTaskLinkClick(event, task);
    });

    $(document).on('submit', '#submit_form', function (event) {
        event.preventDefault();
        // Serialize form data including 'identifier'
        console.log($(this))
        var formData = $(this).serializeArray();
        console.log("PUT",formData)

        var identifierValue = $('#identifier').val();
        if(!identifierValue){
            console.log(identifierValue, " Must not send update req")
            return 
        }
        var msgDiv = $("#message");
        $.ajax({
            url: $(this).attr('action'),
            type: 'PUT',
            data: formData,
            success: function (response) {
                console.log(response);
                // location.reload();
                $('#hide_it').hide();
                $('#submit_form').attr('action', '/add_task');
                $('#submit_form').attr('method', 'POST');

                $('#submit_new_task').text('Create New Task');
                // Populate form with data
                $('#submit_form')[0].reset();
                
                msgDiv.addClass("success");
                console.log("response",response)
                msgDiv.html(response.message);
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
            },
            error: function (error) {
                console.error('Error deleting task:', error);
                // console.log(error["responseText"])
                msgDiv.addClass("failed");
                console.log(error)
                msgDiv.html(error);
                msgDiv.css("display", "block");

                setTimeout(function() {
                msgDiv.removeClass("failed");
                msgDiv.html("");
                msgDiv.css("display", "none");
                }, showMessage);
            }
        })
    })

    $(document).on('click', '#delete-task-btn', function (event) {
        event.preventDefault();
        var id = $('#identifier').val(); // Assuming identifier exists in a form input field
        var formData = [{ name: 'identifier', value: id }];
        console.log("DELETE",formData);
        var msgDiv = $("#message");
        $.ajax({
            url: '/delete_task', 
            type: 'DELETE',
            data: formData,
            success: function (response) {
                // location.reload();
                $('#hide_it').hide();
                $('#submit_form').attr('action', '/add_task');
                $('#submit_form').attr('method', 'POST');

                $('#submit_new_task').text('Create New Task');
                // Populate form with data
               $('#submit_form')[0].reset();
                 
                msgDiv.addClass("success");
                msgDiv.html(response.message);
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

            },
            error: function (error) {
                console.error('Error deleting task:', error);
                // console.log(error["responseText"])
                msgDiv.addClass("failed");
                console.log(error)
                msgDiv.html(error);
                msgDiv.css("display", "block");

                setTimeout(function() {
                msgDiv.removeClass("failed");
                msgDiv.html("");
                msgDiv.css("display", "none");
                }, showMessage);
                }
            });
        });
});

