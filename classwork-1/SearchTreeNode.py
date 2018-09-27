'''
SearchTreeNodes contain the following information for BFS:

=== state ===
The state represented by the node, a tuple:
(x, y) = (col, row)

=== action ===
The action used to transition from the parent to this node.
- The action's value is None if the initial state
- The action's value will be a string "U", "D", "L", "R" otherwise

=== parent ===
The parent of this node in the search tree.
- The parent's value is None if the initial state
- The parent's value is a reference to the parent node otherwise
'''
class SearchTreeNode:
    
    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent
