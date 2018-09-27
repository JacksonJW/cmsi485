'''
Authors: Jackson Watkins, Merci Magallanes, Benjamin Smith, James Byrne
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import *
from SearchTreeNode import SearchTreeNode
from queue import *
import unittest

class Pathfinder:

    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]
    def createPath(node):
        result = []
        while node.parent: # pylint: disable=no-member
            result.insert(0, node.action) # pylint: disable=no-member
            node = node.parent # pylint: disable=no-member
        return result

    def solve(problem):
        queue = Queue()
        queue.put(SearchTreeNode(problem.initial, None, None)) # pylint: disable=no-member
        while queue:
            parent = queue.get()
            if problem.goalTest(parent.state): # pylint: disable=no-member
                return Pathfinder.createPath(parent)
            possibleMoves = problem.transitions(parent.state)# pylint: disable=no-member
            for move in possibleMoves:
                queue.put(SearchTreeNode(move[1], move[0], parent))

        return []

class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXXX", "X*...X", "XXXX.X", "XG...X", "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 8)

    def test_maze4(self):
        maze = ["XXXXXXX", "X*....X", "XXX.XXX", "X.....X", "X.XXX.X", "X.XG..X", "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 10)



if __name__ == '__main__':
    unittest.main()
