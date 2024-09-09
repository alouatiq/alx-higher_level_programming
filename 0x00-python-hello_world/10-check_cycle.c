#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the list.
 * Description:
 * Uses Floyd's Cycle Detection Algorithm
 * (Tortoise and Hare) with two pointers:
 * 'slow' moves one step, 'fast' moves two
 * steps. If they meet, a cycle exists. 
 * If 'fast' reaches the end (NULL),
 * there's no cycle.
 * Return: 1 if a cycle is found, 0 if no cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;  // Slow pointer moving one step at a time
	listint_t *fast = list;  // Fast pointer moving two steps at a time

	// Traverse the list
	while (fast && fast->next)
	{
		slow = slow->next;         // Move slow by one node
		fast = fast->next->next;   // Move fast by two nodes

		if (slow == fast)          // If they meet, a cycle exists
			return (1);
	}

	// If fast pointer reaches the end, there's no cycle
	return (0);
}
