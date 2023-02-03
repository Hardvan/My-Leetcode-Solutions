/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    // Getting no. of nodes
    int count = 0;
    struct ListNode *p, *prev = NULL;
    for(p=head; p!=NULL; p=p->next)
        count++;
    
    int ind = count - n; // index to be deleted
    int i = 0;

    p = head;
    while(p != NULL)
    {
        if (ind == i)
        {
            // First Node
            if (prev == NULL)
            {
                head = p->next;
                break;
            }
            else
            {
                prev->next = p->next;
                free(p);
                break;
            }
        }

        i++;
        prev = p;
        p = p->next;
    }

    return head;
}
