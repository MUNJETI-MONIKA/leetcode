class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m,n=len(matrix),len(matrix[0])
        for r in range(m):
            for c in range (1,n):
                matrix[r][c]+=matrix[r][c-1]
        count=0
        for c1 in range(n):
            for c2 in range(c1,n):
                sum_counts={0:1}
                current_sum=0
                for r in range(m):
                    row_sum=matrix[r][c2]-(matrix[r][c1-1] if c1>0 else 0)
                    current_sum+=row_sum
                    if (current_sum-target) in sum_counts:
                        count+=sum_counts[current_sum-target]
                    sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1  
        return count
