import numpy as np
#WORLD
world = np.zeros((10,10),tuple)
world[0] = 255
world[:,0] = 255
world[:,-1] = 255
world[-1] = 255

#SNAKE
head_position = (4,4)

blocks = [head_position]
current_position = np.array(head_position)
for i in range(1, 3):
    # Direction inverse of moving
    current_position = current_position - [0,1]
    blocks.append(tuple(current_position))

blocks1 = set(blocks)
print(blocks1,type(blocks1))
#FOOD POSITION
current_available_food_positions1 = set(zip(*np.where(world == 0))).difference(set(blocks))
print(current_available_food_positions1,type(current_available_food_positions1))
print(f'Вывод доступных сейчас позиций: '+str(len(current_available_food_positions1)))
# # current_available_food_positions = current_available_food_positions1.difference_update(blocks)

# #PRINT
# print(current_available_food_positions, type(current_available_food_positions))
# print(len(current_available_food_positions))
#current_available_food_positions= set(world - blocks)