class Solution {
    public int[] plusOne(int[] digits) {
        int newDigitSize = digits.length;
        for (int i = digits.length - 1; i >= 0; i--){
            if (digits[i] < 9){
                digits[i]++;
                break;
            } else {
                digits[i] = digits[i] / 10;
                if (i != 0){
                    digits[i - 1] += (digits[i] % 10);
                } else {
                    newDigitSize++;
                }
            }
        }
        int[] newDigits = new int[newDigitSize];
        if (newDigits.length == digits.length){
            newDigits = digits;
        } else {
            newDigits[0] = 1;
            for (int i = 1; i < newDigits.length; i++){
                newDigits[i] = digits[i - 1];
            }
        }
        return newDigits;
    }
}