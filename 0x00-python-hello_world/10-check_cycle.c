#include "lists.h"
/**
 *check_cycle - To check a cycle in a linked list
 *@list: the list variable to be checked
 *Return: 1 if the cycle is present, 0 if none
 */
int check_cylce(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;
if (!list)
return (0);
while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
