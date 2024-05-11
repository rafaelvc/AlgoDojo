# https://www.youtube.com/watch?v=a1RaIqkdG0c&list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA&index=2
import timeit

sched = [(6,8), (6,12), (6,7), (7,8), (7,10), (8,9), (8,10), (9,12), (9,10), (10,11), (10,12), (11,12) ]

def max_celebs_time_inc(sched):           
    start, end = sched[0]
    for c in sched:
        start = min(c[0], start)
        end = max(c[1], end)
    sorted_start = iter(sched)
    sorted_end = iter(sorted(sched, key=lambda x: x[1]))
    time_arrival = next(sorted_start)[0]
    time_leaving = next(sorted_end)[1]
    celeb_count = 0
    max_celeb, celeb_time = 0, 0
    # density = [0] * (end - start)
    for i in range(start, end):
        if i == time_arrival:
            next_arrival = time_arrival
            while next_arrival == time_arrival:
                celeb_count += 1
                try:
                    next_arrival = next(sorted_start)[0]
                except StopIteration:
                    break
            time_arrival = next_arrival
        if i == time_leaving:
            next_leaving = time_leaving
            while next_leaving == time_leaving:
                celeb_count -= 1
                try:
                    next_leaving = next(sorted_end)[1]
                except StopIteration:
                    break
            time_leaving = next_leaving
        if max_celeb <= celeb_count:
            max_celeb = celeb_count
            celeb_time = i 
        # density[i-start] = celeb_count

    # print (density)

    # print ('{} celebs will be at the party from {} to {}'.format(max_celeb, celeb_time, celeb_time+1))

# def max_celebs_time_dict(sched):           
#     # arrivals_leaves = defaultdict(lambda : 0)
#     arrivals = {}
#     leaves = {}
#     t_start, t_end = sched[0]
#     for start,end in sched:
#         if start in arrivals:
#             arrivals[start] += 1
#         else:
#             arrivals[start] = 1
#         if end in leaves:
#             leaves[end] += 1
#         else:
#             leaves[end] = 1
#         t_start = min(t_start, start)
#         t_end = max(t_end, end)
#        
#     print (arrivals, leaves)
#     max_celeb, celeb_time = 0,0
#     celeb_count = 0
#     for t in range(t_start, t_end):
#         celeb_count += (arrivals.get(t,0) - leaves.get(t+1, 0))
#         if max_celeb < celeb_count:
#             max_celeb = celeb_count
#             celeb_time = t
#     print ('{} celebs will be at the party from {} to {}'.format(max_celeb, celeb_time, celeb_time+1))


def max_celebs_time_brute(sched_):

    start, end = sched_[0]
    for c in sched_:
        start = min(c[0], start)
        end = max(c[1], end)

    density = [0] * (end - start)
    for i in range(start, end):
       for c in sched_:
            if i >= c[0] and i < c[1]:
                density[i-start] += 1

    max_celeb = 0
    for ix, celebs in enumerate(density, start):
        if max_celeb < celebs:
            celeb_time = ix
            max_celeb = celebs
        
    # print ('{} celebs will be at the party from {} to {}'.format(max_celeb, celeb_time, celeb_time+1))

# start = timeit.default_timer()
# max_celebs_time_inc(sched)
# print (timeit.default_timer() - start)
 
# start = timeit.default_timer()
# max_celebs_time_brute(sched)
# print (timeit.default_timer() - start)


sched = [(6,8), (6,12), (6,7), (7,8), (7,10), (8,9), (8,10), (9,12), (9,10), (10,11), (10,12), (11,12) ]

def max_celebs_time_test(sched_):
    start, end = sched_[0]
    for c in sched_:
        start = min(c[0], start)
        end = max(c[1], end)
    density = [0] * (end - start)
    for arrival, leaving in sched_:
        density[arrival-start] += 1
 #       density[leaving-end] -= 1
    print (density)

        
max_celebs_time_test(sched)



# max_celebs_time_dict(sched)

#x = timeit.timeit ("max_celebs_time_brute(sched)", globals=globals() ) 
# print( timeit.timeit ('f1(a)', globals=globals() ) )
# max_celebs_time_brute(sched)


# start_d = {}
# end_d = {}
# for c in sched:
#     if c[0] in start_d:
#         start_d[c[0]] += 1
#     else:
#         start_d[c[0]] = 1
#     if c[1] in end_d:
#         end_d[c[1]] += 1
#     else:
#         end_d[c[1]] = 1