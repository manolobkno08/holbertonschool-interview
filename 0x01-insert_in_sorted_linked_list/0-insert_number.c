#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node into the list
 * @head: current node
 * @number: numbert to insert into the list
 *
 * Description: add number into singly linked
 */

listint_t *insert_node(listint_t **head, int number)
{
	// Create new node and pointer to save value h
	listint_t *newNode;
	listint_t *h = *head;

	// Storage memory
	newNode = malloc(sizeof(listint_t));
	if (newNode)
	{
		// Set node value to n and next pointer
		newNode->n = number;
		newNode->next = NULL;

		if(*head == NULL || (*head)->n >= number)
		{
			newNode->next = *head;
			*head = newNode;
		}
		else
		{
			while(h->next != NULL && h->next->n < number)
			{
				h = h->next;
			}
			newNode->next = h->next;
			h->next = newNode;
		}
		return (newNode);
	}
	return (NULL);
}
