# Solution for "2391. Minimum Amount of Time to Collect Garbage"
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.insert(0, 0)

        total, highest_glass, highest_metal, highest_paper = 0, 0, 0, 0

        for house in range(len(garbage)):
            highest_glass = house if 'G' in garbage[house] else highest_glass
            highest_metal = house if 'M' in garbage[house] else highest_metal
            highest_paper = house if 'P' in garbage[house] else highest_paper

            glass = garbage[house].count('G')
            metal = garbage[house].count('M')
            paper = garbage[house].count('P')
            total += glass + metal + paper

        for house in range(len(garbage)):
            total += travel[house] if highest_glass >= house else 0
            total += travel[house] if highest_metal >= house else 0
            total += travel[house] if highest_paper >= house else 0
            
        return total
