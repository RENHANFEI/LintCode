class Node(object):
    def __init__(self, name, alive=True):
        self.name = name
        self.alive = alive
        self.children = []


class FamilyTree(object):
    def __init__(self):
        self.root = Node(name='root', alive=False)
        self.nodes_hash = {'root':self.root}
        self.succession = []
        self.changed = False

    def birth(self, name, parent='root'):
        baby = Node(name)
        parent_node = self.nodes_hash[parent]
        parent_node.children.append(baby)
        self.nodes_hash[name] = baby
        self.changed = True

    def death(self, node):
        self.nodes_hash[node].alive = False
        self.changed = True

    def succeed(self):
        if self.changed:
            self.succession = []
            self.__preorder(self.root)
            self.changed = False
        return self.succession

    def __preorder(self, node):
        if node.alive:
            self.succession.append(node.name)
        children = node.children
        for child in children:
            self.__preorder(child)

family = FamilyTree()
family.birth('A')
family.birth('B', 'A')
family.birth('C', 'A')
family.birth('D', 'A')
family.birth('E', 'B')
family.birth('F', 'B')
print(family.succeed())
family.birth('G', 'E')
print(family.succeed())
family.death('A')
print(family.succeed())
family.death('E')
print(family.succeed())
