# You only need to edit the `solve_helper` method
# You are welcome to add helper methods if you'd like
class PathSolver:
  def __init__(self, num_rows, num_cols, obstacles):
    self.num_cols = num_cols
    self.num_rows = num_rows
    self.obstacles = obstacles # A set of tuples, each with the format (row, col)
 
  # TODO: Implement me! 
  def solve_helper(self, row_idx, col_idx):
    if row_idx == 0 and col_idx == 0:
        return 1
    if row_idx - 1 < 0 or (row_idx-1, col_idx) in self.obstacles:
        res1 = 0
    else:
        res1 = self.solve_helper(row_idx-1, col_idx)
    if col_idx - 1 < 0 or (row_idx, col_idx-1) in self.obstacles:
        res2 = 0
    else:
        res2 = self.solve_helper(row_idx, col_idx-1)
    return res1 + res2
  
  # Just to simplify things, I will always call your code via this function
  # You shouldn't need to change it
  def solve(self):
    return self.solve_helper(self.num_rows - 1, self.num_cols - 1)

if __name__ == '__main__':
  # Here's a simple base case
  # It's the 3x3 example from question 1, with two obstacles (not in the corners)
  solver = PathSolver(3, 3, {(1,0), (1,1)})
  print(solver.solve())
  solver2 = PathSolver(2, 3, {})
  print(solver2.solve())
