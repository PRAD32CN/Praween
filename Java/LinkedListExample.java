import java.util.*;
public class LinkedListExample{
	public static void main(String args[]){
		LinkedList<String> linkedlist=new LinkedList<String>();
		linkedlist.add ("Item1");
		linkedlist.add ("Item2");
		linkedlist.add ("Item3");
		linkedlist.add ("Item4");
		linkedlist.add ("Item5");

		/*Display Linked List Content*/
         System.out.println("Linked List Content: " +linkedlist);
		
         /*Add First and Last Element*/
         linkedlist.addFirst("First Item");
         linkedlist.addLast("Last Item");
         System.out.println("LinkedList Content after addition: " +linkedlist);

         /*This is how to get and set Values*/
         Object firstvar = linkedlist.get(0);
         System.out.println("First element: " +firstvar);
         linkedlist.set(0, "Changed first item");
         Object firstvar2 = linkedlist.get(0);
         System.out.println("First element after update by set method: " +firstvar2);

         System.out.println("Linked List Content: " +linkedlist);


	}
}