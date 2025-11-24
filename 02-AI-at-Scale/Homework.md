# Ai4ScienceHw2
Author: Quan Gan

## Problem 1
Try different combinations of model sizes (layer count with --n-layers=?) and tp-degrees (--tp=?) to get an idea of what works

Answer:
The default configuration (--n-layer=32) is oversized for one GPU. It will run when using the tensor parallelism with 4 degrees. The result is as follows

<img src="/Assets/TimerunTp4n32.jpg"  />

Reducing the Tp to 2, the model becomes oversized.

<img src="/Assets/tp2n32OutofMem.jpg"  />

Reducing the layer to 16, keep the Tp=2. Polaris is able to run the training

<img src="/Assets/tp2n16.jpg"  />

For n=16 and tp=1, the GPU is out of memory again

<img src="/Assets/tp1n16OutofMem.jpg"  />

These results suggest the ratio of tp and layers should satisfy $\frac{n}{tp}<8$.

## Problem 2

Document how the performance changes with 8-layer model and TP of 1,2,4 (--n-layhers=8 --tp=?)

Answer:
The running time when varying TP is as follows:

<img src="/Assets/TpvsRunTime.svg"  />

The result suggests increasing TP could linearly reduce the computation time when the intra_GPU communitating time is small.
