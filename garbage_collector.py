# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
from typing import List

class Solution:

    TRUCK_PAPER = 'P'
    TRUCK_METAL = 'M'
    TRUCK_GLASS = 'G'

    houses = {}

    def run_truck(self, garbage_type, garbage, travel):
        gsize = 0
        travel_cost = 0
        # last_house = -1
        partial_tcost = 0
        for house, garbage in enumerate(garbage):
            g = garbage.count(garbage_type)
            gsize += g 
            if house > 0:
                partial_tcost += travel[house-1]
            if g != 0:
                travel_cost = partial_tcost
        # if last_house != -1:
        #     # print (travel[:last_house])
        #     travel_cost = sum(travel[:last_house])
        return (gsize + travel_cost)
 

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        return self.run_truck(Solution.TRUCK_PAPER, garbage, travel) +\
               self.run_truck(Solution.TRUCK_GLASS, garbage, travel) +\
               self.run_truck(Solution.TRUCK_METAL, garbage, travel)

    # def run_truck(self, garbage_type, garbage, travel):
    #     
    #     for house, garbage in enumerate(garbage):
    #         h_p, h_g, h_m = 0,0,0            
    #         for garbage_t in garbage:
    #             if garbage_t == Solution.TRUCK_PAPER:
    #                 h_p += 1
    #             elif garbage_t == Solution.TRUCK_GLASS:
    #                 h_g += 1
    #             elif garbage_t == Solution.TRUCK_METAL:
    #                 h_m += 1
    #         if h_p != 0 andhouse > 0:
    #             travel_cost += travel[house-1] 
    #         if h_g != 0 and house > 0:
    #             travel_cost += travel[house-1] 
    #         Solutions.houses[house] = ( h_g, h_p )
    #         g = garbage.count(garbage_type)


class Solution2:
    
    # O(a,b) = ab + 2b => (a+2)b

    TRUCK_PAPER = 'P'
    TRUCK_METAL = 'M'
    TRUCK_GLASS = 'G'
    enum_truck = {TRUCK_PAPER:0, TRUCK_GLASS:1, TRUCK_METAL:2}

    def count_garbage(self, garbage, house):
        if house in self.house_garbage_count:
            return
        p, g, m = 0, 0, 0
        for pack in garbage[house]:
            if pack == Solution2.TRUCK_PAPER:
                p += 1
            elif pack == Solution2.TRUCK_GLASS:
                g += 1
            elif pack == Solution2.TRUCK_METAL:
                m += 1
        self.house_garbage_count[house] = (p, g, m)

    def run_truck(self, garbage_type, garbage, travel):
        gsize = 0
        travel_cost = 0
        partial_tcost = 0
        for house in range(0, len(garbage)):
            self.count_garbage(garbage, house)
            g = self.house_garbage_count[house][ Solution2.enum_truck[garbage_type] ]
            gsize += g
            if house > 0:
                partial_tcost += travel[house-1]
            if g != 0:
                travel_cost = partial_tcost
        # print (self.house_garbage_count)
        return (gsize + travel_cost)

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        self.house_garbage_count = {}
        return  self.run_truck(Solution2.TRUCK_PAPER, garbage, travel) +\
                self.run_truck(Solution2.TRUCK_GLASS, garbage, travel) +\
                self.run_truck(Solution2.TRUCK_METAL, garbage, travel)


s = Solution2()
print (s.garbageCollection(["G","P","GP","GG"], [2,4,3]))
print (s.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))


