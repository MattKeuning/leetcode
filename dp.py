# This will hold the dynamic programming (tabular) solution

# You only need to edit the `solve_helper` method
# You are welcome to add helper methods if you'd like
class PathSolver:
  def __init__(self, num_rows, num_cols, obstacles):
    self.num_cols = num_cols
    self.num_rows = num_rows
    self.obstacles = obstacles # A set of tuples, each with the format (row, col)
    self.res = None

  # TODO: Implement me!
  def solve_helper(self, row_idx, col_idx):
    pass

  # Just to simplify things, I will always call your code via this function
  # You shouldn't need to change it
  def solve(self):
    return self.solve_helper(self.num_rows - 1, self.num_cols - 1)

  def solve_dp(self):
    self.res = [[0]*(self.num_cols) for i in range(self.num_rows)]
    for row, col in self.obstacles:
        self.res[row][col] = -1
    for i in range(self.num_cols):
        if self.res[0][i] == -1:
            break
        self.res[0][i] = 1
    for i in range(self.num_rows):
        if self.res[i][0] == -1:
            break
        self.res[i][0] = 1
    for i in range(1, self.num_rows):
        for j in range(1, self.num_cols):
            if self.res[i][j] == -1:
                continue
            if self.res[i-1][j] == -1 and self.res[i][j-1] != -1:
                self.res[i][j] = self.res[i][j-1]
                continue
            if self.res[i][j-1] == -1 and self.res[i-1][j] != -1:
                self.res[i][j] = self.res[i-1][j]
                continue
            if self.res[i-1][j] == -1 and self.res[i][j-1] == -1:
                self.res[i][j] = 0
                continue
            self.res[i][j] = self.res[i-1][j] + self.res[i][j-1]
    
    return self.res[-1][-1]

  def show_res(self, l):
    for i in l:
        print(i)
    return

if __name__ == '__main__':
  # Here's a simple base case
  # It's the 3x3 example from question 1, with two obstacles (not in the corners)
  # solver = PathSolver(3, 3, {(1,0), (1,1)})
  # print(solver.solve())
  solve = PathSolver(3,3,{(1,0), (1,1)})
  #solve.dp()
  print(solve.dp())
