import sys

class Nqueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
    
    def solve(self):
        results = []
        self._solve_problem(0, results)
        return results
    
    def _is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1
    

        i = row - 1
        j = col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        return True
    
    def _solve_problem(self, row, results):
        if row == self.n:
            # Add the result to the list
            result = []
            for i in range(self.n):
                for j in range(self.n):
                    if self.board[i][j] == 1:
                        result.append([i, j])
            results.append(result)
            return
        
        for col in range(self.n):
            if self._is_safe(row, col):
                self.board[row][col] = 1
                self._solve_problem(row + 1, results)
                self.board[row][col] = 0

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)
    
    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solver = Nqueens(N)
    results = solver.solve()
    
    # Print the results
    for result in results:
        print(result)
