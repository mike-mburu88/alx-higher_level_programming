#include "lists.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 *insert_node - inserts node in a singly linked list
 *@head: the head pointer in the list
 *@number: the number value to be inserted
 *Return: NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *new;
new = malloc(sizeof(listint_t))
if new == NULL)
return (NULL);
new->next = number;
if (node == NULL || node->n >= number)
{
new->next = node;
*head = new;
return (new);
}
while (node && node->next && node->next->n < number)
node = node->next;
new->next = node->next;
node->next = new;
return (new);
}
