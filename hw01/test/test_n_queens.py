# tests/test_n_queens.py
import unittest
from src.n_queens import NQueensSolver

class TestNQueens(unittest.TestCase):
    def test_n4_solutions(self):
        """测试 N=4 时的解"""
        solver = NQueensSolver(4)
        solutions = solver.solve()
        # N=4 时，标准的八皇后问题有 2 个解
        self.assertEqual(len(solutions), 2)

        # 验证每个解的合法性（这是测试的核心）
        for solution in solutions:
            self.assertTrue(self.is_solution_valid(4, solution), f"Solution {solution} is invalid")

    def test_n8_solutions(self):
        """测试 N=8 时的解"""
        solver = NQueensSolver(8)
        solutions = solver.solve()
        # N=8 时，标准的八皇后问题有 92 个解
        self.assertEqual(len(solutions), 92)

        # 由于计算量较大，这里只验证前几个解的合法性
        for solution in solutions[:5]: # 验证前5个解
            self.assertTrue(self.is_solution_valid(8, solution), f"Solution {solution} is invalid")

    def is_solution_valid(self, n, board):
        """
        辅助函数：验证一个给定的解是否合法
        逻辑：检查每一行的皇后是否与其他行的皇后冲突
        """
        for row in range(n):
            col = board[row]

            # 检查列冲突
            for r in range(row):
                if board[r] == col:
                    return False

            # 检查左上对角线冲突
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i] == j:
                    return False
                i -= 1
                j -= 1

            # 检查右上对角线冲突
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i] == j:
                    return False
                i -= 1
                j += 1

        return True

if __name__ == '__main__':
    unittest.main()
