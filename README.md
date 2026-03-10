# OpenMM-CpH

This package implements constant pH simulations with OpenMM.

**Warning:** This is still prerelease code.  It has not yet been well validated.  You are
encouraged to test it and give feedback, but do not rely on the results to be accurate.

For instructions on how to use it, see [the tutorial](Tutorial.ipynb).

This package is based on the algorithm described in the following paper, except that it uses
simulated tempering in place of replica exchange.

> Swails, J. M., York, D. M., and Roitberg, A. E. "Constant pH Replica Exchange Molecular Dynamics
> in Explicit Solvent Using Discrete Protonation States: Implementation, Testing, and Validation."
> J. Chem. Theory Comput., 2014. https://doi.org/10.1021/ct401042b

It is based on discrete protonation states in hybrid solvent.  It alternates between two operations:

1. Run ordinary molecular dynamics in explicit solvent with fixed protonation states.
2. Perform Monte Carlo moves to select new protonation states based on the energy in implicit solvent.

Before running a simulation, you first need to determine reference energies for all protonation
states.  This accounts for factors that cannot be determined from the force field, such as the
energy required to break the covalent bond holding a hydrogen in place.  They are typically
determined by simulating a small model compound in a box of water, varying the pH, and determining
what reference energy reproduces the experimental pKa.  The `ReferenceEnergyFinder` class
automates this process.  See the tutorial for instructions on how to use it.

This package makes a few assumptions you need to be aware of.

1. There is a one-to-one correspondence between residues and titratable sites.  If a residue
   contains multiple titratable hydrogens, you need to treat all of them as a single site and
   enumerate all allowed combinations of hydrogens as distinct states.
2. You provide a single Topology describing your model, and a force field describing how to
   parameterize it.  `Modeller.addHydrogens()` gets called to construct the different versions
   of each site, and `ForceField.createSystem()` gets called to create Systems.  This means
   you must be able to parameterize the model with a ForceField object.  You cannot use models
   that were parameterized in another program and loaded from Amber, CHARMM, or Gromacs files.
3. Changing the state of a residue can only affect parameters within that residue.  It cannot
   change per-particle parameters of atoms in other residues.  In practice, this means you can
   vary sites on the side chains of a protein, but usually not ones on the backbone.
4. It can only modify parameters of the following forces: NonbondedForce, GBSAOBCForce, and
   any custom force that has a per-particle parameter called "charge".  This means, for example,
   that it cannot be used with the AMOEBA force field.