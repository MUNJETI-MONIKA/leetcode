import java.util.Arrays;

class Solution {
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        
        int[] last = new int[m + 1];
        Arrays.fill(last, -1);
        last[m] = n;
        
        int ptr = n - 1;
        for (int j = m - 1; j >= 0; j--) {
            while (ptr >= 0 && word1.charAt(ptr) != word2.charAt(j)) {
                ptr--;
            }
            if (ptr >= 0) {
                last[j] = ptr;
                ptr--;
            }
        }
        
        int[] ans = new int[m];
        boolean changed = false;
        int j = 0;
        
        for (int i = 0; i < n && j < m; i++) {
            if (word1.charAt(i) == word2.charAt(j)) {
                ans[j++] = i;
            } else if (!changed && last[j + 1] > i) {
                ans[j++] = i;
                changed = true;
            }
        }
        
        return j == m ? ans : new int[0];
    }
}