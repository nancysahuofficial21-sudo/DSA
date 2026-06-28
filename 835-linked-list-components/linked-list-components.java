/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.HashSet;
import java.util.Set;
class Solution {
    public int numComponents(ListNode head, int[] nums) {
        int count=0;
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        ListNode current = head;
        while(current!=null){
            if(numSet.contains(current.val)&&((current.next==null)||(!numSet.contains(current.next.val)))){
                count++;

            }
            current=current.next;
            
                
        }
        return count;
                
                
                
            
    
        

        
    }
}