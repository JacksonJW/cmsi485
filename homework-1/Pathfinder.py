'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to all
of the goals with optimal cost.

This task is done in the solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''
import unittest
import itertools
from queue import PriorityQueue
from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode

# Calculates the manhattan distance beteen the parent node<tuple> (state)
# and the goal node<tuple> (goal)
def manhattanDist(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def createPath(node):
    result = []
    while node.parent:
        result.append(node.action)
        node = node.parent
    result.reverse()
    return result

def getDirectionsToGoal(problem, initial, goal):
    # "goals" is in the form i.e. [(2, 2), (2, 1), ... ]
    heuristicCostFromInitial = manhattanDist(initial, goal) # ONE GOAL
    initial = SearchTreeNode(initial, None, None, 0, heuristicCostFromInitial)
    closedList = []
    costToNode = 0

    # find the shortest path to the goal state avoiding walls implement a closed list
    frontier = PriorityQueue()
    frontier.put(initial)

    # ('U', 1, (2,3))
    # state, action, parent, totalCost, heuristicCost
    while frontier:
        parent = frontier.get()

        if parent.heuristicCost == 0:
            return createPath(parent)

        closedList.append(parent.state)
        possibleTransitions = problem.transitions(parent.state)

        # if possibleTransitions:

        for possibleTransition in possibleTransitions:
            transitionStateIndex = 2
            costToNode = parent.totalCost + \
            problem.cost(possibleTransition[transitionStateIndex])

            if possibleTransition[transitionStateIndex] not in closedList \
            or costToNode < parent.totalCost:

                heuristicCost = manhattanDist(
                    possibleTransition[transitionStateIndex], goal)
                newNode = SearchTreeNode(possibleTransition[transitionStateIndex],
                                         possibleTransition[0], parent, costToNode,
                                         heuristicCost)
                frontier.put(newNode)

    return "no solution"


def solve(problem, initial, goals):
    for goal in goals:
        if not problem.transitions(goal):
            return None

    possiblePaths = list(itertools.permutations(goals))

    listOfPaths = []

    for permutation in possiblePaths:
        initialCopy = initial
        listOfDirections = []
        for goal in permutation:

            listOfDirections.extend(
                getDirectionsToGoal(problem, initialCopy, goal))

            initialCopy = goal

        listOfPaths.append(listOfDirections)

    return min(listOfPaths)


class PathfinderTests(unittest.TestCase):
    # These first 4 tests include one goal state to ensure one goal state works
    # with the lowest cost.

    def test_maze1(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 8)

    def test_maze2(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(3, 3), (5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze3(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.MMX",
                "X...M.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze4(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.XXX",
                "X...X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)


    # These 4 tests include one goal state to ensure one goal state works
    # with the lowest cost.

    def test_maze5(self):
        maze = ["XXXXX",
                "X...X",
                "X...X",
                "X.M.X",
                "XXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(3, 1)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 4)

    def test_maze6(self):
        maze = ["XXXXXXX",
                "X....XX",
                "X.X.M.X",
                "X.M...X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 6)

    def test_maze7(self):
        maze = ["XXXXXXX",
                "X.M...X",
                "X.X.X.X",
                "X...X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 8)

    def test_maze8(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.XXX",
                "X...X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals = [(5, 3)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)

    def test_maze9(self):
        maze = ["XXXXX",
                "X...X",
                "XXX.X",
                "X...X",
                "XXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals = [(3, 1), (1, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 6)


if __name__ == '__main__':
    unittest.main()
