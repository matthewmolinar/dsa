""" Linked Lists

- Used in many List, Queue & Stack implementations.

Terminology:
- Head: the  first node in a linked list

-Tail: last node in a linked list

-Pointer: reference to another node

-Node: an object that contains data and a pointer



SINGLY VS DOUBLY LINKED LISTS


Singly linked lists only hold a ref to the next node. In the implementation u keep ref to head and tail for quick node additions and removals.

Doubly linked list holds ref to the next and previous node. Keep head and tail for doubly linked list for quick additionals and removals.



Singly and Doubly Linked List Pros and Cons

Singly Linked List:
Pros: Uses less memory, Simpler implementation
Cons: Cannot easily access previous elements


Doubly Linked List:
Pros: can be traversed backwards
Cons: 2x memory used


**Inserting Singly linked list**

1st step: create a ref to head
2nd step: seek up to but not including the node we want to include
3rd step: adjust next pointer on the new node to point to next node and adjust next pointer on the previous node to point to the new node


** Inserting Doubly Linked List**

1st step: create a traversal pointer at the head
2nd: advance it until you are just before the insertion position
3rd: create new node, point new nodes next pointer to next node and point new nodes previous pointer to the previous node
4th: make the next next node's prev point point to new node
5th: make previous node's next pointer point to new node

change exactly 4 pointers.


** Removing from singly linked list **
1st step: create trav1 and trav2. trav1 is at head and trav2 is at head.next
2nd: advance trav2 until we find the node we want to remove while also advancing trav1.
3rd: create a temp pointer for the node want to remove. advance trav2 to next node.
4th: set trav1's next pointer to be equal to trav2.
5th: remove temp node.

** Removing from doubly linked list **
1st: seek up to the node we want to remove but only need 1 pointer since we can trav backwards.
2nd: once we reach the target node, we will set previous node's next pointer to the next node, and set next node's previous pointer to previous node.
3rd: all done!



** Complexity analysis**
Singly LinkedList:
Search - O(n) have to traverse all elements
Insert at head - O(1) we maintain a pointer to head so we can insert at head in O(1)
Insert at tail - O(1) same as above

Remove at head: O(1) we have ref so we just remove it
Remove at tail: O(n) we have to seek to the end of the list to replace the tail node with the new tail node
Remove in middle: O(n) worst case we would need to seek O(n-1) elements

Doubly LinkedList:
Search - O(n) have to traverse all elements
Insert at head - O(1) we maintain a pointer to head so we can insert at head in O(1)
Insert at tail - O(1) same as above
Remove at head: O(1) 

Remove at tail: O(1) we have ref to tail and ref to prev node so we can remove and replace in o(1)
Remove in middle: We would have to seek O(n-1) at worst case.




"""
