"""Class for do Monte Carlo algorithm.
"""

from copy import deepcopy
import numpy as np
from math import exp
from tqdm import tqdm
from random import uniform, shuffle

import amino_acid_class.sequence_manipulator as seq_man


class MonteCarlo:
    """An object = A Monte Carlo applyer.
    """
    energy = 0
    buffer = None
    K_B = 0.0019872

    def __init__(self, seq_manip, t_min, t_max):
        self.seq_manip = seq_manip

        self.t_min = t_min
        self.t_max = t_max

    def move(self, temperature):
        which_amino_acid = list(range(self.seq_manip.get_seq_length()))
        shuffle(which_amino_acid)

        coord_manip = self.seq_manip.get_coord_manip()
        self.buffer = coord_manip.get_coord_list()

        move_set = [
            seq_man.AminoAcidManip.end_move
            # seq_man.AminoAcidManip.corner_move,
            # seq_man.AminoAcidManip.crankshaft_move
        ]
        shuffle(move_set)

        amino_acid = self.seq_manip.get_link_sequence()[which_amino_acid[0]]
        move_done = False

        for move in move_set:
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
        """Define if a move is doable or not trough probability.

        Parameters
        ----------
        energy : int
            The actual conformation's energy.
        temperature : int
            The system temperature.
        coord_manip : CoordManip
            A CoordManip object.
        """
        d_energy = energy - self.energy

        if d_energy < 0:
            self.buffer = deepcopy(coord_manip.get_coord_list())
            self.energy = energy
        else:
            if exp(-d_energy / (temperature * self.K_B)) < uniform(0, 1):
                self.buffer = deepcopy(coord_manip.get_coord_list())
                self.energy = energy
            else:
                coord_manip.set_whole_coord(self.buffer)

    def monte_carlo(self, step, do_r_p):
        """Do a Monte Carlo algorithm.
        """
        temperature = range(self.t_min, self.t_max + 1, 1)

        for i, temp in enumerate(temperature):
            self.seq_manip.set_path(do_r_p)
            description = f"DOING MC {i + 1}/{len(temperature)}"

            for i in tqdm(range(step), desc=description):
                energy = self.move(temp)

            print("\n--========================--")
            print("--=|  MONTE CARLO DONE  |=--")
            print(f"--=| Final energy: {energy:4.0f} |=--")
            print(f"--=|  Temperature: {temp:4d} |=--")
            print("--========================--\n")

    def repl_ex_monte_carlo(self, cut_off, m_c_step, total_step, do_r_p):
        energy = 0
        energy_list = []
        step = 0
        temperature = range(self.t_min, self.t_max, 1)

        replica = []
        coord_manip = self.seq_manip.get_coord_manip()

        while energy < cut_off or total_step > step:

            for i, temp in enumerate(temperature):
                if step == 0:
                    self.seq_manip.set_path(do_r_p)
                else:
                    coord_manip.set_whole_coord(replica[i])

                for i in range(m_c_step):
                    act_energy = self.move(temp)

                energy_list += [act_energy]
                replica += [deepcopy(coord_manip)]

            for i in range(len(temperature) - 1):
                exchange = self.__test_proba(energy_list[i:i + 2],
                                             temperature[i:i + 2])

                if exchange:
                    buffer = replica[i]
                    replica[i] = replica[i + 1]
                    replica[i + 1] = buffer

                    print(f"Exchange between {temperature[i]} and"
                          f" {temperature[i + 1]}")

            energy = min(energy_list)

            step += 1

    def __test_proba(self, energy, temperature):
        delta = (1 / (self.K_B * temperature[1])
                 - 1 / (self.K_B * temperature[0])) * (energy[1] - energy[0])

        if delta <= 0:
            return True
        elif exp(-delta) < uniform(0, 1):
            return True

        return False
