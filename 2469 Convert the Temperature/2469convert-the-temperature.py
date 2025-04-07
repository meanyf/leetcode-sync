class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [round(celsius + 273.15, 5), round(celsius * 1.80 + 32.00, 5)]