from qiskit import QuantumCircuit,Aer,execute
from qiskit.circuit import ParameterVector
import numpy as np
import matplotlib.pyplot as plt

def get_cost(params,target_phi,layers,ry=False):
"""
return the distance of the state obtained through given parameter from the target state
params: the list of parameters to be used to obtain step size
target_phi: target state
layers: the number of layers of the circuit to be used
ry: whether the modified circuit with ry in place of rx is to be used
"""
	# print(params)

	# make the circuit
	qc=QuantumCircuit(4)
	count=0
	for l in range(layers):
		for i in range(4):
			if ry:
				qc.ry(params[count],i)
			else:
				qc.rx(params[count],i)
			count+=1
		for i in range(4):
			qc.rz(params[count],i)
			count+=1
		for i in range(3):
			for j in range(i+1,4):
				qc.cz(i,j)

	# qc.draw('mpl')
	# plt.show()
	# print(qc)
	# input()

	# run the simulation, get the final resulting state
	backend=Aer.get_backend('statevector_simulator')
	state=execute(qc,backend).result().get_statevector()
	# print(state)

	# cost=distance=norm of the difference between the target and the obtained state
	cost=np.linalg.norm(target_phi-state)

	return cost

def find_dist(layers,seed,target_phi,max_iter,lr=0.1,ry=False):
"""
return the least distance from the target state which can be obtained using gradient descent

layers: the number of layers of the circuit to use
seed: seed for random initialisation of the target state
target_phi: target state as a numpy array of length 16
max_iter: maximum number of iterations of gradient descent
lr: initial step size of the algorithm
ry: whether the modified circuit using ry in place of rx is to be used
"""

	np.random.seed(seed)

	# parameter initialisation
	params=np.random.rand(layers*8,1)*2*np.pi
	# print(params)

	iter=1

	# least cost so far
	min_cost_found=float('inf')

	# cost obtained in previous iteration for step update
	prev_cost=float('inf')

	while True:
		print("\n\niter=",iter)

		# cost obtained from the current set of parameters
		cost1=get_cost(params,target_phi,layers,ry)
		print("cost=",cost1)
		# print()

		# gradient to be obtained using approximation by finite differences
		grad=np.zeros((layers*8,1))

		for i in range(len(params)):
			delta=1e-3
			new_params=params.copy()
			# print(new_params)
			# print(delta)
			new_params[i]+=delta
			# print(new_params)

			cost2=get_cost(new_params,target_phi,layers,ry)
			# print(cost2-cost1)

			# ith element of gradient= (change in cost)/(amount of change in ith parameter value)
			grad[i]=(cost2-cost1)/delta

		# print("gradient:",grad)
		print("gradient norm=",np.linalg.norm(grad))

		# parameter update
		params=params-lr*grad

		# may have overshot the minima, decrease step size
		if cost1>prev_cost:
			lr/=2

		# step size too small, should be close enough to minima
		if lr<1e-3:
			return min_cost_found

		print("lr=",lr)


		# new minimum cost
		if cost1<min_cost_found:
			min_cost_found=cost1

		# gradient too low, almost at an extremum
		if np.linalg.norm(grad)<1e-4:
			return min_cost_found

		if iter>=max_iter:
			return min_cost_found

		iter+=1
		prev_cost=cost1




# list of averaged least distances for each layer
obtained_distances=[]


# the largest number of layers we want to test our circuit on 
no_layers=10


for layers in range(no_layers):
	print("\n\n\n\n"+"*"*10+"Starting trial for layers=",layers+1,"*"*10)

	# averaged minimum distance obtained over all target states
	avg_dist=0

	# initialise target state with a different seed each time
	for target_seed in range(4):

		print("\n\n\n"+"#"*10+"Target with seed: ",target_seed,"#"*10)

		np.random.seed(target_seed)

		# the target state
		target_phi=np.random.rand(16)
		target_phi/=np.linalg.norm(target_phi)

		print(target_phi)

		# min_dist=least distance obtained over all random initialisations of the parameters
		min_dist=float('inf')
		for seed in range(10):
			print("\n\n"+"="*10+"Seed=",seed,"="*10)
			dist=find_dist(layers+1,seed,target_phi,500,0.5,False)
			if dist<min_dist:
				min_dist=dist


		print("min_dist found=",min_dist)
		avg_dist+=min_dist
		# obtained_distances.append(min_dist)

	avg_dist/=4
	print("\n\navg_dist=",avg_dist)
	obtained_distances.append(avg_dist)


print(obtained_distances)

# list of [1,2,...,no_layers]
layers_list=[]
for i in range(no_layers):
	layers_list.append(i+1)

plt.plot(layers_list,obtained_distances)
plt.xlabel('No of layers')
plt.ylabel('Least distance achieved')
plt.show()





