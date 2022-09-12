from copy import deepcopy
from math import exp

from random import uniform, shuffle

import amino_acid_class.sequence_manipulator as seq_manip


class MonteCarlo:
    energy = 0
    buffer = None

    def __init__(self, seq_manip, t_min, t_max, p_pull_move, step):
        self.seq_manip = seq_manip

        self.t_min = t_min
        self.t_max = t_max

        self.p_pull_move = p_pull_move
        self.step = step

    def move(self, temperature):
        which_amino_acid = list(range(self.seq_manip.get_seq_length()))
        shuffle(which_amino_acid)

        coord_manip = self.seq_manip.get_coord_manip()
        self.buffer = coord_manip.get_coord_list()

        move_set = [
            # seq_manip.AminoAcidManip.end_move,
            # seq_manip.AminoAcidManip.corner_move,
            # seq_manip.AminoAcidManip.crankshaft_move,
            seq_manip.AminoAcidManip.pull_moves
        ]
        shuffle(move_set)

        amino_acid = self.seq_manip.get_link_sequence()[which_amino_acid[0]]
        move_done = False

        for move in move_set:
            if move == seq_manip.AminoAcidManip.pull_moves:
                if self.p_pull_move < uniform(0, 1):
                    move_done = move(self.seq_manip, amino_acid)

                    if not move_done:
                        continue
            else:
                move_done = move(self.seq_manip, amino_acid)

                if not move_done:
                    continue

            self.__probability(
                coord_manip.calc_energy(self.seq_manip.get_sequence_model()),
                temperature,
                coord_manip
            )

        return coord_manip.calc_energy(self.seq_manip.get_sequence_model())

    def __probability(self, energy, temperature, coord_manip):
        d_energy = energy - self.energy

        if d_energy < 0:
            self.buffer = deepcopy(coord_manip.get_coord_list())
            self.energy = energy
        else:
            if exp(-d_energy / temperature) < uniform(0, 1):
                self.buffer = deepcopy(coord_manip.get_coord_list())
                self.energy = energy
            else:
                coord_manip.set_whole_coord(self.buffer)

    def monte_carlo(self):
        temperature = range(self.t_min, self.t_max, 1)

        # for temp in temperature:
        for i in range(self.step):
            energy = self.move(200)

        print("\n--========================--")
        print("--=|  MONTE CARLO DONE  |=--")
        print(f"--=| Final energy: {energy:4.0f} |=--")
        print("--========================--\n")
