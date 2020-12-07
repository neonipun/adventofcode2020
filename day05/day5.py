import math
locations = dict()
seat_ids = set()

def decode(key):
    if key in locations:
        return locations[key]
    else:
        ll = 0 
        ul = 127 if key[0] in {'F', 'B'} else 7
        for k in key:
            if k == 'F' or k == 'L':
                ul = math.floor((ll + ul)/2)
            else:
                ll = math.ceil((ll + ul)/2)
        locations[key] = ll 
    
    return locations[key]

with open('input', 'r') as f:
    highest_seat_id = 0 
    for boarding_pass in f.readlines():
        boarding_pass = boarding_pass.strip()
        row_key, column_key = boarding_pass[:7], boarding_pass[7:]

        row = decode(row_key)
        column = decode(column_key)
        
        seat_id = row * 8 + column
        seat_ids.add(seat_id)
        highest_seat_id = seat_id if seat_id > highest_seat_id else highest_seat_id

print(f'highest_seat_id = {highest_seat_id}')

print(f'BBFFBBFRLL - row = {decode("BBFFBBF")} column = {decode("RLL")} id = {decode("BBFFBBF") * 8 + decode("RLL")}')

for i in range(highest_seat_id):
    if i not in seat_ids and i+1 in seat_ids and i-1 in seat_ids:
        print(f'My seat_id = {i}')
        break