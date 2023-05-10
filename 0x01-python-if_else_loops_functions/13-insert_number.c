#include "lists.h"

/**
 * insert_node - Function Inserts a number into a sorted singly-linked list.
 * @head: Pointer the head of the linked-list.
 * @number: The number to insert.
 *
 * Return: NULL - If the function fails.
 *         Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /* Create a new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;
    new_node->n = number;
    new_node->next = NULL;

    /* If the list is empty, make the new node the head and return */
    if (*head == NULL) {
        *head = new_node;
        return new_node;
    }

    /* Swivel the list to find the right place to insert the new node */
    current = *head;
    while (current->next != NULL && current->next->n < number)
        current = current->next;

    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}

