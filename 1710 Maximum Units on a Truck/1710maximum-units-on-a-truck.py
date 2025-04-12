class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        boxes = 0
        res = 0
        for box in boxTypes:
            if boxes == truckSize or truckSize == 0: return res
            if boxes + box[0] <= truckSize:
                res += box[1] * box[0]
                boxes += box[0]
            else:
                res += box[1] * (truckSize - boxes)
                boxes += box[0] * (truckSize - boxes)
                truckSize = 0
        return res