#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: - Pointer to the list to be checked.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *acc = list;
	listint_t *lag = list;


	if (list == NULL)
		return (0);

	while (acc && acc->next)
	{
		acc = acc->next->next;
		lag = lag->next;
		if (acc == lag)
			return (1);
	}
	return (0);
}
