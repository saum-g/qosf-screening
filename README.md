# Description

In this repository I have attempted screening task 1 for qosf mentorship program applications. 

I have created a random 16 length vector and normalised it to produce my target state. I have used a gradient descent algorithm with adaptive step sizes to minimise the distance of the state produced by the circuit with the target state. In order to account for non-convexity in the cost function, I repeated the experiment for each layer with parameters initialised randomly with 10 different seeds. As a part of the bonus question I tried replacing the rx gate of odd blocks with ry gates. 

## Results
The results obtained for both the circuits show that the cost decreases very fast with the number of layers initially, but then becomes constant for higher layers. 
The performance of the two circuits differ slightly and it the modified circuit does not perform as well as the original one. The distance achieved with the modified circuit decreases slowly with the number of layers in comparison to the original circuit though the results converge for higher layers. 

Plots for 10 layers of the original circuit and comparison of the two circuits for upto 8 layers have been added to the plots/ folder
