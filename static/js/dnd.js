// Define draggables and dropboxes
const draggables = document.querySelectorAll('.draggable');
const dropboxes = document.querySelectorAll('.dropbox');

// Function to handle drag start
function handleDragStart(draggable) {
    // Adds a 'dragging' class to the draggable element
    draggable.classList.add('dragging');
    // Gets the status of the draggable's parent element
    var currStatus = getTaskStatus(draggable.parentElement);
    console.log(draggable.parentElement)
    // Remove Bucket Color
    var color = determineColor(currStatus)
    console.log("Remove color:", color)
    draggable.classList.remove(color);
    draggable.classList.remove(currStatus);
    console.log("Remove color:", color)
}

// Function to handle drag end
function handleDragEnd(draggable) {
    console.log('drag end');
    // Removes the 'dragging' class from the draggable element
    draggable.classList.remove('dragging');
    // Gets the status of the draggable's parent element
    var newStatus = getTaskStatus(draggable.parentElement);

    // Add New Bucket Color
    var newColor = determineColor(newStatus);
    console.log("New color:", newColor)
    draggable.classList.add(newColor);
    draggable.classList.add(newStatus);
    // Updates the status in the dataset of the draggable
    draggable.dataset.status = newStatus;
}

// Event listeners for draggables
draggables.forEach(draggable => {
    // Adds dragstart and dragend event listeners to each draggable element
    draggable.addEventListener('dragstart', () => {
        handleDragStart(draggable);
    });

    draggable.addEventListener('dragend', () => {
        handleDragEnd(draggable);
    });
});

// Event listener for dropboxes
dropboxes.forEach(dropbox => {
    // Adds a dragover event listener to each dropbox element
    dropbox.addEventListener('dragover', e => {
        e.preventDefault();
        const afterElement = getDragAfterElement(dropbox, e.clientY);
        const draggable = document.querySelector('.dragging');

        // Checks and handles the position of the dragged element within the dropbox
        if (afterElement == null) {
            dropbox.appendChild(draggable);
        } else {
            dropbox.insertBefore(draggable, afterElement);
        }
    });
});

// Function to determine the element's status
function getTaskStatus(container) {
    // Returns the status of the element based on its parent's class
    if (container.classList.contains('in_progs')) {
        return 'in_prog';
    } else if (container.classList.contains('dones')) {
        return 'done';
    } else if (container.classList.contains('todos')) {
        return 'todo';
    }else {
        return '';
    }
}

// Function to determine the element the mouse is directly after in the dropbox
function getDragAfterElement(container, y){
  // determine all element in current container
  // that is not currently being dragged
  const draggableElements = [...container.querySelectorAll('.draggable:not(.dragging)')]
  if (draggableElements.length === 0) {
    // console.log("No draggable elements")
    return null;
  }
  // determines which element is directly below dragging element
  return  draggableElements.reduce((closest, child) => {
    const box = child.getBoundingClientRect()
    const offset = y - box.top - box.height/2
    if (offset < 0 && offset > closest.offset){
      return { offset:offset, element:child }
    } else{
      return closest
    }
  },{offset:Number.NEGATIVE_INFINITY}).element
}

function determineColor(status){
    console.log(status)
    
    if(status =="done"){
        return "metallic_done"
    }
    else if(status=="todo"){
        return "metallic_todo"
    }
    else if(status=="in_prog"){
        return "metallic_in_prog"
    }
    else{
        return ""
    }
}

console.log('dnd.js - end');
