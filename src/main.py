"""Script to applied a MC/REMC algorithm on protein folding with Dill's H/P
model.

Simplet usage
-------------
python3 src/main.py -i AA -s 1 -o file.csv
    -i : str
        The input sequence.
    -s : int
        The number of Monte Carlo step to perform.
    -o : str
        An output file with energy in it.
"""

__authors__ = "ROUAUD Lucas"
__contact__ = "lucas.rouaud@gmail.com"
__date__ = "14/09/2022"
__version__ = "1.0.0"

# Importation of other python module.
import textwrap

# Importation of "homemade" python module.
import general_function.parsing as pars
import general_function.translation as trlt
import amino_acid_class.sequence_manipulator as seq_manip
import monte_carlo.monte_carlo as mc

if __name__ == "__main__":
    argument = pars.parsing()
    seq_list = trlt.translation(argument["seq_list"])

    for sequence in seq_list:
        print("----------------------------------------")
        print(textwrap.fill(sequence, width=40))
        print("----------------------------------------")

        monte_carlo = mc.MonteCarlo(
            seq_manip.AminoAcidManip(sequence),
            argument["tmin"],
            argument["tmax"],
            argument["output"],
            argument["mf"]
        )

        if argument["remc"]:
            monte_carlo.repl_ex_monte_carlo(argument["co"], argument["step"],
                                            argument["ts"], argument["rp"])
        else:
            monte_carlo.monte_carlo(argument["step"], argument["rp"])
