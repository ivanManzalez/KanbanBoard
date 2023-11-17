// Define draggables and dropboxes
const draggables = document.querySelectorAll('.draggable');
const dropboxes = document.querySelectorAll('.dropbox');

// Function to handle drag start
function handleDragStart(draggable) {
    // Adds a 'dragging' class to the draggable element
    draggable.classList.add('dragging');
    // Gets the status of the draggable's parent element
    var newStatus = getTaskStatus(draggable.parentElement);
    // Updates the status in the dataset of the draggable
    draggable.dataset.status = newStatus;
}

// Function to handle drag end
function handleDragEnd(draggable) {
    console.log('drag end');
    // Removes the 'dragging' class from the draggable element
    draggable.classList.remove('dragging');
    // Gets the status of the draggable's parent element
    var newStatus = getTaskStatus(draggable.parentElement);
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
    if (container.classList.contains('in_prog')) {
        return 'in_prog';
    } else if (container.classList.contains('dones')) {
        return 'done';
    } else {
        return 'todo';
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

console.log('dnd.js - end');
