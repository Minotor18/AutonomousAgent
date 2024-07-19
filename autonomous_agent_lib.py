import math
import random

memory = None
direction = None
target_location = None
agent_coords = None
seen_set = []
memo_coords = []

def go_memo(env):
    global agent_coords
    global direction
    global memory
    global target_location
    if memory != None:
        if math.sqrt((memory[1][0] - agent_coords[0])**2 + (memory[1][1] - agent_coords[1])**2) < 2.5:

            if math.sqrt((target_location[0] - agent_coords[0])**2 + (target_location[1] - agent_coords[1])**2) < 2.5:

                return True
            else:

                while True:
                    move(env)
        else:
            if agent_coords[0] < memory[1][0]:
                if agent_coords[1] > memory[1][1]:
                    direction = 2*math.pi + math.atan2(memory[1][1] - agent_coords[1], memory[1][0] - agent_coords[0])
                else:
                    direction = math.atan2(memory[1][1] - agent_coords[1], memory[1][0] - agent_coords[0])
            else:
                if agent_coords[1] > memory[1][1]:
                    direction = 3*math.pi - math.atan2(memory[1][1] - agent_coords[1], memory[1][0] - agent_coords[0])
                else:
                    direction = math.pi - math.atan2(memory[1][1] - agent_coords[1], memory[1][0] - agent_coords[0])
            direction = math.atan2(memory[1][1] - agent_coords[1], memory[1][0] - agent_coords[0])
            while math.sqrt((memory[1][0] - agent_coords[0])**2 + (memory[1][1] - agent_coords[1])**2) > 2.5:   
                move(env)
                memo_coords.append(agent_coords)

def move(env):
    global agent_coords
    global direction
    global target_location
    lidar_blocks, lidar_target = lidar(env)
    if len(lidar_blocks) > 0:
        for block in lidar_blocks:
            if math.sqrt((block[0] - agent_coords[0])**2 + (block[1] - agent_coords[1])**2) < 2.5:
                print(block)
                print(agent_coords)
                print("FAILED")
                return "failed"
    if lidar_target[1]:
        target_location = lidar_target[0]
    if target_location == None:
        wander(env)
    else:
        if math.sqrt((target_location[0] - agent_coords[0])**2 + (target_location[1] - agent_coords[1])**2) < 2.5:
            return True
        else:
            if agent_coords[0] < target_location[0]:
                if agent_coords[1] > target_location[1]:
                    direction = 2*math.pi + math.atan2(target_location[1] - agent_coords[1], target_location[0] - agent_coords[0])
                else:
                    direction = math.atan2(target_location[1] - agent_coords[1], target_location[0] - agent_coords[0])
            else:
                if agent_coords[1] > target_location[1]:
                    direction = 3*math.pi - math.atan2(target_location[1] - agent_coords[1], target_location[0] - agent_coords[0])
                else:
                    direction = math.pi - math.atan2(target_location[1] - agent_coords[1], target_location[0] - agent_coords[0])
            direction = math.atan2(target_location[1] - agent_coords[1], target_location[0] - agent_coords[0])
        wander(env)

def wander(env):
    global agent_coords
    global direction
    global memory
    lidar_blocks, _ = lidar(env)
    if len(lidar_blocks) > 0:
        for block in lidar_blocks:
            if math.sqrt((block[0] - agent_coords[0])**2 + (block[1] - agent_coords[1])**2) < 5:
                tmp_direction = create_tmp_direction(block, True)
                agent_coords = (agent_coords[0] + math.cos(tmp_direction), agent_coords[1] + math.sin(tmp_direction))
                if agent_coords[0] < 2.5 or agent_coords[0] > 97.5 or agent_coords[1] < 2.5 or agent_coords[1] > 197.5:
                    agent_coords = (agent_coords[0] - math.cos(tmp_direction), agent_coords[1] - math.sin(tmp_direction))
                    tmp_direction = None

                while tmp_direction == None:
                    tmp_direction = create_tmp_direction(block)
                    agent_coords = (agent_coords[0] + math.cos(tmp_direction), agent_coords[1] + math.sin(tmp_direction))
                    if agent_coords[0] < 2.5 or agent_coords[0] > 97.5 or agent_coords[1] < 2.5 or agent_coords[1] > 197.5 :
                        agent_coords = (agent_coords[0] - math.cos(tmp_direction), agent_coords[1] - math.sin(tmp_direction))
                        tmp_direction = None
                agent_coords = (agent_coords[0] - math.cos(tmp_direction), agent_coords[1] - math.sin(tmp_direction))
                direction = tmp_direction
    if direction != None:
        agent_coords = (agent_coords[0] + math.cos(direction), agent_coords[1] + math.sin(direction))
        if agent_coords[0] < 2.5 or agent_coords[0] > 97.5 or agent_coords[1] < 2.5 or agent_coords[1] > 197.5 :
                agent_coords = (agent_coords[0] - math.cos(direction), agent_coords[1] - math.sin(direction))
                direction = None
    while direction == None:
        direction = random.uniform(0, 2*math.pi)
        agent_coords = (agent_coords[0] + math.cos(direction), agent_coords[1] + math.sin(direction))
        if agent_coords[0] < 2.5 or agent_coords[0] > 97.5 or agent_coords[1] < 2.5 or agent_coords[1] > 197.5 :
            agent_coords = (agent_coords[0] - math.cos(direction), agent_coords[1] - math.sin(direction))
            direction = None
    
def create_tmp_direction(block, do_i_do_that = False):
    global agent_coords
    if agent_coords[0] < block[0]:
        if agent_coords[1] > block[1]:
            tmp_direction = 2*math.pi + math.atan2(block[1] - agent_coords[1], block[0] - agent_coords[0])
        else:
            tmp_direction = math.atan2(block[1] - agent_coords[1], block[0] - agent_coords[0])
    else:
        if agent_coords[1] > block[1]:
            tmp_direction = 3*math.pi - math.atan2(block[1] - agent_coords[1], block[0] - agent_coords[0])
        else:
            tmp_direction = math.pi - math.atan2(block[1] - agent_coords[1], block[0] - agent_coords[0])
    tmp_direction = math.atan2(block[1] - agent_coords[1], block[0] - agent_coords[0])
    if do_i_do_that:
        agent_coords = (agent_coords[0] + math.cos(tmp_direction + math.pi), agent_coords[1] + math.sin(tmp_direction + math.pi))
        if agent_coords[0] < 2.5 or agent_coords[0] > 97.5 or agent_coords[1] < 2.5 or agent_coords[1] > 197.5 :
            agent_coords = (agent_coords[0] - math.cos(tmp_direction - math.pi), agent_coords[1] - math.sin(tmp_direction - math.pi))
    rand = random.randint(0,1)
    if rand == 0:
        tmp_direction += math.pi/2
    else:
        tmp_direction -= math.pi/2
    if tmp_direction > 2*math.pi:
        tmp_direction -= 2*math.pi
    return tmp_direction

def lidar(env):
    global agent_coords
    blocks_seen = []
    target = ((0,0), False)
    for i in env["blocks"]:
        if math.sqrt((i[0] - agent_coords[0])**2 + (i[1] - agent_coords[1])**2) <= 15:
            blocks_seen.append(i)
    if math.sqrt((env["target"][0] - agent_coords[0])**2 + (env["target"][1] - agent_coords[1])**2) <= 15:
        target = (env["target"], True)
    for block in blocks_seen:
        if block != None and block not in seen_set:
            seen_set.append(block)
    return blocks_seen, target

def get_coords():
    global agent_coords
    return agent_coords

def agent(start_coords, end_coords, env, memory_in):
    global memory
    global agent_coords
    agent_coords = (random.uniform(start_coords[0], end_coords[0]), random.uniform(start_coords[1], end_coords[1]))
    while is_blocked(env, agent_coords):
        agent_coords = (random.uniform(start_coords[0], end_coords[0]), random.uniform(start_coords[1], end_coords[1]))
    memory = memory_in
    return agent_coords

def is_blocked(env, coords):
    for i in env["blocks"]:
        if math.sqrt((i[0] - coords[0])**2 + (i[1] - coords[1])**2) < 3.5:
            return True
    if math.sqrt((env["target"][0] - coords[0])**2 + (env["target"][1] - coords[1])**2) < 7.5:
        return True
    return False

def overlap(blocks, new_block, threshold):
    for i in range(len(blocks)):
        if math.sqrt((blocks[i][0] - new_block[0])**2 + (blocks[i][1] - new_block[1])**2) < threshold:
            return True
    return False

def overlap_all(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks)): 
            if i != j and math.sqrt((blocks[i][0] - blocks[j][0])**2 + (blocks[i][1] - blocks[j][1])**2) < 2:
                return True
    return False

def learn():
    global memory
    global seen_set
    global target_location
    blocks = list(seen_set)
    target = target_location
    if memory == None:
        average_blocks = blocks[0]
        for i in range(1, len(blocks)):
            average_blocks = (average_blocks[0] + blocks[i][0], average_blocks[1] + blocks[i][1])
        average_blocks = (average_blocks[0] / len(blocks), average_blocks[1] / len(blocks))
        memory = (average_blocks, target)
    else:
        average_blocks = blocks[0]
        for i in range(1, len(blocks)):
            average_blocks = (average_blocks[0] + blocks[i][0], average_blocks[1] + blocks[i][1])
        memory = (((memory[0][0]*2/3 + average_blocks[0]/3*len(blocks)), memory[0][1]*2/3 + average_blocks[1]/3*len(blocks)), (memory[1][0]*2/3 + target[0]/3, memory[1][1]*2/3 + target[1]/3))
    return memory

def create_map():
    dunya_genislik = 100
    dunya_yukseklik = 200

    hedef_konum_x = random.uniform(5, 95)
    hedef_konum_y = random.uniform(185, 195)
    hedef = (hedef_konum_x, hedef_konum_y)
    engel_sayisi = 80

    engeller = []

    while len(engeller) < engel_sayisi:
        engel_baslangic_x = random.uniform(1, 99)
        engel_baslangic_y = random.uniform(21, 179)

        engel = (engel_baslangic_x, engel_baslangic_y)

        if not overlap(engeller, engel, 2):
            engeller.append(engel)

    while overlap(engeller, hedef, 6):
        hedef_konum_x = random.uniform(5, 95)
        hedef_konum_y = random.uniform(185, 195)
        hedef = (hedef_konum_x, hedef_konum_y)

    benim_haritam = {
        "length": dunya_genislik,
        "height": dunya_yukseklik,
        "target": hedef,
        "blocks": engeller
    }

    return benim_haritam