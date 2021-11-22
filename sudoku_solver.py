class Sudoku(object):
    """Represents a 9x9 sized Sudoku puzzle.

    Initializing creates an empty Sudoku; empty spaces in Sudoku puzzle are represented by '.' character.

    Attributes:
        _puzzle (list): list of length 9 of length 9 strings representing Sudoku.

    """

    def __init__(self):
        empty_row = []
        for i in range(9):
            empty_row.append('.')
        empty_sudoku = []
        for i in range(9):
            empty_sudoku.append(empty_row.copy())
        self._puzzle = empty_sudoku

    @property
    def puzzle(self):
        return self._puzzle

    @puzzle.setter
    def puzzle(self, new_puzzle):
        self._puzzle = new_puzzle

    @puzzle.deleter
    def puzzle(self):
        del self._puzzle

    def get_row(self, row: int):
        """Returns row of Sudoku puzzle.

        Args:
            row (int): Value between 0-8 for row in Sudoku, 0 is top of puzzle.

        Returns:
            list: List representing row of Sudoku

        """
        return self.puzzle[row]

    def set_row(self, row_num: int, new_row: list):
        """Sets row of Sudoku.puzzle to new value

        Args:
            row_num (int): Row number from 0-8 being changed, 0 is the top of puzzle.
            new_row (list): String of 9 characters consisting of numbers and '.' to set the row to.

        """
        self.puzzle[row_num] = new_row

    def get_column(self, column: int):
        """Calculates a string representation of specific column.

        Args:
            column (int): Value between 0-8 for column of Sudoku, 0 is left of puzzle.

        Returns:
            list: List representing column of Sudoku.

        """
        sudoku_column = []
        for i in range(9):
            sudoku_column.append(self.get_row(i)[column])
        return sudoku_column

    def set_column(self, column_num: int, new_column: list):
        """Sets column of Sudoku.puzzle to new value.

        Args:
            column_num (int): Row number from 0-8 being changed, 0 is the left of puzzle.
            new_column (list): String of 9 characters consisting of numbers and '.' to set the column to.

        """
        for i in range(9):
            self.puzzle[i][column_num] = new_column[i]

    def get_segment(self, row: int, column: int):
        """Calculates a specific 3x3 segment of Sudoku.

        The returned string is a concatenation of the three rows of the returned segment, e.g.:
                123
                456     --->    '123456789'
                789

        Args:
            row (int): Value between 0-2 representing segment row of Sudoku puzzle, 0 is top of puzzle.
            column (int): Value between 0-2 representing segment column of Sudoku puzzle, 0 is left of puzzle.

        Returns:
            str: String representing values in segment of Sudoku.

        """
        sudoku_segment = []
        for i in range(3 * row, 3 * row + 3):
            for j in range(3 * column, 3 * column + 3):
                sudoku_segment.append(self.get_row(i)[j])
        return sudoku_segment

    def set_segment(self, row: int, column: int, new_segment: list):
        """Sets segment of Sudoku.puzzle to new value.

        Args:
            row (int): Value between 0-2 representing segment row of Sudoku puzzle, 0 is top of puzzle.
            column (int): Value between 0-2 representing segment column of Sudoku puzzle, 0 is left of puzzle.
            new_segment: String of 9 characters consisting of numbers and '.' to set the segment to.

        """
        k = 0
        for i in range(3 * row, 3 * row + 3):
            for j in range(3 * column, 3 * column + 3):
                self.puzzle[i][j] = new_segment[k]
                k += 1

    def validate_input(self, input_item: "list, str"):
        """

        Args:
            input_item (list, str): List or string to be validated by function.

        Returns:
            bool: True if validated, False if invalid string or list.

        """


    def __str__(self):
        s = ''
        for row in self.puzzle[:-1]:
            for item in row:
                s += item
            s += '\n'
        for item in self.puzzle[-1]:
            s += item
        return s


test_puzzle = Sudoku()
print(test_puzzle)
test_row = list('........1')
test_puzzle.set_segment(0, 0, test_row)
print()
print(test_puzzle)
