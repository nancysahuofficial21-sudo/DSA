public class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }

        // Step 1: Find the middle of the linked list
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse the second half of the list
        ListNode prev = null;
        ListNode current = slow;
        while (current != null) {
            ListNode nextTmp = current.next;
            current.next = prev;
            prev = current;
            current = nextTmp;
        }

        // Step 3: Compare the first half and the reversed second half
        ListNode firstHalfPointer = head;
        ListNode secondHalfPointer = prev; // 'prev' is now the head of the reversed second half
        
        while (secondHalfPointer != null) {
            if (firstHalfPointer.val != secondHalfPointer.val) {
                return false; // Mismatch found
            }
            firstHalfPointer = firstHalfPointer.next;
            secondHalfPointer = secondHalfPointer.next;
        }

        return true;
    }
}
