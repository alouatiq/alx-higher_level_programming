#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Double pointer to the head of the list
 * @number: The number to insert
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    /* Assign data to the new node */
    new_node->n = number;
    new_node->next = NULL;

    /* If the list is empty or the new node needs to be the new head */
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Find the correct insertion point */
    current = *head;
    while (current->next != NULL && current->next->n < number)
    {
        current = current->next;
    }

    /* Insert the new node at the correct position */
    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}
