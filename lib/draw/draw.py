# -*- coding: utf-8 -*-
from pylouvain import PyLouvain
import math
from matplotlib import pyplot as plt
import networkx as nx
import base64
import io

c2i_path = 'data/tbC2I.txt'
coordinate_path = 'data/coordinate.txt'

def plot(x):
    # 获取社区划分
    pyl = PyLouvain.from_file(c2i_path)
    node_dict = pyl.node_dict # key是253916-2的形式，value是编号的形式
    reverse_node_dict = dict(zip(node_dict.values(), node_dict.keys()))# key是编号的形式，value是253916-2的形式
    partition, q = pyl.apply_method()
    #print(partition)
    #print("模块度：",q)

    # 给各个社区节点分配颜色
    community_num = len(partition)
    #print('community_num:',community_num)
    color_board = ['red','green','blue','pink','orange','purple','scarlet']
    color = {}
    for index in range(community_num):
        #print("社区"+str(index+1)+":"+str(len(partition[index])))
        for node_id in partition[index]:
            color[node_id] = color_board[index] # color为一个字典，key为编号形式的节点，value为所属社区的颜色
    new_color_dict = sorted(color.items(), key=lambda d:d[0], reverse = False)# 将color字典按照key的大小排序，并返回一个list
    node_list = [reverse_node_dict[item[0]] for item in new_color_dict] #存储编号从小到大顺序对应的253916-2的形式的节点
    color_list = [item[1] for item in new_color_dict]#存储node_list中对应的节点颜色
    #print(node_list)
    #print(color_list)

    #构建networkx无向图
    G = nx.Graph()
    f = open(c2i_path, 'r')
    lines = f.readlines()
    f.close()
    edge_list = [] #存储边列表
    edge_width = [] #存储边列表对应的边粗细
    edge_color = [] #存储边列表对应的边颜色
    for line in lines:
        n = line.split()
        if not n:
            break
        G.add_edge(n[0],n[1],weight=float(n[2]))
        edge_list.append([n[0],n[1]])
        if color[node_dict[n[0]]] == color[node_dict[n[1]]]:#如果边的两端颜色相同
            edge_color.append(color[node_dict[n[0]]]) #则使用点的颜色作为边的颜色
        else:
            edge_color.append('c') #否则使用其他颜色
        if float(n[2]) > x: #阈值
            edge_width.append(float(n[2])/100.0)
        else:
            edge_width.append(0.0)

    # 可视化
    plt.figure(figsize=(15, 10), dpi=100)
    f = open(coordinate_path, encoding='utf-8')
    pos_dict = eval(f.read())
    f.close()
    _node = [int(item.split("-")[-1])%4 for item in node_list] #提取后缀模4取余
    node_0_index_list,node_1_index_list,node_2_index_list,node_3_index_list = [], [], [], []
    for index,item in enumerate(_node): #划分不同后缀余数的群，以便给每个群分配一个节点的形状 node_shape 防止都用圆形，导致同一经纬度的节点重叠在一起
        if item == 0:
            node_0_index_list.append(index)
        if item == 1:
            node_1_index_list.append(index)
        if item == 2:
            node_2_index_list.append(index)
        if item == 3:
            node_3_index_list.append(index)
    #print("node_list:",_node)
    nx.draw_networkx_nodes(G, pos_dict, nodelist=[node_list[i] for i in node_0_index_list],node_shape=7, node_color=[color_list[i] for i in node_0_index_list], node_size=50)
    nx.draw_networkx_nodes(G, pos_dict, nodelist=[node_list[i] for i in node_1_index_list],node_shape=4, node_color=[color_list[i] for i in node_1_index_list], node_size=50)
    nx.draw_networkx_nodes(G, pos_dict, nodelist=[node_list[i] for i in node_2_index_list],node_shape=5, node_color=[color_list[i] for i in node_2_index_list], node_size=50)
    nx.draw_networkx_nodes(G, pos_dict, nodelist=[node_list[i] for i in node_3_index_list],node_shape=6, node_color=[color_list[i] for i in node_3_index_list], node_size=50)
    nx.draw_networkx_edges(G, pos_dict, edgelist = edge_list, width = edge_width, alpha=1, edge_color=edge_color)
    return plt

def save_jpg(x, path):
    plt = plot(x)
    plt.savefig(path, format='jpg', bbox_inches='tight')

def get_base64(x):
    plt = plot(x)
    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes, format='jpg', bbox_inches='tight')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())
    return 'data:image/jpg;base64,' + pic_hash.decode('utf-8')
