from qiskit import QuantumCircuit,Aer,execute
from qiskit.circuit import ParameterVector
import numpy as np
import matplotlib.pyplot as plt

def get_cost(params,target_phi,layers):
	# print(params)
	qc=QuantumCircuit(4)
	count=0
	for l in range(layers):
		for i in range(4):
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
	backend=Aer.get_backend('statevector_simulator')
	state=execute(qc,backend).result().get_statevector()
	# print(state)

	cost=np.linalg.norm(target_phi-state)

	return cost

def find_dist(layers,seed,target_phi,max_iter,lr=0.1):
	
	# seed=0

	np.random.seed(seed)

	# layers=2
	params=np.random.rand(layers*8,1)*2*np.pi
	# print(params)

	iter=1

	min_cost_found=float('inf')
	prev_cost=float('inf')

	while True:
		print("\n\niter=",iter)
		# lr=0.1
		cost1=get_cost(params,target_phi,layers)
		print("cost=",cost1)
		# print()
		grad=np.zeros((layers*8,1))

		for i in range(len(params)):
			delta=1e-3
			new_params=params.copy()
			# print(new_params)
			# print(delta)
			new_params[i]+=delta
			# print(new_params)

			cost2=get_cost(new_params,target_phi,layers)
			# print(cost2-cost1)

			grad[i]=(cost2-cost1)/delta

		# print("gradient:",grad)
		print("gradient norm=",np.linalg.norm(grad))


		params=params-lr*grad

		if cost1>prev_cost:
			lr/=2

		if lr<1e-3:
			return min_cost_found

		print("lr=",lr)


		# break

		if cost1<min_cost_found:
			min_cost_found=cost1

		if np.linalg.norm(grad)<1e-4:
			return min_cost_found

		if iter>=max_iter:
			return min_cost_found

		iter+=1
		prev_cost=cost1



np.random.seed(0)

target_phi=np.random.rand(16)
target_phi/=np.linalg.norm(target_phi)

print(target_phi)


obtained_distances=[]

no_layers=10


for layers in range(no_layers):
	print("\n\n\n\n"+"*"*10+"Starting trial for layers=",layers+1,"*"*10)

	min_dist=float('inf')
	for seed in range(10):
		print("\n\n"+"="*10+"Seed=",seed,"="*10)
		dist=find_dist(layers+1,seed,target_phi,500,0.5)
		if dist<min_dist:
			min_dist=dist


	print("min_dist found=",min_dist)
	obtained_distances.append(min_dist)


print(obtained_distances)

layers_list=[]
for i in range(no_layers):
	layers_list.append(i+1)

plt.plot(layers_list,obtained_distances)
plt.xlabel('No of layers')
plt.ylabel('Least distance achieved')
plt.show()





