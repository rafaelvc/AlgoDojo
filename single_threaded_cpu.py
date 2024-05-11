#https://leetcode.com/problems/single-threaded-cpu/
from typing import List
import heapq as h
from collections import deque
# from queue import PriorityQueue
from cProfile import Profile
from pstats import SortKey, Stats
import time


class Solution:
    def getOrderForSorted(self, tasks: List[List[int]]) -> List[int]:
        time_counter = tasks[0][0]
        tasks_order = []
        cpu_time = 0
        tasks_queue = []
        unscheduled_tasks = len(tasks)
        ix_task = 0
        while unscheduled_tasks > 0:
            for ix, t in enumerate(tasks[ix_task:]): 
                if t[0] == time_counter:
                    h.heappush( tasks_queue, (t[1], ix + ix_task) )
                    unscheduled_tasks -= 1
                else: 
                    break
            ix_task = len(tasks) - unscheduled_tasks
            if cpu_time == 0 and unscheduled_tasks > 0: # CPU is ready for taking another task
                cpu_time, ix = h.heappop( tasks_queue )
                tasks_order.append(ix)
            if cpu_time > 0:
                cpu_time -= 1
            time_counter += 1
        tasks_order.extend([h.heappop(tasks_queue)[1] for i in range(0, len(tasks_queue))])
        return tasks_order 

    def getOrderForSorted2(self, tasks: List[List[int]]) -> List[int]:
        start = time.time()
        for ix, t in enumerate(tasks):
            t.append(ix)
        tasks = sorted(tasks, key=lambda x: x[0])
        print ("sortime: ", time.time() - start)
        tasks_order = []
        cpu_time = 0
        tasks_queue = []
        # tasks_queue = PriorityQueue()
        unscheduled_tasks = len(tasks)
        ix_task = 0
        time_counter = tasks[0][0]

        start1 = time.time()
        while unscheduled_tasks > 0:
            # if cpu_time == 0 and len(tasks_queue) == 0: # CPU is idle so advances in time to get next task
            #    time_counter = tasks[ix_task][0]
            # for ix, t in enumerate(tasks[ix_task:], ix_task):
            # if time.time() - start1 > 30:
            #    print ("Stop")
            for t in tasks[ix_task:]:
                 #if time_counter > t[0]:
                 #   print ("loop found")
                 #   print (time_counter,  tasks_queue.queue, cpu_time)
                 #   return 
                if t[0] == time_counter:
                    # h.heappush( tasks_queue, (t[1], ix) )
                    h.heappush( tasks_queue, (t[1], t[2]) )
                    # start = time.time()
                    # tasks_queue.put((t[1], t[2]))
                    # if time.time() - start > 1.0:
                    #    print ("timeout queue put")
                    #    print (time_counter,  tasks_queue.queue, cpu_time)
                    #    return
                    unscheduled_tasks -= 1
                else: 
                    break
            if unscheduled_tasks == 0:
                break
            ix_task = len(tasks) - unscheduled_tasks
            # if cpu_time == 0 and tasks_queue.qsize() > 0: # CPU is ready for taking another task
            #     # cpu_time, ix = h.heappop( tasks_queue )
            #     cpu_time, ix = tasks_queue.get()
            #     tasks_order.append(ix)
            next_task_at = tasks[ix_task][0]
            # if cpu_time == 0 and tasks_queue.qsize() > 0: # CPU is ready for taking another task
            if cpu_time == 0 and len(tasks_queue) > 0: # CPU is ready for taking another task
                cpu_time, ix = h.heappop( tasks_queue )
                # cpu_time, ix = tasks_queue.get()
                tasks_order.append(ix)
                if (time_counter + cpu_time) < next_task_at:
                # while tasks_queue.qsize() > 0:
                    while len(tasks_queue) > 0:
                        time_counter += cpu_time
                        # cpu_time, ix = tasks_queue.queue[0]
                        cpu_time, ix = tasks_queue[0]
                        if (time_counter + cpu_time) > next_task_at: 
                            cpu_time = 0
                            # time_counter += 1
                            # cpu_time -= (next_task_at - time_counter) 
                            time_counter = next_task_at
                            break
                        # cpu_time, ix = tasks_queue.get()
                        cpu_time, ix = h.heappop( tasks_queue )
                        tasks_order.append(ix)
            elif time_counter + cpu_time > next_task_at: # Current task is longer
                cpu_time -= (next_task_at - time_counter) 
                time_counter = next_task_at
            else:
                cpu_time = self._update_cpu_time (cpu_time)
                time_counter += 1
        tasks_order.extend([h.heappop(tasks_queue)[1] for i in range(0, len(tasks_queue))])
        # tasks_order.extend([tasks_queue.get()[1] for i in range(0, tasks_queue.qsize())])
        return tasks_order 

    # @profile
    def getOrderForSorted3(self, tasks: List[List[int]]) -> List[int]:
        for ix, t in enumerate(tasks):
            t.append(ix)
        tasks = sorted(tasks, key=lambda x: x[0])
        tasks_order = []
        cpu_time = 0
        tasks_queue = []
        unscheduled_tasks = len(tasks)
        ix_task = 0
        time_counter = tasks[0][0]
        while unscheduled_tasks > 0:
            # schedule tasks at time_counter
            ix = ix_task
            while ix < len(tasks) and tasks[ix][0] == time_counter:
                # h.heappush( tasks_queue, (tasks[ix][1], tasks[ix][2]) ) 
                h.heappush( tasks_queue, (tasks[ix][1], ix) ) 
                unscheduled_tasks -= 1
                ix += 1
            if unscheduled_tasks == 0:
                break
            ix_task = len(tasks) - unscheduled_tasks
            next_task_at = tasks[ix_task][0]
            if cpu_time == 0: # CPU free for taking new tasks
                while len(tasks_queue) > 0:
                    cpu_time, ix = h.heappop(tasks_queue)
                    tasks_order.append(ix)
                    cpu_free_at = time_counter + cpu_time
                    if cpu_free_at < next_task_at:
                        # time_counter += cpu_time
                        time_counter = time_counter + cpu_time if len(tasks_queue) > 0 else next_task_at
                        cpu_time = 0
                    else:
                        cpu_time -= (next_task_at - time_counter) 
                        time_counter = next_task_at 
                        break
                continue 
            cpu_free_at = time_counter + cpu_time
            if cpu_free_at < next_task_at:
                time_counter += cpu_time
                cpu_time = 0
            else:
                cpu_time -= (next_task_at - time_counter) 
                time_counter = next_task_at 
        tasks_order.extend([h.heappop(tasks_queue)[1] for i in range(0, len(tasks_queue))])
        return tasks_order 

    def _cpu_time_dec(self, vl):
        self.cpu_time -= vl
        if self.cpu_time < 0: 
            self.cpu_time = 0
            return True
        return False

    def run_tasks_up_to(self, tasks_queue, curtime, upto, tasks_order, cputime=0):
        if cputime == 0 and len(tasks_queue) > 0:
            while curtime + cpu_time < upto:
                cpu_time, ix = h.heappop( tasks_queue )
                if curtime + cpu_time > upto:
                    h.heappush( tasks_queue, (cpu_time, ix) )
                    return 0, curtime
                tasks_order.append(ix)
                curtime += cpu_time
            return cpu_time, curtime
        return 0,0


    def getOrder0(self, tasks: List[List[int]]) -> List[int]:
        # add the index once task list is unsorted
        for ix, t in enumerate(tasks):
            t.append(ix)
        time_counter = 1
        tasks_order = []
        cpu_time = 0
        tasks_queue = []
        unscheduled_tasks = len(tasks)
        while unscheduled_tasks > 0:
            tasks_scheduled = 0
            for i in range(0, len(tasks)):
                ix = i - tasks_scheduled
                if tasks[ix][0] == time_counter:
                    h.heappush( tasks_queue, (tasks[ix][1], tasks[ix][2]) )
                    unscheduled_tasks -= 1
                    del tasks[ix]
            if cpu_time == 0 and len(tasks_queue) > 0: # CPU is ready for taking another task
                cpu_time, ix = h.heappop( tasks_queue )
                tasks_order.append(ix)
            if cpu_time > 0:
                cpu_time -= 1
            time_counter += 1
        tasks_order.extend([h.heappop(tasks_queue)[1] for i in range(0, len(tasks_queue))])
        return tasks_order 

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # add the index once task list is unsorted
        for ix, t in enumerate(tasks):
            t.append(ix)
        time_counter = min(tasks)[1]
        tasks_order = []
        cpu_time = 0
        tasks_queue = []
        unscheduled_tasks = len(tasks)
        while unscheduled_tasks > 0:
            tasks_scheduled = 0
            for i in range(0, len(tasks)):
                ix = i - tasks_scheduled
                if tasks[ix][0] == time_counter:
                    h.heappush( tasks_queue, (tasks[ix][1], tasks[ix][2]) )
                    unscheduled_tasks -= 1
                    del tasks[ix]
            if cpu_time == 0 and len(tasks_queue) > 0: # CPU is ready for taking another task
                cpu_time, ix = h.heappop( tasks_queue )
                tasks_order.append(ix)
            if cpu_time > 0:
                cpu_time -= 1
            time_counter += 1
        tasks_order.extend([h.heappop(tasks_queue)[1] for i in range(0, len(tasks_queue))])
        return tasks_order 

# Como foi o processo de elaboração do algoritmo:
# A ideia inicial sempre foi de usar um contador de tempo, atribuir o tempo de tarefa ao contador do cpu, decrementar o
# o contador do cpu a cada iteracao e usar uma priority queue para fazer o scheduling das tarefas priorizando as com menor tempo de execucao
# Durante a implementação 
# 1 - A primeira intuição estava certa porém eu tentei transformar as tasks em deque para no laço principal ir fazendo o pop nela 
#     e testando se o tamanhos das tasks > 0, me perdi ai.
# 2 - Recomecei o algoritmo do zero e vi que a ideia inicial estava certa, abandonei a ideia do dequeue
#     e usei o contador unscheduled tasks 
# 3 - O ix_tasks estava sendo incrementado a cada push de task e ai gerava erro e vi que o ix_tasks deve sempre ficar no mesmo 
#     valor na iteração corrente (ix_tasks precisava ser usado mas nao estava claro pois ele desconta as tarefas ja processas na task list)
# 4 - Outro problema estava relacionado a eu achar que a iteração na heapq respeita a ordem de prioridade, mas nao a iteração respeita
#      a ordem de inclusao, a ordem de prioridade e respeita apenas quando usa-se a funcao heappo 
# 5 - Esta gerando um index out of range..., preciso comecar o contador de tempo direto na primeira tarefa e preciso ordenar a lista de tasks a principio
# 6 - O algoritimo não está funcionando para o segundo test case da submissão, o problema é que se reordenar as tasklists conforme o tempo de inclusão
#      os indexes originais de cada task são perdidos
# 7 - Recriamos o algoritmo para adicionar o indice da task na list, nao estamos mais utilizando o ix_tasks, o algoritmo passou ate o test case 23 de 39 no leetcode.
     # Dois problemas: ficar reescaneando a lista de tasks a cada iteração, e esperar o time_counter atingir o mesmo tempo da proxima task
       # Problema 1 - estou fazendo um del a cada elemento da lista que é agendado para processamento na heapq
# 8 - voltei no algoritmo anterior iten 6 dessa lista, adicionei o task index e fiz a ordenação ai funcionou e foi até o test case 27, 
      # continuamos com o problema 2, o time counter fica girando até igualar com o tempo da primeira tarefa da lista de tarefas agendadas.

# 9 - Consegui resolver o problema 1 e 2, o cpu_timer e o time_counter sempre são atualizados de forma que o o laço não fica girando até a 
      # tarefa ser finalizada pelo CPU, pois o objetivo é apenas ordenar as tasks então se não tem tarefa para entrar no tempo em que outra 
      # está em execução a tarefa atual é finalizada cpu_timer = 0 e enquanto a proxima tarefa está longe de (next_task_at) 
      # de entrar na fila vamos esvaziando a fila (heapqpop) de tarefas agendas e vamos processando. 

# 10 - Ainda tem problema de time limit, fui investigar usando um line profiling (pip install line_profiler) e encontrei um gargalo na linha
       # (for t in tasks[ix_task:]) para 100k tasks, então troquei a laço por um while, aqui na verdade é a lógica porque estão fatiando a
       # a lista mas na maioria das vezes é apenas os primeiros itens do slice, então uma lógica com while fica melhor.
    
# 11 - Achei um ultimo problema de logica debugando (time_counter = time_counter + cpu_time if len(tasks_queue) > 0 else next_task_at) ou seja
      # o time counter deve ser igual a next_task caso a fila de tarefas agendadas esteja zerada. 

# 12 - PriorityQueue não melhor o desempenho. Uma pequena piora porque multithreading (thread safe) é considerado no processamento.


# print (Solution().getOrder([[1,2], [2,5], [2,4], [3,2]]))
# print (Solution().getOrder([[1,5], [1,2],[1,1]]))
# print (Solution().getOrder([[1,2],[2,4],[3,2],[4,1]]))
# print (Solution().getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))

# print (Solution().getOrderForSorted3([[1,2], [2,5], [2,4], [3,2]]))
# print (Solution().getOrderForSorted3([[1,5], [1,2],[1,1]]))
# print (Solution().getOrderForSorted3([[1,2],[2,4],[3,2],[4,1]]))
# print (Solution().getOrderForSorted3([[7,10],[7,12],[7,5],[7,4],[7,2]]))
# [6,1,2,9,4,10,0,11,5,13,3,8,12,7]

# print (Solution().getOrderForSorted2(nums))
# with Profile() as profile:
#    print(f"{Solution().getOrderForSorted3(nums)}")
#    (
#      Stats(profile)
#      .strip_dirs()
#      .sort_stats(SortKey.CALLS)
#      .print_stats()
#    )

# print (Solution().getOrderForSorted3([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
# print (Solution().getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))

# [15,14,13,1,6,3,5,12,8,11,9,4,10,7,0,2]
print (Solution().getOrderForSorted3([[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]))

# nums = [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]] # check this time exceed
# print (Solution().getOrderForSorted3(nums))

