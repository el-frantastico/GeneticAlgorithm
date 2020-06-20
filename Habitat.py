from abc import ABC, abstractmethod


class Habitat(ABC):

    def __init__(self, number_of_genes_in_each_organism):
        self._numberOfGenesInOrganism = number_of_genes_in_each_organism
        self._organisms = []
        self._ideal_habitat = []
        super().__init__()

# Habitat Manipulation
    def add_organism(self, organism):
        if len(organism.genes()) != self._numberOfGenesInOrganism:
            print("[WARNING] Attempted to add an organism with incorrect number of genes. "
                  "Skipping organism: " + str(organism))
        else:
            self._organisms.append(organism)

    def add_organisms(self, organisms):
        for organism in organisms:
            self.add_organism(organism)

    def set_ideal_habitat(self, ideal_habitat_matrix):
        #TODO: Check if the ideal_habitat_matrix is the expected result size and throw warning if not.
        self._ideal_habitat = ideal_habitat_matrix;
        return

# Habitat Calculation
    def calculate_for_organism(self, organism, matrix_of_parameters):
        set_of_results = []
        for set_of_parameters in matrix_of_parameters:
            set_of_results.append(self._calculate_for_organism(organism, set_of_parameters))

        return set_of_results

    def calculate_for_organisms(self, organisms, matrix_of_parameters):
        matrix_of_results = []
        for organism in organisms:
            matrix_of_results.append(self.calculate_for_organism(organism, matrix_of_parameters))

        return matrix_of_results

    def calculate_for_habitat(self, matrix_of_parameters):
        return self.calculate_for_organisms(self._organisms, matrix_of_parameters)

# Abstract Methods
    @abstractmethod
    def _calculate_for_organism(self, organism, set_of_parameers):
        passt