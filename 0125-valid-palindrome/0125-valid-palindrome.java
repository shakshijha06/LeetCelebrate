class Solution {
    public boolean isPalindrome(String s) {
        int left=0;
        int right=s.length()-1;
        while(left<right)//move till left is less than right
        {
            while(left<right && !Character.isLetterOrDigit(s.charAt(left)))//check if any non alphanumeric character in any index left encounter
            { 
                left++;//increment left if yes
            }
            while(left<right && !Character.isLetterOrDigit(s.charAt(right)))//check if any non alphanumeric characters in any index right encounters 
            {
                right--;//decrement right if yes
            }
            if(Character.toLowerCase(s.charAt(left))!= Character.toLowerCase(s.charAt(right)))//compare characters 
            {
                return false;
                }
                left++;
                right--;
            
        }return true;
    }
}