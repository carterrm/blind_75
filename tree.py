
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

