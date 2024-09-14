#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
	listint_t *second_half, *mid_node = NULL;
	int result = 1;  /* Default is a palindrome */

	if (*head == NULL || (*head)->next == NULL)  /* Empty or single element list */
		return (1);

	/* Use the fast and slow pointer technique to find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	/* If the list has an odd number of nodes, skip the middle node */
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;  /* Terminate the first half */

	/* Reverse the second half of the list */
	reverse_list(&second_half);

	/* Compare the first half and the reversed second half */
	result = compare_lists(*head, second_half);

	/* Restore the list to its original form */
	reverse_list(&second_half);

	/* Reattach the second half to the middle node (if exists) */
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}

	return (result);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: double pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists node by node
 * @head1: first linked list
 * @head2: second linked list
 * Return: 1 if both lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}

	/* Both lists should reach NULL at the same time */
	return (head1 == NULL && head2 == NULL);
}
