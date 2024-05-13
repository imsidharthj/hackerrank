k = int(input("members of each group: "))
room_number = [int(i) for i in input().split()]
'''
count_dict = {}
for room in room_number:
    if room in count_dict:
        count_dict[room] += 1
    else:
        count_dict[room] = 1

output = 0
for room, count in count_dict.items():
    if count < k:
        output = output + room
'''
actual_rooms = list(set(room_number)) * k
difference = sum(actual_rooms) - sum(room_number)
output = difference//(k-1)
print(output)