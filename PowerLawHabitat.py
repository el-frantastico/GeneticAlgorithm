from Habitat import *
from Organism import *


class PowerLawHabitat(Habitat):

    def _calculate_for_organism(self, organism, set_of_parameters):
        if len(organism.genes()) - 1 != len(set_of_parameters):
            print("[ERROR] Power Law formula requires one more gene than parameters available." +
                  "Organism: " + str(organism) +
                  "Number of Genes: " + str(len(organism.genes())) +
                  "Number of Parameters " + str(len(set_of_parameters)))

            return []

        result = organism.genes()[0]

        for index in range(0, len(set_of_parameters)):
            result = result * (set_of_parameters[index] ** organism.genes()[index + 1])

        return result
