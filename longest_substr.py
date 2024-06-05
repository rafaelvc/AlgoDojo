# https://leetcode.com/problems/construct-the-longest-new-string/
from typing import List
from functools import cache

# Prestar bem atençao no problema, eu achei que depois de AB só podia BB, 
# mas na verdade depois de AB pode outro AB ou BB.
# Somente passou o time limit exceed com o uso do @cache

# Verifiquei soluções de outros autores para o problema e se trata de um
# puzzle a ser resolvido na relação matemática entre as variaveis de entrada 
# do que algo que tem busca por solução com otimização em conjutno com alguma estrutura de dados, ou 
# puzzle parcial e o restante é busca por solução etc. Parece ser mais quebra a cabeça do 
# que treinar DSA. Cheguei a tentar otimizar algo para algumas entradas mas mesmo
# assim não há decrescimo de tempo de execucao significativo no Leetcode
# Uma sugestao de melhoria é usar um algoritmo stackead sem recursao, mas como já gastei bastante tempo
# nesse problema vou partir pra outro. 
# Acho que o ponte forte dessa resolução foi usar @cache como memoization/DP o que tornou a solução
# aplicavel no Leetcode. Treinar algoritmos recursivos também foi bom.

class Solution:

    def str_sizes(self, x, y, z) -> List[int]:
        self.memo = {}
        self.found = False
        return max(self.str_sizes_(1, x, y, z), self.str_sizes_(2, x, y, z), self.str_sizes_(3, x, y, z))
    @cache
    def str_sizes_(self, pick, x, y, z) -> List[int]:
        if self.found:
            return 0
        if x == 0 and y == 0 and z == 0:
            self.found = True
            return 0
        if (pick == 1 and x == 0) or (pick == 2 and y == 0) or (pick == 3 and z == 0):
            return 0
        if pick == 1:
            x -= 1
            pick = 2 
            return 2 + self.str_sizes_(pick, x, y, z)
        elif pick == 2:
            y -= 1
            aa = 2 + self.str_sizes_(1, x, y, z)
            ab = 2 + self.str_sizes_(3, x, y, z)
            return max (aa, ab)
        elif pick == 3:
            z -= 1
            aa = 2 + self.str_sizes_(1, x, y, z)
            ab = 2 + self.str_sizes_(3, x, y, z)
            return max (aa, ab)
        return 0
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            return 2*(x + y + z)
        if y == z and x < y:
            return 2*(2*x + z + 1)
        if y == z and x > y:
            return 2*(2*y + z + 1)
        return self.str_sizes(x, y, z)


print (Solution().longestString(2,2,2))
print (Solution().longestString(2,5,1))
print (Solution().longestString(3,2,2))
print (Solution().longestString(1,39,14)) #34

    # # 1 == 'AA'
    # # 2 == 'BB'
    # # 3 == 'AB
    # dict_ = {1: 2,  2: (1,3), 3: 1}

    # def get_next(self, last):
    #     # BB if 'AA' or 'AB' > 0
    #     
    #     if last is None:
    #         self.y -= 1
    #         return 'BB'

    #     if last == 'AA' and self.y > 0:
    #         self.y -= 1
    #         return 'BB'
    #     if last == 'AB' and self.x > 0:
    #         self.x -= 1
    #         return 'AA'
    #     if last == 'BB' and (self.x > 0 or self.z > 0):
    #         if self.x == 0:
    #             self.z -= 1
    #             return 'AB'
    #         if self.z == 0:
    #             self.x -= 1
    #             return 'AA'
    #         if self.x >= self.z:
    #             self.x -= 1
    #             return 'AA'
    #         self.z -= 1
    #         return 'AB'
    #     return ''
