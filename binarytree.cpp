#include <stdio.h>
#include <stdlib.h>
#include "binarytree.h"

// create new BST node
struct node* newNode(int item)
{
	struct node* temp
		= (struct node*)malloc(sizeof(struct node));
	temp->key = item;
	temp->left = temp->right = NULL;
	return temp;
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

// create BST
void binaryarray(struct node* root, int array[], int size)
{
	int i;
    root = insert(root, array[0]);
    for (i=1; i<size; i++)
    {
        insert(root, array[i]);
    }
	printf("\nBinary Tree Sort:\n");
	inorder(root);
	printf("\n");
}
