import itertools
import copy
from typing import Generator, Union


class Sudoku(object):
    """Represents a 9x9 sized Sudoku puzzle.

    Initializing creates an empty Sudoku; empty spaces in Sudoku puzzle are represented by '.' character.

    Attributes:
        puzzle (list): list of length 9 of length 9 strings representing Sudoku.

    """

    def __init__(self):
        empty_row = SudokuList('.........')
        empty_sudoku = []
        for i in range(9):
            empty_sudoku.append(copy.deepcopy(empty_row))
        self.puzzle = empty_sudoku

    def get_row(self, row: int):
        """Returns row of Sudoku puzzle.

        Args:
            row (int): Value between 0-8 for row in Sudoku, 0 is top of puzzle.

        Returns:
            list: List representing row of Sudoku

        """
        return self.puzzle[row]

    def set_row(self, row_num: int, new_row: "SudokuList"):
        """Sets row of Sudoku.puzzle to new value

        Args:
            row_num (int): Row number from 0-8 being changed, 0 is the top of puzzle.
            new_row (SudokuList): List of 9 characters consisting of numbers and '.' to set the row to.

        """
        self.puzzle[row_num] = copy.deepcopy(new_row)

    def get_column(self, column: int) -> "SudokuList":
        """Calculates a string representation of specific column.

        Args:
            column (int): Value between 0-8 for column of Sudoku, 0 is left of puzzle.

        Returns:
            list: List representing column of Sudoku.

        """
        sudoku_column = []
        for i in range(9):
            sudoku_column.append(self.get_row(i)[column])
        return SudokuList(sudoku_column)

    def set_column(self, column_num: int, new_column: "SudokuList"):
        """Sets column of Sudoku.puzzle to new value.

        Args:
            column_num (int): Row number from 0-8 being changed, 0 is the left of puzzle.
            new_column (SudokuList): List of 9 characters consisting of numbers and '.' to set the column to.

        """
        copied_column = copy.deepcopy(new_column)
        for i in range(9):
            self.puzzle[i][column_num] = copied_column[i]

    def get_segment(self, row: int, column: int) -> "SudokuList":
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
        return SudokuList(sudoku_segment)

    def set_segment(self, row: int, column: int, new_segment: "SudokuList"):
        """Sets segment of Sudoku.puzzle to new value.

        Args:
            row (int): Value between 0-2 representing segment row of Sudoku puzzle, 0 is top of puzzle.
            column (int): Value between 0-2 representing segment column of Sudoku puzzle, 0 is left of puzzle.
            new_segment (SudokuList): List of 9 characters consisting of numbers and '.' to set the segment to.

        """
        copied_segment = copy.deepcopy(new_segment)
        k = 0
        for i in range(3 * row, 3 * row + 3):
            for j in range(3 * column, 3 * column + 3):
                self.puzzle[i][j] = copied_segment[k]
                k += 1

    def check_legality(self) -> bool:
        """Checks to ensure all columns and segments are legal SudokuLists
        
        NOTE: Assumes all rows were set using set_row and would therefore already be know to be legal.

        Returns:
            bool: True if Sudoku is currently legal, False if it is not.

        """
        for column in range(9):
            if not self.get_column(column).validate_list():
                return False
        for i in range(3):
            for j in range(3):
                if not self.get_segment(i, j).validate_list():
                    return False
        return True

    def input(self):
        """Asks user for an input of all rows of Sudoku and checks for legality.

        Returns:
            None

        """
        print("Please enter rows of Sudoku; use '.' for blank spaces:")
        legal_sudoku = False
        while not legal_sudoku:
            for row in range(9):
                valid_row = False
                while not valid_row:
                    new_row = SudokuList(input("Row {}: ".format(row+1)))
                    valid_row = new_row.validate_list()
                    if valid_row:
                        self.set_row(row, new_row)
                    else:
                        print("Row must must be 9 items long contain only unique integers from 1-9 or '.' for blank "
                              "spaces.")
                    if not self.check_legality():
                        print("Sudoku entered is not legal, please start from beginning ensuring all rows column and "
                              "segments contain only unique digits.")
                        break
                else:
                    continue
                break

    def solve(self):
        """Solves the Sudoku puzzle of the associated object.

        If Sudoku puzzle has multiple solutions, first found correct solution will be returned rather than all
        solutions. If no solution can be found due to improper starting conditions, ValueError is raised.

        Returns:
            Sudoku: Solved version of self.puzzle

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


class SudokuList(object):
    """Represents a row, column or segment of Sudoku as list of characters.

    __init__ checks if input string is a valid SudokuList.

    Args:
        input_string (str, list): string or list of either '.' representing blank spaces or unique character digits 1-9.

    Attributes:
        values (list): represents Sudoku list (row, column, segment).
    """

    def __init__(self, input_string: Union[str, list]):
        self.values = list(input_string)

    def validate_list(self) -> bool:
        """Ensures SudokuList is legal.

        Checks to ensure all items are unique digits 1-9 or any number of '.'

        Returns:
            bool: True if input is a valid Sudoku list, False if not.

        """
        if type(self.values) != str and type(self.values) != list:
            return False
        if len(self.values) != 9:
            return False
        test_dict = {}
        for item in self.values:
            if item.isdigit():
                if item == '0':
                    return False
                elif len(item) > 1:
                    return False
                else:
                    test_dict[item] = test_dict.get(item, 0) + 1
                    if test_dict[item] > 1:
                        return False
            elif not item == '.':
                return False
        else:
            return True

    def valid_permutations(self) -> Generator["SudokuList", None, None]:
        """Determines all valid permutations of full legal SudokuLists using self as seed.

        Function will return a list of SudokuList elements that are all the valid permutations of existing SudokuList
        object. All returned elements will be the original SudokuList with blank elements filled in in all permutations.

        Yields:
            list: permutation of valid SudokuList

        """
        permute_base = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for item in self.values:
            if not item == '.':
                permute_base.remove(item)
        for permutation_partial in itertools.permutations(permute_base):
            i = 0
            permutation = []
            for value in self.values:
                if value == '.':
                    permutation.append(permutation_partial[i])
                    i += 1
                else:
                    permutation.append(value)
            yield SudokuList(permutation)

    def __str__(self):
        print_str = "<"
        for item in self.values:
            print_str += item
        print_str += ">"
        return print_str

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value


test_puzzle = Sudoku()
test_puzzle.input()
