"""
В файле furry_road.txt указываются плитки дороги шириной 5 клеток
Напишите автопилот, который едет сверху вниз и на каждый ряд выбирает, куда ехать: left, right, stay
При наличии нескольких вариантов машина держится правой стороны (на картинке она слева)
Программа должна считывать файл построчно
"""

# Load road
filename = '05_furry_road_three.txt'
with open(filename, 'r', encoding='utf-8') as file:
    data = file.readlines()
    road = [line.strip('\n') for line in data]
    road_lidar = [line.replace(' ','') for line in road]

# Lidar
car_pos = 2

for line in road_lidar:
    # if next lane is free go straight
    if line[car_pos] == '░':
        print('Stay')
    else:
        # if not most right lane
        # check right, than left lane
        if car_pos != 0:
            if line[car_pos-1] == '░':
                print('Right')
                car_pos -= 1
            elif line[car_pos+1] == '░':
                print('Left')
                car_pos += 1
            else:
                print('Stop!')
                break
        # if on most right lane
        # check only left lane
        else:
            if line[car_pos + 1] == '░':
                print('Left')
                car_pos += 1
            else:
                print('Stop!')
                break
