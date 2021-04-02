class Solution:
    def kClosest(self, points, k):
        def get_len(point):
            return point[0]**2 + point[1]**2

        def partition(lo, hi):
            if lo == hi:
                return lo
            i, j = lo, hi
            while i < j:
                while i < j and get_len(points[lo]) <= get_len(points[j]):
                    j -= 1
                while i < j and get_len(points[lo]) >= get_len(points[i]):
                    i += 1
                points[i], points[j] = points[j], points[i]
            points[i], points[lo] = points[lo], points[j]
            return i

        def inner(k):
            le, ri = 0, len(points)-1
            while le <= ri:
                mid = partition(le, ri)
                if mid < k-1:
                    le = mid+1
                elif mid > k-1:
                    ri = mid-1
                else:
                    return points[:k]
        return inner(k)


print(Solution().kClosest([[0,1],[1,0]], 2))

