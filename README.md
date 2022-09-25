# NOTE AUX CORRECTEURS

> 1. Le rapport se situe dans `doc/report/ROUAUD_rapport.pdf`.
> 2. Un jeu de données avec des séquences `.fasta` se trouve dans `data`. Les résultats sont compressés dans `data/output.tar.gz`.

# PROJECT_PY_MONTE_CARLO

This program is a implementation of a Replica Exchange Monte Carlo algorithm (REMC) described in the paper _"A replica exchange Monte Carlo algorithm for protein folding in the HP model"_, by THACHUK C. and _al_.

## Installation

Simply clone this repository by doing:

```bash
git clone git@github.com:FilouPlains/PROJECT_PY_MONTE_CARLO.git
```

## Conda initialization

You need module that are not install into base python. To do so, and to simplify the process, an environment `src/project_mc.yml` have already been create.

To used it, simply type (if you are in `PROJECT_PY_MONTE_CARLO/`):

```bash
conda env create -n project_mc -f env/project_mc.yml
conda activate project_mc
```

**You are now able to launch the program**.

## Simplest example

To launch the program, the minimap require argument are given next (if you are in `PROJECT_PY_MONTE_CARLO/`):

```bash
python3 src/main.py -i AA -s 1 -o file.csv
```

Obviously, there's a lot of parameters. simply type this to have the help:

```bash
python3 src/main.py -h
```

Or this:

```bash
python3 src/main.py --help
```

**Now, let's describe one by one all possible arguments:**
|           argument           | description                                                                                                                            |
| :--------------------------: | :------------------------------------------------------------------------------------------------------------------------------------- |
|          -h, --help          | Display the help.                                                                                                                      |
|       **-i, --input**        | Give the input sequence. You can type it or give a `.fasta` file.                                                                      |
|        **-s, --step**        | The number of MC steps to perform. You have to give an integer.                                                                        |
|       **-o, --output**       | Print a file (`file.csv`) with data in it from the MC algorithm.                                                                       |
| -tmin, --minimal_temperature | The minimal temperature to start the replica (from tmin to tmax, both include, with a step of 1).                                      |
| -tmax, --maximal_temperature | The maximal temperature to start the replica (from tmin to tmax, both include, with a step of 1).                                      |
|             -rp              | Place the given sequence randomly on a grid. Note that if this parameters is not given, the sequence will be put linearly on the grid. |
|       -mf, --mol_file        | Give `file.mol2` as output. You can, like this, visualize the trajectory. ***WARNINGS:* Huge file and take time to be produce!**       |
|            -remc             | When given, do a replica exchange MC.                                                                                                  |
|       *-co, --cut_off*       | Energy that serve as a cut-off. Only negative integer possible.                                                                                 |
|     *-ts, --total_step*      | Number of exchange to do. *Note that the number of operation when this parameter is given is `-s * -ts`.*                              |

> **Note :** Argument in bold **HAVE TO BE GIVEN** so the program could work well.

> **Note :** Argument in italics **HAVE TO BE GIVEN** if the option **-remc** is input.

The most full example is given next:

```bash
python3 src/main.py
    -i sequence.fasta
    -s 10
    -o file.csv
    -tmin 20
    -tmax 30
    -mf file.mol2
    -rp
    -remc
    -co -5
    -ts 5
```

> **Note:** Personalize error can been thrown. If you want a more detailed explanation, check `doc/ERROR.md`.

## To take in consideration

The REMC algorithm take **way** more time to be done than the MC algorithm.
