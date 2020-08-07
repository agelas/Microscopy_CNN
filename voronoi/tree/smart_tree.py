from tree.smart_node import SmartNode

class SmartTree:
    '''
    AVL tree aka self-balancing binary search tree
    '''

    @staticmethod
    def find(root: SmartNode, key, **kwargs):
        node = root
        while node is not None:
            if key == node.get_key(**kwargs):
                break
            elif key < node.get_key(**kwargs):
                node = node.left
            else:
                node = node.right

        return node

    @staticmethod
    def find_value(root: SmartNode, query: SmartNode, compare = lambda x, y: x == y, **kwargs):
        '''
        Find a node using a query node and a comparison function

        param root: (SmartNode) The root too start searching from
        param query: (SmartNode) The node we're looking for
        param compare: (lambda) Lambda expression to compare the node against the query
        param kwargs: Optional arguments to be passed to the get_key() functions
        return: (SmartNode or None) Returns the node that corresponds to the query or None
        '''
        key = query.get_key(**kwargs)
        node = root
        while node is not None:
            if key == node.get_key(**kwargs):
                if compare(node.data, query.data):
                    return node
                left = SmartTree.find_value(node.left, query, compare, **kwargs)
                if left is None:
                    right = SmartTree.find_value(node.right, query, compare, **kwargs)
                    return right
                return left
            elif key < node.get_key(**kwargs):
                node = node.left
            else:
                node = node.right

        return node

    @staticmethod
    def find_leaf_node(root: SmartNode, key, **kwargs):
        '''
        Traverses the internal nodes using the key until it reaches a leaf node.
        Will take left path if it is unclear which path to take

        param root: (SmartNode) The root of the sub tree to travel down
        param key: The key to use to determine the path
        param kwargs: Optional arguments passsed to the get_key() function
        return: (SmartNode) The node found at the end of the traversal
        '''

        node = root
        while node is not None:
            #If the node is a leaf, we're done
            if node.is_leaf():
                return node
            elif key == node.get_key(**kwargs) and not node.is_leaf():
                #Take the left path if possible
                if node.left is not None:
                    return node.left.maximum()
                #Take the right path if all else fails
                return node.right.minimum()
            elif key < node.get_key(**kwargs):
                node = node.left
            else:
                node = node.right
        return node

    @staticmethod
    def insert(root: SmartNode, node: SmartNode, **kwargs):

        node_key = node.get_key(**kwargs) if node is not None else None
        root_key = root.get_key(**kwargs) if root is not None else None

        #Regular BST insert
        if root is None:
            return node
        elif node_key < root_key:
            root.left = SmartTree.insert(root.left, node, **kwargs)
        else:
            root.right = SmartTree.insert(root.right, node, **kwargs)
        
        #Update the height of parent node
        root.update_height()

        #If the node is unbalanced, then balance it
        balance = root.balance

        #Left left
        if balance > 1 and node_key < root.left.get_key(**kwargs):
            return SmartTree.rotate_right(root)
        
        #Right right
        if balance < -1 and node_key > root.right.get_key(**kwargs):
            return SmartTree.rotate_left(root)

        #Left right
        if balance > 1 and node_key > root.left.get_key(**kwargs):
            root.left = SmartTree.rotate_left(root.left)
            return SmartTree.rotate_right(root)

        #Right left
        if balance < -1 and node_key < root.right.get_key(**kwargs):
            root.right = SmartTree.rotate_right(root.right)
            return SmartTree.rotate_left(root)

        return root
    
    @staticmethod
    def delete(root: SmartNode, key: int, **kwargs):
        if root is None:
            return root
        elif key < root.get_key():
            root.left = SmartTree.delete(root.left, key)
        elif key > root.get_key():
            root.right = SmartTree.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right.minimum()
            root.data = temp.data
            root.right = SmartTree.delete(root.right, temp.value.get_key(**kwargs))
        
        #If tree has only one node, return it
        if root is None:
            return root

        #Update the height of the ancestor node
        root.update_height()

        #Balance the tree
        root = SmartTree.balance(root)

        return root

    @staticmethod
    def balance_and_propagate(node):
        '''
        Walks up the tree recursively and rebalances all nodes, until it reaches the 
        new root

        param node: (SmartNode) The starting point, everything below this point should be
                    balanced
        return: (SmartNode) The root of the balanced tree
        '''
        node = SmartTree.balance(node)

        if node.parent is None:
            return node

        return SmartTree.balance_and_propagate(node.parent)

    @staticmethod
    def balance(node):
        '''
        Balance the tree if it is unbalanced

        param node: (SmartNode) The root node of the tree to balance
        return: (SmartNode) The new root of the sub tree
        '''
        #Left Left
        if node.balance > 1 and node.left.balance >= 0:
            return SmartTree.rotate_right(node)

        #Right Right
        if node.balance < -1 and node.right.balance <= 0:
            return SmartTree.rotate_left(node)

        #Left Right
        if node.balance > 1 and node.left.balance < 0:
            node.left = SmartTree.rotate_left(node.left)
            return SmartTree.rotate_right(node)

        #Right Left
        if node.balance < -1 and node.right.balance > 0:
            node.right = SmartTree.rotate_right(node.right)
            return SmartTree.rotate_left(node)

        return node

    @staticmethod
    def rotate_left(z):
        '''
        Rotate tree to the left

        param z: (SmartNode) The root of the subtree
        return: (SmartNode) The new root of the subtree
        '''
        #Assign parents
        grandparent = z.parent
        y = z.right
        T2 = y.left

        y.parent = grandparent

        if grandparent is not None:
            if z.is_left_child():
                grandparent.left = y
            else:
                grandparent.right = y

        #Perform rotation
        y.left = z
        z.right = T2

        #Update heights
        z.update_height()
        y.update_height()

        return y

    @staticmethod
    def rotate_right(z):
        '''
        Rotate tree to the right

        param z: (SmartNode) The root of the sub tree
        return: (SmartNode) The new root of the sub tree
        '''
        grandparent = z.parent
        y = z.left
        T3 = y.right
        #Assign parents
        y.parent = grandparent
        T3 = y.right

        if grandparent is not None:
            if z.is_left_child():
                grandparent.left = y
            else:
                grandparent.right = y

        #Perform rotation
        y.right = z
        z.left = T3

        #Update heights
        z.update_height()
        y.update_height()

        return y

        