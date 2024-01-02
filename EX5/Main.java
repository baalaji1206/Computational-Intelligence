public class Main {
    public List<String> summaryRanges(int[] nums) {
        List<String> ans = new ArrayList<String>();
        int i=0,j,curr;
        while(i<nums.length){
            curr = nums[i];
            j=i+1;
            curr+=1;
            while(j<nums.length && curr==nums[j]){
                ++j;
                ++curr;
            }
            if(i!=j){
                String s = String.valueOf(nums[i]+"->"+String.valueOf(nums[j-1]));
                ans.add(s);
            }
            else{
                String s = String.valueOf(nums[i]);
                ans.add(s);
            }
            i=j;
        }
        return ans;
    }}