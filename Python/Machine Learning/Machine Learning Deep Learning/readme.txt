Deep Learning has been around for a long time, but processing power has only
    recently been available to allow automation of DL.

Geoffrey Hinton is the Godfather of DL, works at Google

Many input values and few output layers, also hidden layers in-between
    There may be more hidden layers than input layers, and multiple
    hidden layers

Calcs the weighted sum (inputs may have weights) of the inputs and uses the activation function to 
    produce the output

The Threshold function is: if x > 0, then x = 1, else 0
The Sigmoid function is: x = 1/(1+e^-x), used to predict probability
The Rectifier function is: x = max(x,0), used most in DL
The Hyperbolic Tangent fuction is: goes from -1 to 1

In the hidden layer is where the Rectifier functions could be applied,
    then the output layer could apply the Sigmoid, for example

NNs are more powerful than a multiple linear regressions (multiple inputs)
    because of the hidden layer.  The hidden layer picks (via learning) 
    only certain combinations of inputs, to create multi-dimensional inputs, to create 
    a new input value based on the old input values.

A NN learns by comparing the predicted output value to the actual value, then updates
    the weights by a cost function (C = 0.5(y-hat - y)^2), this is 
    called back-propogation

Gradient Descent finds the best weights which minimizes the Cost function.
    The best weight has a zero slope.

Sometimes a zero slope weight is not the best weight, so a Stochastic 
    Gradient Descent is necessary, which adjust the weights everytime
    a neuron is calculated.  This results in different output values
    everytime the NN is run.

Weights are initially set at zero or near zero, randomly.

An Epoch is one set of outputs after the NN is run.






     








