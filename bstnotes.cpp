#include <stdio.h>
#include <stdlib.h>

// binary tree insert operation
struct node
{
	int key;
	struct node *left, *right;
};
// create new BST node
struct node* newNode(int item)
{
	struct node* temp
		= (struct node*)malloc(sizeof(struct node));
	temp->key = item;
	temp->left = temp->right = NULL;
	return temp;
}
// inorder traversal of BST
void inorder(struct node* root)
{
	if (root!=NULL)
	{
		inorder(root->left);
		printf("%d\n", root->key);
		inorder(root->right);
	}
}
// insert new node with given key in BST
struct node* insert(struct node* node, int key)
{
    // if tree is empty, return new node
    if (node == NULL)
        return newNode(key);
    // otherwise, recur down tree
    if (key<node->key)
        node->left = insert(node->left, key);
    else if (key>node->key)
        node->right = insert(node->right, key);
    // return unchanged node pointer
    return node;
}

// driver code
int main()
{
    int i;
    int a[] = {2, 46, 5, 8, 235, 75, 3, 8, 22, 4};
    int len = sizeof(a)/sizeof(a[0]);

	struct node* root = NULL;
    root = insert(root, a[0]);
    for (i=1; i<len; i++)
    {
        insert(root,a[i]);
    }

    // print inorder traversal of the BST
    inorder(root);

    return 0;
}
