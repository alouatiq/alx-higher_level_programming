#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

size_t print_listint(const listint_t *h)
{
	const listint_t *current = h;
	size_t n = 0;

	while (current != NULL)
	{
	    printf("%i\n", current->n);
	    current = current->next;
	    n++;
	}

	return n;
}

listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current;

	if (!new_node)
	    return NULL;

	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
	{
	    *head = new_node;
	}
	else
	{
	    current = *head;
	    while (current->next != NULL)
	        current = current->next;
	    current->next = new_node;
	}
	
	return new_node;
}

void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
	    current = head;
	    head = head->next;
	    free(current);
	}
}
