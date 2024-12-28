class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() > haystack.length()){
            return -1;
        }
        boolean inHaystack = false;
        int range = haystack.length() - needle.length();
        for (int i = 0; i <= range; i++){  
            if (haystack.charAt(i) == needle.charAt(0)){
                int currIndex = i;
                for (int j = 0; j < needle.length(); j++){
                    if (needle.charAt(j) == haystack.charAt(currIndex)){
                        currIndex++;
                        inHaystack = true;
                    } else {
                        inHaystack = false;
                        break;
                    }
                }
            }
            if (inHaystack){
                return i;
            }
        }
        return -1;
    }
}