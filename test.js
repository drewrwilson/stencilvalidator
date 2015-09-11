var cv = require('opencv');
var matrix;
var matrixOutput = new cv.Matrix;


var lowThresh = 0;
var highThresh = 100;
var nIters = 2;
var maxArea = 2500;

cv.readImage('stencil.png', function(err, im) {
  if (err) throw err;
  matrix = im;
});

console.log(matrix);

//invert the image
matrix.bitwiseNot(matrixOutput);

//save image to file
matrix.save('YO-CJ-INVERTED.png');

matrix.canny(lowThresh, highThresh);

matrix.save('YO-CJ-INVERTED-post-thresh.png');

//take the contour of the image
contours = matrix.findContours();
console.log('Number of contours: ');
console.log(contours.size());

  //count the countours
