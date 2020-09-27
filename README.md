# Description

In this repository I have attempted screening task 1 for qosf mentorship program applications. 

I have created a random 16 length vector and normalised it to produce my target state. I have used a gradient descent algorithm with adaptive step sizes to minimise the distance of the state produced by the circuit with the target state. In order to account for non-convexity in the cost function, I repeated the experiment for each layer with parameters initialised randomly with 10 different seeds. As a part of the bonus question I tried replacing the rx gate of odd blocks with ry gates.

In order to find out the extent to which choosing the target state will affect our obtained cost I ran the experiment over different seeds for calculating the target state and then averaged over the least cost obtained for each target state.

## Results
Obtained plot for upto 10 layers of the original circuit and minimum calculated over 10 randomly initialised parameters is present in plots/least_dist_vs_layers.png . The results indicate that the distance decreases very fast with the number of layers initially, but then becomes almost constant for higher layers.

A plot comparing the performance of the modified circuit with ry gate in place of rx for upto 8 layers is present in plots/least_dist_vs_layers_diff_circuits.png . Both plots show exponentially decreasing distance with the number of layers in the circuit but the modified circuit does not perform as well as the original one. The distance achieved with the modified circuit decreases slowly with the number of layers in comparison to the original circuit though the results converge for higher layers. 

Performance of upto 6 layers of the original circuit for the originally chosen target state is compared with averaged performance over 4 randomly chosen target states as described above in plots/comparison_with_average.png . The plot shows that the exponentially decreasing trend of the originally obtained plot was not specific to the target state and is in fact expected behaviour for any target state. However, the averaged plot seems to drop slower in comparison to the target state but that can be attributed to the lesser number of initialised parameters it was optimised on (3 instead of 10).


