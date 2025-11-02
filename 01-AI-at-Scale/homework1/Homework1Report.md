# Homework 1 

## Counting Device with torch.cuda.device_count()

Using the function torch.cuda.device_count() and insert in the [modified code](./pytorch_2p8_ddp_prof_mod.py).
The result is shown as follows 

<img src="./Assets/CountingDeviceResult.jpg"/>

## Running under different Dimension

All the following runs are under signle node with two ranks. For each GPU, 2 cores were assigned to it.

|  | src | tgt | runtime |
| --- | --- | --- | --- |
| 1 | (2048,1,512) | (2048,20,512) | 10.48s |
| 2 | (2048,20,512) | (2048,20,512) | 11.42s |
| 3 | (2048,200,512) | (2048,200,512) | 127.78s |
| 4 | (2048,20,256) | (2048,200,256) | 120.15s |
| 5 | (2048,20,512) | (2048,100,512) | 118.50s |
| 6 | (2048,20,512) | (2048,50,512) | 11.52s |


The result shows when the dimension grows larger, the running time is bottle necked by I/O and the CPU power, evidence will be present in the following sections 

## Collective communication between nodes

This section compares the configuration with 2 ranks run on a single node and 2 ranks run on separate nodes. In both cases teh src=torch.rand((2048,20,512) and tgt=src=torch.rand((2048,20,512). In single node case, the running time is 11.42s and for 2 nodes case, the running time is 37.40s. The 2 nodes case runs almost 4 times longer 


In conclusion, running on seperate nodes will increase the communication cost.


## Large Dimension Bottle Neck

When the size of the data is large, namely when the sequence size is equal or more than 100


## Effect of Datatypes
