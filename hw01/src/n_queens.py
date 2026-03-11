# src/n_queens.py
class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        """
        检查在(row, col)放置皇后是否安全。
        Bug: 故意注释掉了对角线冲突检查，导致算法可能产生非法解。
        """
        # 检查当前列是否有皇后
        for i in range(row):
            if board[i] == col:
                return False

        # 检查左上对角线
        # Bug: 下面的循环被错误地注释掉了
        # for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        #     if board[i] == j:
        #         return False

        # 检查右上对角线
        # Bug: 下面的循环被错误地注释掉了
        # for i, j in zip(range(row-1, -1, -1), range(col+1, self.n)):
        #     if board[i] == j:
        #         return False

        # 修正后的对角线检查（如果你需要一个正确的版本用于对比）
        # 检查左上对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i] == j:
                return False
            i -= 1
            j -= 1

        # 检查右上对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < self.n:
            if board[i] == j:
                return False
            i -= 1
            j += 1

        return True

    def solve_util(self, board, row):
        # 所有行都已处理完毕，找到一个解
        if row == self.n:
            self.solutions.append(board[:])
            return

        # 尝试在当前行的每一列放置皇后
        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row] = col
                self.solve_util(board, row + 1)
                # 回溯
                # board[row] = -1 # 此处不需要重置，因为下一次循环会覆盖

    def solve(self):
        self.solutions = []
        # 初始化棋盘，board[i] 表示第 i 行皇后所在的列
        board = [-1] * self.n
        self.solve_util(board, 0)
        return self.solutions

    def print_solutions(self):
        """以可视化的方式打印所有解"""
        for i, solution in enumerate(self.solutions):
            print(f"Solution {i + 1}:")
            for row in range(self.n):
                line = ""
                for col in range(self.n):
                    if solution[row] == col:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print()
