var imageUrls = ["python.png","php.png","mysql.png"];
var previousButton = document.getElementById("previousButton");
var nextButton = document.getElementById("nextButton");
  
 
var currentImageIndex = 0;
  

function showCurrentImage() {
  galleryImage.src = imageUrls[currentImageIndex];
}
  
  
function showPreviousImage() {
  currentImageIndex--;
  if (currentImageIndex < 0) {
    currentImageIndex = imageUrls.length - 1;
  }
  showCurrentImage();
}

function showNextImage() {
  currentImageIndex++;
  if (currentImageIndex >= imageUrls.length) {
    currentImageIndex = 0;
  }
  showCurrentImage();
}


  previousButton.addEventListener("click", showPreviousImage);
  nextButton.addEventListener("click", showNextImage);
  
 
  showCurrentImage();
  