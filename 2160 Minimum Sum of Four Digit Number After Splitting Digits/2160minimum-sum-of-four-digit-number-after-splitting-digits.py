class Solution:
    def minimumSum(self, num: int) -> int:
        ds = [int(d) for d in str(num)]
        ds.sort()
        ds[1], ds[2] = ds[2], ds[1]
        print(ds)
        if ds[1] == 0:
            return ds[1] + ds[2] * 10 + ds[3]
        if ds[0] == 0 and ds[1] == 0:
            return ds[1] + ds[3]

        return sum([ds[2] * 10 + ds[3], ds[0] * 10 + ds[1]])