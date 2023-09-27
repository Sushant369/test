"""
Path planning - BFS, DFS & A star
"""

from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
import random


def plot_planner(grid_size, start_pose, goal_pose, obstacles, path, nodes_explored, animation=False):
    """
    Plot the grid map. Show start and goal post, path, obstacles, etc.
    :param grid_size: list(2) - grid size x & y
    :param start_pose: list(2) - x & y pose of start position
    :param goal_pose: list (2) - x & y pose of goal position
    :param obstacles: list (n, 2) - x & y pose of multiple obstacles
    :param path: list (n, 2) - x & y pose of each cell in the path
    :param nodes_explored: dict (n) - index of nodes explored
    :param animation: bool - to show animation in plot or not
    :return:
    """

    plt.show()

    fig, ax = plt.subplots()
    ax.set(
        xlim=(0, grid_size[0]), xticks=np.arange(1, grid_size[1]),
        ylim=(0, grid_size[1]), yticks=np.arange(1, grid_size[1])
    )
    plt.grid()

    # Plot obstacles
    for each_ob in obstacles:
        plt.fill_between([each_ob[1], each_ob[1]+1], each_ob[0], each_ob[0]+1, color='black')

    # Plot nodes explored
    for each_node in nodes_explored:
        x, y = index_to_grid(grid_size, each_node)
        plt.fill_between([y, y+1], x, x+1, color='yellow')
        if animation:
            plt.pause(1)

    for ind, each_pa in enumerate(path):
        plt.fill_between([each_pa[1], each_pa[1] + 1], each_pa[0], each_pa[0] + 1, color='blue')
        plt.text(each_pa[1] + 0.25, each_pa[0] + 0.25, ind, color='white')
        if animation:
            plt.pause(1)

    # Plot start and goal pose
    plt.fill_between([start_pose[1], start_pose[1] + 1], start_pose[0], start_pose[0] + 1, color='blue',
                     edgecolor='green', linewidth=5)
    plt.fill_between([goal_pose[1], goal_pose[1] + 1], goal_pose[0], goal_pose[0] + 1, color='blue',
                     edgecolor='red', linewidth=5)

    plt.show()


def compute_children(parent_xy, moves=8):
    """
    A list of possible moves for robot. Up, Down, Left, Right and diagonals.
    :param moves: number of ways robot can move
    :param parent_xy: list(2) - x y pose of current node
    :return: list(n, 2) - x y pose of different moves.
    """
    px, py = parent_xy

    child_xy = []

    if moves == 4:

        child_xy = [
            [px + 1, py],  # Up
            [px, py + 1],  # Right
            [px - 1, py],  # Bottom
            [px, py - 1],  # Left
        ]

    else:
        child_xy = [
            [px + 1, py],       # Up
            [px + 1, py + 1],   # Up-Right
            [px, py + 1],       # Right
            [px - 1, py + 1],   # Bottom-Right
            [px - 1, py],       # Bottom
            [px - 1, py - 1],   # Bottom-Left
            [px, py - 1],       # Left
            [px + 1, py - 1],   # Up-left
        ]

    return child_xy


def compute_child_node(parent_xy):
    """
    A list of possible moves for robot. Up, Down, Left, Right and diagonals.
    :param parent_xy: list(2) - x y pose of current node
    :return: list(n, 2) - x y pose of different moves.
    """
    px, py = parent_xy

    child_xy = [
        [px + 1, py],       # Up
        [px + 1, py + 1],   # Up-Right
        [px, py + 1],       # Right
        [px - 1, py + 1],   # Bottom-Right
        [px - 1, py],       # Bottom
        [px - 1, py - 1],   # Bottom-Left
        [px, py - 1],       # Left
        [px + 1, py - 1],   # Up-left
    ]

    return child_xy


def check_valid_move(node, grid, obs):
    """
    Check if move is valid - no obstacle and not outside grid
    :param node: list(2) - x y of current pose
    :param grid: list(2) - x y limit of grid size
    :param obs: list(n, 2) - x y pose of multiple obstacles
    :return: True/False to indicate valid move
    """
    valid_move = True
    if node in obs:
        valid_move = False
    elif node[0] < 0:
        valid_move = False
    elif node[0] >= grid[0]:
        valid_move = False
    elif node[1] < 0:
        valid_move = False
    elif node[1] >= grid[1]:
        valid_move = False

    return valid_move


def construct_path(grid, parents, goal):
    """
    Compute path in our searched map
    :param grid: list(2) - x y max limit of grid
    :param parents: dict(n) - list of parent index and child node in x y
    :param goal: list(2) - x y pose of goal
    :return: list(n, 2) - path from start to goal in x y
    """

    path = []
    cur_node = goal
    while cur_node:
        path.append(cur_node)
        parent_node = parents[grid_to_index(grid, cur_node)]
        cur_node = parent_node

    return path[::-1]


def construct_path_nodes(nodes_explored, goal_node):
    path = []
    cur_node = goal_node
    while cur_node.par_ind != -1:
        path.append(cur_node.xy)
        parent_ind = cur_node.par_ind
        cur_node = nodes_explored[parent_ind]

    path.append(cur_node.xy)

    return path[::-1]


def grid_to_index(grid, xy):
    """
    Convert grid x y pose to index value
    :param grid: list(2) - x y max limit of grid
    :param xy: list(2) - x y pose
    :return: index (int) - index of node in grid
    """
    return (xy[0] * grid[0]) + xy[1]


def index_to_grid(grid, ind):
    """
    convert index number in to grid position of x y
    :param grid: list(2) - x y max limit of grid
    :param ind: (int) index value of node in grid
    :return: node list (2) x y pose in grid
    """
    r = ind // grid[0]
    c = ind % grid[1]
    return [r, c]


def create_map(grid_x=10, grid_y=10):
    """
    Create a map with start, goal, obstacles for given grid size
    :param grid_x: (int) x limit of grid
    :param grid_y: (int) y limit of grid
    :return: start, goal, list_obs (n, 2) , grid (2)
    """

    random.seed(datetime.now().timestamp())

    total_cell = grid_x * grid_y
    grid = [grid_x, grid_y]
    start_ind = random.randint(0, total_cell)
    start = index_to_grid(grid, start_ind)

    goal_ind = random.randint(0, total_cell)
    attempt = 10
    while (goal_ind != start_ind) and attempt:
        goal_ind = random.randint(0, total_cell)
        attempt -= 1
    goal = index_to_grid(grid, goal_ind)

    num_obs = total_cell//20
    list_obs = []
    for _ in range(num_obs):
        obs_ind = random.randint(0, total_cell)
        if (obs_ind != start_ind) and (obs_ind != goal_ind):
            obs = index_to_grid(grid, obs_ind)
            list_obs.append(obs)

    return start, goal, list_obs, grid
