#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - a function that checks for if a singlt list has a cycle
 *
 * @list: linked list to be checked
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)

{
	/* Initialize two pointers: slow and fast */
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

/*Check if not a list from begining and returns a 0 */
	if (!list)
		return (0);

/* Swivel the list using the slow and fast pointers */
	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		/* Move the slow pointer one step forward */
		slow_ptr = slow_ptr->next;
		/* Move the fast pointer two steps forward */
		fast_ptr = fast_ptr->next->next;
		/* If the two pointers meet, there is a cycle in the list */
		if (slow_ptr == fast_ptr)
			return (1);
	}

/* If end of the list, there is no cycle */
	return (0);
}
