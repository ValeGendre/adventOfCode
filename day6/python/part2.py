n=14

with open("day6/ressources/input.txt") as f:
    data_packet = f.readline()

def data_packet_to_iterable(n:int):
    l= []
    for i in range(n-1):
        l.append(data_packet[i:-(n-i-1)])
    l.append(data_packet[i+1:])
    return l

for idx, packet in enumerate(zip(*data_packet_to_iterable(n)), start=n):
    if len(set(packet))==n:
        print(idx)
        break