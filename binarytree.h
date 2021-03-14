// binary tree insert operation
struct node
{
	int key;
	struct node *left, *right;
};

void inorder(struct node* root);
void binaryarray(struct node* root, int array[], int size);