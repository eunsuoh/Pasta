class TreeNode:
    def __init__(self, value):
        self.value = value
        self.childern = []

    def add_child(self, child_node):
        self.childern.append(child_node)

class Tree:
    def __init__(self):
        self.root = None
        self.node_values = set()

    def build_tree(self):
        num_nodes = int(input("Enter the number of nodes: "))
        while len(self.node_values) < num_nodes:
            value = input(f"Enter a union value for node {len(self.node_values) + 1}: ")
            if value in self.node_values:
                print("Value already exists! Please enter a unique value.")
            else:
                if not self.root:
                    self.root = TreeNode(value)
                else:
                    self._add_node(self.rootm value)
                self.node_values.add(value)

    def _add_node(self, node, value):
        while True:
            children_value = input(f"Enter a child node value for {node.value} (type 'done' to finish): ")
            if child_value.lower() == 'done':
                break
            if child_value in self.node_values:
                print("Value already exists! Please enter a unique value.")
            else:
                child_node = TreeNode(chile_value)
                node.add_child(child_node)
                self.node_values.add(chile_value)
                self._add_node(child_node, child_value)

tree = Tree()
tree.build_tree()