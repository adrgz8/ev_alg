# Evolutionary Algorithms

This repository was created to compare and test different Evolutionary Algorithms.

Evolutionary Algorithms (in evol_algs.py file):

* PBIL
* CGA
* UMDA

Optimization problems (in opt_problems.py file):

* One Max
* Dec One Max
* K Dec One Max (Not implemented yet)

To run the main file, it is possible to add (optional) parsers.
If parsers are not added, the default EA is UMDA solving default Optimization problem One Max

```python
python main.py
```

It is possible to plot results by adding

```python
--plotting
```

To compare all Evolutionary Algorithms with all Optimization Problems. (This will plot results by default):

```python
python main.py --compare_all
```

It is possible to change the parameters for the Evolutionary Algorithm.
The default parameters are:

```python
length = 50
N = 100
epochs = 100
lr = 0.1
mutation = 0.02
shift = 0.05
```

For example, if we want to have bigger N, more epochs and decrease learning rate:

```python
python main.py --compare_all --N 200 --epochs 1000 --lr 0.2
```
