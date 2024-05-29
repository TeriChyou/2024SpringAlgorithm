## 2024 05 29
# queens function --> solve and place_queen methods
# promising function --> check_place method
# backTracking => go back to the previous possible and doable result and keep resulting out the other result.

class Queens:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self): # queen
        positions = [-1] * self.size
        self.place_queen(positions, 0)

    def place_queen(self, positions, target_row): # queen
        if target_row == self.size:
            self.show_full_board(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.place_queen(positions, target_row + 1)

    @staticmethod
    def check_place(positions, ocuppied_rows, column):  # promising
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
                return False
        return True

    def show_full_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def get_solutions(self):
        return self.solutions


size = input("Enter the board size: ")
queen = Queens(int(size))
print("Number of solutions:", queen.get_solutions())