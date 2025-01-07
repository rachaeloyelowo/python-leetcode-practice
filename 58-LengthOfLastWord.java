class Solution {
    public int lengthOfLastWord(String s) {
        int wrdLen = 0;

        for (int i = s.length() - 1; i >= 0; i--){
            if (s.charAt(i) != ' '){
                int j = i;
                while (s.charAt(j) != ' '){
                    wrdLen++;
                    if (j - 1 < s.length() && j - 1 >= 0){
                        j--;
                    } else {
                        break;
                    }
                }
                break;
            }
        }
        return wrdLen;
    }
}