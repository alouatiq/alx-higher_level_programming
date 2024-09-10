#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    if (list == NULL)
        return (0);

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;        /* Move slow pointer by 1 step */
        fast = fast->next->next;  /* Move fast pointer by 2 steps */

        if (slow == fast)         /* If both pointers meet, cycle is detected */
            return (1);
    }

    return (0); /* No cycle detected */
}
