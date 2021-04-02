class Solution:
    def kClosest(self, points, k):
        def get_len(point):
            if len(point) != 3:
                point.append(point[0]**2 + point[1]**2)
            return point[2]

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
            res = list()
            le, ri = 0, len(points)-1
            while le <= ri and k > 0:
                mid = partition(le, ri)
                res.append((points[mid][0], points[mid][1]))
                k -= 1
                if mid < k:
                    le = mid+1
                elif mid > k:
                    ri = mid-1
            return res

        return inner(k)


