# The Hydrophobic Polar Model for proteins

This repo contains an implementation in Python of the HP model for proteins. 

## Introduction 

Proteins have a key role in almost all the biological process, they are used for structural, communication, energy storage, catalysis and many other purposes inside
the cells. To carry out its intended biological functions a protein needs to reach its folded shape. Some models have been developed in order to understand how proteins
reach their folded shape. In this work an approach to understand this behavior was done by using the hydrophobic polar model together with the Metropolis and
simulated annealing algorithms.

## Background 

Proteins are formed by long chains of length between 50 to 20 thousand monomers called amino acids, there are 20 different of them that can be combined on this
chains, the sequence of this monomers gives the protein an unique structure and function. An important property of proteins is that they manage to find the proper
structure within a universe of possibilities in just some seconds, it has been found that if a protein is put back into its biological natural environment it folds into its
natural configuration.

In physics the problem of the structure and shape of the proteins has been approached from a statistical physics and energetic point of view with some help of optimization computational methods.
In some of this approaches the folding process is considered to happen randomly with certain probability which depends on the energy configuration of that struc-
ture, the energy of each state is considered to be the one of the joins of the chain, the amino acid bonds.

The Hydrophobic Polar (HP) model is a simplified model for studying proteins folding. In this model amino acids which conform the protein structure are con-
sidered of only two types, hydrophobic (H) or polar (P) and the protein folding is given by a self avoiding walk, i.e. a sequence of movements in a lattice where
a point is not visited more than once. The folded state of a protein can be seen as an minimum energy state, this can be understood if we consider that certain
amino acid chains are able to participate in the hydrogen bonding network of their environment and the binding with particles of the its surrounding its determine by
the way it is folded.

Simulations can be held by considering a two dimensional lattice where a protein is considered to exists in a sequence of points x1, x2, ..., xn . The energy is calculated by
counting the number of HH contacts

![equation1](Images/eq1.png)

Considering E i the different energies of a particular sequence, g i the different number of folded states with that energy, also known as degeneracy, then by using
Boltzmann statistics, the probability in thermal equilibrium for a particular state with energy E i us given by

![equation2](Images/eqn2.png)

with Z the partition function defined as

![equation3](Images/eqn3.png)

### Metropolis Algorithm

Monte Carlo method turns to be a god tool when it comes to thermodynamical systems where the total number of possibilities is a non-trivial large astronomical
number. It allows us to get an estimate from a small but representative fraction of the total population. By using this method it is possible to construct a trajectory
in the configuration space that allow us to visit the states according to Boltzmann distribution.

In order to have a better performance a criterion for accepting and rejecting moves to new configurations can be implemented. The Metropolis algorithm considers 
there is a probability of accepting a move when this causes an energy decrease, when the energy change is positive the move is accepted with an exponential prob-
ability.

![equation4](Images/eqn4.png)

With w_vv 0 the probability per unit time that if it is in a state v, it will make a transition to state v 0 and β = 1/k B T , kB is the Boltzmann constant and T is the
temperature, in this case a parameter to control the probability of a acceptance.

### Simulated Annealing

Simulated annealing is a method to find an acceptable solution to an optimization problem. It is particular good for problems where it is needed to find a maximum or
a minimum. The idea of the algorithm is to mimic the process from where it takes its name, this is the process that happens in the misplaced atoms of a metal that
is heated and then slowly cooled. It makes use of the Metropolis algorithm but it provides a way to control the probability of acceptance of unfavorable energetically
steps, this means adjusting the temperature T. From equation 2.4 it is possible to realize that as T is large the probability of accepting changes where the energy does
not decreases is big but as it decreases the changes to higher energy states should be less probable. An important part of the simulated annealing algorithm is to choose
a good way to low the temperature, this is known as annealing schedules.

