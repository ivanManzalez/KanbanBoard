

function generateImageUrl(width, height) {
  return `https://picsum.photos/${width}/${height}/?grayscale&blur=10`
}

window.onload = function() {
    // Replace 'background/url' with your actual image URL
    var w = window.innerWidth;
    var h = window.innerHeight;
    var url = generateImageUrl(w, h)
    document.documentElement.style.backgroundImage = `url(${url})`;
  };