import java.util.*;
class Solution{
    public List<List<Integer>>threeSum(int[] num) {
        Arrays.sort(num);
        int n=num.length;
        List<List<Integer>> result= new ArrayList<>();
        for (int i= 0;i<n-2;i++)
        {
            if(num[i]>0)
            break;
            if (i>0 && num[i]==num[i-1])
            continue;
            if(num[i]+num[i+1]+num[i+2]>0)
            break;
            if(num[i]+num[n-2]+num[n-1]<0)
            continue;
            int left=i+1;
            int right=n-1;
            int first=num[i];
            while(left<right)
            {
                int total= first+num[left]+num[right];
                if(total==0)
                {
                    result.add(Arrays.asList(first,num[left],num[right]));
                    left++;
                    right--;
                    while(left<right && num[left]==num[left-1]){
                    left++;}
                    while(left<right && num[right]==num[right+1]){
                    right--;}

                }
                else if(total<0){
                left++;}
                else { right--;}
            }
        } return result;
    }
}