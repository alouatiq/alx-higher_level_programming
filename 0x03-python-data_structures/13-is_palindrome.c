#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *mid_node = NULL;
	listint_t *second_half;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;
	reverse(&second_half);

	int result = compare_lists(*head, second_half);

	reverse(&second_half);

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
 * reverse - reverses a singly linked list
 * @head: double pointer to the head of the list
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

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
 * compare_lists - compares two linked lists
 * @head1: first linked list
 * @head2: second linked list
 * Return: 1 if identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
		{
			return (0);
		}
		head1 = head1->next;
		head2 = head2->next;
	}
	return (head1 == NULL && head2 == NULL);
}
