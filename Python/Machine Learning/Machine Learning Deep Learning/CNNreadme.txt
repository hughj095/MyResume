

CNN is Convolutional Neural Network

You have an input image with pixels, and a feature detector which is 3x3.
Then multiply each pixel value by it's feature detector partner, resulting in a new feature map.

Different feature maps have different results on the original image (ie. Edge Detect)

The highest number in the resulting feature map is an integral part of machine learning image detection.

The ReLU layer applies the Rectifier model to Convolutional Layer feature maps.  It breaks up 
linearity by removing the negative (black) pixels.

Max Pooling finds the max value in a set of pixels, and it only keeps that number.  This helps when 
images are not stadardized, have different resolutions, are stretched, etc.

Step 1 is Convolution, Step 2 is Pooling

Step 3 is Flattening.  Flattening stacks the 3x3 pixel example into a 1x9 rows of pixels.

Step 4 is Full Connection which connects each layer and neuron and back-propogates to adjust the weights.

Finally, The Output neurons take the highest weighted neuarons and multiply their values to 
get the final probablility of the image (is a dog or cat).












