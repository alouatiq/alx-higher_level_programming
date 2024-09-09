#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Singly linked list
 * @n: Integer stored in the node
 * @next: Pointer to the next node
 *
 * Description: This structure defines a node in a singly linked list,
 * where each node contains an integer `n` and a pointer `next` to the
 * next node in the list.
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function Prototypes */

/**
 * print_listint - Prints all elements of a listint_t list
 * @h: Pointer to the head of the list
 * 
 * Return: The number of nodes in the list
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list
 * @head: Double pointer to the head of the list
 * @n: Integer value to store in the new node
 * 
 * Return: Address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - Frees a listint_t list
 * @head: Pointer to the head of the list
 *
 * Description: This function will free all the nodes in the list.
 */
void free_listint(listint_t *head);

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to the head of the list
 * 
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
