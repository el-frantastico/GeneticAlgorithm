class Organism:

    def __init__(self, genes):
        self._genes = genes
        self.average_result = 0
        self.error_deviation = 0

    def genes(self):
        return self._genes

    def calculate_error_deviation(self, experimental_result):
        error = (experimental_result - self.average_result) / experimental_result
        self.error_deviation = error
        return error
