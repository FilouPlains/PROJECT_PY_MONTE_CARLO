"""Class for do Monte Carlo algorithm.
"""
# Importation of other python module.
from copy import deepcopy
from math import exp
from random import uniform, shuffle
from tqdm import tqdm

# Importation of "homemade" python module.
import amino_acid_class.sequence_manipulator as seq_man
import output.output as out


class MonteCarlo:
    """An object = A Monte Carlo applier.
    """
    energy = 0
    buffer = None

    # Boltzmann's constant.
    K_B = 0.0019872

    def __init__(self, seq_manip, t_min, t_max, file, mol2):
        """Constructor for doing the MC/REMC algorithm.

        Parameters
        ----------
        seq_manip : AminoAcidManip
            The object that manipulate a given sequence.
        t_min : int
            Minimal temperature.
        t_max : int
            Maximal temperature.
        file : str
            The `.csv` file to write.
        mol2 : str
            The `.mol2` file to write.
        """
        self.seq_manip = seq_manip

        self.t_min = t_min
        self.t_max = t_max

        self.csv = out.Output(file)

        # The `.mol2` is optional.
        if mol2:
            self.mol2 = out.Output(mol2, True)
        else:
            self.mol2 = None

    def move(self, temperature):
        """Testing and doing a move on the sequence.

        Parameters
        ----------
        temperature : int
            The temperature which we do the movement.

        Returns
        -------
        int
            The energy of the new conformation obtain.
        """
        which_amino_acid = list(range(self.seq_manip.get_seq_length()))
        shuffle(which_amino_acid)

        coord_manip = self.seq_manip.get_coord_manip()
        self.buffer = coord_manip.get_coord_list()

        # Like that, we have 1/3 to select each move.
        move_set = [
            seq_man.AminoAcidManip.end_move,
            seq_man.AminoAcidManip.corner_move,
            seq_man.AminoAcidManip.crankshaft_move
        ]
        shuffle(move_set)

        amino_acid = self.seq_manip.get_link_sequence()[which_amino_acid[0]]
        move_done = False

        # Try all movement. If no movement done, count as a MC step.
        for move in move_set:
            move_done = move(self.seq_manip, amino_acid)

            if not move_done:
                continue

            # Try if the movement is favorable or not and compute the
            # probability of doing it.
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

        # Favorable movement.
        if d_energy < 0:
            self.buffer = deepcopy(coord_manip.get_coord_list())
            self.energy = energy
        # Unfavourable movement: try with a probability to do it anyway.
        else:
            if exp(-d_energy / (temperature * self.K_B)) < uniform(0, 1):
                self.buffer = deepcopy(coord_manip.get_coord_list())
                self.energy = energy
            else:
                coord_manip.set_whole_coord(self.buffer)

    def monte_carlo(self, step, do_r_p):
        """Do a simple MC algorithm.

        Parameters
        ----------
        step : int
            Number of steps to perform.
        do_r_p : bool
            If `True`, put the sequence linearly. Else, if `False`, put it
            randomly.
        """
        temperature = range(self.t_min, self.t_max + 1, 1)

        # Each replica at a given temperature.
        for i, temp in enumerate(temperature):
            self.seq_manip.set_path(do_r_p)
            description = f"DOING MC {i + 1}/{len(temperature)}"

            # Do a MC movement.
            for j in tqdm(range(step), desc=description):
                energy = self.move(temp)
                self.csv.add_line(temp, energy, j)

                if self.mol2 is not None:
                    self.mol2.write_mol2(
                        self.seq_manip.get_coord_manip().get_coord_list(),
                        self.seq_manip.get_sequence_model()
                    )

            print("\n--========================--")
            print("--=|  MONTE CARLO DONE  |=--")
            print(f"--=| Final energy: {energy:4.0f} |=--")
            print(f"--=|  Temperature: {temp:4d} |=--")
            print("--========================--\n")

        # Closing the results file.
        self.csv.end_csv()

        if self.mol2 is not None:
            self.mol2.end_mol2()

    def repl_ex_monte_carlo(self, cut_off, m_c_step, total_step, do_r_p):
        """Do a REMC algorithm.

        Parameters
        ----------
        cut_off : int
            Energy that give when to stop the algorithm.
        m_c_step : int
            Number of classical MC steps to perform.
        total_step : int
            Number of replica exchange to do. `TOTAL_STEP = m_c_step
            * total_step`
        do_r_p : bool
            Do a random placement ? `True` no (linear), `False` yes.
        """
        energy = 0
        energy_list = []
        step = 0
        temperature = range(self.t_min, self.t_max, 1)

        replica = []
        coord_manip = self.seq_manip.get_coord_manip()

        # Check the cut-off and the number of steps done.
        while energy < cut_off or total_step > step:
            description = f"TEMP. {step + 1}/{total_step}"
            
            # Do the MC for each temperature.
            for i, temp in tqdm(enumerate(temperature), desc=description):
                if step == 0:
                    self.seq_manip.set_path(do_r_p)
                else:
                    coord_manip.set_whole_coord(replica[i])

                # Do the simple MC algorithm.
                for j in range(m_c_step):
                    act_energy = self.move(temp)
                    self.csv.add_line(temp, energy, j)
                    
                    if self.mol2 is not None:
                        self.mol2.write_mol2(
                            self.seq_manip.get_coord_manip().get_coord_list(),
                            self.seq_manip.get_sequence_model()
                        )

                energy_list.append(act_energy)
                replica.append(deepcopy(coord_manip.get_coord_list()))

            # Checking if a replica exchange is doable.
            for i in range(len(temperature) - 1):
                exchange = self.__test_proba(energy_list[i:i + 2],
                                             temperature[i:i + 2])

                if exchange:
                    buffer = replica[i]
                    replica[i] = replica[i + 1]
                    replica[i + 1] = buffer

            energy = min(energy_list)

            step += 1

        # Print each result in the terminal.
        for i, temp in enumerate(temperature):
            print("\n--========================--")
            print("--=|  MONTE CARLO DONE  |=--")
            print(f"--=| Final energy: {energy_list[i]:4.0f} |=--")
            print(f"--=|  Temperature: {temp:4d} |=--")
            print("--========================--\n")

        # Closing the file.
        self.csv.end_csv()

        if self.mol2 is not None:
            self.mol2.end_mol2()

    def __test_proba(self, energy, temperature):
        """Try the probability of doing a REMC. If so, return `True`.

        **PRIVATE_METHOD**

        Parameters
        ----------
        energy : list[int, int]
            The energy to compare.
        temperature : list[int, int]
            The temperature to compare.

        Returns
        -------
        bool
            Return `True` for doing a exchange after probability computation.
            Else, return `False`.
        """
        # Computing the probability.
        delta = (1 / (self.K_B * temperature[1])
                 - 1 / (self.K_B * temperature[0])) * (energy[1] - energy[0])

        if delta <= 0:
            return True
        elif exp(-delta) < uniform(0, 1):
            return True

        return False
