#include "lists.h"

/*
 * Task 10: Function to detect if there is a cycle in a singly linked list
 * Uses Floyd's Cycle Detection Algorithm (Tortoise and Hare method)
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (slow && fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
            return (1);  // Cycle detected
    }
    return (0);  // No cycle
}
