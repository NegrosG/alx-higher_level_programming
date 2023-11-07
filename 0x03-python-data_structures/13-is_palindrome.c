#include "lists.h"

/**
  *palindrome - this is the recursive pallind
  *@head: head list
  *Return; 0 if it is not a palimdrome
  *1 if it takes a palimdrome
  */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
  *aux_pallind - funct to know pallindrome
  *@head: head list
  *@end: end list
  */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
