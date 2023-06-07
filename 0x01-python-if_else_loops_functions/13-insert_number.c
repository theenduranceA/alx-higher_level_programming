#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - Function that inserts a number into sorted singly-linked list
 * @head: A pointer the linked list.
 * @number: The number to be inserted.
 *
 * Return: Pointer to the new node.
 * NULL, if function fails.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (node != NULL && (node->n >= number))
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node && node->next && (node->next->n < number))
		node = node->next;

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
