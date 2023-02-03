/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;
    
    struct ListNode *p, *q;
    p = list1;
    while(p->next != NULL)
        p = p->next;
    p->next = list2;

    for(p = list1; p->next != NULL; p = p->next)
    {
        for(q = p->next; q != NULL; q = q->next)
        {
            if (p->val > q->val)
            {
                int temp = p->val;
                p->val = q->val;
                q->val = temp;
            }
        }
    }

    return list1;
}
