class Solution {
    public int rob(int[] nums) {
        int[] maxrob= new int[nums.length];
        if(nums.length==0)
            return 0;
        if(nums.length==1)
            return nums[0];
        if(nums.length==2)
            return Math.max(nums[0],nums[1]);
        
        maxrob[0]=nums[0];
        maxrob[1]=Math.max(nums[0],nums[1]);
        for(int i=2;i<nums.length;i++){
            maxrob[i]=Math.max(maxrob[i-2]+nums[i],maxrob[i-1]);
            System.out.println(maxrob[i]);

        
        }
        return maxrob[nums.length-1];
    }
}