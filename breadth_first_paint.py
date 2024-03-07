# pag. 361 Crack code interview questions.  The author suggests to implement 
# same algorithm using depth first, which is similar used  in graph search

# Search in sets in python should be O(1) 

def paint_fill_depth_first(screen, r, c, n):
    queue = []
    queue.append((r,c))
    visited = set()
    o = screen[r][c]
    while len(queue) > 0:
        r,c = queue.pop()
        if screen[r][c] == o:
            screen[r][c] = n
        visited.add((r,c))
        if r-1 >= 0 and screen[r-1][c] == o and (r-1,c) not in visited:
            queue.append((r-1,c))
        if r+1 < len(screen) and screen[r+1][c] == o and (r+1,c) not in visited:
            queue.append((r+1,c))
        if c-1 >= 0 and screen[r][c-1] == o and (r,c-1) not in visited:
            queue.append((r,c-1))
        if c+1 < len(screen[0]) and screen[r][c+1] == o and (r,c+1) not in visited:
            queue.append((r,c+1))

screen = [ [1,1,1,1],
           [1,2,2,2],
           [2,2,2,1],]
# print (len(screen))
# paint_fill_depth_first(screen, 0,0, 3, 1)
# paint_fill_depth_first(screen, 0,0, 0)
# print (screen)
paint_fill_depth_first(screen, 2,3, 0)
print (screen)

screen = [ [1,1,1,1,1],
           [1,2,2,2,1],
           [1,2,2,2,1],
           [1,1,1,1,1],]

paint_fill_depth_first(screen, 1,1, 0)
print (screen)

#


# print (screen[0][0])
# print (screen[1][0])
# print (len(screen[0]))