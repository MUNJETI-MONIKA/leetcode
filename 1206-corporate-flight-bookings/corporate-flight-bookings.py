class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff=[0]*(n+1)
        for first,last,seats in bookings:
            diff[first-1]+=seats
            if last<n:
                diff[last]-=seats
        for i in range(1,n):
            diff[i]+=diff[i-1]
        return diff[:n]
