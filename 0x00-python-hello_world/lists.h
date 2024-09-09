#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/* 
 * Task 10: Define a struct for a singly linked list
 * Prototype for the check_cycle function to detect cycles in a linked list
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
