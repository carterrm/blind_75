from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_dfs(root, count):
    count += 1
    left_count = max_depth_dfs(root.left, count) if root.left is not None else 0
    right_count = max_depth_dfs(root.right, count) if root.right is not None else 0
    return max(count, left_count, right_count)


def max_tree_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    return max_depth_dfs(root, 0)


def same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    if p.val == q.val:
        if p.left is None and p.right is None and q.left is None and q.right is None:
            return True
        return same_tree(p.left, q.left) and same_tree(p.right, q.right)
    else:
        return False


def invert_tree(root: TreeNode) -> TreeNode:
    # Top approach is DFS- since it doesn't require use of a queue, it's faster & better on memory (90.63% runtime, 69.88% memory)
    if root is None or (root.left is None and root.right is None):
        return root
    else:
        invert_tree(root.left)
        invert_tree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp
    return root
    # Bottom approach is BFS, which is slower & worse on memory.

    # if root is None:
    #     return None
    # bfs = deque()
    # bfs.append(root)
    # while len(bfs) != 0:
    #     current = bfs.popleft()
    #     if current.left is not None:
    #         bfs.append(current.left)
    #     if current.right is not None:
    #         bfs.append(current.right)
    #     temp = current.left
    #     current.left = current.right
    #     current.right = temp
    # return root


def validate_binary_tree(root: TreeNode) -> bool:
    #Beats 75.53% on runtime, 18.73% on memory usage

    def solve_valid_bst(root, floor, ceiling):
        if root is None:
            return True
        if root.val < floor or root.val > ceiling:
            return False
        if root.right is not None and root.right.val <= root.val:
            return False
        if root.left is not None and root.left.val >= root.val:
            return False
        if not solve_valid_bst(root.left, floor, root.val - 1) or not solve_valid_bst(root.right, root.val + 1, ceiling):
            return False
        else:
            return True

    return solve_valid_bst(root, -2**31, (2**31) - 1)
