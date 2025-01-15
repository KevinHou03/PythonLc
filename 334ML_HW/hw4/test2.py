import numpy as np

# a = np.array([1, 0, 0, 0, 1, 0, 1, 1])
# print(a[1])  # 2
# for index, element in enumerate(a):
#     if element == 1:
#         a[index] = 1
#     if element == 0:
#         a[index] = -1
#
#
#
# yHat = np.array(([1, -1, 1, -1, 1, 1, -1],[1, -1, 1, -1, 1, 1, -1],[1, -1, 1, -1, 1, 1, -1],[1, -1, 1, -1, 1, 1, -1]))
# yTrue = np.array([1, -1, 1, 1, 1, -1, -1])


#
# def calc_mistake(yhat, ytrue):
#     label_num = yHat.shape[0]
#     mistake_count = 0
#     for i in range(0, label_num):
#         if yhat[i] != ytrue[i]:
#             mistake_count += 1
#     return mistake_count



# for index, elem in enumerate(yHat):
#     print(index,'\n')
#     print(elem)
#
# print('********')
#
# for i in range(0,yHat.shape[0]):
#     print(i,'\n')
#     print(yHat[i])

# for i in range(0,10,2):
#     print(i)

sample_num = 130
k = 5
distance = sample_num // k
for i in range(0, sample_num, distance):
    print(i)


    '''
    /******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
 
#include <stdio.h>
#include <stdlib.h>

struct Node{
    int value;
    struct Node* next;
};

struct Node* addFirst(int x, struct Node* head) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    
    if(head == NULL){
        return newNode;
    }

    newNode->value = x;
    newNode->next = head;

    return newNode; // 返回新的头节点
}

struct Node* addLast(int x, struct Node* head){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    
    newNode -> value = x;
    newNode -> next = NULL;
    
    if (head == NULL) {
        // 如果链表为空，新节点成为链表的唯一节点
        return newNode;
    }
    
    struct Node* current = head;
    while(current -> next != NULL){
        current = current -> next;
    }
    current->next = newNode;
    return head;
}

struct Node* removeFirst(int x, struct Node* head){
    if ( head == NULL )            // Check if list is empty
      {
         return NULL;
      }
    struct Node* ret = head -> next;
    free(head);
    return ret;
}

int list_len(struct Node* head){
    struct Node* temp = head;
    int counter = 0;
    while(temp -> next != NULL){
        temp = temp -> next;
        counter += 1;
    }
    return (counter + 1);
}

struct Node* removeLast(int x, struct Node* head){
    
    if (head == NULL) {
        // 如果链表为空，新节点成为链表的唯一节点
        return NULL;
    }
    if ( head->next == NULL )
      {
         free(head);          // De-allocated deleted node
         return NULL;      // Return the empty list
      }
      
    struct Node* current = head;
    struct Node* previous = head;
    
    while(current -> next != NULL){
        previous = current;
        current = current -> next;
    }
    previous -> next = NULL;
    free(current);
    return head;
    
}
struct Node* insertAt(struct Node *h, int x, int pos ){
    if(pos == 0 || h == NULL){
        
return addFirst(x,h);  // 返回新的头节点
}
    if(pos >= (list_len(h) + 1)){
        return h;
    }
        
    struct Node* current = h;
    struct Node* previous = h;
    for(int i = 0; i < pos; i++){
        previous = current;
        current = current -> next;
    }
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> value = x;
    previous -> next = newNode;
    newNode -> next = current;
    return h;
}

struct Node *removeAt(struct Node *h, int pos ){
    if (h == NULL || pos < 0 || pos >= (list_len(h))) {
        // 无效的参数，返回原链表
        return h;
    }
    if (pos == 0) {
        struct Node* newHead = h->next;
        free(h);
        return newHead;
    }
    
    struct Node* current = h;
    struct Node* previous = h;
    struct Node* nextOne = h;
    for(int i = 0; i < pos; i++){
        previous = current;
        current = current -> next;
    }
    nextOne = current -> next;
    previous -> next = nextOne;
    free(current);
    return h;
}

void printList(struct Node* head){// head is what we can get
    struct Node* current = head;
    if ( head == NULL )            // Check if list is empty
      {
         return;
      }
    while(current != NULL){
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("NULL\n");
}

int main(){
    
   struct Node *head = NULL;
   int k;

   printList(head);

   for (k = 0; k < 5; k++ )
   {
      head = addFirst(k,head);
      printList(head);
   }
//   head = insertAt(head,9,4);
//   printList(head);

// head = removeAt(head,0);
// printList(head);
   
   struct Node *head2 = NULL;
      for (k = 0; k < 5; k++ )
   {
      head2 = addLast(k,head2);
      printList(head2);
   }
   
   
   head2 = removeAt(head2,2);
   printf("%d",list_len(head2));


    // head2 = removeAt(head2,0);
    // printList(head2);
 
    return 0;//HANDLE THE EXCEPTION!
}
    '''