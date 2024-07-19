import autonomous_agent_lib as aal
import matplotlib.pyplot as plt

m_map = aal.create_map()
memory = None
start_coords = (2.5, 2.5)
end_coords = (97.5, 17.5)
m_agent = aal.agent(start_coords, end_coords, m_map, memory)

x_coords = []
y_coords = []
bx_coords = []
by_coords = []
for block in m_map["blocks"]:
    bx_coords.append(block[0])
    by_coords.append(block[1])
if memory != None:
    aal.go_memo(m_agent, memory)
else:
    while True:
        output = aal.move(m_map)
        x_coords.append(aal.get_coords()[0])
        y_coords.append(aal.get_coords()[1])
        if output == True:
            memory = aal.learn()
            #plt.scatter(x_coords, y_coords, color="green")
            plt.scatter(bx_coords, by_coords, color="red")
            plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
            plt.show()
            print(memory)
            break
        if output == "failed":
            plt.scatter(x_coords, y_coords, color="green")
            plt.scatter(bx_coords, by_coords, color="red")
            plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
            #plt.show()
            #break
            exit()
bx1_coords = []
by1_coords = []
x1_coords = []
y1_coords = []
m_agent = aal.agent(start_coords, end_coords, m_map, memory)
if memory != None:
    aal.go_memo(m_map)
    for block in aal.seen_set:
        bx1_coords.append(block[0])
        by1_coords.append(block[1])
    for coords in aal.memo_coords:
        x1_coords.append(coords[0])
        y1_coords.append(coords[1])
    plt.scatter(x1_coords, y1_coords, color="cyan")
    plt.scatter(bx1_coords, by1_coords, color="black")
    plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
    #plt.show()

aal.memo_coords = []
bx2_coords = []
by2_coords = []
x2_coords = []
y2_coords = []
m_agent = aal.agent(start_coords, end_coords, m_map, memory)
if memory != None:
    aal.go_memo(m_map)
    for block in aal.seen_set:
        bx2_coords.append(block[0])
        by2_coords.append(block[1])
    for coords in aal.memo_coords:
        x2_coords.append(coords[0])
        y2_coords.append(coords[1])
    plt.scatter(x2_coords, y2_coords, color="red")
    plt.scatter(bx2_coords, by2_coords, color="black")
    plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
    #plt.show()

aal.memo_coords = []
bx3_coords = []
by3_coords = []
x3_coords = []
y3_coords = []
m_agent = aal.agent(start_coords, end_coords, m_map, memory)
if memory != None:
    aal.go_memo(m_map)
    for block in aal.seen_set:
        bx3_coords.append(block[0])
        by3_coords.append(block[1])
    for coords in aal.memo_coords:
        x3_coords.append(coords[0])
        y3_coords.append(coords[1])
    plt.scatter(x3_coords, y3_coords, color="purple")
    plt.scatter(bx3_coords, by3_coords, color="black")
    plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
    #plt.show()

aal.memo_coords = []
bx4_coords = []
by4_coords = []
x4_coords = []
y4_coords = []
m_agent = aal.agent(start_coords, end_coords, m_map, memory)
if memory != None:
    aal.go_memo(m_map)
    for block in aal.seen_set:
        bx4_coords.append(block[0])
        by4_coords.append(block[1])
    for coords in aal.memo_coords:
        x4_coords.append(coords[0])
        y4_coords.append(coords[1])
    plt.scatter(x4_coords, y4_coords, color="yellow")
    plt.scatter(bx4_coords, by4_coords, color="black")
    plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
    plt.show()
number_to_color_dict ={0: "dimgray", 1: "green", 2: "blue", 3: "yellow", 4: "purple", 5: "orange", 6: "pink", 7: "black", 8: "lawngreen", 9: "gray", 10: "brown", 11: "cyan", 12: "magenta", 13: "lime", 14: "navy", 15: "teal", 16: "maroon", 17: "olive", 18: "violet", 19: "indigo"}
bx_coords = []
by_coords = []
for coords in m_map["blocks"]:
    bx_coords.append(coords[0])
    by_coords.append(coords[1])

agent_coords = []

for i in range(1):
        aal.memo_coords = []
        x_coords = []
        y_coords = []
        aal.target_location = None
        m_agent = aal.agent(start_coords, end_coords, m_map, memory)
        if memory != None:
            aal.go_memo(m_map)
            aal.target_location = m_map["target"]
            for coords in aal.memo_coords:
                x_coords.append(coords[0])
                y_coords.append(coords[1])
            plt.scatter(x_coords, y_coords, color=number_to_color_dict[i])
            plt.scatter(bx_coords, by_coords, color="red")
            plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
            #plt.show()
        else:
            while True:
                output = aal.move(m_map)
                x_coords.append(aal.get_coords()[0])
                y_coords.append(aal.get_coords()[1])
                if output == True:
                    memory = aal.learn()
                    plt.scatter(x_coords, y_coords, color="green")
                    plt.scatter(bx_coords, by_coords, color="red")
                    plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
                    #plt.show()
                    break
                if output == "failed":
                    plt.scatter(x_coords, y_coords, color="green")
                    plt.scatter(bx_coords, by_coords, color="red")
                    plt.scatter([m_map["target"][0] - 5, m_map["target"][0] - 5, m_map["target"][0] + 5, m_map["target"][0] + 5], [m_map["target"][1] - 5, m_map["target"][1] + 5, m_map["target"][1] - 5, m_map["target"][1] + 5], color="blue")
                    #plt.show()
                    #break
                    exit()
        agent_coords.append((x_coords, y_coords))
        break


