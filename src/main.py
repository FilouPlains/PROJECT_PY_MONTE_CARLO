# Importation of other python module.
import os
import sys

# Importation of "homemade" python module.
import function.parsing as pars


if __name__ == "__main__":
    argument = pars.parsing()

    print(argument["input"])
