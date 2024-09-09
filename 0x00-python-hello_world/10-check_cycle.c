#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;  // Slow pointer, moves one step at a time
    listint_t *fast = list;  // Fast pointer, moves two steps at a time

    // Traverse the list as long as fast and fast->next are not NULL
    while (slow && fast && fast->next)
    {
        slow = slow->next;         // Move slow pointer by one step
        fast = fast->next->next;   // Move fast pointer by two steps

        if (slow == fast)          // If both pointers meet, there is a cycle
            return (1);
    }

    // If we reach here, no cycle was found
    return (0);
}
