
$(document).ready(function(){
console.log('dnd.js - begin');
const draggables = document.querySelectorAll('.draggable');
const dropboxes = document.querySelectorAll('.dropbox');

console.log('dnd.js - draggables loaded');

// draggable - Event listeners
draggables.forEach(draggable => {
  // console.log(draggable.id);
  draggable.addEventListener('dragstart', () => {
    // console.log('drag start')
    draggable.classList.add('dragging');
    var newStatus = getTaskStatus(draggable.parentElement);
    draggable.dataset.status=newStatus;
    // li.dataset.status = 'todo';
  })

  draggable.addEventListener('dragend', () => {
    console.log('drag end')
    draggable.classList.remove('dragging')
    var newStatus = getTaskStatus(draggable.parentElement);
    draggable.dataset.status=newStatus;
    // draggable.classList.add(newStatus);
  })
})

// dropboxes - Event listeners
dropboxes.forEach(dropbox => {
  
  dropbox.addEventListener('dragover', e => {
    // console.log('dragover')
    // by default - dropping is disabled
    e.preventDefault();
    const afterElement = getDragAfterElement(dropbox, e.clientY)
    // get currently dragging element
    const draggable = document.querySelector('.dragging')
    // console.log("draggable = ",draggable);
    // console.log("afterElement = ", afterElement);

    if (afterElement == null){
    // append dragged element to end of dropbox
    dropbox.appendChild(draggable)
    }else{
      dropbox.insertBefore(draggable, afterElement)
    }
  })
})

//  determine which elems surround dragging in dropbox
// determines mouse position while dragging and return
// which ever elem our mouse position is directly after
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

function getTaskStatus(container){
  if (container.classList.contains('in_prog')){
      // console.log('in progress bucket');
      return 'in_prog';

    }else if(container.classList.contains('dones')){
      // console.log('dones bucket');
      return 'done';
    }
    else{
      // console.log('todo bucket');
      return 'todo';
    }
}//cassandra ql

console.log('dnd.js - end');
});



// 