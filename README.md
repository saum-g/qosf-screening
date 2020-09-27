# Description

In this repository I have attempted screening task 1 for qosf mentorship program applications. 

I have created a random 16 length vector and normalised it to produce my target state. I have used a gradient descent algorithm with adaptive step sizes to minimise the distance of the state produced by the circuit with the target state. In order to account for non-convexity in the cost function, I repeated the experiment for each layer with 10 randomly initialised set of parameters. As a part of the bonus question I tried replacing the rx gate of odd blocks with ry gates.

In order to find out the extent to which the target state affects our obtained cost I ran the experiment over different seeds for calculating the target state and then averaged over the least cost obtained for each target state.

## Results
The least distance obtained seems to decrease exponentially with the number of layers used. Thus, though the distance decreases very fast with the number of layers initially, it becomes almost constant for higher layers. A plot of least distance obtained versus the number of layers for upto 10 layers of the original circuit and minimum calculated over 10 randomly initialised parameters is present in plots/least_dist_vs_layers.png . 

Using ry gates in place of rx gates still achieves the exponential decrease in cost as can be seen in the plot for upto 8 layers of both circuits at plots/least_dist_vs_layers_diff_circuits.png . The distance achieved with the modified circuit decreases slowly with the number of layers in comparison to the original circuit though the results converge for higher layers. 

Performance of upto 6 layers of the original circuit for the originally chosen target state is compared with averaged performance over 4 randomly chosen target states in plots/comparison_with_average.png . The plot indicates that the exponentially decreasing trend of the originally obtained plot was not specific to the target state and is in fact expected behaviour for any target state. The averaged plot seems to drop slower in comparison to the target state. This can be due to the fact that it the averaged plot was optimised on 3 sets of initial parameters rather than the 10 sets of parameters used for the original target state.


