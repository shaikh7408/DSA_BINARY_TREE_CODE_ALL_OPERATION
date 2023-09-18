from node import Node
class Binary_Tree:
    def __init__(self,head:Node):
        self.head=head
    def add(self,new_node:Node):
        current_node=self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError("Value Already exits")
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node=current_node.right
                else:
                    current_node.right=new_node
                    break
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node=current_node.left
                else:
                    current_node.left=new_node
                    break


    def find_node(self,value:int):
        current_node=self.head
        while current_node:
            if  value == current_node.value:
                return current_node
            elif value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node = current_node.left
            elif value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
        raise  LookupError(f'The Value {value} not exits in a tree')
    def Inorder(self):
        self.Inorder_recursive(self.head)

    def Inorder_recursive(self,current_node):
        if not current_node:
            return
        self.Inorder_recursive(current_node.left)
        print(current_node)
        self.Inorder_recursive(current_node.right)
    def preorder(self):
        self.preorder_recursive(self.head)
    def preorder_recursive(self,current_node):
        if not current_node:
            return
        print(current_node)
        self.Inorder_recursive(current_node.left)
        self.Inorder_recursive(current_node.right)

    def find_parent_node(self,value:int)->Node:
        current_node=self.head
        if self.head and self.head.value==value:
            return self.head
        while current_node:
            if(current_node.left and current_node.left.value==value or current_node.right and current_node.right.value==value ):
                return current_node
            elif value>current_node.value:
                current_node=current_node.right
            elif value<current_node.value:
                current_node=current_node.left
    def Right_most_node(self,node:Node)->Node:
        current_node=node
        while current_node.right:
            current_node=current_node.right
        return current_node
    def deleting_node(self,value: int):
        deleting_element=self.find_node(value)
        parent_of_deleting_element=self.find_parent_node(value)
        if deleting_element.left and deleting_element.right:
            rightmost=self.Right_most_node(deleting_element.left)
            parents_of_righmost_node=self.find_parent_node(rightmost.value)
            if parents_of_righmost_node != deleting_element:
                parents_of_righmost_node.right = rightmost.left
                rightmost.left = deleting_element.left
            rightmost.right = deleting_element.right
            if deleting_element==parent_of_deleting_element.left:
                parent_of_deleting_element.left=rightmost
            elif deleting_element==parent_of_deleting_element.right:
                parent_of_deleting_element.right=rightmost
            else:
                self.head=rightmost
        elif deleting_element.left or deleting_element.right:
            if deleting_element==parent_of_deleting_element.right:
                parent_of_deleting_element=deleting_element.right or deleting_element.left
            elif deleting_element==parent_of_deleting_element.left:
                parent_of_deleting_element=deleting_element.right or deleting_element.left
            else:
                self.head=deleting_element.right or deleting_element.left
            pass
        else:#thats means there i no child
            if deleting_element==parent_of_deleting_element.left:
                parent_of_deleting_element.left=None
            elif deleting_element==parent_of_deleting_element.right:
                parent_of_deleting_element.right=None
            else:
                self.head=None







