# Homework 1 

## Counting Device with torch.cuda.device_count()

Using the function torch.cuda.device_count() and insert in the [modified code](./pytorch_2p8_ddp_prof_mod.py).
The result is shown as follows 

<img src="./Assets/CountingDeviceResult.jpg"/>

## Running under different Dimension

All the following runs are under signle node with two ranks. For each GPU, 2 cores were assigned to it.
For the dimension of src and tgt to be (2048,1,512) and (2048,20,512), the running time is 10.48s.
When src=torch.rand(2048,20,512) and tgt=torch.rand(2048,20,512), the running time is 11.42s.
When src=torch.rand(2048,200,512) and tgt=torch.rand(2048,200,512), the running time is 127.78s.
When src=torch.rand(2048,20,256) and tgt=torch.rand(2048,200,256), the running time is 120.15s.
When src=torch.rand(2048,20,512) and tgt=torch.rand(2048,100,512), the running time is 118.50s.
When src=torch.rand(2048,20,512) and tgt=torch.rand(2048,50,512), the running time is 11.52s.
The result shows when the dimension grows larger, the running time is bottle necked by I/O and the CPU power, evidence will be present in the following sections 

## Collective communication between nodes

This section compares the configuration with 2 ranks run on a single node and 2 ranks run on separate nodes.


In conclusion, running on seperate nodes will increase the communication cost.


## Large Dimension Bottle Neck

When the size of the data is large, namely when the sequence size is equal or more than 100


## Effect of Datatypes
