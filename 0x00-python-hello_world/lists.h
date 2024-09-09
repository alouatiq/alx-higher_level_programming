#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/* 
 * Task 10: Define a struct for a singly linked list
 * Prototype for the check_cycle function to detect cycles in a linked list
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
