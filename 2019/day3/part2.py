# O(M + N)

f = open("input.txt", 'r')
w1 = list(f.readline().split(','))
w2 = list(f.readline().split(','))

ret = float('inf') 

# set of instructions (i, j) that w1 exists in
# mapped to the distance traveled (signal strength) to get there
c1 = {} 

for w, wire in enumerate([w1, w2]):
    position = [0, 0]
    dist = 0
    for instruction in wire:
        direction = instruction[0]
        magnitude = int(instruction.strip()[1:])
        index = 0 if direction in ['U', 'D'] else 1
        negative = -1 if direction in ['L', 'D'] else 1
        
        original = position[index]
        while position[index] != original + magnitude * negative:
            t = tuple(position)
            if w == 0:
                if t not in c1:
                    c1[t] = dist 
            else:
                if t in c1 and not (position[0] == 0 and position[1] == 0):
                    ret = min(ret, dist + c1[t])
                
            position[index] += negative
            dist += 1

print(ret)
