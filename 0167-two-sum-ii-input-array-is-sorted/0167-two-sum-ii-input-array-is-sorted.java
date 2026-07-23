class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i=0;
        int j=numbers.length-1;
        while(i<j)
        {
            int currsum=numbers[i]+numbers[j];
            if (currsum==target)
            {
                return new int[]{i+1,j+1};
            }
            else if (currsum<target)
            {
                i++;
            }
            else 
            {
                j--;
            }

        }return  new int[]{};
    } 
}

