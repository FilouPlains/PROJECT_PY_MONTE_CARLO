"""Functions necessary for the translate a sequence into the H/P model.
"""

import sys

# Global variable as far as it will be declare at each end of recursion, so
# theoretically `n` times.
HP_DEFINITION = {
    # Polar amino acid.
    "G": "H",
    "P": "H",
    "A": "H",
    "V": "H",
    "I": "H",
    "L": "H",
    "M": "H",
    "F": "H",
    "Y": "H",
    "W": "H",
    # Hydrophobic amino acid.
    "R": "P",
    "H": "P",
    "K": "P",
    "D": "P",
    "E": "P",
    "S": "P",
    "T": "P",
    "N": "P",
    "Q": "P",
    "C": "P",
    "U": "P"
}


def translation(sequence_list):
    """Translate given sequence(s) into the H/P model.

    Parameters
    ----------
    sequence_list : list[string]
        A list of sequence to test.

    Returns
    -------
    list[string]
        The sequence adapted into H/P model.
    """
    translate_seq = []

    # Appending each sequence translate into H/P model.
    for sequence in sequence_list:
        translate_seq += [__attribution(sequence, len(sequence))]

    return translate_seq


def __attribution(sequence, size):
    """Recursive dichotomous function to attribute quicker H/P model correctly.

    **PRIVATE_FUNCTION**

    Parameters
    ----------
    sequence : string
        The sequence to translate.
    size : _type_
        The string size.

    Returns
    -------
    string
        The adapted sequence.
    """

    # Simplest case, returning the value of H or P define in the upper
    # dictionary.
    if size == 1:
        if sequence in HP_DEFINITION.keys():
            return HP_DEFINITION[sequence]
        else:
            sys.exit(f"ERROR: amino acid '{sequence}' unknown, please check"
                     " your fasta file")
    else:
        left = __attribution(sequence[:size // 2], size // 2)
        # When odd number encounter, adding 1 to the int() division, else ERROR.
        right = __attribution(sequence[size // 2:], size // 2 + size % 2)

        return left + right
