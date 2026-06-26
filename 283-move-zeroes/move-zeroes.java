class Solution {
    public void moveZeroes(int[] nums) {
        int n= nums.length;
        int windex=0;
        for(int i=0; i<n; i++ ){
            if(nums[i]!=0){
                nums[windex]=nums[i];
                windex+=1;

            }
        }
        for(int j=windex; j<n; j++){
            nums[j]=0;
        }
        
        
    }
}