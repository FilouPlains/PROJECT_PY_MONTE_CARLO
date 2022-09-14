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
        print("--------------------")
        print(textwrap.fill(sequence, width=40))
        print("--------------------")

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
