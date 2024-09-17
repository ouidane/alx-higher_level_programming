#include "lists.h"

/**
 * reverse_listint - Reverses a singly linked list
 * @head: Pointer to the pointer of the first node in the list
 *
 * Return: Pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *first_half = *head, *second_half = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    second_half = reverse_listint(&slow);

    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
            return (0);
        first_half = first_half->next;
        second_half = second_half->next;
    }

    return (1);
}
