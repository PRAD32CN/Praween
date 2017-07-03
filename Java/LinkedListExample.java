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
		//linkedlist.addFirst("First Item");

	}
}