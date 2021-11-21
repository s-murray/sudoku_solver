class Sudoku(object):
    """Represents a 9x9 sized Sudoku puzzle.

    Initializing creates an empty Sudoku; empty spaces in Sudoku puzzle are represented by '.' character.

    """

    def __init__(self):
        empty_row = '.........'
        empty_sudoku = []
        for i in range(9):
            empty_sudoku[i] = empty_row
        self.puzzle = empty_sudoku

    def get_puzzle(self):
        """list: length 9 list of strings of length 9 defining Sudoku"""
        return self.puzzle

    def determine_row(self, row: int):
        """Returns row of Sudoku puzzle.

        Args:
            row (int): Value between 1-9 for row in Sudoku, 1 is top of puzzle.

        Returns:
            str:  String representing row of Sudoku

        """
        return self.get_puzzle()[row]

    def determine_column(self, column: int):
        """Calculates a string representation of specific column.

        Args:
            column (int): Value between 1-9 for column of Sudoku, 1 is left of puzzle.

        Returns:
            str: String representing column of Sudoku.

        """
        sudoku_column = ''
        for i in range(9):
            sudoku_column += self.determine_row(i)[column]
        return sudoku_column

    def determine_segment(self, row: int, column: int):
        """Calculates a specific 3x3 segment of Sudoku.

        The returned string is a concatenation of the three rows of the returned segment, e.g.:
                123
                456     --->    '123456789'
                789

        Args:
            row (int): Value between 1-3 representing segment row of Sudoku puzzle, 1 is top of puzzle.
            column (int): Value between 1-3 representing segment column of Sudoku puzzle, 1 is left of puzzle.

        Returns:
            str: String representing values in segment of Sudoku.

        """
