// binary tree insert operation
struct node
{
	int key;
	int count;
	struct node *left, *right;
};

void inorder(struct node* root);
void binaryarray(int array[], int size);