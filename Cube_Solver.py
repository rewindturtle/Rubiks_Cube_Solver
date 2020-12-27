import numpy as np
import copy


W = 0 # White
B = 1 # Blue
R = 2 # Red
G = 3 # Green
O = 4 # Orange
Y = 5 # Yellow

# Edges and Corner Pieces
WGO = 0
WG = 1
WGR = 2
WO = 3
WR = 5
WBO = 6
WB = 7
WBR = 8
GO = 9
GR = 11
BO = 15
BR = 17
YGO = 18
YG = 19
YGR = 20
YO = 21
YR = 23
YBO = 24
YB = 25
YBR = 26


def simplify_move_list(move_list):
    not_simple = True
    while not_simple:
        if len(move_list) > 1:
            not_simple = False
            new_move_list = []
            not_skip = True
            for i in range(len(move_list) - 1):
                if not_skip:
                    if move_list[i] == 'U1':
                        if move_list[i + 1] == 'U1':
                            new_move_list.append('U2')
                            not_skip = False
                        elif move_list[i + 1] == 'U2':
                            new_move_list.append('U3')
                            not_skip = False
                        elif move_list[i + 1] != 'U3':
                            new_move_list.append('U1')
                        else:
                            not_skip = False
                    elif move_list[i] == 'U2':
                        if move_list[i + 1] == 'U1':
                            new_move_list.append('U3')
                            not_skip = False
                        elif move_list[i + 1] == 'U3':
                            new_move_list.append('U1')
                            not_skip = False
                        elif move_list[i + 1] != 'U2':
                            new_move_list.append('U2')
                        else:
                            not_skip = False
                    elif move_list[i] == 'U3':
                        if move_list[i + 1] == 'U2':
                            new_move_list.append('U1')
                            not_skip = False
                        elif move_list[i + 1] == 'U3':
                            new_move_list.append('U2')
                            not_skip = False
                        elif move_list[i + 1] != 'U1':
                            new_move_list.append('U3')
                        else:
                            not_skip = False
                    elif move_list[i] == 'F1':
                        if move_list[i + 1] == 'F1':
                            new_move_list.append('F2')
                            not_skip = False
                        elif move_list[i + 1] == 'F2':
                            new_move_list.append('F3')
                            not_skip = False
                        elif move_list[i + 1] != 'F3':
                            new_move_list.append('F1')
                        else:
                            not_skip = False
                    elif move_list[i] == 'F2':
                        if move_list[i + 1] == 'F1':
                            new_move_list.append('F3')
                            not_skip = False
                        elif move_list[i + 1] == 'F3':
                            new_move_list.append('F1')
                            not_skip = False
                        elif move_list[i + 1] != 'F2':
                            new_move_list.append('F2')
                        else:
                            not_skip = False
                    elif move_list[i] == 'F3':
                        if move_list[i + 1] == 'F2':
                            new_move_list.append('F1')
                            not_skip = False
                        elif move_list[i + 1] == 'F3':
                            new_move_list.append('F2')
                            not_skip = False
                        elif move_list[i + 1] != 'F1':
                            new_move_list.append('F3')
                        else:
                            not_skip = False
                    elif move_list[i] == 'R1':
                        if move_list[i + 1] == 'R1':
                            new_move_list.append('R2')
                            not_skip = False
                        elif move_list[i + 1] == 'R2':
                            new_move_list.append('R3')
                            not_skip = False
                        elif move_list[i + 1] != 'R3':
                            new_move_list.append('R1')
                        else:
                            not_skip = False
                    elif move_list[i] == 'R2':
                        if move_list[i + 1] == 'R1':
                            new_move_list.append('R3')
                            not_skip = False
                        elif move_list[i + 1] == 'R3':
                            new_move_list.append('R1')
                            not_skip = False
                        elif move_list[i + 1] != 'R2':
                            new_move_list.append('R2')
                        else:
                            not_skip = False
                    elif move_list[i] == 'R3':
                        if move_list[i + 1] == 'R2':
                            new_move_list.append('R1')
                            not_skip = False
                        elif move_list[i + 1] == 'R3':
                            new_move_list.append('R2')
                            not_skip = False
                        elif move_list[i + 1] != 'R1':
                            new_move_list.append('R3')
                        else:
                            not_skip = False
                    elif move_list[i] == 'D1':
                        if move_list[i + 1] == 'D1':
                            new_move_list.append('D2')
                            not_skip = False
                        elif move_list[i + 1] == 'D2':
                            new_move_list.append('D3')
                            not_skip = False
                        elif move_list[i + 1] != 'D3':
                            new_move_list.append('D1')
                        else:
                            not_skip = False
                    elif move_list[i] == 'D2':
                        if move_list[i + 1] == 'D1':
                            new_move_list.append('D3')
                            not_skip = False
                        elif move_list[i + 1] == 'D3':
                            new_move_list.append('D1')
                            not_skip = False
                        elif move_list[i + 1] != 'D2':
                            new_move_list.append('D2')
                        else:
                            not_skip = False
                    elif move_list[i] == 'D3':
                        if move_list[i + 1] == 'D2':
                            new_move_list.append('D1')
                            not_skip = False
                        elif move_list[i + 1] == 'D3':
                            new_move_list.append('D2')
                            not_skip = False
                        elif move_list[i + 1] != 'D1':
                            new_move_list.append('D3')
                        else:
                            not_skip = False
                    elif move_list[i] == 'B1':
                        if move_list[i + 1] == 'B1':
                            new_move_list.append('B2')
                            not_skip = False
                        elif move_list[i + 1] == 'B2':
                            new_move_list.append('B3')
                            not_skip = False
                        elif move_list[i + 1] != 'B3':
                            new_move_list.append('B1')
                        else:
                            not_skip = False
                    elif move_list[i] == 'B2':
                        if move_list[i + 1] == 'B1':
                            new_move_list.append('B3')
                            not_skip = False
                        elif move_list[i + 1] == 'B3':
                            new_move_list.append('B1')
                            not_skip = False
                        elif move_list[i + 1] != 'B2':
                            new_move_list.append('B2')
                        else:
                            not_skip = False
                    elif move_list[i] == 'B3':
                        if move_list[i + 1] == 'B2':
                            new_move_list.append('B1')
                            not_skip = False
                        elif move_list[i + 1] == 'B3':
                            new_move_list.append('B2')
                            not_skip = False
                        elif move_list[i + 1] != 'B1':
                            new_move_list.append('B3')
                        else:
                            not_skip = False
                    elif move_list[i] == 'L1':
                        if move_list[i + 1] == 'L1':
                            new_move_list.append('L2')
                            not_skip = False
                        elif move_list[i + 1] == 'L2':
                            new_move_list.append('L3')
                            not_skip = False
                        elif move_list[i + 1] != 'L3':
                            new_move_list.append('L1')
                        else:
                            not_skip = False
                    elif move_list[i] == 'L2':
                        if move_list[i + 1] == 'L1':
                            new_move_list.append('L3')
                            not_skip = False
                        elif move_list[i + 1] == 'L3':
                            new_move_list.append('L1')
                            not_skip = False
                        elif move_list[i + 1] != 'L2':
                            new_move_list.append('L2')
                        else:
                            not_skip = False
                    elif move_list[i] == 'L3':
                        if move_list[i + 1] == 'L2':
                            new_move_list.append('L1')
                            not_skip = False
                        elif move_list[i + 1] == 'L3':
                            new_move_list.append('L2')
                            not_skip = False
                        elif move_list[i + 1] != 'L1':
                            new_move_list.append('L3')
                        else:
                            not_skip = False
                else:
                    not_skip = True
                    not_simple = True

            if not_skip:
                new_move_list.append(move_list[i + 1])
            else:
                not_simple = True
            move_list = new_move_list
        else:
            new_move_list = move_list
            break

    return new_move_list


def swap_moves(move_list, code):
    new_move_list = []

    if code == W:
        new_move_list = move_list
    elif code == B:
        for move in move_list:
            if move == 'D1':
                new_move_list.append('F1')
            elif move == 'D2':
                new_move_list.append('F2')
            elif move == 'D3':
                new_move_list.append('F3')
            elif move == 'F1':
                new_move_list.append('U1')
            elif move == 'F2':
                new_move_list.append('U2')
            elif move == 'F3':
                new_move_list.append('U3')
            elif move == 'U1':
                new_move_list.append('B1')
            elif move == 'U2':
                new_move_list.append('B2')
            elif move == 'U3':
                new_move_list.append('B3')
            elif move == 'B1':
                new_move_list.append('D1')
            elif move == 'B2':
                new_move_list.append('D2')
            elif move == 'B3':
                new_move_list.append('D3')
            else:
                new_move_list.append(move)
    elif code == R:
        for move in move_list:
            if move == 'D1':
                new_move_list.append('R1')
            elif move == 'D2':
                new_move_list.append('R2')
            elif move == 'D3':
                new_move_list.append('R3')
            elif move == 'R1':
                new_move_list.append('U1')
            elif move == 'R2':
                new_move_list.append('U2')
            elif move == 'R3':
                new_move_list.append('U3')
            elif move == 'U1':
                new_move_list.append('L1')
            elif move == 'U2':
                new_move_list.append('L2')
            elif move == 'U3':
                new_move_list.append('L3')
            elif move == 'L1':
                new_move_list.append('D1')
            elif move == 'L2':
                new_move_list.append('D2')
            elif move == 'L3':
                new_move_list.append('D3')
            else:
                new_move_list.append(move)
    elif code == G:
        for move in move_list:
            if move == 'D1':
                new_move_list.append('B1')
            elif move == 'D2':
                new_move_list.append('B2')
            elif move == 'D3':
                new_move_list.append('B3')
            elif move == 'F1':
                new_move_list.append('D1')
            elif move == 'F2':
                new_move_list.append('D2')
            elif move == 'F3':
                new_move_list.append('D3')
            elif move == 'U1':
                new_move_list.append('F1')
            elif move == 'U2':
                new_move_list.append('F2')
            elif move == 'U3':
                new_move_list.append('F3')
            elif move == 'B1':
                new_move_list.append('U1')
            elif move == 'B2':
                new_move_list.append('U2')
            elif move == 'B3':
                new_move_list.append('U3')
            else:
                new_move_list.append(move)
    elif code == O:
        for move in move_list:
            if move == 'D1':
                new_move_list.append('L1')
            elif move == 'D2':
                new_move_list.append('L2')
            elif move == 'D3':
                new_move_list.append('L3')
            elif move == 'R1':
                new_move_list.append('D1')
            elif move == 'R2':
                new_move_list.append('D2')
            elif move == 'R3':
                new_move_list.append('D3')
            elif move == 'U1':
                new_move_list.append('R1')
            elif move == 'U2':
                new_move_list.append('R2')
            elif move == 'U3':
                new_move_list.append('R3')
            elif move == 'L1':
                new_move_list.append('U1')
            elif move == 'L2':
                new_move_list.append('U2')
            elif move == 'L3':
                new_move_list.append('U3')
            else:
                new_move_list.append(move)
    elif code == Y:
        for move in move_list:
            if move == 'D1':
                new_move_list.append('U1')
            elif move == 'D2':
                new_move_list.append('U2')
            elif move == 'D3':
                new_move_list.append('U3')
            elif move == 'F1':
                new_move_list.append('B1')
            elif move == 'F2':
                new_move_list.append('B2')
            elif move == 'F3':
                new_move_list.append('B3')
            elif move == 'U1':
                new_move_list.append('D1')
            elif move == 'U2':
                new_move_list.append('D2')
            elif move == 'U3':
                new_move_list.append('D3')
            elif move == 'B1':
                new_move_list.append('F1')
            elif move == 'B2':
                new_move_list.append('F2')
            elif move == 'B3':
                new_move_list.append('F3')
            else:
                new_move_list.append(move)

    return new_move_list


def face2blue(face):
    new_face = face.copy()
    new_face = np.where(face == B, W, new_face)
    new_face = np.where(face == Y, B, new_face)
    new_face = np.where(face == G, Y, new_face)
    new_face = np.where(face == W, G, new_face)
    return new_face


def face2red(face):
    new_face = face.copy()
    new_face = np.where(face == R, W, new_face)
    new_face = np.where(face == Y, R, new_face)
    new_face = np.where(face == O, Y, new_face)
    new_face = np.where(face == W, O, new_face)
    return new_face


def face2green(face):
    new_face = face.copy()
    new_face = np.where(face == W, B, new_face)
    new_face = np.where(face == B, Y, new_face)
    new_face = np.where(face == Y, G, new_face)
    new_face = np.where(face == G, W, new_face)
    return new_face


def face2orange(face):
    new_face = face.copy()
    new_face = np.where(face == W, R, new_face)
    new_face = np.where(face == R, Y, new_face)
    new_face = np.where(face == Y, O, new_face)
    new_face = np.where(face == O, W, new_face)
    return new_face


def face2yellow(face):
    new_face = face.copy()
    new_face = np.where(face == Y, W, new_face)
    new_face = np.where(face == W, Y, new_face)
    new_face = np.where(face == G, B, new_face)
    new_face = np.where(face == B, G, new_face)
    return new_face


def pos2blue(pos):
    # B to W
    # Y to B
    # G to Y
    # W to G
    new_pos = pos.copy()
    new_pos = np.where(pos == YBO, WBO, new_pos)
    new_pos = np.where(pos == YGO, YBO, new_pos)
    new_pos = np.where(pos == YBR, WBR, new_pos)
    new_pos = np.where(pos == YGR, YBR, new_pos)
    new_pos = np.where(pos == WBO, WGO, new_pos)
    new_pos = np.where(pos == WBR, WGR, new_pos)
    new_pos = np.where(pos == WGO, YGO, new_pos)
    new_pos = np.where(pos == WGR, YGR, new_pos)

    new_pos = np.where(pos == YG, YB, new_pos)
    new_pos = np.where(pos == YB, WB, new_pos)
    new_pos = np.where(pos == YO, BO, new_pos)
    new_pos = np.where(pos == YR, BR, new_pos)
    new_pos = np.where(pos == WG, YG, new_pos)
    new_pos = np.where(pos == WB, WG, new_pos)
    new_pos = np.where(pos == WO, GO, new_pos)
    new_pos = np.where(pos == WR, GR, new_pos)
    new_pos = np.where(pos == BR, WR, new_pos)
    new_pos = np.where(pos == BO, WO, new_pos)
    new_pos = np.where(pos == GR, YR, new_pos)
    new_pos = np.where(pos == GO, YO, new_pos)

    new_pos = np.where(pos == 4, 10, new_pos)
    new_pos = np.where(pos == 10, 22, new_pos)
    new_pos = np.where(pos == 22, 16, new_pos)
    new_pos = np.where(pos == 16, 4, new_pos)
    return new_pos


def pos2red(pos):
    # R to W
    # Y to R
    # O to Y
    # W to O
    new_pos = pos.copy()
    new_pos = np.where(pos == YBO, YBR, new_pos)
    new_pos = np.where(pos == YGO, YGR, new_pos)
    new_pos = np.where(pos == YBR, WBR, new_pos)
    new_pos = np.where(pos == YGR, WGR, new_pos)
    new_pos = np.where(pos == WBO, YBO, new_pos)
    new_pos = np.where(pos == WBR, WBO, new_pos)
    new_pos = np.where(pos == WGO, YGO, new_pos)
    new_pos = np.where(pos == WGR, WGO, new_pos)

    new_pos = np.where(pos == YG, GR, new_pos)
    new_pos = np.where(pos == YB, BR, new_pos)
    new_pos = np.where(pos == YO, YR, new_pos)
    new_pos = np.where(pos == YR, WR, new_pos)
    new_pos = np.where(pos == WG, GO, new_pos)
    new_pos = np.where(pos == WB, BO, new_pos)
    new_pos = np.where(pos == WO, YO, new_pos)
    new_pos = np.where(pos == WR, WO, new_pos)
    new_pos = np.where(pos == BR, WB, new_pos)
    new_pos = np.where(pos == BO, YB, new_pos)
    new_pos = np.where(pos == GR, WG, new_pos)
    new_pos = np.where(pos == GO, YG, new_pos)

    new_pos = np.where(pos == 4, 12, new_pos)
    new_pos = np.where(pos == 12, 22, new_pos)
    new_pos = np.where(pos == 22, 14, new_pos)
    new_pos = np.where(pos == 14, 4, new_pos)
    return new_pos


def pos2green(pos):
    # W to B
    # B to Y
    # Y to G
    # G to W
    new_pos = pos.copy()
    new_pos = np.where(pos == WBO, YBO, new_pos)
    new_pos = np.where(pos == YBO, YGO, new_pos)
    new_pos = np.where(pos == WBR, YBR, new_pos)
    new_pos = np.where(pos == YBR, YGR, new_pos)
    new_pos = np.where(pos == WGO, WBO, new_pos)
    new_pos = np.where(pos == WGR, WBR, new_pos)
    new_pos = np.where(pos == YGO, WGO, new_pos)
    new_pos = np.where(pos == YGR, WGR, new_pos)

    new_pos = np.where(pos == YB, YG, new_pos)
    new_pos = np.where(pos == WB, YB, new_pos)
    new_pos = np.where(pos == BO, YO, new_pos)
    new_pos = np.where(pos == BR, YR, new_pos)
    new_pos = np.where(pos == YG, WG, new_pos)
    new_pos = np.where(pos == WG, WB, new_pos)
    new_pos = np.where(pos == GO, WO, new_pos)
    new_pos = np.where(pos == GR, WR, new_pos)
    new_pos = np.where(pos == WR, BR, new_pos)
    new_pos = np.where(pos == WO, BO, new_pos)
    new_pos = np.where(pos == YR, GR, new_pos)
    new_pos = np.where(pos == YO, GO, new_pos)

    new_pos = np.where(pos == 10, 4, new_pos)
    new_pos = np.where(pos == 22, 10, new_pos)
    new_pos = np.where(pos == 16, 22, new_pos)
    new_pos = np.where(pos == 4, 16, new_pos)
    return new_pos


def pos2orange(pos):
    # W to R
    # R to Y
    # Y to O
    # O to W
    new_pos = pos.copy()
    new_pos = np.where(pos == YBR, YBO, new_pos)
    new_pos = np.where(pos == YGR, YGO, new_pos)
    new_pos = np.where(pos == WBR, YBR, new_pos)
    new_pos = np.where(pos == WGR, YGR, new_pos)
    new_pos = np.where(pos == YBO, WBO, new_pos)
    new_pos = np.where(pos == WBO, WBR, new_pos)
    new_pos = np.where(pos == YGO, WGO, new_pos)
    new_pos = np.where(pos == WGO, WGR, new_pos)

    new_pos = np.where(pos == GR, YG, new_pos)
    new_pos = np.where(pos == BR, YB, new_pos)
    new_pos = np.where(pos == YR, YO, new_pos)
    new_pos = np.where(pos == WR, YR, new_pos)
    new_pos = np.where(pos == GO, WG, new_pos)
    new_pos = np.where(pos == BO, WB, new_pos)
    new_pos = np.where(pos == YO, WO, new_pos)
    new_pos = np.where(pos == WO, WR, new_pos)
    new_pos = np.where(pos == WB, BR, new_pos)
    new_pos = np.where(pos == YB, BO, new_pos)
    new_pos = np.where(pos == WG, GR, new_pos)
    new_pos = np.where(pos == YG, GO, new_pos)

    new_pos = np.where(pos == 12, 4, new_pos)
    new_pos = np.where(pos == 22, 12, new_pos)
    new_pos = np.where(pos == 14, 22, new_pos)
    new_pos = np.where(pos == 4, 14, new_pos)
    return new_pos


def pos2yellow(pos):
    # B to G
    # Y to W
    # G to B
    # W to Y
    new_pos = pos.copy()
    new_pos = np.where(pos == YBO, WGO, new_pos)
    new_pos = np.where(pos == YGO, WBO, new_pos)
    new_pos = np.where(pos == YBR, WGR, new_pos)
    new_pos = np.where(pos == YGR, WBR, new_pos)
    new_pos = np.where(pos == WBO, YGO, new_pos)
    new_pos = np.where(pos == WBR, YGR, new_pos)
    new_pos = np.where(pos == WGO, YBO, new_pos)
    new_pos = np.where(pos == WGR, YBR, new_pos)

    new_pos = np.where(pos == YG, WB, new_pos)
    new_pos = np.where(pos == YB, WG, new_pos)
    new_pos = np.where(pos == YO, WO, new_pos)
    new_pos = np.where(pos == YR, WR, new_pos)
    new_pos = np.where(pos == WG, YB, new_pos)
    new_pos = np.where(pos == WB, YG, new_pos)
    new_pos = np.where(pos == WO, YO, new_pos)
    new_pos = np.where(pos == WR, YR, new_pos)
    new_pos = np.where(pos == BR, GR, new_pos)
    new_pos = np.where(pos == BO, GO, new_pos)
    new_pos = np.where(pos == GR, BR, new_pos)
    new_pos = np.where(pos == GO, BO, new_pos)

    new_pos = np.where(pos == 4, 22, new_pos)
    new_pos = np.where(pos == 10, 16, new_pos)
    new_pos = np.where(pos == 22, 4, new_pos)
    new_pos = np.where(pos == 16, 10, new_pos)
    return new_pos


class Rubiks_Cube:
    def __init__(self):
        self.positions = np.arange(27).reshape((3, 3, 3)).astype(int)
        self.down_face = W * np.ones((3, 3)).astype(int)
        self.front_face = B * np.ones((3, 3)).astype(int)
        self.right_face = R * np.ones((3, 3)).astype(int)
        self.back_face = G * np.ones((3, 3)).astype(int)
        self.left_face = O * np.ones((3, 3)).astype(int)
        self.up_face = Y * np.ones((3, 3)).astype(int)
        self.move_list = []

    def is_solved(self):
        if not all(x == self.down_face.reshape(9)[0] for x in self.down_face.reshape(9)):
            return False
        elif not all(x == self.front_face.reshape(9)[0] for x in self.front_face.reshape(9)):
            return False
        elif not all(x == self.right_face.reshape(9)[0] for x in self.right_face.reshape(9)):
            return False
        elif not all(x == self.back_face.reshape(9)[0] for x in self.back_face.reshape(9)):
            return False
        elif not all(x == self.left_face.reshape(9)[0] for x in self.left_face.reshape(9)):
            return False
        elif not all(x == self.up_face.reshape(9)[0] for x in self.up_face.reshape(9)):
            return False
        else:
            return True

    def reset(self):
        self.positions = np.arange(27).reshape((3, 3, 3)).astype(int)
        self.down_face = W * np.ones((3, 3)).astype(int)
        self.front_face = B * np.ones((3, 3)).astype(int)
        self.right_face = R * np.ones((3, 3)).astype(int)
        self.back_face = G * np.ones((3, 3)).astype(int)
        self.left_face = O * np.ones((3, 3)).astype(int)
        self.up_face = Y * np.ones((3, 3)).astype(int)

    def checksum(self):
        checksum = np.sum(self.down_face)
        checksum += np.sum(self.front_face)
        checksum += np.sum(self.right_face)
        checksum += np.sum(self.back_face)
        checksum += np.sum(self.left_face)
        checksum += np.sum(self.up_face)
        if checksum == 9 * (W + B + R + G + O + Y):
            return True
        else:
            return False

    def perform_moves(self, moves):
        self.move_list = simplify_move_list(self.move_list + moves)
        for move in moves:
            if move == 'U1':
                self.U1()
            elif move == 'U2':
                self.U2()
            elif move == 'U3':
                self.U3()
            elif move == 'D1':
                self.D1()
            elif move == 'D2':
                self.D2()
            elif move == 'D3':
                self.D3()
            elif move == 'R1':
                self.R1()
            elif move == 'R2':
                self.R2()
            elif move == 'R3':
                self.R3()
            elif move == 'L1':
                self.L1()
            elif move == 'L2':
                self.L2()
            elif move == 'L3':
                self.L3()
            elif move == 'F1':
                self.F1()
            elif move == 'F2':
                self.F2()
            elif move == 'F3':
                self.F3()
            elif move == 'B1':
                self.B1()
            elif move == 'B2':
                self.B2()
            elif move == 'B3':
                self.B3()

    def scramble(self):
        moves = np.random.randint(18, size=25)
        move_list = []
        for move in moves:
            if move == 0:
                self.D1()
                move_list.append('D1')
            elif move == 1:
                self.D2()
                move_list.append('D2')
            elif move == 2:
                self.D3()
                move_list.append('D3')
            elif move == 3:
                self.F1()
                move_list.append('F1')
            elif move == 4:
                self.F2()
                move_list.append('F2')
            elif move == 5:
                self.F3()
                move_list.append('F3')
            elif move == 6:
                self.R1()
                move_list.append('R1')
            elif move == 7:
                self.R2()
                move_list.append('R2')
            elif move == 8:
                self.R3()
                move_list.append('R3')
            elif move == 9:
                self.B1()
                move_list.append('B1')
            elif move == 10:
                self.B2()
                move_list.append('B2')
            elif move == 11:
                self.B3()
                move_list.append('B3')
            elif move == 12:
                self.L1()
                move_list.append('L1')
            elif move == 13:
                self.L2()
                move_list.append('L2')
            elif move == 14:
                self.L3()
                move_list.append('L3')
            elif move == 15:
                self.U1()
                move_list.append('U1')
            elif move == 16:
                self.U2()
                move_list.append('U2')
            elif move == 17:
                self.U3()
                move_list.append('U3')
        print(simplify_move_list(move_list))

    # Rotates D layer 90° CW
    def D1(self):
        self.positions[0] = np.rot90(self.positions[0], 1)
        self.down_face = np.rot90(self.down_face, 3)
        front = self.front_face[2].copy()
        right = self.right_face[2].copy()
        back = self.back_face[2].copy()
        left = self.left_face[2].copy()
        self.front_face[2] = left
        self.right_face[2] = front
        self.back_face[2] = right
        self.left_face[2] = back

    # Rotates D layer 180°
    def D2(self):
        self.positions[0] = np.rot90(self.positions[0], 2)
        self.down_face = np.rot90(self.down_face, 2)
        front = self.front_face[2].copy()
        right = self.right_face[2].copy()
        back = self.back_face[2].copy()
        left = self.left_face[2].copy()
        self.front_face[2] = back
        self.right_face[2] = left
        self.back_face[2] = front
        self.left_face[2] = right

    # Rotates D layer 90° CCW
    def D3(self):
        self.positions[0] = np.rot90(self.positions[0], 3)
        self.down_face = np.rot90(self.down_face, 1)
        front = self.front_face[2].copy()
        right = self.right_face[2].copy()
        back = self.back_face[2].copy()
        left = self.left_face[2].copy()
        self.front_face[2] = right
        self.right_face[2] = back
        self.back_face[2] = left
        self.left_face[2] = front

    # Rotates F layer 90° CW
    def F1(self):
        self.positions[:, 2] = np.rot90(self.positions[:, 2], 1)
        self.front_face = np.rot90(self.front_face, 3)
        down = self.down_face[0].copy()
        right = self.right_face[:, 0].copy()
        up = self.up_face[2].copy()
        left = self.left_face[:, 2].copy()
        self.down_face[0] = np.flip(right)
        self.right_face[:, 0] = up
        self.up_face[2] = np.flip(left)
        self.left_face[:, 2] = down

    # Rotates F layer 180°
    def F2(self):
        self.positions[:, 2] = np.rot90(self.positions[:, 2], 2)
        self.front_face = np.rot90(self.front_face, 2)
        down = self.down_face[0].copy()
        right = self.right_face[:, 0].copy()
        up = self.up_face[2].copy()
        left = self.left_face[:, 2].copy()
        self.down_face[0] = np.flip(up)
        self.right_face[:, 0] = np.flip(left)
        self.up_face[2] = np.flip(down)
        self.left_face[:, 2] = np.flip(right)

    # Rotates F layer 90° CCW
    def F3(self):
        self.positions[:, 2] = np.rot90(self.positions[:, 2], 3)
        self.front_face = np.rot90(self.front_face, 1)
        down = self.down_face[0].copy()
        right = self.right_face[:, 0].copy()
        up = self.up_face[2].copy()
        left = self.left_face[:, 2].copy()
        self.down_face[0] = left
        self.right_face[:, 0] = np.flip(down)
        self.up_face[2] = right
        self.left_face[:, 2] = np.flip(up)

    # Rotates R layer 90° CW
    def R1(self):
        self.positions[:, :, 2] = np.rot90(self.positions[:, :, 2], 3)
        self.right_face = np.rot90(self.right_face, 3)
        down = self.down_face[:, 2].copy()
        front = self.front_face[:, 2].copy()
        up = self.up_face[:, 2].copy()
        back = self.back_face[:, 0].copy()
        self.down_face[:, 2] = np.flip(back)
        self.front_face[:, 2] = down
        self.up_face[:, 2] = front
        self.back_face[:, 0] = np.flip(up)

    # Rotates R layer 180°
    def R2(self):
        self.positions[:, :, 2] = np.rot90(self.positions[:, :, 2], 2)
        self.right_face = np.rot90(self.right_face, 2)
        down = self.down_face[:, 2].copy()
        front = self.front_face[:, 2].copy()
        up = self.up_face[:, 2].copy()
        back = self.back_face[:, 0].copy()
        self.down_face[:, 2] = up
        self.front_face[:, 2] = np.flip(back)
        self.up_face[:, 2] = down
        self.back_face[:, 0] = np.flip(front)

    # Rotates R layer 90° CCW
    def R3(self):
        self.positions[:, :, 2] = np.rot90(self.positions[:, :, 2], 1)
        self.right_face = np.rot90(self.right_face, 1)
        down = self.down_face[:, 2].copy()
        front = self.front_face[:, 2].copy()
        up = self.up_face[:, 2].copy()
        back = self.back_face[:, 0].copy()
        self.down_face[:, 2] = front
        self.front_face[:, 2] = up
        self.up_face[:, 2] = np.flip(back)
        self.back_face[:, 0] = np.flip(down)

    # Rotates B layer 90° CW
    def B1(self):
        self.positions[:, 0] = np.rot90(self.positions[:, 0], 3)
        self.back_face = np.rot90(self.back_face, 3)
        down = self.down_face[2].copy()
        right = self.right_face[:, 2].copy()
        up = self.up_face[0].copy()
        left = self.left_face[:, 0].copy()
        self.down_face[2] = left
        self.right_face[:, 2] = np.flip(down)
        self.up_face[0] = right
        self.left_face[:, 0] = np.flip(up)

    # Rotates B layer 180°
    def B2(self):
        self.positions[:, 0] = np.rot90(self.positions[:, 0], 2)
        self.back_face = np.rot90(self.back_face, 2)
        down = self.down_face[2].copy()
        right = self.right_face[:, 2].copy()
        up = self.up_face[0].copy()
        left = self.left_face[:, 0].copy()
        self.down_face[2] = np.flip(up)
        self.right_face[:, 2] = np.flip(left)
        self.up_face[0] = np.flip(down)
        self.left_face[:, 0] = np.flip(right)

    # Rotates B layer 90° CCW
    def B3(self):
        self.positions[:, 0] = np.rot90(self.positions[:, 0], 1)
        self.back_face = np.rot90(self.back_face, 1)
        down = self.down_face[2].copy()
        right = self.right_face[:, 2].copy()
        up = self.up_face[0].copy()
        left = self.left_face[:, 0].copy()
        self.down_face[2] = np.flip(right)
        self.right_face[:, 2] = up
        self.up_face[0] = np.flip(left)
        self.left_face[:, 0] = down

    # Rotates L layer 90° CW
    def L1(self):
        self.positions[:, :, 0] = np.rot90(self.positions[:, :, 0], 1)
        self.left_face = np.rot90(self.left_face, 3)
        down = self.down_face[:, 0].copy()
        front = self.front_face[:, 0].copy()
        up = self.up_face[:, 0].copy()
        back = self.back_face[:, 2].copy()
        self.down_face[:, 0] = front
        self.front_face[:, 0] = up
        self.up_face[:, 0] = np.flip(back)
        self.back_face[:, 2] = np.flip(down)

    # Rotates L layer 180°
    def L2(self):
        self.positions[:, :, 0] = np.rot90(self.positions[:, :, 0], 2)
        self.left_face = np.rot90(self.left_face, 2)
        down = self.down_face[:, 0].copy()
        front = self.front_face[:, 0].copy()
        up = self.up_face[:, 0].copy()
        back = self.back_face[:, 2].copy()
        self.down_face[:, 0] = up
        self.front_face[:, 0] = np.flip(back)
        self.up_face[:, 0] = down
        self.back_face[:, 2] = np.flip(front)

    # Rotates L layer 90° CCW
    def L3(self):
        self.positions[:, :, 0] = np.rot90(self.positions[:, :, 0], 3)
        self.left_face = np.rot90(self.left_face, 1)
        down = self.down_face[:, 0].copy()
        front = self.front_face[:, 0].copy()
        up = self.up_face[:, 0].copy()
        back = self.back_face[:, 2].copy()
        self.down_face[:, 0] = np.flip(back)
        self.front_face[:, 0] = down
        self.up_face[:, 0] = front
        self.back_face[:, 2] = np.flip(up)

    # Rotates U layer 90° CW
    def U1(self):
        self.positions[2] = np.rot90(self.positions[2], 3)
        self.up_face = np.rot90(self.up_face, 3)
        front = self.front_face[0].copy()
        right = self.right_face[0].copy()
        back = self.back_face[0].copy()
        left = self.left_face[0].copy()
        self.front_face[0] = right
        self.right_face[0] = back
        self.back_face[0] = left
        self.left_face[0] = front

    # Rotates U layer 180°
    def U2(self):
        self.positions[2] = np.rot90(self.positions[2], 2)
        self.up_face = np.rot90(self.up_face, 2)
        front = self.front_face[0].copy()
        right = self.right_face[0].copy()
        back = self.back_face[0].copy()
        left = self.left_face[0].copy()
        self.front_face[0] = back
        self.right_face[0] = left
        self.back_face[0] = front
        self.left_face[0] = right

    # Rotates U layer 90° CCW
    def U3(self):
        self.positions[2] = np.rot90(self.positions[2], 1)
        self.up_face = np.rot90(self.up_face, 1)
        front = self.front_face[0].copy()
        right = self.right_face[0].copy()
        back = self.back_face[0].copy()
        left = self.left_face[0].copy()
        self.front_face[0] = left
        self.right_face[0] = front
        self.back_face[0] = right
        self.left_face[0] = back

    # Rotates cube around x-axis 90° CW
    def X1(self):
        self.positions = np.rot90(self.positions, 3, axes=(0,1))
        self.right_face = np.rot90(self.right_face, 3)
        self.left_face = np.rot90(self.left_face, 1)
        front = self.front_face.copy()
        down = self.down_face.copy()
        back = self.back_face.copy()
        up = self.up_face.copy()
        self.front_face = down
        self.down_face = np.flipud(np.fliplr(back))
        self.back_face = np.flipud(np.fliplr(up))
        self.up_face = front

    # Rotates cube around x-axis 180°
    def X2(self):
        self.positions = np.rot90(self.positions, 2, axes=(0,1))
        self.right_face = np.rot90(self.right_face, 2)
        self.left_face = np.rot90(self.left_face, 2)
        front = self.front_face.copy()
        down = self.down_face.copy()
        back = self.back_face.copy()
        up = self.up_face.copy()
        self.front_face = np.flipud(np.fliplr(back))
        self.down_face = up
        self.back_face = np.flipud(np.fliplr(front))
        self.up_face = down

    # Rotates cube around x-axis 90° CCW
    def X3(self):
        self.positions = np.rot90(self.positions, 1, axes=(0,1))
        self.right_face = np.rot90(self.right_face, 1)
        self.left_face = np.rot90(self.left_face, 3)
        front = self.front_face.copy()
        down = self.down_face.copy()
        back = self.back_face.copy()
        up = self.up_face.copy()
        self.front_face = up
        self.down_face = front
        self.back_face = np.flipud(np.fliplr(down))
        self.up_face = np.flipud(np.fliplr(back))

    # Rotates cube around y-axis 90° CW
    def Y1(self):
        self.positions = np.rot90(self.positions, 3, axes=(1,2))
        self.down_face = np.rot90(self.down_face, 1)
        self.up_face = np.rot90(self.up_face, 3)
        front = self.front_face.copy()
        right = self.right_face.copy()
        back = self.back_face.copy()
        left = self.left_face.copy()
        self.front_face = right
        self.right_face = back
        self.back_face = left
        self.left_face = front

    # Rotates cube around y-axis 180°
    def Y2(self):
        self.positions = np.rot90(self.positions, 2, axes=(1,2))
        self.down_face = np.rot90(self.down_face, 2)
        self.up_face = np.rot90(self.up_face, 2)
        front = self.front_face.copy()
        right = self.right_face.copy()
        back = self.back_face.copy()
        left = self.left_face.copy()
        self.front_face = back
        self.right_face = left
        self.back_face = front
        self.left_face = right

    # Rotates cube around y-axis 90° CCW
    def Y3(self):
        self.positions = np.rot90(self.positions, 1, axes=(1,2))
        self.down_face = np.rot90(self.down_face, 3)
        self.up_face = np.rot90(self.up_face, 1)
        front = self.front_face.copy()
        right = self.right_face.copy()
        back = self.back_face.copy()
        left = self.left_face.copy()
        self.front_face = left
        self.right_face = front
        self.back_face = right
        self.left_face = back

    # Rotates cube around z-axis 90° CW
    def Z1(self):
        self.positions = np.rot90(self.positions, 3, axes=(0,2))
        self.front_face = np.rot90(self.front_face, 1)
        self.back_face = np.rot90(self.back_face, 3)
        down = self.down_face.copy()
        right = self.right_face.copy()
        up = self.up_face.copy()
        left = self.left_face.copy()
        self.down_face = np.rot90(left, 1)
        self.right_face = np.rot90(down, 1)
        self.up_face = np.rot90(right, 1)
        self.left_face = np.rot90(up, 1)

    # Rotates cube around z-axis 180°
    def Z2(self):
        self.positions = np.rot90(self.positions, 2, axes=(0,2))
        self.front_face = np.rot90(self.front_face, 2)
        self.back_face = np.rot90(self.back_face, 2)
        down = self.down_face.copy()
        right = self.right_face.copy()
        up = self.up_face.copy()
        left = self.left_face.copy()
        self.down_face = np.rot90(up, 2)
        self.right_face = np.rot90(left, 2)
        self.up_face = np.rot90(down, 2)
        self.left_face = np.rot90(right, 2)

    # Rotates cube around z-axis 90° CCW
    def Z3(self):
        self.positions = np.rot90(self.positions, 1, axes=(0,2))
        self.front_face = np.rot90(self.front_face, 3)
        self.back_face = np.rot90(self.back_face, 1)
        down = self.down_face.copy()
        right = self.right_face.copy()
        up = self.up_face.copy()
        left = self.left_face.copy()
        self.down_face = np.rot90(right, 3)
        self.right_face = np.rot90(up, 3)
        self.up_face = np.rot90(left, 3)
        self.left_face = np.rot90(down, 3)

    # Swaps faces so that blue is on the bottom
    def swap2blue(self):
        self.X3()
        self.down_face = face2blue(self.down_face)
        self.front_face = face2blue(self.front_face)
        self.right_face = face2blue(self.right_face)
        self.back_face = face2blue(self.back_face)
        self.left_face = face2blue(self.left_face)
        self.up_face = face2blue(self.up_face)
        self.positions = pos2blue(self.positions)

    # Swaps faces so that red is on the bottom
    def swap2red(self):
        self.Z3()
        self.down_face = face2red(self.down_face)
        self.front_face = face2red(self.front_face)
        self.right_face = face2red(self.right_face)
        self.back_face = face2red(self.back_face)
        self.left_face = face2red(self.left_face)
        self.up_face = face2red(self.up_face)
        self.positions = pos2red(self.positions)

    # Swaps faces so that green is on the bottom
    def swap2green(self):
        self.X1()
        self.down_face = face2green(self.down_face)
        self.front_face = face2green(self.front_face)
        self.right_face = face2green(self.right_face)
        self.back_face = face2green(self.back_face)
        self.left_face = face2green(self.left_face)
        self.up_face = face2green(self.up_face)
        self.positions = pos2green(self.positions)

    # Swaps faces so that orange is on the bottom
    def swap2orange(self):
        self.Z1()
        self.down_face = face2orange(self.down_face)
        self.front_face = face2orange(self.front_face)
        self.right_face = face2orange(self.right_face)
        self.back_face = face2orange(self.back_face)
        self.left_face = face2orange(self.left_face)
        self.up_face = face2orange(self.up_face)
        self.positions = pos2orange(self.positions)

    # Swaps faces so that yellow is on the bottom
    def swap2yellow(self):
        self.X2()
        self.down_face = face2yellow(self.down_face)
        self.front_face = face2yellow(self.front_face)
        self.right_face = face2yellow(self.right_face)
        self.back_face = face2yellow(self.back_face)
        self.left_face = face2yellow(self.left_face)
        self.up_face = face2yellow(self.up_face)
        self.positions = pos2yellow(self.positions)


class Solver:
    def solve(self, cube):
        self.best_move_list = []
        self.shortest_moves = np.inf

        edges = [WG, WO, WR, WB]

        self.colour_code = W
        white_cube = copy.deepcopy(cube)
        self.solve_cross(white_cube, edges)

        self.colour_code = B
        blue_cube = copy.deepcopy(cube)
        blue_cube.swap2blue()
        self.solve_cross(blue_cube, edges)

        self.colour_code = R
        red_cube = copy.deepcopy(cube)
        red_cube.swap2red()
        self.solve_cross(red_cube, edges)

        self.colour_code = G
        green_cube = copy.deepcopy(cube)
        green_cube.swap2green()
        self.solve_cross(green_cube, edges)

        self.colour_code = O
        orange_cube = copy.deepcopy(cube)
        orange_cube.swap2orange()
        self.solve_cross(orange_cube, edges)

        self.colour_code = Y
        yellow_cube = copy.deepcopy(cube)
        yellow_cube.swap2yellow()
        self.solve_cross(yellow_cube, edges)

        return self.best_move_list

    def solve_cross(self, cube, edges):
        for edge in edges:
            moves = []
            new_edges = edges.copy()
            new_edges.remove(edge)
            perm_cube = copy.deepcopy(cube)
            edge_loc = np.argwhere(perm_cube.positions == edge).squeeze()

            # Placing White-Green Edge
            if edge == WG:  # piece

                if np.array_equal(edge_loc, [0, 0, 1]):  # position
                    if perm_cube.back_face[2, 1] == W:  # orientation
                        moves = ['B2', 'U3', 'L3', 'B1']
                        if perm_cube.down_face[0, 1] == W and perm_cube.left_face[2, 1] == O:
                            moves = moves + ['L1']

                elif np.array_equal(edge_loc, [0, 1, 0]):
                    if perm_cube.down_face[1, 0] == W:
                        if (perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W) or (
                                perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W):
                            moves = ['L2', 'U1', 'B2']
                        else:
                            moves = ['D3']
                    else:
                        moves = ['L1', 'B1']

                elif np.array_equal(edge_loc, [0, 1, 2]):
                    if perm_cube.down_face[1, 2] == W:
                        if (perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W) or (
                                perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W):
                            moves = ['R2', 'U3', 'B2']
                        else:
                            moves = ['D1']
                    else:
                        moves = ['R3', 'B3']

                elif np.array_equal(edge_loc, [0, 2, 1]):
                    if perm_cube.down_face[0, 1] == W:
                        if (perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W) or (
                                perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W):
                            moves = ['F2', 'U2', 'B2']
                        else:
                            moves = ['D2']
                    else:
                        moves = ['F2', 'U1', 'L3', 'B1']
                        if perm_cube.down_face[0, 1] == W and perm_cube.left_face[2, 1] == O:
                            moves = moves + ['L1']

                elif np.array_equal(edge_loc, [1, 0, 0]):
                    if perm_cube.left_face[1, 0] == W:
                        moves = ['B1']
                    else:
                        if perm_cube.down_face[1, 0] == W and perm_cube.left_face[2, 1] == O:
                            moves = ['L1', 'U1', 'B2']
                        else:
                            moves = ['L1', 'U1', 'L3', 'B2']

                elif np.array_equal(edge_loc, [1, 0, 2]):
                    if perm_cube.right_face[1, 2] == W:
                        moves = ['B3']
                    else:
                        if perm_cube.down_face[1, 2] == W and perm_cube.right_face[2, 1] == R:
                            moves = ['R3', 'U3', 'B2']
                        else:
                            moves = ['R3', 'U3', 'R1', 'B2']

                elif np.array_equal(edge_loc, [1, 2, 0]):
                    if perm_cube.front_face[1, 0] == W:
                        moves = ['L3', 'U1', 'B2']
                        if perm_cube.down_face[0, 1] == W and perm_cube.left_face[2, 1] == O:
                            moves = moves + ['L1']
                    else:
                        moves = ['F1', 'U2', 'B2']
                        if perm_cube.down_face[0, 1] == W and perm_cube.front_face[2, 1] == B:
                            moves = moves + ['F3']

                elif np.array_equal(edge_loc, [1, 2, 2]):
                    if perm_cube.front_face[1, 2] == W:
                        moves = ['R1', 'U3', 'B2']
                        if perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W:
                            moves = moves + ['R3']
                    else:
                        moves = ['F3', 'U2', 'B2']
                        if perm_cube.down_face[0, 1] == W and perm_cube.front_face[2, 1] == B:
                            moves = moves + ['F1']

                elif np.array_equal(edge_loc, [2, 0, 1]):
                    if perm_cube.up_face[0, 1] == W:
                        moves = ['B2']
                    else:
                        moves = ['U3', 'L3', 'B1']
                        if perm_cube.down_face[0, 1] == W and perm_cube.left_face[2, 1] == O:
                            moves = moves + ['L1']

                elif np.array_equal(edge_loc, [2, 1, 0]):
                    if perm_cube.up_face[1, 0] == W:
                        moves = ['U1', 'B2']
                    else:
                        moves = ['L3', 'B1']
                        if perm_cube.down_face[0, 1] == W and perm_cube.left_face[2, 1] == O:
                            moves = moves + ['L1']

                elif np.array_equal(edge_loc, [2, 1, 2]):
                    if perm_cube.up_face[1, 2] == W:
                        moves = ['U3', 'B2']
                    else:
                        moves = ['R1', 'B3']
                        if perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W:
                            moves = moves + ['R3']

                elif np.array_equal(edge_loc, [2, 2, 1]):
                    if perm_cube.up_face[2, 1] == W:
                        moves = ['U2', 'B2']
                    else:
                        moves = ['U3', 'R1', 'B3']
                        if perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W:
                            moves = moves + ['R3']

            # Placing White-Orange Edge
            elif edge == WO:

                if np.array_equal(edge_loc, [0, 1, 0]):  # position
                    if perm_cube.left_face[2, 1] == W:  # orientation
                        moves = ['L2', 'U3', 'F3', 'L1']
                        if perm_cube.down_face[1, 2] == W and perm_cube.front_face[2, 1] == B:
                            moves = moves + ['F1']

                elif np.array_equal(edge_loc, [0, 2, 1]):
                    if perm_cube.down_face[0, 1] == W:
                        if (perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W) or (
                                perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W):
                            moves = ['F2', 'U1', 'L2']
                        else:
                            moves = ['D3']
                    else:
                        moves = ['F1', 'L1']

                elif np.array_equal(edge_loc, [0, 0, 1]):
                    if perm_cube.down_face[2, 1] == W:
                        if (perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W) or (
                                perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W):
                            moves = ['B2', 'U3', 'L2']
                        else:
                            moves = ['D1']
                    else:
                        moves = ['B3', 'L3']

                elif np.array_equal(edge_loc, [0, 1, 2]):
                    if perm_cube.down_face[1, 2] == W:
                        if (perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W) or (
                                perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W):
                            moves = ['R2', 'U2', 'L2']
                        else:
                            moves = ['D2']
                    else:
                        moves = ['R2', 'U1', 'F3', 'L1']
                        if perm_cube.down_face[1, 2] == W and perm_cube.front_face[2, 1] == B:
                            moves = moves + ['F1']

                elif np.array_equal(edge_loc, [1, 2, 0]):
                    if perm_cube.front_face[1, 0] == W:
                        moves = ['L1']
                    else:
                        if perm_cube.down_face[0, 1] == W and perm_cube.front_face[2, 1] == B:
                            moves = ['F1', 'U1', 'L2']
                        else:
                            moves = ['F1', 'U1', 'F3', 'L2']

                elif np.array_equal(edge_loc, [1, 0, 0]):
                    if perm_cube.back_face[1, 2] == W:
                        moves = ['L3']
                    else:
                        if perm_cube.down_face[2, 1] == W and perm_cube.back_face[2, 1] == G:
                            moves = ['B3', 'U3', 'L2']
                        else:
                            moves = ['B3', 'U3', 'B1', 'L2']

                elif np.array_equal(edge_loc, [1, 2, 2]):
                    if perm_cube.right_face[1, 0] == W:
                        moves = ['F3', 'U1', 'L2']
                        if perm_cube.down_face[1, 2] == W and perm_cube.front_face[2, 1] == B:
                            moves = moves + ['F1']
                    else:
                        moves = ['R1', 'U2', 'L2']
                        if perm_cube.down_face[1, 2] == W and perm_cube.right_face[2, 1] == R:
                            moves = moves + ['R3']

                elif np.array_equal(edge_loc, [1, 0, 2]):
                    if perm_cube.right_face[1, 2] == W:
                        moves = ['B1', 'U3', 'L2']
                        if perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W:
                            moves = moves + ['B3']
                    else:
                        moves = ['R3', 'U2', 'L2']
                        if perm_cube.down_face[1, 2] == W and perm_cube.right_face[2, 1] == R:
                            moves = moves + ['R1']

                elif np.array_equal(edge_loc, [2, 1, 0]):
                    if perm_cube.up_face[1, 0] == W:
                        moves = ['L2']
                    else:
                        moves = ['U3', 'F3', 'L1']
                        if perm_cube.down_face[1, 2] == W and perm_cube.front_face[2, 1] == B:
                            moves = moves + ['F1']

                elif np.array_equal(edge_loc, [2, 2, 1]):
                    if perm_cube.up_face[2, 1] == W:
                        moves = ['U1', 'L2']
                    else:
                        moves = ['F3', 'L1']
                        if perm_cube.down_face[1, 2] == W and perm_cube.front_face[2, 1] == B:
                            moves = moves + ['F1']

                elif np.array_equal(edge_loc, [2, 0, 1]):
                    if perm_cube.up_face[0, 1] == W:
                        moves = ['U3', 'L2']
                    else:
                        moves = ['B1', 'L3']
                        if perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W:
                            moves = moves + ['B3']

                elif np.array_equal(edge_loc, [2, 1, 2]):
                    if perm_cube.up_face[1, 2] == W:
                        moves = ['U2', 'L2']
                    else:
                        moves = ['U3', 'B1', 'L3']
                        if perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W:
                            moves = moves + ['B3']

            # Placing White-Blue Edge
            elif edge == WB:

                if np.array_equal(edge_loc, [0, 2, 1]):  # position
                    if perm_cube.front_face[2, 1] == W:  # orientation
                        moves = ['F2', 'U3', 'R3', 'F1']
                        if perm_cube.down_face[2, 1] == W and perm_cube.right_face[2, 1] == R:
                            moves = moves + ['R1']

                elif np.array_equal(edge_loc, [0, 1, 2]):
                    if perm_cube.down_face[1, 2] == W:
                        if (perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W) or (
                                perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W):
                            moves = ['R2', 'U1', 'F2']
                        else:
                            moves = ['D3']
                    else:
                        moves = ['R1', 'F1']

                elif np.array_equal(edge_loc, [0, 1, 0]):
                    if perm_cube.down_face[1, 0] == W:
                        if (perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W) or (
                                perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W):
                            moves = ['L2', 'U3', 'F2']
                        else:
                            moves = ['D1']
                    else:
                        moves = ['L3', 'F3']

                elif np.array_equal(edge_loc, [0, 0, 1]):
                    if perm_cube.down_face[2, 1] == W:
                        if (perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W) or (
                                perm_cube.right_face[2, 1] == R and perm_cube.down_face[1, 2] == W):
                            moves = ['B2', 'U2', 'F2']
                        else:
                            moves = ['D2']
                    else:
                        moves = ['B2', 'U1', 'R3', 'F1']
                        if perm_cube.down_face[2, 1] == W and perm_cube.right_face[2, 1] == R:
                            moves = moves + ['R1']

                elif np.array_equal(edge_loc, [1, 2, 2]):
                    if perm_cube.right_face[1, 0] == W:
                        moves = ['F1']
                    else:
                        if perm_cube.down_face[1, 2] == W and perm_cube.right_face[2, 1] == R:
                            moves = ['R1', 'U1', 'F2']
                        else:
                            moves = ['R1', 'U1', 'R3', 'F2']

                elif np.array_equal(edge_loc, [1, 2, 0]):
                    if perm_cube.left_face[1, 2] == W:
                        moves = ['F3']
                    else:
                        if perm_cube.down_face[1, 0] == W and perm_cube.left_face[2, 1] == O:
                            moves = ['L3', 'U3', 'F2']
                        else:
                            moves = ['L3', 'U3', 'L1', 'F2']

                elif np.array_equal(edge_loc, [1, 0, 2]):
                    if perm_cube.back_face[1, 0] == W:
                        moves = ['R3', 'U1', 'F2']
                        if perm_cube.down_face[2, 1] == W and perm_cube.right_face[2, 1] == R:
                            moves = moves + ['R1']
                    else:
                        moves = ['B1', 'U2', 'F2']
                        if perm_cube.down_face[2, 1] == W and perm_cube.back_face[2, 1] == G:
                            moves = moves + ['B3']

                elif np.array_equal(edge_loc, [1, 0, 0]):
                    if perm_cube.back_face[1, 2] == W:
                        moves = ['L1', 'U3', 'F2']
                        if perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W:
                            moves = moves + ['L3']
                    else:
                        moves = ['B3', 'U2', 'F2']
                        if perm_cube.down_face[2, 1] == W and perm_cube.back_face[2, 1] == G:
                            moves = moves + ['B1']

                elif np.array_equal(edge_loc, [2, 2, 1]):
                    if perm_cube.up_face[2, 1] == W:
                        moves = ['F2']
                    else:
                        moves = ['U3', 'R3', 'F1']
                        if perm_cube.down_face[2, 1] == W and perm_cube.right_face[2, 1] == R:
                            moves = moves + ['R1']

                elif np.array_equal(edge_loc, [2, 1, 2]):
                    if perm_cube.up_face[1, 2] == W:
                        moves = ['U1', 'F2']
                    else:
                        moves = ['R3', 'F1']
                        if perm_cube.down_face[2, 1] == W and perm_cube.right_face[2, 1] == R:
                            moves = moves + ['R1']

                elif np.array_equal(edge_loc, [2, 1, 0]):
                    if perm_cube.up_face[1, 0] == W:
                        moves = ['U3', 'F2']
                    else:
                        moves = ['L1', 'F3']
                        if perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W:
                            moves = moves + ['L3']

                elif np.array_equal(edge_loc, [2, 0, 1]):
                    if perm_cube.up_face[0, 1] == W:
                        moves = ['U2', 'F2']
                    else:
                        moves = ['U3', 'L1', 'F3']
                        if perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W:
                            moves = moves + ['L3']

            # Placing White-Red Edge
            elif edge == WR:

                if np.array_equal(edge_loc, [0, 1, 2]):  # position
                    if perm_cube.right_face[2, 1] == W:  # orientation
                        moves = ['R2', 'U3', 'B3', 'R1']
                        if perm_cube.down_face[1, 0] == W and perm_cube.back_face[2, 1] == G:
                            moves = moves + ['B1']

                elif np.array_equal(edge_loc, [0, 0, 1]):
                    if perm_cube.down_face[2, 1] == W:
                        if (perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W) or (
                                perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W):
                            moves = ['B2', 'U1', 'R2']
                        else:
                            moves = ['D3']
                    else:
                        moves = ['B1', 'R1']

                elif np.array_equal(edge_loc, [0, 2, 1]):
                    if perm_cube.down_face[0, 1] == W:
                        if (perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W) or (
                                perm_cube.left_face[2, 1] == O and perm_cube.down_face[1, 0] == W):
                            moves = ['F2', 'U3', 'R2']
                        else:
                            moves = ['D1']
                    else:
                        moves = ['F3', 'R3']

                elif np.array_equal(edge_loc, [0, 1, 0]):
                    if perm_cube.down_face[1, 0] == W:
                        if (perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W) or (
                                perm_cube.back_face[2, 1] == G and perm_cube.down_face[2, 1] == W):
                            moves = ['L2', 'U2', 'R2']
                        else:
                            moves = ['D2']
                    else:
                        moves = ['L2', 'U1', 'B3', 'R1']
                        if perm_cube.down_face[1, 0] == W and perm_cube.back_face[2, 1] == G:
                            moves = moves + ['B1']

                elif np.array_equal(edge_loc, [1, 0, 2]):
                    if perm_cube.back_face[1, 0] == W:
                        moves = ['R1']
                    else:
                        if perm_cube.down_face[2, 1] == W and perm_cube.back_face[2, 1] == G:
                            moves = ['B1', 'U1', 'R2']
                        else:
                            moves = ['B1', 'U1', 'B3', 'R2']

                elif np.array_equal(edge_loc, [1, 2, 2]):
                    if perm_cube.front_face[1, 2] == W:
                        moves = ['R3']
                    else:
                        if perm_cube.down_face[0, 1] == W and perm_cube.front_face[2, 1] == B:
                            moves = ['F3', 'U3', 'R2']
                        else:
                            moves = ['F3', 'U3', 'F1', 'R2']

                elif np.array_equal(edge_loc, [1, 0, 0]):
                    if perm_cube.left_face[1, 0] == W:
                        moves = ['B3', 'U1', 'R2']
                        if perm_cube.down_face[1, 0] == W and perm_cube.back_face[2, 1] == G:
                            moves = moves + ['B1']
                    else:
                        moves = ['L1', 'U2', 'R2']
                        if perm_cube.down_face[1, 0] == W and perm_cube.left_face[2, 1] == O:
                            moves = moves + ['L3']

                elif np.array_equal(edge_loc, [1, 2, 0]):
                    if perm_cube.left_face[1, 2] == W:
                        moves = ['F1', 'U3', 'R2']
                        if perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W:
                            moves = moves + ['F3']
                    else:
                        moves = ['L3', 'U2', 'R2']
                        if perm_cube.down_face[1, 0] == W and perm_cube.left_face[2, 1] == O:
                            moves = moves + ['L1']

                elif np.array_equal(edge_loc, [2, 1, 2]):
                    if perm_cube.up_face[1, 2] == W:
                        moves = ['R2']
                    else:
                        moves = ['U3', 'B3', 'R1']
                        if perm_cube.down_face[1, 0] == W and perm_cube.back_face[2, 1] == G:
                            moves = moves + ['B1']

                elif np.array_equal(edge_loc, [2, 0, 1]):
                    if perm_cube.up_face[0, 1] == W:
                        moves = ['U1', 'R2']
                    else:
                        moves = ['B3', 'R1']
                        if perm_cube.down_face[1, 0] == W and perm_cube.back_face[2, 1] == G:
                            moves = moves + ['B1']

                elif np.array_equal(edge_loc, [2, 2, 1]):
                    if perm_cube.up_face[2, 1] == W:
                        moves = ['U3', 'R2']
                    else:
                        moves = ['F1', 'R3']
                        if perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W:
                            moves = moves + ['F3']

                elif np.array_equal(edge_loc, [2, 1, 0]):
                    if perm_cube.up_face[1, 0] == W:
                        moves = ['U2', 'R2']
                    else:
                        moves = ['U3', 'F1', 'R3']
                        if perm_cube.front_face[2, 1] == B and perm_cube.down_face[0, 1] == W:
                            moves = moves + ['F3']

            perm_cube.perform_moves(moves)

            if len(perm_cube.move_list) < self.shortest_moves:
                if perm_cube.down_face[0, 1] == W and perm_cube.down_face[1, 0] == W \
                    and perm_cube.down_face[1, 2] == W and perm_cube.down_face[2, 1] == W:
                    corners = [WGO, WGR, WBO, WBR]
                    self.solve_F2L(perm_cube, corners)
                elif len(new_edges) > 0:
                    self.solve_cross(perm_cube, new_edges)

    def solve_F2L(self, cube, corners):
        for corner in corners:
            moves = []
            continue_solving = True
            new_corners = corners.copy()
            new_corners.remove(corner)
            perm_cube = copy.deepcopy(cube)
            corner_loc = np.argwhere(perm_cube.positions == corner).squeeze()

            # Placing White-Blue-Red Corner and Blue-Red Edge
            if corner == WBR:

                if np.array_equal(corner_loc, [0, 2, 2]):

                    # Rotates Edge in Place
                    if (perm_cube.up_face[1, 2] == R and perm_cube.right_face[0, 1] == B) or \
                        (perm_cube.up_face[0, 1] == B and perm_cube.back_face[0, 1] == R):
                        moves = ['U1']
                    elif (perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == B) or \
                        (perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == R):
                        moves = ['U2']
                    elif (perm_cube.up_face[1, 0] == R and perm_cube.left_face[0, 1] == B) or \
                        (perm_cube.up_face[2, 1] == B and perm_cube.front_face[0, 1] == R):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.down_face[0, 2] == W:
                        if perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == B:
                            moves = ['U1', 'R1', 'U3', 'R3', 'U3', 'F3', 'U1', 'F1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == R:
                            moves = ['U3', 'F3', 'U1', 'F1', 'U1', 'R1', 'U3', 'R3']
                        elif perm_cube.front_face[1, 2] == R and perm_cube.right_face[1, 0] == B:
                            moves = ['R1', 'U3', 'R3', 'U1', 'F3', 'U2', 'F1', 'U1', 'F3', 'U2', 'F1']

                    elif perm_cube.down_face[0, 2] == B:
                        if perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == B:
                            moves = ['F3', 'U1', 'F1', 'U3', 'F3', 'U1', 'F1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == R:
                            moves = ['R1', 'U1', 'R3', 'U3', 'R1', 'U1', 'R3']
                        elif perm_cube.front_face[1, 2] == R and perm_cube.right_face[1, 0] == B:
                            moves = ['R1', 'U1', 'R3', 'U3', 'R1', 'U3', 'R3', 'U2', 'F3', 'U3', 'F1']
                        elif perm_cube.front_face[1, 2] == B and perm_cube.right_face[1, 0] == R:
                            moves = ['R1', 'U3', 'R3', 'U1', 'R1', 'U2', 'R3', 'U1', 'R1', 'U3', 'R3']

                    elif perm_cube.down_face[0, 2] == R:
                        if perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == B:
                            moves = ['F3', 'U3', 'F1', 'U1', 'F3', 'U3', 'F1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == R:
                            moves = ['R1', 'U3', 'R3', 'U1', 'R1', 'U3', 'R3']
                        elif perm_cube.front_face[1, 2] == R and perm_cube.right_face[1, 0] == B:
                            moves = ['R1', 'U3', 'R3', 'U1', 'F3', 'U3', 'F1', 'U3', 'F3', 'U3', 'F1']
                        elif perm_cube.front_face[1, 2] == B and perm_cube.right_face[1, 0] == R:
                            moves = ['R1', 'U3', 'R3', 'U3', 'R1', 'U1', 'R3', 'U3', 'R1', 'U2', 'R3']

                elif corner_loc[0] == 2:

                    # Rotates Edge in Place
                    if np.array_equal(corner_loc, [2, 0, 2]):
                        moves = ['U1']
                    elif np.array_equal(corner_loc, [2, 0, 0]):
                        moves = ['U2']
                    elif np.array_equal(corner_loc, [2, 2, 0]):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.front_face[0, 2] == B and perm_cube.right_face[0, 0] == W:
                        if perm_cube.up_face[0, 1] == B and perm_cube.back_face[0, 1] == R:
                            moves = ['R1', 'U1', 'R3']
                        elif perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == B:
                            moves = ['U3', 'F3', 'U1', 'F1']
                        elif perm_cube.front_face[1, 2] == B and perm_cube.right_face[1, 0] == R:
                            moves = ['U1', 'F3', 'U1', 'F1', 'U1', 'F3', 'U2', 'F1']
                        elif perm_cube.front_face[1, 2] == R and perm_cube.right_face[1, 0] == B:
                            moves = ['U1', 'F3', 'U3', 'F1', 'U3', 'R1', 'U1', 'R3']
                        elif perm_cube.up_face[1, 2] == R and perm_cube.right_face[0, 1] == B:
                            moves = ['R1', 'U3', 'R3', 'U2', 'F3', 'U3', 'F1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == B:
                            moves = ['U1', 'F3', 'U2', 'F1', 'U1', 'F3', 'U2', 'F1']
                        elif perm_cube.up_face[1, 0] == R and perm_cube.left_face[0, 1] == B:
                            moves = ['U1', 'F3', 'U3', 'F1', 'U1', 'F3', 'U2', 'F1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == R:
                            moves = ['U3', 'R1', 'U3', 'R3', 'U1', 'R1', 'U1', 'R3']
                        elif perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == R:
                            moves = ['U3', 'R1', 'U1', 'R3', 'U1', 'R1', 'U1', 'R3']
                        elif perm_cube.up_face[2, 1] == B and perm_cube.front_face[0, 1] == R:
                            moves = ['U1', 'F3', 'U2', 'F1', 'U3', 'R1', 'U1', 'R3']

                    elif perm_cube.front_face[0, 2] == W and perm_cube.right_face[0, 0] == R:
                        if perm_cube.up_face[1, 0] == R and perm_cube.left_face[0, 1] == B:
                            moves = ['F3', 'U3', 'F1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == R:
                            moves = ['U1', 'R1', 'U3', 'R3']
                        elif perm_cube.front_face[1, 2] == B and perm_cube.right_face[1, 0] == R:
                            moves = ['U3', 'R1', 'U3', 'R3', 'U3', 'R1', 'U2', 'R3']
                        elif perm_cube.front_face[1, 2] == R and perm_cube.right_face[1, 0] == B:
                            moves = ['U3', 'R1', 'U1', 'R3', 'U1', 'F3', 'U3', 'F1']
                        elif perm_cube.up_face[2, 1] == B and perm_cube.front_face[0, 1] == R:
                            moves = ['F3', 'U1', 'F1', 'U2', 'R1', 'U1', 'R3']
                        elif perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == R:
                            moves = ['U3', 'R1', 'U2', 'R3', 'U3', 'R1', 'U2', 'R3']
                        elif perm_cube.up_face[0, 1] == B and perm_cube.back_face[0, 1] == R:
                            moves = ['U3', 'R1', 'U1', 'R3', 'U3', 'R1', 'U2', 'R3']
                        elif perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == B:
                            moves = ['U1', 'F3', 'U1', 'F1', 'U3', 'F3', 'U3', 'F1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == B:
                            moves = ['U1', 'F3', 'U3', 'F1', 'U3', 'F3', 'U3', 'F1']
                        elif perm_cube.up_face[1, 2] == R and perm_cube.right_face[0, 1] == B:
                            moves = ['U3', 'R1', 'U2', 'R3', 'U1', 'F3', 'U3', 'F1']

                    elif perm_cube.up_face[2, 2] == W and perm_cube.right_face[0, 0] == B:
                        if perm_cube.front_face[1, 2] == B and perm_cube.right_face[1, 0] == R:
                            moves = ['R1', 'U1', 'R3', 'U3', 'R1', 'U1', 'R3', 'U3', 'R1', 'U1', 'R3']
                        elif perm_cube.front_face[1, 2] == R and perm_cube.right_face[1, 0] == B:
                            moves = ['R1', 'U3', 'R3', 'U1', 'F3', 'U1', 'F1']
                        elif perm_cube.up_face[2, 1] == B and perm_cube.front_face[1, 0] == R:
                            moves = ['R1', 'U1', 'R3', 'U2', 'R1', 'U1', 'R3', 'U3', 'R1', 'U1', 'R3']
                        elif perm_cube.up_face[1, 0] == B and perm_cube.left_face[1, 0] == R:
                            moves = ['U2', 'R1', 'U1', 'R3', 'U1', 'R1', 'U3', 'R3']
                        elif perm_cube.up_face[0, 1] == B and perm_cube.back_face[1, 0] == R:
                            moves = ['U1', 'R1', 'U2', 'R3', 'U1', 'R1', 'U3', 'R3']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[1, 0] == R:
                            moves = ['R1', 'U2', 'R3', 'U3', 'R1', 'U1', 'R3']
                        elif perm_cube.up_face[1, 2] == R and perm_cube.right_face[1, 0] == B:
                            moves = ['F3', 'U3', 'F1', 'U2', 'F3', 'U3', 'F1', 'U1', 'F3', 'U3', 'F1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[1, 0] == B:
                            moves = ['U2', 'F3', 'U3', 'F1', 'U3', 'F3', 'U1', 'F1']
                        elif perm_cube.up_face[1, 0] == R and perm_cube.left_face[1, 0] == B:
                            moves = ['U3', 'F3', 'U2', 'F1', 'U3', 'F3', 'U1', 'F1']
                        elif perm_cube.up_face[2, 1] == R and perm_cube.front_face[1, 0] == B:
                            moves = ['F3', 'U2', 'F1', 'U1', 'F3', 'U3', 'F1']

                perm_cube.perform_moves(moves)
                if not (perm_cube.positions[0, 2, 2] == WBR and perm_cube.positions[1, 2, 2] == BR):
                    continue_solving = False

            # Placing White-Green-Red Corner and Green-Red Edge
            elif corner == WGR:

                if np.array_equal(corner_loc, [0, 0, 2]):

                    # Rotates Edge in Place
                    if (perm_cube.up_face[0, 1] == G and perm_cube.back_face[0, 1] == R) or \
                        (perm_cube.up_face[1, 0] == R and perm_cube.left_face[0, 1] == G):
                        moves = ['U1']
                    elif (perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == R) or \
                        (perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == G):
                        moves = ['U2']
                    elif (perm_cube.up_face[2, 1] == G and perm_cube.front_face[0, 1] == R) or \
                        (perm_cube.up_face[1, 2] == R and perm_cube.right_face[0, 1] == G):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.down_face[2, 2] == W:
                        if perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == R:
                            moves = ['U1', 'B1', 'U3', 'B3', 'U3', 'R3', 'U1', 'R1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == G:
                            moves = ['U3', 'R3', 'U1', 'R1', 'U1', 'B1', 'U3', 'B3']
                        elif perm_cube.right_face[1, 2] == G and perm_cube.back_face[1, 0] == R:
                            moves = ['B1', 'U3', 'B3', 'U1', 'R3', 'U2', 'R1', 'U1', 'R3', 'U2', 'R1']

                    elif perm_cube.down_face[2, 2] == R:
                        if perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == R:
                            moves = ['R3', 'U1', 'R1', 'U3', 'R3', 'U1', 'R1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == G:
                            moves = ['B1', 'U1', 'B3', 'U3', 'B1', 'U1', 'B3']
                        elif perm_cube.right_face[1, 2] == G and perm_cube.back_face[1, 0] == R:
                            moves = ['B1', 'U1', 'B3', 'U3', 'B1', 'U3', 'B3', 'U2', 'R3', 'U3', 'R1']
                        elif perm_cube.right_face[1, 2] == R and perm_cube.back_face[1, 0] == G:
                            moves = ['B1', 'U3', 'B3', 'U1', 'B1', 'U2', 'B3', 'U1', 'B1', 'U3', 'B3']

                    elif perm_cube.down_face[2, 2] == G:
                        if perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == R:
                            moves = ['R3', 'U3', 'R1', 'U1', 'R3', 'U3', 'R1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == G:
                            moves = ['B1', 'U3', 'B3', 'U1', 'B1', 'U3', 'B3']
                        elif perm_cube.right_face[1, 2] == G and perm_cube.back_face[1, 0] == R:
                            moves = ['B1', 'U3', 'B3', 'U1', 'R3', 'U3', 'R1', 'U3', 'R3', 'U3', 'R1']
                        elif perm_cube.right_face[1, 2] == R and perm_cube.back_face[1, 0] == G:
                            moves = ['B1', 'U3', 'B3', 'U3', 'B1', 'U1', 'B3', 'U3', 'B1', 'U2', 'B3']

                elif corner_loc[0] == 2:

                    # Rotates Edge in Place
                    if np.array_equal(corner_loc, [2, 0, 0]):
                        moves = ['U1']
                    elif np.array_equal(corner_loc, [2, 2, 0]):
                        moves = ['U2']
                    elif np.array_equal(corner_loc, [2, 2, 2]):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.right_face[0, 2] == R and perm_cube.back_face[0, 0] == W:
                        if perm_cube.up_face[1, 0] == R and perm_cube.left_face[0, 1] == G:
                            moves = ['B1', 'U1', 'B3']
                        elif perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == R:
                            moves = ['U3', 'R3', 'U1', 'R1']
                        elif perm_cube.right_face[1, 2] == R and perm_cube.back_face[1, 0] == G:
                            moves = ['U1', 'R3', 'U1', 'R1', 'U1', 'R3', 'U2', 'R1']
                        elif perm_cube.right_face[1, 2] == G and perm_cube.back_face[1, 0] == R:
                            moves = ['U1', 'R3', 'U3', 'R1', 'U3', 'B1', 'U1', 'B3']
                        elif perm_cube.up_face[0, 1] == G and perm_cube.back_face[0, 1] == R:
                            moves = ['B1', 'U3', 'B3', 'U2', 'R3', 'U3', 'R1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == R:
                            moves = ['U1', 'R3', 'U2', 'R1', 'U1', 'R3', 'U2', 'R1']
                        elif perm_cube.up_face[2, 1] == G and perm_cube.front_face[0, 1] == R:
                            moves = ['U1', 'R3', 'U3', 'R1', 'U1', 'R3', 'U2', 'R1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == G:
                            moves = ['U3', 'B1', 'U3', 'B3', 'U1', 'B1', 'U1', 'B3']
                        elif perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == G:
                            moves = ['U3', 'B1', 'U1', 'B3', 'U1', 'B1', 'U1', 'B3']
                        elif perm_cube.up_face[1, 2] == R and perm_cube.right_face[0, 1] == G:
                            moves = ['U1', 'R3', 'U2', 'R1', 'U3', 'B1', 'U1', 'B3']

                    elif perm_cube.right_face[0, 2] == W and perm_cube.back_face[0, 0] == G:
                        if perm_cube.up_face[2, 1] == G and perm_cube.front_face[0, 1] == R:
                            moves = ['R3', 'U3', 'R1']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[0, 1] == G:
                            moves = ['U1', 'B1', 'U3', 'B3']
                        elif perm_cube.right_face[1, 2] == R and perm_cube.back_face[1, 0] == G:
                            moves = ['U3', 'B1', 'U3', 'B3', 'U3', 'B1', 'U2', 'B3']
                        elif perm_cube.right_face[1, 2] == G and perm_cube.back_face[1, 0] == R:
                            moves = ['U3', 'B1', 'U1', 'B3', 'U1', 'R3', 'U3', 'R1']
                        elif perm_cube.up_face[1, 2] == R and perm_cube.right_face[0, 1] == G:
                            moves = ['R3', 'U1', 'R1', 'U2', 'B1', 'U1', 'B3']
                        elif perm_cube.up_face[2, 1] == R and perm_cube.front_face[0, 1] == G:
                            moves = ['U3', 'B1', 'U2', 'B3', 'U3', 'B1', 'U2', 'B3']
                        elif perm_cube.up_face[1, 0] == R and perm_cube.left_face[0, 1] == G:
                            moves = ['U3', 'B1', 'U1', 'B3', 'U3', 'B1', 'U2', 'B3']
                        elif perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == R:
                            moves = ['U1', 'R3', 'U1', 'R1', 'U3', 'R3', 'U3', 'R1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == R:
                            moves = ['U1', 'R3', 'U3', 'R1', 'U3', 'R3', 'U3', 'R1']
                        elif perm_cube.up_face[0, 1] == G and perm_cube.back_face[0, 1] == R:
                            moves = ['U3', 'B1', 'U2', 'B3', 'U1', 'R3', 'U3', 'R1']

                    elif perm_cube.up_face[0, 2] == W and perm_cube.back_face[0, 0] == R:
                        if perm_cube.right_face[1, 2] == R and perm_cube.back_face[1, 0] == G:
                            moves = ['B1', 'U1', 'B3', 'U3', 'B1', 'U1', 'B3', 'U3', 'B1', 'U1', 'B3']
                        elif perm_cube.right_face[1, 2] == G and perm_cube.back_face[1, 0] == R:
                            moves = ['B1', 'U3', 'B3', 'U1', 'R3', 'U1', 'R1']
                        elif perm_cube.up_face[1, 2] == R and perm_cube.right_face[1, 0] == G:
                            moves = ['B1', 'U1', 'B3', 'U2', 'B1', 'U1', 'B3', 'U3', 'B1', 'U1', 'B3']
                        elif perm_cube.up_face[2, 1] == R and perm_cube.front_face[1, 0] == G:
                            moves = ['U2', 'B1', 'U1', 'B3', 'U1', 'B1', 'U3', 'B3']
                        elif perm_cube.up_face[1, 0] == R and perm_cube.left_face[1, 0] == G:
                            moves = ['U1', 'B1', 'U2', 'B3', 'U1', 'B1', 'U3', 'B3']
                        elif perm_cube.up_face[0, 1] == R and perm_cube.back_face[1, 0] == G:
                            moves = ['B1', 'U2', 'B3', 'U3', 'B1', 'U1', 'B3']
                        elif perm_cube.up_face[0, 1] == G and perm_cube.back_face[1, 0] == R:
                            moves = ['R3', 'U3', 'R1', 'U2', 'R3', 'U3', 'R1', 'U1', 'R3', 'U3', 'R1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[1, 0] == R:
                            moves = ['U2', 'R3', 'U3', 'R1', 'U3', 'R3', 'U1', 'R1']
                        elif perm_cube.up_face[2, 1] == G and perm_cube.front_face[1, 0] == R:
                            moves = ['U3', 'R3', 'U2', 'R1', 'U3', 'R3', 'U1', 'R1']
                        elif perm_cube.up_face[1, 2] == G and perm_cube.right_face[1, 0] == R:
                            moves = ['R3', 'U2', 'R1', 'U1', 'R3', 'U3', 'R1']

                perm_cube.perform_moves(moves)
                if not (perm_cube.positions[0, 0, 2] == WGR and perm_cube.positions[1, 0, 2] == GR):
                    continue_solving = False

            # Placing White-Green-Orange Corner and Green-Orange Edge
            elif corner == WGO:

                if np.array_equal(corner_loc, [0, 0, 0]):

                    # Rotates Edge in Place
                    if (perm_cube.up_face[1, 0] == O and perm_cube.left_face[0, 1] == G) or \
                        (perm_cube.up_face[2, 1] == G and perm_cube.front_face[0, 1] == O):
                        moves = ['U1']
                    elif (perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == G) or \
                        (perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == O):
                        moves = ['U2']
                    elif (perm_cube.up_face[1, 2] == O and perm_cube.right_face[0, 1] == G) or \
                        (perm_cube.up_face[0, 1] == G and perm_cube.back_face[0, 1] == O):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.down_face[2, 0] == W:
                        if perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == G:
                            moves = ['U1', 'L1', 'U3', 'L3', 'U3', 'B3', 'U1', 'B1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == O:
                            moves = ['U3', 'B3', 'U1', 'B1', 'U1', 'L1', 'U3', 'L3']
                        elif perm_cube.back_face[1, 2] == O and perm_cube.left_face[1, 0] == G:
                            moves = ['L1', 'U3', 'L3', 'U1', 'B3', 'U2', 'B1', 'U1', 'B3', 'U2', 'B1']

                    elif perm_cube.down_face[2, 0] == G:
                        if perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == G:
                            moves = ['B3', 'U1', 'B1', 'U3', 'B3', 'U1', 'B1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == O:
                            moves = ['L1', 'U1', 'L3', 'U3', 'L1', 'U1', 'L3']
                        elif perm_cube.back_face[1, 2] == O and perm_cube.left_face[1, 0] == G:
                            moves = ['L1', 'U1', 'L3', 'U3', 'L1', 'U3', 'L3', 'U2', 'B3', 'U3', 'B1']
                        elif perm_cube.back_face[1, 2] == G and perm_cube.left_face[1, 0] == O:
                            moves = ['L1', 'U3', 'L3', 'U1', 'L1', 'U2', 'L3', 'U1', 'L1', 'U3', 'L3']

                    elif perm_cube.down_face[2, 0] == O:
                        if perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == G:
                            moves = ['B3', 'U3', 'B1', 'U1', 'B3', 'U3', 'B1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == O:
                            moves = ['L1', 'U3', 'L3', 'U1', 'L1', 'U3', 'L3']
                        elif perm_cube.back_face[1, 2] == O and perm_cube.left_face[1, 0] == G:
                            moves = ['L1', 'U3', 'L3', 'U1', 'B3', 'U3', 'B1', 'U3', 'B3', 'U3', 'B1']
                        elif perm_cube.back_face[1, 2] == G and perm_cube.left_face[1, 0] == O:
                            moves = ['L1', 'U3', 'L3', 'U3', 'L1', 'U1', 'L3', 'U3', 'L1', 'U2', 'L3']

                elif corner_loc[0] == 2:

                    # Rotates Edge in Place
                    if np.array_equal(corner_loc, [2, 2, 0]):
                        moves = ['U1']
                    elif np.array_equal(corner_loc, [2, 2, 2]):
                        moves = ['U2']
                    elif np.array_equal(corner_loc, [2, 0, 2]):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.back_face[0, 2] == G and perm_cube.left_face[0, 0] == W:
                        if perm_cube.up_face[2, 1] == G and perm_cube.front_face[0, 1] == O:
                            moves = ['L1', 'U1', 'L3']
                        elif perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == G:
                            moves = ['U3', 'B3', 'U1', 'B1']
                        elif perm_cube.back_face[1, 2] == G and perm_cube.left_face[1, 0] == O:
                            moves = ['U1', 'B3', 'U1', 'B1', 'U1', 'B3', 'U2', 'B1']
                        elif perm_cube.back_face[1, 2] == O and perm_cube.left_face[1, 0] == G:
                            moves = ['U1', 'B3', 'U3', 'B1', 'U3', 'L1', 'U1', 'L3']
                        elif perm_cube.up_face[1, 0] == O and perm_cube.left_face[0, 1] == G:
                            moves = ['L1', 'U3', 'L3', 'U2', 'B3', 'U3', 'B1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == G:
                            moves = ['U1', 'B3', 'U2', 'B1', 'U1', 'B3', 'U2', 'B1']
                        elif perm_cube.up_face[1, 2] == O and perm_cube.right_face[0, 1] == G:
                            moves = ['U1', 'B3', 'U3', 'B1', 'U1', 'B3', 'U2', 'B1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == O:
                            moves = ['U3', 'L1', 'U3', 'L3', 'U1', 'L1', 'U1', 'L3']
                        elif perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == O:
                            moves = ['U3', 'L1', 'U1', 'L3', 'U1', 'L1', 'U1', 'L3']
                        elif perm_cube.up_face[0, 1] == G and perm_cube.back_face[0, 1] == O:
                            moves = ['U1', 'B3', 'U2', 'B1', 'U3', 'L1', 'U1', 'L3']

                    elif perm_cube.back_face[0, 2] == W and perm_cube.left_face[0, 0] == O:
                        if perm_cube.up_face[1, 2] == O and perm_cube.right_face[0, 1] == G:
                            moves = ['B3', 'U3', 'B1']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[0, 1] == O:
                            moves = ['U1', 'L1', 'U3', 'L3']
                        elif perm_cube.back_face[1, 2] == G and perm_cube.left_face[1, 0] == O:
                            moves = ['U3', 'L1', 'U3', 'L3', 'U3', 'L1', 'U2', 'L3']
                        elif perm_cube.back_face[1, 2] == O and perm_cube.left_face[1, 0] == G:
                            moves = ['U3', 'L1', 'U1', 'L3', 'U1', 'B3', 'U3', 'B1']
                        elif perm_cube.up_face[0, 1] == G and perm_cube.back_face[0, 1] == O:
                            moves = ['B3', 'U1', 'B1', 'U2', 'L1', 'U1', 'L3']
                        elif perm_cube.up_face[1, 2] == G and perm_cube.right_face[0, 1] == O:
                            moves = ['U3', 'L1', 'U2', 'L3', 'U3', 'L1', 'U2', 'L3']
                        elif perm_cube.up_face[2, 1] == G and perm_cube.front_face[0, 1] == O:
                            moves = ['U3', 'L1', 'U1', 'L3', 'U3', 'L1', 'U2', 'L3']
                        elif perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == G:
                            moves = ['U1', 'B3', 'U1', 'B1', 'U3', 'B3', 'U3', 'B1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == G:
                            moves = ['U1', 'B3', 'U3', 'B1', 'U3', 'B3', 'U3', 'B1']
                        elif perm_cube.up_face[1, 0] == O and perm_cube.left_face[0, 1] == G:
                            moves = ['U3', 'L1', 'U2', 'L3', 'U1', 'B3', 'U3', 'B1']

                    elif perm_cube.up_face[0, 0] == W and perm_cube.left_face[0, 0] == G:
                        if perm_cube.back_face[1, 2] == G and perm_cube.left_face[1, 0] == O:
                            moves = ['L1', 'U1', 'L3', 'U3', 'L1', 'U1', 'L3', 'U3', 'L1', 'U1', 'L3']
                        elif perm_cube.back_face[1, 2] == O and perm_cube.left_face[1, 0] == G:
                            moves = ['L1', 'U3', 'L3', 'U1', 'B3', 'U1', 'B1']
                        elif perm_cube.up_face[0, 1] == G and perm_cube.back_face[1, 0] == O:
                            moves = ['L1', 'U1', 'L3', 'U2', 'L1', 'U1', 'L3', 'U3', 'L1', 'U1', 'L3']
                        elif perm_cube.up_face[1, 2] == G and perm_cube.right_face[1, 0] == O:
                            moves = ['U2', 'L1', 'U1', 'L3', 'U1', 'L1', 'U3', 'L3']
                        elif perm_cube.up_face[2, 1] == G and perm_cube.front_face[1, 0] == O:
                            moves = ['U1', 'L1', 'U2', 'L3', 'U1', 'L1', 'U3', 'L3']
                        elif perm_cube.up_face[1, 0] == G and perm_cube.left_face[1, 0] == O:
                            moves = ['L1', 'U2', 'L3', 'U3', 'L1', 'U1', 'L3']
                        elif perm_cube.up_face[1, 0] == O and perm_cube.left_face[1, 0] == G:
                            moves = ['B3', 'U3', 'B1', 'U2', 'B3', 'U3', 'B1', 'U1', 'B3', 'U3', 'B1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[1, 0] == G:
                            moves = ['U2', 'B3', 'U3', 'B1', 'U3', 'B3', 'U1', 'B1']
                        elif perm_cube.up_face[1, 2] == O and perm_cube.right_face[1, 0] == G:
                            moves = ['U3', 'B3', 'U2', 'B1', 'U3', 'B3', 'U1', 'B1']
                        elif perm_cube.up_face[0, 1] == O and perm_cube.back_face[1, 0] == G:
                            moves = ['B3', 'U2', 'B1', 'U1', 'B3', 'U3', 'B1']

                perm_cube.perform_moves(moves)
                if not (perm_cube.positions[0, 0, 0] == WGO and perm_cube.positions[1, 0, 0] == GO):
                    continue_solving = False

            # Placing White-Blue-Orange Corner and Blue-Orange Edge
            elif corner == WBO:

                if np.array_equal(corner_loc, [0, 2, 0]):

                    # Rotates Edge in Place
                    if (perm_cube.up_face[2, 1] == B and perm_cube.front_face[0, 1] == O) or \
                        (perm_cube.up_face[1, 2] == O and perm_cube.right_face[0, 1] == B):
                        moves = ['U1']
                    elif (perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == O) or \
                        (perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == B):
                        moves = ['U2']
                    elif (perm_cube.up_face[0, 1] == B and perm_cube.back_face[0, 1] == O) or \
                        (perm_cube.up_face[1, 0] == O and perm_cube.left_face[0, 1] == B):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.down_face[0, 0] == W:
                        if perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == O:
                            moves = ['U1', 'F1', 'U3', 'F3', 'U3', 'L3', 'U1', 'L1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == B:
                            moves = ['U3', 'L3', 'U1', 'L1', 'U1', 'F1', 'U3', 'F3']
                        elif perm_cube.left_face[1, 2] == B and perm_cube.front_face[1, 0] == O:
                            moves = ['F1', 'U3', 'F3', 'U1', 'L3', 'U2', 'L1', 'U1', 'L3', 'U2', 'L1']

                    elif perm_cube.down_face[0, 0] == O:
                        if perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == O:
                            moves = ['L3', 'U1', 'L1', 'U3', 'L3', 'U1', 'L1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == B:
                            moves = ['F1', 'U1', 'F3', 'U3', 'F1', 'U1', 'F3']
                        elif perm_cube.left_face[1, 2] == B and perm_cube.front_face[1, 0] == O:
                            moves = ['F1', 'U1', 'F3', 'U3', 'F1', 'U3', 'F3', 'U2', 'L3', 'U3', 'L1']
                        elif perm_cube.left_face[1, 2] == O and perm_cube.front_face[1, 0] == B:
                            moves = ['F1', 'U3', 'F3', 'U1', 'F1', 'U2', 'F3', 'U1', 'F1', 'U3', 'F3']

                    elif perm_cube.down_face[0, 0] == B:
                        if perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == O:
                            moves = ['L3', 'U3', 'L1', 'U1', 'L3', 'U3', 'L1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == B:
                            moves = ['F1', 'U3', 'F3', 'U1', 'F1', 'U3', 'F3']
                        elif perm_cube.left_face[1, 2] == B and perm_cube.front_face[1, 0] == O:
                            moves = ['F1', 'U3', 'F3', 'U1', 'L3', 'U3', 'L1', 'U3', 'L3', 'U3', 'L1']
                        elif perm_cube.left_face[1, 2] == O and perm_cube.front_face[1, 0] == B:
                            moves = ['F1', 'U3', 'F3', 'U3', 'F1', 'U1', 'F3', 'U3', 'F1', 'U2', 'F3']

                elif corner_loc[0] == 2:

                    # Rotates Edge in Place
                    if np.array_equal(corner_loc, [2, 2, 2]):
                        moves = ['U1']
                    elif np.array_equal(corner_loc, [2, 0, 2]):
                        moves = ['U2']
                    elif np.array_equal(corner_loc, [2, 0, 0]):
                        moves = ['U3']

                    perm_cube.perform_moves(moves)
                    moves = []

                    if perm_cube.left_face[0, 2] == O and perm_cube.front_face[0, 0] == W:
                        if perm_cube.up_face[1, 2] == O and perm_cube.right_face[0, 1] == B:
                            moves = ['F1', 'U1', 'F3']
                        elif perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == O:
                            moves = ['U3', 'L3', 'U1', 'L1']
                        elif perm_cube.left_face[1, 2] == O and perm_cube.front_face[1, 0] == B:
                            moves = ['U1', 'L3', 'U1', 'L1', 'U1', 'L3', 'U2', 'L1']
                        elif perm_cube.left_face[1, 2] == B and perm_cube.front_face[1, 0] == O:
                            moves = ['U1', 'L3', 'U3', 'L1', 'U3', 'F1', 'U1', 'F3']
                        elif perm_cube.up_face[2, 1] == B and perm_cube.front_face[0, 1] == O:
                            moves = ['F1', 'U3', 'F3', 'U2', 'L3', 'U3', 'L1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == O:
                            moves = ['U1', 'L3', 'U2', 'L1', 'U1', 'L3', 'U2', 'L1']
                        elif perm_cube.up_face[0, 1] == B and perm_cube.back_face[0, 1] == O:
                            moves = ['U1', 'L3', 'U3', 'L1', 'U1', 'L3', 'U2', 'L1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == B:
                            moves = ['U3', 'F1', 'U3', 'F3', 'U1', 'F1', 'U1', 'F3']
                        elif perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == B:
                            moves = ['U3', 'F1', 'U1', 'F3', 'U1', 'F1', 'U1', 'F3']
                        elif perm_cube.up_face[1, 0] == O and perm_cube.left_face[0, 1] == B:
                            moves = ['U1', 'L3', 'U2', 'L1', 'U3', 'F1', 'U1', 'F3']

                    elif perm_cube.left_face[0, 2] == W and perm_cube.front_face[0, 0] == B:
                        if perm_cube.up_face[0, 1] == B and perm_cube.back_face[0, 1] == O:
                            moves = ['L3', 'U3', 'L1']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[0, 1] == B:
                            moves = ['U1', 'F1', 'U3', 'F3']
                        elif perm_cube.left_face[1, 2] == O and perm_cube.front_face[1, 0] == B:
                            moves = ['U3', 'F1', 'U3', 'F3', 'U3', 'F1', 'U2', 'F3']
                        elif perm_cube.left_face[1, 2] == B and perm_cube.front_face[1, 0] == O:
                            moves = ['U3', 'F1', 'U1', 'F3', 'U1', 'L3', 'U3', 'L1']
                        elif perm_cube.up_face[1, 0] == O and perm_cube.left_face[0, 1] == B:
                            moves = ['L3', 'U1', 'L1', 'U2', 'F1', 'U1', 'F3']
                        elif perm_cube.up_face[0, 1] == O and perm_cube.back_face[0, 1] == B:
                            moves = ['U3', 'F1', 'U2', 'F3', 'U3', 'F1', 'U2', 'F3']
                        elif perm_cube.up_face[1, 2] == O and perm_cube.right_face[0, 1] == B:
                            moves = ['U3', 'F1', 'U1', 'F3', 'U3', 'F1', 'U2', 'F3']
                        elif perm_cube.up_face[1, 0] == B and perm_cube.left_face[0, 1] == O:
                            moves = ['U1', 'L3', 'U1', 'L1', 'U3', 'L3', 'U3', 'L1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[0, 1] == O:
                            moves = ['U1', 'L3', 'U3', 'L1', 'U3', 'L3', 'U3', 'L1']
                        elif perm_cube.up_face[2, 1] == B and perm_cube.front_face[0, 1] == O:
                            moves = ['U3', 'F1', 'U2', 'F3', 'U1', 'L3', 'U3', 'L1']

                    elif perm_cube.up_face[2, 0] == W and perm_cube.front_face[0, 0] == O:
                        if perm_cube.left_face[1, 2] == O and perm_cube.front_face[1, 0] == B:
                            moves = ['F1', 'U1', 'F3', 'U3', 'F1', 'U1', 'F3', 'U3', 'F1', 'U1', 'F3']
                        elif perm_cube.left_face[1, 2] == B and perm_cube.front_face[1, 0] == O:
                            moves = ['F1', 'U3', 'F3', 'U1', 'L3', 'U1', 'L1']
                        elif perm_cube.up_face[1, 0] == O and perm_cube.left_face[1, 0] == B:
                            moves = ['F1', 'U1', 'F3', 'U2', 'F1', 'U1', 'F3', 'U3', 'F1', 'U1', 'F3']
                        elif perm_cube.up_face[0, 1] == O and perm_cube.back_face[1, 0] == B:
                            moves = ['U2', 'F1', 'U1', 'F3', 'U1', 'F1', 'U3', 'F3']
                        elif perm_cube.up_face[1, 2] == O and perm_cube.right_face[1, 0] == B:
                            moves = ['U1', 'F1', 'U2', 'F3', 'U1', 'F1', 'U3', 'F3']
                        elif perm_cube.up_face[2, 1] == O and perm_cube.front_face[1, 0] == B:
                            moves = ['F1', 'U2', 'F3', 'U3', 'F1', 'U1', 'F3']
                        elif perm_cube.up_face[2, 1] == B and perm_cube.front_face[1, 0] == O:
                            moves = ['L3', 'U3', 'L1', 'U2', 'L3', 'U3', 'L1', 'U1', 'L3', 'U3', 'L1']
                        elif perm_cube.up_face[1, 2] == B and perm_cube.right_face[1, 0] == O:
                            moves = ['U2', 'L3', 'U3', 'L1', 'U3', 'L3', 'U1', 'L1']
                        elif perm_cube.up_face[0, 1] == B and perm_cube.back_face[1, 0] == O:
                            moves = ['U3', 'L3', 'U2', 'L1', 'U3', 'L3', 'U1', 'L1']
                        elif perm_cube.up_face[1, 0] == B and perm_cube.left_face[1, 0] == O:
                            moves = ['L3', 'U2', 'L1', 'U1', 'L3', 'U3', 'L1']

                perm_cube.perform_moves(moves)
                if not (perm_cube.positions[0, 2, 0] == WBO and perm_cube.positions[1, 2, 0] == BO):
                    continue_solving = False

            if continue_solving:
                if len(perm_cube.move_list) < self.shortest_moves:
                    if len(new_corners) > 0:
                        self.solve_F2L(perm_cube, new_corners)
                    else:
                        self.solve_OLL(perm_cube)

    def solve_OLL(self, cube):
        moves = []
        new_cube = copy.deepcopy(cube)

        u_check = new_cube.up_face.reshape(9) == (Y * np.ones(9).astype(int))
        f_check = new_cube.front_face[0, :] == (Y * np.ones(3).astype(int))
        r_check = new_cube.right_face[0, :] == (Y * np.ones(3).astype(int))
        b_check = new_cube.back_face[0, :] == (Y * np.ones(3).astype(int))
        l_check = new_cube.left_face[0, :] == (Y * np.ones(3).astype(int))

        # Dot
        if np.array_equal(u_check, [False, False, False, False, True, False, False, False, False]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['R1', 'U1', 'B3', 'R1', 'B1', 'R2', 'U3', 'R3', 'F1', 'R1', 'F3']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['B1', 'U1', 'L3', 'B1', 'L1', 'B2', 'U3', 'B3', 'R1', 'B1', 'R3']
            elif np.array_equal(f_check, [True, True, True]) and np.array_equal(b_check, [False, True, False]):
                moves = ['R3', 'F1', 'R1', 'F3', 'U2', 'R3', 'F1', 'R1', 'F2', 'U2', 'F1']
            elif np.array_equal(r_check, [True, True, True]) and np.array_equal(l_check, [False, True, False]):
                moves = ['B3', 'R1', 'B1', 'R3', 'U2', 'B3', 'R1', 'B1', 'R2', 'U2', 'R1']
            elif np.array_equal(b_check, [True, True, True]) and np.array_equal(f_check, [False, True, False]):
                moves = ['L3', 'B1', 'L1', 'B3', 'U2', 'L3', 'B1', 'L1', 'B2', 'U2', 'B1']
            elif np.array_equal(l_check, [True, True, True]) and np.array_equal(r_check, [False, True, False]):
                moves = ['F3', 'L1', 'F1', 'L3', 'U2', 'F3', 'L1', 'F1', 'L2', 'U2', 'L1']
        elif np.array_equal(u_check, [False, False, False, False, True, False, False, False, True]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, True]):
                moves = ['F3', 'B2', 'L1', 'B3', 'L1', 'F1', 'U2', 'F3', 'L1', 'B3', 'F1']
            elif np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [False, True, False]):
                moves = ['F3', 'U2', 'F3', 'L1', 'F1', 'L3', 'U3', 'L3', 'U3', 'L1', 'U3', 'F1']
        elif np.array_equal(u_check, [False, False, True, False, True, False, False, False, False]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, True]):
                moves = ['R3', 'L2', 'F1', 'L3', 'F1', 'R1', 'U2', 'R3', 'F1', 'L3', 'R1']
            elif np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['R3', 'U2', 'R3', 'F1', 'R1', 'F3', 'U3', 'F3', 'U3', 'F1', 'U3', 'R1']
        elif np.array_equal(u_check, [True, False, False, False, True, False, False, False, False]):
            if np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, True, True]):
                moves = ['B3', 'F2', 'R1', 'F3', 'R1', 'B1', 'U2', 'B3', 'R1', 'F3', 'B1']
            elif np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['B3', 'U2', 'B3', 'R1', 'B1', 'R3', 'U3', 'R3', 'U3', 'R1', 'U3', 'B1']
        elif np.array_equal(u_check, [False, False, False, False, True, False, True, False, False]):
            if np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, True, True]):
                moves = ['L3', 'R2', 'B1', 'R3', 'B1', 'L1', 'U2', 'L3', 'B1', 'R3', 'L1']
            elif np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [False, True, False]):
                moves = ['L3', 'U2', 'L3', 'B1', 'L1', 'B3', 'U3', 'B3', 'U3', 'B1', 'U3', 'L1']
        elif np.array_equal(u_check, [True, False, False, False, True, False, False, False, True]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [True, True, False]):
                moves = ['R1', 'U1', 'R3', 'U1', 'R3', 'F1', 'R1', 'F3', 'U2', 'R3', 'F1', 'R1', 'F3']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [True, True, False]):
                moves = ['L1', 'U1', 'L3', 'U1', 'L3', 'B1', 'L1', 'B3', 'U2', 'L3', 'B1', 'L1', 'B3']
        elif np.array_equal(u_check, [False, False, True, False, True, False, True, False, False]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [True, True, False]):
                moves = ['B1', 'U1', 'B3', 'U1', 'B3', 'R1', 'B1', 'R3', 'U2', 'B3', 'R1', 'B1', 'R3']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [True, True, False]):
                moves = ['F1', 'U1', 'F3', 'U1', 'F3', 'L1', 'F1', 'L3', 'U2', 'F3', 'L1', 'F1', 'L3']
        elif np.array_equal(u_check, [True, False, True, False, True, False, True, False, True]):
            moves = ['R1', 'L3', 'B2', 'R3', 'L1', 'U2', 'R1', 'L3', 'B1', 'R3', 'L1', 'U2', 'R1', 'L3', 'B2', 'R3', 'L1']
        elif np.array_equal(u_check, [True, False, True, False, True, False, False, False, False]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['R3', 'U2', 'F1', 'R1', 'U1', 'R3', 'U3', 'F2', 'U2', 'F1', 'R1']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [True, True, True]):
                moves = ['B1', 'L1', 'U1', 'L3', 'U1', 'B3', 'U2', 'B3', 'R1', 'B1', 'R3']
        elif np.array_equal(u_check, [True, False, False, False, True, False, True, False, False]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['B3', 'U2', 'R1', 'B1', 'U1', 'B3', 'U3', 'R2', 'U2', 'R1', 'B1']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [True, True, True]):
                moves = ['L1', 'F1', 'U1', 'F3', 'U1', 'L3', 'U2', 'L3', 'B1', 'L1', 'B3']
        elif np.array_equal(u_check, [False, False, False, False, True, False, True, False, True]):
            if np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, True, False]):
                moves = ['L3', 'U2', 'B1', 'L1', 'U1', 'L3', 'U3', 'B2', 'U2', 'B1', 'L1']
            elif np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [True, True, True]):
                moves = ['F1', 'R1', 'U1', 'R3', 'U1', 'F3', 'U2', 'F3', 'L1', 'F1', 'L3']
        elif np.array_equal(u_check, [False, False, True, False, True, False, False, False, True]):
            if np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, True, False]):
                moves = ['F3', 'U2', 'L1', 'F1', 'U1', 'F3', 'U3', 'L2', 'U2', 'L1', 'F1']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [True, True, True]):
                moves = ['R1', 'B1', 'U1', 'B3', 'U1', 'R3', 'U2', 'R3', 'F1', 'R1', 'F3']

        # Line
        elif np.array_equal(u_check, [False, True, False, False, True, False, False, True, False]):
            if np.array_equal(f_check, [True, False, False]) and np.array_equal(b_check, [False, False, True]):
                moves = ['R3', 'U3', 'F3', 'U1', 'F3', 'L1', 'F1', 'L3', 'F1', 'R1']
            elif np.array_equal(b_check, [True, False, False]) and np.array_equal(f_check, [False, False, True]):
                moves = ['L3', 'U3', 'B3', 'U1', 'B3', 'R1', 'B1', 'R3', 'B1', 'L1']
            elif np.array_equal(r_check, [True, True, True]) and np.array_equal(l_check, [True, True, True]):
                moves = ['R1', 'U3', 'B2', 'D1', 'B3', 'U2', 'B1', 'D3', 'B2', 'U1', 'R3']
            elif np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [False, True, True]):
                moves = ['R1', 'U1', 'B1', 'U3', 'B3', 'U1', 'B1', 'U3', 'B3', 'R3']
            elif np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [False, True, True]):
                moves = ['L1', 'U1', 'F1', 'U3', 'F3', 'U1', 'F1', 'U3', 'F3', 'L3']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['F3', 'L3', 'F1', 'U3', 'B3', 'U1', 'B1', 'U3', 'B3', 'U1', 'B1', 'F3', 'L1', 'F1']
        elif np.array_equal(u_check, [False, False, False, True, True, True, False, False, False]):
            if np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [False, True, True]):
                moves = ['F1', 'U1', 'R1', 'U3', 'R3', 'U1', 'R1', 'U3', 'R3', 'F3']
            elif np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [False, True, True]):
                moves = ['B1', 'U1', 'L1', 'U3', 'L3', 'U1', 'L1', 'U3', 'L3', 'B3']
            elif np.array_equal(r_check, [True, False, False]) and np.array_equal(l_check, [False, False, True]):
                moves = ['B3', 'U3', 'R3', 'U1', 'R3', 'F1', 'R1', 'F3', 'R1', 'B1']
            elif np.array_equal(l_check, [True, False, False]) and np.array_equal(r_check, [False, False, True]):
                moves = ['F3', 'U3', 'L3', 'U1', 'L3', 'B1', 'L1', 'B3', 'L1', 'F1']
            elif np.array_equal(f_check, [True, True, True]) and np.array_equal(b_check, [True, True, True]):
                moves = ['B1', 'U3', 'L2', 'D1', 'L3', 'U2', 'L1', 'D3', 'L2', 'U1', 'B3']
            elif np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['L3', 'B3', 'L1', 'U3', 'R3', 'U1', 'R1', 'U3', 'R3', 'U1', 'R1', 'L3', 'B1', 'L1']

        # Cross
        elif np.array_equal(u_check, [False, True, False, True, True, True, False, True, False]):
            if np.array_equal(f_check, [True, False, False]) and np.array_equal(b_check, [False, False, True]):
                moves = ['L1', 'U3', 'R3', 'U1', 'L3', 'U1', 'R1', 'U1', 'R3', 'U1', 'R1']
            elif np.array_equal(r_check, [True, False, False]) and np.array_equal(l_check, [False, False, True]):
                moves = ['F1', 'U3', 'B3', 'U1', 'F3', 'U1', 'B1', 'U1', 'B3', 'U1', 'B1']
            elif np.array_equal(b_check, [True, False, False]) and np.array_equal(f_check, [False, False, True]):
                moves = ['R1', 'U3', 'L3', 'U1', 'R3', 'U1', 'L1', 'U1', 'L3', 'U1', 'L1']
            elif np.array_equal(l_check, [True, False, False]) and np.array_equal(r_check, [False, False, True]):
                moves = ['B1', 'U3', 'F3', 'U1', 'B3', 'U1', 'F1', 'U1', 'F3', 'U1', 'F1']
            elif np.array_equal(f_check, [False, False, False]) and np.array_equal(b_check, [False, False, False]):
                moves = ['R1', 'U1', 'R3', 'U1', 'R1', 'U3', 'R3', 'U1', 'R1', 'U2', 'R3']
            elif np.array_equal(r_check, [False, False, False]) and np.array_equal(l_check, [False, False, False]):
                moves = ['B1', 'U1', 'B3', 'U1', 'B1', 'U3', 'B3', 'U1', 'B1', 'U2', 'B3']
        elif np.array_equal(u_check, [False, True, False, True, True, True, False, True, True]):
            if np.array_equal(f_check, [True, False, False]) and np.array_equal(b_check, [True, False, False]):
                moves = ['L3', 'U1', 'R1', 'U3', 'L1', 'U1', 'R3']
            elif np.array_equal(f_check, [False, False, False]) and np.array_equal(b_check, [False, False, True]):
                moves = ['R3', 'U2', 'R1', 'U1', 'R3', 'U1', 'R1']
        elif np.array_equal(u_check, [False, True, True, True, True, True, False, True, False]):
            if np.array_equal(r_check, [True, False, False]) and np.array_equal(l_check, [True, False, False]):
                moves = ['F3', 'U1', 'B1', 'U3', 'F1', 'U1', 'B3']
            elif np.array_equal(r_check, [False, False, False]) and np.array_equal(l_check, [False, False, True]):
                moves = ['B3', 'U2', 'B1', 'U1', 'B3', 'U1', 'B1']
        elif np.array_equal(u_check, [True, True, False, True, True, True, False, True, False]):
            if np.array_equal(b_check, [True, False, False]) and np.array_equal(f_check, [True, False, False]):
                moves = ['R3', 'U1', 'L1', 'U3', 'R1', 'U1', 'L3']
            elif np.array_equal(b_check, [False, False, False]) and np.array_equal(f_check, [False, False, True]):
                moves = ['L3', 'U2', 'L1', 'U1', 'L3', 'U1', 'L1']
        elif np.array_equal(u_check, [False, True, False, True, True, True, True, True, False]):
            if np.array_equal(l_check, [True, False, False]) and np.array_equal(r_check, [True, False, False]):
                moves = ['B3', 'U1', 'F1', 'U3', 'B1', 'U1', 'F3']
            elif np.array_equal(l_check, [False, False, False]) and np.array_equal(r_check, [False, False, True]):
                moves = ['F3', 'U2', 'F1', 'U1', 'F3', 'U1', 'F1']
        elif np.array_equal(u_check, [True, True, False, True, True, True, True, True, False]):
            if np.array_equal(f_check, [False, False, True]) and np.array_equal(b_check, [True, False, False]):
                moves = ['R3', 'F3', 'L1', 'F1', 'R1', 'F3', 'L3', 'F1']
            elif np.array_equal(r_check, [True, False, True]) and np.array_equal(l_check, [False, False, False]):
                moves = ['B2', 'D1', 'B3', 'U2', 'B1', 'D3', 'B3', 'U2', 'B3']
        elif np.array_equal(u_check, [False, True, False, True, True, True, True, True, True]):
            if np.array_equal(r_check, [False, False, True]) and np.array_equal(l_check, [True, False, False]):
                moves = ['B3', 'R3', 'F1', 'R1', 'B1', 'R3', 'F3', 'R1']
            elif np.array_equal(b_check, [True, False, True]) and np.array_equal(f_check, [False, False, False]):
                moves = ['L2', 'D1', 'L3', 'U2', 'L1', 'D3', 'L3', 'U2', 'L3']
        elif np.array_equal(u_check, [False, True, True, True, True, True, False, True, True]):
            if np.array_equal(b_check, [False, False, True]) and np.array_equal(f_check, [True, False, False]):
                moves = ['L3', 'B3', 'R1', 'B1', 'L1', 'B3', 'R3', 'B1']
            elif np.array_equal(l_check, [True, False, True]) and np.array_equal(r_check, [False, False, False]):
                moves = ['F2', 'D1', 'F3', 'U2', 'F1', 'D3', 'F3', 'U2', 'F3']
        elif np.array_equal(u_check, [True, True, True, True, True, True, False, True, False]):
            if np.array_equal(l_check, [False, False, True]) and np.array_equal(r_check, [True, False, False]):
                moves = ['F3', 'L3', 'B1', 'L1', 'F1', 'L3', 'B3', 'L1']
            elif np.array_equal(f_check, [True, False, True]) and np.array_equal(b_check, [False, False, False]):
                moves = ['R2', 'D1', 'R3', 'U2', 'R1', 'D3', 'R3', 'U2', 'R3']
        elif np.array_equal(u_check, [True, True, False, True, True, True, False, True, True]):
            if np.array_equal(f_check, [False, False, False]) and np.array_equal(b_check, [True, False, False]):
                moves = ['R3', 'F3', 'L3', 'F1', 'R1', 'F3', 'L1', 'F1']
            elif np.array_equal(b_check, [False, False, False]) and np.array_equal(f_check, [True, False, False]):
                moves = ['L3', 'B3', 'R3', 'B1', 'L1', 'B3', 'R1', 'B1']
        elif np.array_equal(u_check, [False, True, True, True, True, True, True, True, False]):
            if np.array_equal(r_check, [False, False, False]) and np.array_equal(l_check, [True, False, False]):
                moves = ['B3', 'R3', 'F3', 'R1', 'B1', 'R3', 'F1', 'R1']
            elif np.array_equal(l_check, [False, False, False]) and np.array_equal(r_check, [True, False, False]):
                moves = ['F3', 'L3', 'B3', 'L1', 'F1', 'L3', 'B1', 'L1']

        # 4 Corners
        elif np.array_equal(u_check, [True, True, True, False, True, True, True, False, True]):
            moves = ['R1', 'L3', 'B3', 'R3', 'L1', 'U2', 'R1', 'L3', 'B3', 'R3', 'L1']
        elif np.array_equal(u_check, [True, True, True, True, True, False, True, False, True]):
            moves = ['B1', 'F3', 'L3', 'B3', 'F1', 'U2', 'B1', 'F3', 'L3', 'B3', 'F1']
        elif np.array_equal(u_check, [True, False, True, True, True, False, True, True, True]):
            moves = ['L1', 'R3', 'F3', 'L3', 'R1', 'U2', 'L1', 'R3', 'F3', 'L3', 'R1']
        elif np.array_equal(u_check, [True, False, True, False, True, True, True, True, True]):
            moves = ['F1', 'B3', 'R3', 'F3', 'B1', 'U2', 'F1', 'B3', 'R3', 'F3', 'B1']
        elif np.array_equal(u_check, [True, False, True, True, True, True, True, False, True]):
            moves = ['L3', 'R1', 'U1', 'R3', 'U3', 'L1', 'R3', 'F1', 'R1', 'F3']
        elif np.array_equal(u_check, [True, True, True, False, True, False, True, True, True]):
            moves = ['F3', 'B1', 'U1', 'B3', 'U3', 'F1', 'B3', 'R1', 'B1', 'R3']

        # Shape _|, |_, |¯, and ¯|
        elif np.array_equal(u_check, [False, True, False, True, True, False, True, False, False]):
            if np.array_equal(f_check, [False, True, True]) and np.array_equal(b_check, [False, False, True]):
                moves = ['L1', 'F1', 'R3', 'F1', 'R1', 'F2', 'L3']
            elif np.array_equal(l_check, [True, False, False]) and np.array_equal(r_check, [True, True, False]):
                moves = ['U2', 'B1', 'F2', 'L3', 'F1', 'L3', 'F3', 'L2', 'F1', 'L3', 'F1', 'B3']
        elif np.array_equal(u_check, [False, False, False, True, True, False, False, True, True]):
            if np.array_equal(r_check, [False, True, True]) and np.array_equal(l_check, [False, False, True]):
                moves = ['F1', 'R1', 'B3', 'R1', 'B1', 'R2', 'F3']
            elif np.array_equal(f_check, [True, False, False]) and np.array_equal(b_check, [True, True, False]):
                moves = ['U2', 'L1', 'R2', 'F3', 'R1', 'F3', 'R3', 'F2', 'R1', 'F3', 'R1', 'L3']
        elif np.array_equal(u_check, [False, False, True, False, True, True, False, True, False]):
            if np.array_equal(b_check, [False, True, True]) and np.array_equal(f_check, [False, False, True]):
                moves = ['R1', 'B1', 'L3', 'B1', 'L1', 'B2', 'R3']
            elif np.array_equal(r_check, [True, False, False]) and np.array_equal(l_check, [True, True, False]):
                moves = ['U2', 'F1', 'B2', 'R3', 'B1', 'R3', 'B3', 'R2', 'B1', 'R3', 'B1', 'F3']
        elif np.array_equal(u_check, [True, True, False, False, True, True, False, False, False]):
            if np.array_equal(l_check, [False, True, True]) and np.array_equal(r_check, [False, False, True]):
                moves = ['B1', 'L1', 'F3', 'L1', 'F1', 'L2', 'B3']
            elif np.array_equal(b_check, [True, False, False]) and np.array_equal(f_check, [True, True, False]):
                moves = ['U2', 'R1', 'L2', 'B3', 'L1', 'B3', 'L3', 'B2', 'L1', 'B3', 'L1', 'R3']
        elif np.array_equal(u_check, [True, True, False, True, True, False, False, False, True]):
            if np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [False, False, False]):
                moves = ['F1', 'R3', 'F3', 'R1', 'U1', 'R1', 'U3', 'R3']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, False, True]):
                moves = ['B3', 'U2', 'B2', 'L3', 'B3', 'L1', 'B3', 'U2', 'B1']
        elif np.array_equal(u_check, [False, False, True, True, True, False, True, True, False]):
            if np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [False, False, False]):
                moves = ['R1', 'B3', 'R3', 'B1', 'U1', 'B1', 'U3', 'B3']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, False, True]):
                moves = ['L3', 'U2', 'L2', 'F3', 'L3', 'F1', 'L3', 'U2', 'L1']
        elif np.array_equal(u_check, [True, False, False, False, True, True, False, True, True]):
            if np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [False, False, False]):
                moves = ['B1', 'L3', 'B3', 'L1', 'U1', 'L1', 'U3', 'L3']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, False, True]):
                moves = ['F3', 'U2', 'F2', 'R3', 'F3', 'R1', 'F3', 'U2', 'F1']
        elif np.array_equal(u_check, [False, True, True, False, True, True, True, False, False]):
            if np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [False, False, False]):
                moves = ['L1', 'F3', 'L3', 'F1', 'U1', 'F1', 'U3', 'F3']
            elif np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, False, True]):
                moves = ['R3', 'U2', 'R2', 'B3', 'R3', 'B1', 'R3', 'U2', 'R1']
        elif np.array_equal(u_check, [False, True, False, True, True, False, False, False, True]):
            if np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [True, False, False]):
                moves = ['R3', 'U3', 'R1', 'F1', 'R3', 'F3', 'U1', 'F1', 'R1', 'F3']
            elif np.array_equal(l_check, [False, False, True]) and np.array_equal(r_check, [False, True, True]):
                moves = ['F1', 'U1', 'F3', 'R3', 'F1', 'R1', 'U3', 'R3', 'F3', 'R1']
        elif np.array_equal(u_check, [False, False, True, True, True, False, False, True, False]):
            if np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [True, False, False]):
                moves = ['B3', 'U3', 'B1', 'R1', 'B3', 'R3', 'U1', 'R1', 'B1', 'R3']
            elif np.array_equal(f_check, [False, False, True]) and np.array_equal(b_check, [False, True, True]):
                moves = ['R1', 'U1', 'R3', 'B3', 'R1', 'B1', 'U3', 'B3', 'R3', 'B1']
        elif np.array_equal(u_check, [True, False, False, False, True, True, False, True, False]):
            if np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [True, False, False]):
                moves = ['L3', 'U3', 'L1', 'B1', 'L3', 'B3', 'U1', 'B1', 'L1', 'B3']
            elif np.array_equal(r_check, [False, False, True]) and np.array_equal(l_check, [False, True, True]):
                moves = ['B1', 'U1', 'B3', 'L3', 'B1', 'L1', 'U3', 'L3', 'B3', 'L1']
        elif np.array_equal(u_check, [False, True, False, False, True, True, True, False, False]):
            if np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [True, False, False]):
                moves = ['F3', 'U3', 'F1', 'L1', 'F3', 'L3', 'U1', 'L1', 'F1', 'L3']
            elif np.array_equal(b_check, [False, False, True]) and np.array_equal(f_check, [False, True, True]):
                moves = ['L1', 'U1', 'L3', 'F3', 'L1', 'F1', 'U3', 'F3', 'L3', 'F1']
        elif np.array_equal(u_check, [False, True, False, True, True, False, True, False, True]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [True, False, True]):
                moves = ['U3', 'R1', 'U2', 'R3', 'U3', 'R1', 'U3', 'R2', 'F3', 'U3', 'F1', 'U1', 'R1']
            elif np.array_equal(b_check, [False, False, False]) and np.array_equal(f_check, [False, True, False]):
                moves = ['L2', 'U1', 'L3', 'F3', 'L1', 'U3', 'L2', 'U1', 'L1', 'F1', 'L3']
        elif np.array_equal(u_check, [False, False, True, True, True, False, False, True, True]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [True, False, True]):
                moves = ['U3', 'B1', 'U2', 'B3', 'U3', 'B1', 'U3', 'B2', 'R3', 'U3', 'R1', 'U1', 'B1']
            elif np.array_equal(l_check, [False, False, False]) and np.array_equal(r_check, [False, True, False]):
                moves = ['F2', 'U1', 'F3', 'R3', 'F1', 'U3', 'F2', 'U1', 'F1', 'R1', 'F3']
        elif np.array_equal(u_check, [True, False, True, False, True, True, False, True, False]):
            if np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [True, False, True]):
                moves = ['U3', 'L1', 'U2', 'L3', 'U3', 'L1', 'U3', 'L2', 'B3', 'U3', 'B1', 'U1', 'L1']
            elif np.array_equal(f_check, [False, False, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['R2', 'U1', 'R3', 'B3', 'R1', 'U3', 'R2', 'U1', 'R1', 'B1', 'R3']
        elif np.array_equal(u_check, [True, True, False, False, True, True, True, False, False]):
            if np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [True, False, True]):
                moves = ['U3', 'F1', 'U2', 'F3', 'U3', 'F1', 'U3', 'F2', 'L3', 'U3', 'L1', 'U1', 'F1']
            elif np.array_equal(r_check, [False, False, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['B2', 'U1', 'B3', 'L3', 'B1', 'U3', 'B2', 'U1', 'B1', 'L1', 'B3']
        elif np.array_equal(u_check, [False, True, False, True, True, False, False, False, False]):
            if np.array_equal(f_check, [False, True, True]) and np.array_equal(b_check, [True, False, False]):
                moves = ['F1', 'R1', 'U1', 'R3', 'U3', 'R1', 'U1', 'R3', 'U3', 'F3']
            elif np.array_equal(f_check, [True, True, True]) and np.array_equal(b_check, [True, False, True]):
                moves = ['L1', 'F3', 'L3', 'F1', 'U2', 'L2', 'B1', 'L1', 'B3', 'L1']
            elif np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [False, False, True]):
                moves = ['R3', 'F3', 'U3', 'F1', 'U1', 'F3', 'U3', 'F1', 'U1', 'R1']
            elif np.array_equal(r_check, [False, True, True]) and np.array_equal(l_check, [True, False, False]):
                moves = ['B3', 'R1', 'B3', 'R3', 'B2', 'U2', 'L3', 'B1', 'L1', 'B3']
            elif np.array_equal(r_check, [True, True, True]) and np.array_equal(l_check, [True, False, True]):
                moves = ['B3', 'R1', 'B1', 'R3', 'U2', 'B2', 'L3', 'B3', 'L1', 'B3']
            elif np.array_equal(b_check, [False, False, True]) and np.array_equal(f_check, [True, True, False]):
                moves = ['R1', 'U3', 'B3', 'U2', 'B3', 'U1', 'B1', 'U3', 'B1', 'U2', 'B1', 'U3', 'R3']
        elif np.array_equal(u_check, [False, False, False, True, True, False, False, True, False]):
            if np.array_equal(r_check, [False, True, True]) and np.array_equal(l_check, [True, False, False]):
                moves = ['R1', 'B1', 'U1', 'B3', 'U3', 'B1', 'U1', 'B3', 'U3', 'R3']
            elif np.array_equal(r_check, [True, True, True]) and np.array_equal(l_check, [True, False, True]):
                moves = ['F1', 'R3', 'F3', 'R1', 'U2', 'F2', 'L1', 'F1', 'L3', 'F1']
            elif np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [False, False, True]):
                moves = ['B3', 'R3', 'U3', 'R1', 'U1', 'R3', 'U3', 'R1', 'U1', 'B1']
            elif np.array_equal(b_check, [False, True, True]) and np.array_equal(f_check, [True, False, False]):
                moves = ['L3', 'B1', 'L3', 'B3', 'L2', 'U2', 'F3', 'L1', 'F1', 'L3']
            elif np.array_equal(b_check, [True, True, True]) and np.array_equal(f_check, [True, False, True]):
                moves = ['L3', 'B1', 'L1', 'B3', 'U2', 'L2', 'F3', 'L3', 'F1', 'L3']
            elif np.array_equal(l_check, [False, False, True]) and np.array_equal(r_check, [True, True, False]):
                moves = ['B1', 'U3', 'L3', 'U2', 'L3', 'U1', 'L1', 'U3', 'L1', 'U2', 'L1', 'U3', 'B3']
        elif np.array_equal(u_check, [False, False, False, False, True, True, False, True, False]):
            if np.array_equal(b_check, [False, True, True]) and np.array_equal(f_check, [True, False, False]):
                moves = ['B1', 'L1', 'U1', 'L3', 'U3', 'L1', 'U1', 'L3', 'U3', 'B3']
            elif np.array_equal(b_check, [True, True, True]) and np.array_equal(f_check, [True, False, True]):
                moves = ['R1', 'B3', 'R3', 'B1', 'U2', 'R2', 'F1', 'R1', 'F3', 'R1']
            elif np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [False, False, True]):
                moves = ['L3', 'B3', 'U3', 'B1', 'U1', 'B3', 'U3', 'B1', 'U1', 'L1']
            elif np.array_equal(l_check, [False, True, True]) and np.array_equal(r_check, [True, False, False]):
                moves = ['F3', 'L1', 'F3', 'L3', 'F2', 'U2', 'R3', 'F1', 'R1', 'F3']
            elif np.array_equal(l_check, [True, True, True]) and np.array_equal(r_check, [True, False, True]):
                moves = ['F3', 'L1', 'F1', 'L3', 'U2', 'F2', 'R3', 'F3', 'R1', 'F3']
            elif np.array_equal(f_check, [False, False, True]) and np.array_equal(b_check, [True, True, False]):
                moves = ['L1', 'U3', 'F3', 'U2', 'F3', 'U1', 'F1', 'U3', 'F1', 'U2', 'F1', 'U3', 'L3']
        elif np.array_equal(u_check, [False, True, False, False, True, True, False, False, False]):
            if np.array_equal(l_check, [False, True, True]) and np.array_equal(r_check, [True, False, False]):
                moves = ['L1', 'F1', 'U1', 'F3', 'U3', 'F1', 'U1', 'F3', 'U3', 'L3']
            elif np.array_equal(l_check, [True, True, True]) and np.array_equal(r_check, [True, False, True]):
                moves = ['B1', 'L3', 'B3', 'L1', 'U2', 'B2', 'R1', 'B1', 'R3', 'B1']
            elif np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [False, False, True]):
                moves = ['F3', 'L3', 'U3', 'L1', 'U1', 'L3', 'U3', 'L1', 'U1', 'F1']
            elif np.array_equal(f_check, [False, True, True]) and np.array_equal(b_check, [True, False, False]):
                moves = ['R3', 'F1', 'R3', 'F3', 'R2', 'U2', 'B3', 'R1', 'B1', 'R3']
            elif np.array_equal(f_check, [True, True, True]) and np.array_equal(b_check, [True, False, True]):
                moves = ['R3', 'F1', 'R1', 'F3', 'U2', 'R2', 'B3', 'R3', 'B1', 'R3']
            elif np.array_equal(r_check, [False, False, True]) and np.array_equal(l_check, [True, True, False]):
                moves = ['F1', 'U3', 'R3', 'U2', 'R3', 'U1', 'R1', 'U3', 'R1', 'U2', 'R1', 'U3', 'F3']
        elif np.array_equal(u_check, [False, True, False, False, True, True, True, False, True]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [True, False, True]):
                moves = ['U3', 'R3', 'U2', 'R1', 'U1', 'R3', 'U1', 'R2', 'B1', 'U1', 'B3', 'U3', 'R3']
            elif np.array_equal(b_check, [False, False, False]) and np.array_equal(f_check, [False, True, False]):
                moves = ['F3', 'L1', 'F3', 'L2', 'U1', 'L1', 'U1', 'L3', 'U3', 'L1', 'F2']
        elif np.array_equal(u_check, [False, True, True, True, True, False, False, False, True]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [True, False, True]):
                moves = ['U3', 'B3', 'U2', 'B1', 'U1', 'B3', 'U1', 'B2', 'L1', 'U1', 'L3', 'U3', 'B3']
            elif np.array_equal(l_check, [False, False, False]) and np.array_equal(r_check, [False, True, False]):
                moves = ['R3', 'F1', 'R3', 'F2', 'U1', 'F1', 'U1', 'F3', 'U3', 'F1', 'R2']
        elif np.array_equal(u_check, [True, False, True, True, True, False, False, True, False]):
            if np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [True, False, True]):
                moves = ['U3', 'L3', 'U2', 'L1', 'U1', 'L3', 'U1', 'L2', 'F1', 'U1', 'F3', 'U3', 'L3']
            elif np.array_equal(f_check, [False, False, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['B3', 'R1', 'B3', 'R2', 'U1', 'R1', 'U1', 'R3', 'U3', 'R1', 'B2']
        elif np.array_equal(u_check, [True, False, False, False, True, True, True, True, False]):
            if np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [True, False, True]):
                moves = ['U3', 'F3', 'U2', 'F1', 'U1', 'F3', 'U1', 'F2', 'R1', 'U1', 'R3', 'U3', 'F3']
            elif np.array_equal(r_check, [False, False, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['L3', 'B1', 'L3', 'B2', 'U1', 'B1', 'U1', 'B3', 'U3', 'B1', 'L2']
        elif np.array_equal(u_check, [False, True, True, False, True, True, False, False, False]):
            if np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [False, False, False]):
                moves = ['L1', 'F2', 'R3', 'F3', 'R1', 'F3', 'L3']
            elif np.array_equal(r_check, [False, False, False]) and np.array_equal(l_check, [False, True, True]):
                moves = ['F3', 'L2', 'B1', 'L1', 'B3', 'L1', 'F1']
        elif np.array_equal(u_check, [True, True, False, True, True, False, False, False, False]):
            if np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [False, False, False]):
                moves = ['F1', 'R2', 'B3', 'R3', 'B1', 'R3', 'F3']
            elif np.array_equal(b_check, [False, False, False]) and np.array_equal(f_check, [False, True, True]):
                moves = ['R3', 'F2', 'L1', 'F1', 'L3', 'F1', 'R1']
        elif np.array_equal(u_check, [False, False, False, True, True, False, True, True, False]):
            if np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [False, False, False]):
                moves = ['R1', 'B2', 'L3', 'B3', 'L1', 'B3', 'R3']
            elif np.array_equal(l_check, [False, False, False]) and np.array_equal(r_check, [False, True, True]):
                moves = ['B3', 'R2', 'F1', 'R1', 'F3', 'R1', 'B1']
        elif np.array_equal(u_check, [False, False, False, False, True, True, False, True, True]):
            if np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [False, False, False]):
                moves = ['B1', 'L2', 'F3', 'L3', 'F1', 'L3', 'B3']
            elif np.array_equal(f_check, [False, False, False]) and np.array_equal(b_check, [False, True, True]):
                moves = ['L3', 'B2', 'R1', 'B1', 'R3', 'B1', 'L1']
        elif np.array_equal(u_check, [True, False, False, True, True, False, False, True, False]):
            if np.array_equal(f_check, [True, False, False]) and np.array_equal(b_check, [True, True, False]):
                moves = ['L3', 'B3', 'L1', 'U3', 'R3', 'U1', 'R1', 'L3', 'B1', 'L1']
            elif np.array_equal(l_check, [False, False, True]) and np.array_equal(r_check, [False, True, True]):
                moves = ['U2', 'F3', 'B2', 'L1', 'B3', 'L1', 'B1', 'L2', 'B3', 'L1', 'F1', 'B3']
        elif np.array_equal(u_check, [False, False, False, False, True, True, True, True, False]):
            if np.array_equal(r_check, [True, False, False]) and np.array_equal(l_check, [True, True, False]):
                moves = ['F3', 'L3', 'F1', 'U3', 'B3', 'U1', 'B1', 'F3', 'L1', 'F1']
            elif np.array_equal(f_check, [False, False, True]) and np.array_equal(b_check, [False, True, True]):
                moves = ['U2', 'R3', 'L2', 'F1', 'L3', 'F1', 'L1', 'F2', 'L3', 'F1', 'R1', 'L3']
        elif np.array_equal(u_check, [False, True, False, False, True, True, False, False, True]):
            if np.array_equal(b_check, [True, False, False]) and np.array_equal(f_check, [True, True, False]):
                moves = ['R3', 'F3', 'R1', 'U3', 'L3', 'U1', 'L1', 'R3', 'F1', 'R1']
            elif np.array_equal(r_check, [False, False, True]) and np.array_equal(l_check, [False, True, True]):
                moves = ['U2', 'B3', 'F2', 'R1', 'F3', 'R1', 'F1', 'R2', 'F3', 'R1', 'B1', 'F3']
        elif np.array_equal(u_check, [False, True, True, True, True, False, False, False, False]):
            if np.array_equal(l_check, [True, False, False]) and np.array_equal(r_check, [True, True, False]):
                moves = ['B3', 'R3', 'B1', 'U3', 'F3', 'U1', 'F1', 'B3', 'R1', 'B1']
            elif np.array_equal(b_check, [False, False, True]) and np.array_equal(f_check, [False, True, True]):
                moves = ['U2', 'L3', 'R2', 'B1', 'R3', 'B1', 'R1', 'B2', 'R3', 'B1', 'L1', 'R3']

        # C
        elif np.array_equal(u_check, [True, True, False, False, True, False, True, True, False]):
            if np.array_equal(f_check, [False, False, False]) and np.array_equal(b_check, [False, False, False]):
                moves = ['R1', 'U1', 'R1', 'B3', 'R3', 'B1', 'U3', 'R3']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, True, False]):
                moves = ['F1', 'U1', 'F3', 'U3', 'R3', 'F3', 'L1', 'F1', 'L3', 'R1']
        elif np.array_equal(u_check, [False, False, False, True, True, True, True, False, True]):
            if np.array_equal(r_check, [False, False, False]) and np.array_equal(l_check, [False, False, False]):
                moves = ['B1', 'U1', 'B1', 'L3', 'B3', 'L1', 'U3', 'B3']
            elif np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['R1', 'U1', 'R3', 'U3', 'B3', 'R3', 'F1', 'R1', 'F3', 'B1']
        elif np.array_equal(u_check, [False, True, True, False, True, False, False, True, True]):
            if np.array_equal(b_check, [False, False, False]) and np.array_equal(f_check, [False, False, False]):
                moves = ['L1', 'U1', 'L1', 'F3', 'L3', 'F1', 'U3', 'L3']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['B1', 'U1', 'B3', 'U3', 'L3', 'B3', 'R1', 'B1', 'R3', 'L1']
        elif np.array_equal(u_check, [True, False, True, True, True, True, False, False, False]):
            if np.array_equal(l_check, [False, False, False]) and np.array_equal(r_check, [False, False, False]):
                moves = ['F1', 'U1', 'F1', 'R3', 'F3', 'R1', 'U3', 'F3']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, True, False]):
                moves = ['L1', 'U1', 'L3', 'U3', 'F3', 'L3', 'B1', 'L1', 'B3', 'F1']

        # L
        elif np.array_equal(u_check, [False, False, False, True, True, True, False, False, True]):
            if np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [True, True, False]):
                moves = ['R3', 'F1', 'R1', 'U1', 'R3', 'F3', 'R1', 'F1', 'U3', 'F3']
            elif np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, True]):
                moves = ['L3', 'B3', 'L1', 'R3', 'U3', 'R1', 'U1', 'L3', 'B1', 'L1']
        elif np.array_equal(u_check, [False, True, True, False, True, False, False, True, False]):
            if np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [True, True, False]):
                moves  = ['B3', 'R1', 'B1', 'U1', 'B3', 'R3', 'B1', 'R1', 'U3', 'R3']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, True]):
                moves = ['F3', 'L3', 'F1', 'B3', 'U3', 'B1', 'U1', 'F3', 'L1', 'F1']
        elif np.array_equal(u_check, [True, False, False, True, True, True, False, False, False]):
            if np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [True, True, False]):
                moves = ['L3', 'B1', 'L1', 'U1', 'L3', 'B3', 'L1', 'B1', 'U3', 'B3']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, True, True]):
                moves = ['R3', 'F3', 'R1', 'L3', 'U3', 'L1', 'U1', 'R3', 'F1', 'R1']
        elif np.array_equal(u_check, [False, True, False, False, True, False, True, True, False]):
            if np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [True, True, False]):
                moves = ['F3', 'L1', 'F1', 'U1', 'F3', 'L3', 'F1', 'L1', 'U3', 'L3']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, True, True]):
                moves = ['B3', 'R3', 'B1', 'F3', 'U3', 'F1', 'U1', 'B3', 'R1', 'B1']
        elif np.array_equal(u_check, [False, False, False, True, True, True, True, False, False]):
            if np.array_equal(f_check, [False, True, True]) and np.array_equal(b_check, [False, True, True]):
                moves = ['L1', 'F3', 'L3', 'U3', 'L1', 'F1', 'L3', 'F3', 'U1', 'F1']
            elif np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [True, True, False]):
                moves = ['R1', 'B1', 'R3', 'L1', 'U1', 'L3', 'U3', 'R1', 'B3', 'R3']
        elif np.array_equal(u_check, [False, True, False, False, True, False, False, True, True]):
            if np.array_equal(r_check, [False, True, True]) and np.array_equal(l_check, [False, True, True]):
                moves = ['F1', 'R3', 'F3', 'U3', 'F1', 'R1', 'F3', 'R3', 'U1', 'R1']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [True, True, False]):
                moves = ['B1', 'L1', 'B3', 'F1', 'U1', 'F3', 'U3', 'B1', 'L3', 'B3']
        elif np.array_equal(u_check, [False, False, True, True, True, True, False, False, False]):
            if np.array_equal(b_check, [False, True, True]) and np.array_equal(f_check, [False, True, True]):
                moves = ['R1', 'B3', 'R3', 'U3', 'R1', 'B1', 'R3', 'B3', 'U1', 'B1']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [True, True, False]):
                moves = ['L1', 'F1', 'L3', 'R1', 'U1', 'R3', 'U3', 'L1', 'F3', 'L3']
        elif np.array_equal(u_check, [True, True, False, False, True, False, False, True, False]):
            if np.array_equal(l_check, [False, True, True]) and np.array_equal(r_check, [False, True, True]):
                moves = ['B1', 'L3', 'B3', 'U3', 'B1', 'L1', 'B3', 'L3', 'U1', 'L1']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [True, True, False]):
                moves = ['F1', 'R1', 'F3', 'B1', 'U1', 'B3', 'U3', 'F1', 'R3', 'F3']

        # P
        elif np.array_equal(u_check, [True, True, False, True, True, False, True, False, False]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, False, False]):
                moves = ['F1', 'U1', 'R1', 'U3', 'R3', 'F3']
            elif np.array_equal(f_check, [False, True, True]) and np.array_equal(b_check, [True, False, False]):
                moves = ['L1', 'U1', 'F3', 'U3', 'L3', 'U1', 'L1', 'F1', 'L3']
        elif np.array_equal(u_check, [False, False, False, True, True, False, True, True, True]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, False, False]):
                moves = ['R1', 'U1', 'B1', 'U3', 'B3', 'R3']
            elif np.array_equal(r_check, [False, True, True]) and np.array_equal(l_check, [True, False, False]):
                moves = ['F1', 'U1', 'R3', 'U3', 'F3', 'U1', 'F1', 'R1', 'F3']
        elif np.array_equal(u_check, [False, False, True, False, True, True, False, True, True]):
            if np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, False, False]):
                moves = ['B1', 'U1', 'L1', 'U3', 'L3', 'B3']
            elif np.array_equal(b_check, [False, True, True]) and np.array_equal(f_check, [True, False, False]):
                moves = ['R1', 'U1', 'B3', 'U3', 'R3', 'U1', 'R1', 'B1', 'R3']
        elif np.array_equal(u_check, [True, True, True, False, True, True, False, False, False]):
            if np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, False, False]):
                moves = ['L1', 'U1', 'F1', 'U3', 'F3', 'L3']
            elif np.array_equal(l_check, [False, True, True]) and np.array_equal(r_check, [True, False, False]):
                moves = ['B1', 'U1', 'L3', 'U3', 'B3', 'U1', 'B1', 'L1', 'B3']
        elif np.array_equal(u_check, [False, True, True, False, True, True, False, False, True]):
            if np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [False, False, True]):
                moves = ['R3', 'U3', 'F1', 'U1', 'R1', 'U3', 'R3', 'F3', 'R1']
            elif np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, False, False]):
                moves = ['F3', 'U3', 'L3', 'U1', 'L1', 'F1']
        elif np.array_equal(u_check, [True, True, True, True, True, False, False, False, False]):
            if np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [False, False, True]):
                moves = ['B3', 'U3', 'R1', 'U1', 'B1', 'U3', 'B3', 'R3', 'B1']
            elif np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, False, False]):
                moves = ['R3', 'U3', 'F3', 'U1', 'F1', 'R1']
        elif np.array_equal(u_check, [True, False, False, True, True, False, True, True, False]):
            if np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [False, False, True]):
                moves = ['L3', 'U3', 'B1', 'U1', 'L1', 'U3', 'L3', 'B3', 'L1']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, False, False]):
                moves = ['B3', 'U3', 'R3', 'U1', 'R1', 'B1']
        elif np.array_equal(u_check, [False, False, False, False, True, True, True, True, True]):
            if np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [False, False, True]):
                moves = ['F3', 'U3', 'L1', 'U1', 'F1', 'U3', 'F3', 'L3', 'F1']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, False, False]):
                moves = ['L3', 'U3', 'B3', 'U1', 'B1', 'L1']

        # T
        elif np.array_equal(u_check, [False, False, True, True, True, True, False, False, True]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['F1', 'R1', 'U1', 'R3', 'U3', 'F3']
            elif np.array_equal(f_check, [True, True, False]) and np.array_equal(b_check, [False, True, True]):
                moves = ['R1', 'U1', 'R3', 'U3', 'R3', 'F1', 'R1', 'F3']
        elif np.array_equal(u_check, [True, True, True, False, True, False, False, True, False]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['R1', 'B1', 'U1', 'B3', 'U3', 'R3']
            elif np.array_equal(r_check, [True, True, False]) and np.array_equal(l_check, [False, True, True]):
                moves = ['B1', 'U1', 'B3', 'U3', 'B3', 'R1', 'B1', 'R3']
        elif np.array_equal(u_check, [True, False, False, True, True, True, True, False, False]):
            if np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, True, False]):
                moves = ['B1', 'L1', 'U1', 'L3', 'U3', 'B3']
            elif np.array_equal(b_check, [True, True, False]) and np.array_equal(f_check, [False, True, True]):
                moves = ['L1', 'U1', 'L3', 'U3', 'L3', 'B1', 'L1', 'B3']
        elif np.array_equal(u_check, [False, True, False, False, True, False, True, True, True]):
            if np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, True, False]):
                moves = ['L1', 'F1', 'U1', 'F3', 'U3', 'L3']
            elif np.array_equal(l_check, [True, True, False]) and np.array_equal(r_check, [False, True, True]):
                moves = ['F1', 'U1', 'F3', 'U3', 'F3', 'L1', 'F1', 'L3']

        # W
        elif np.array_equal(u_check, [False, False, True, False, True, True, True, True, False]):
            if np.array_equal(f_check, [False, False, True]) and np.array_equal(b_check, [False, True, False]):
                moves = ['L1', 'U1', 'L3', 'U1', 'L1', 'U3', 'L3', 'U3', 'L3', 'B1', 'L1', 'B3']
            elif np.array_equal(r_check, [True, False, False]) and np.array_equal(l_check, [False, True, False]):
                moves = ['B3', 'U3', 'B1', 'U3', 'B3', 'U1', 'B1', 'U1', 'B1', 'L3', 'B3', 'L1']
        elif np.array_equal(u_check, [True, True, False, False, True, True, False, False, True]):
            if np.array_equal(r_check, [False, False, True]) and np.array_equal(l_check, [False, True, False]):
                moves = ['F1', 'U1', 'F3', 'U1', 'F1', 'U3', 'F3', 'U3', 'F3', 'L1', 'F1', 'L3']
            elif np.array_equal(b_check, [True, False, False]) and np.array_equal(f_check, [False, True, False]):
                moves = ['L3', 'U3', 'L1', 'U3', 'L3', 'U1', 'L1', 'U1', 'L1', 'F3', 'L3', 'F1']
        elif np.array_equal(u_check, [False, True, True, True, True, False, True, False, False]):
            if np.array_equal(b_check, [False, False, True]) and np.array_equal(f_check, [False, True, False]):
                moves = ['R1', 'U1', 'R3', 'U1', 'R1', 'U3', 'R3', 'U3', 'R3', 'F1', 'R1', 'F3']
            elif np.array_equal(l_check, [True, False, False]) and np.array_equal(r_check, [False, True, False]):
                moves = ['F3', 'U3', 'F1', 'U3', 'F3', 'U1', 'F1', 'U1', 'F1', 'R3', 'F3', 'R1']
        elif np.array_equal(u_check, [True, False, False, True, True, False, False, True, True]):
            if np.array_equal(l_check, [False, False, True]) and np.array_equal(r_check, [False, True, False]):
                moves = ['B1', 'U1', 'B3', 'U1', 'B1', 'U3', 'B3', 'U3', 'B3', 'R1', 'B1', 'R3']
            elif np.array_equal(f_check, [True, False, False]) and np.array_equal(b_check, [False, True, False]):
                moves = ['R3', 'U3', 'R1', 'U3', 'R3', 'U1', 'R1', 'U1', 'R1', 'B3', 'R3', 'B1']

        # Z
        elif np.array_equal(u_check, [True, False, False, True, True, True, False, False, True]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [True, True, False]):
                moves = ['R3', 'F1', 'R1', 'U1', 'R3', 'U3', 'F3', 'U1', 'R1']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [True, True, False]):
                moves = ['L3', 'B1', 'L1', 'U1', 'L3', 'U3', 'B3', 'U1', 'L1']
        elif np.array_equal(u_check, [False, True, True, False, True, False, True, True, False]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [True, True, False]):
                moves = ['B3', 'R1', 'B1', 'U1', 'B3', 'U3', 'R3', 'U1', 'B1']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [True, True, False]):
                moves = ['F3', 'L1', 'F1', 'U1', 'F3', 'U3', 'L3', 'U1', 'F1']
        elif np.array_equal(u_check, [False, False, True, True, True, True, True, False, False]):
            if np.array_equal(f_check, [False, True, False]) and np.array_equal(b_check, [False, True, True]):
                moves = ['L1', 'F3', 'L3', 'U3', 'L1', 'U1', 'F1', 'U3', 'L3']
            elif np.array_equal(b_check, [False, True, False]) and np.array_equal(f_check, [False, True, True]):
                moves = ['R1', 'B3', 'R3', 'U3', 'R1', 'U1', 'B1', 'U3', 'R3']
        elif np.array_equal(u_check, [True, True, False, False, True, False, False, True, True]):
            if np.array_equal(r_check, [False, True, False]) and np.array_equal(l_check, [False, True, True]):
                moves = ['F1', 'R3', 'F3', 'U3', 'F1', 'U1', 'R1', 'U3', 'F3']
            elif np.array_equal(l_check, [False, True, False]) and np.array_equal(r_check, [False, True, True]):
                moves = ['B1', 'L3', 'B3', 'U3', 'B1', 'U1', 'L1', 'U3', 'B3']

        new_cube.perform_moves(moves)
        if len(new_cube.move_list) < self.shortest_moves and np.array_equal(new_cube.up_face, Y * np.ones((3, 3)).astype(int)):
            self.solve_PLL(new_cube)

    def solve_PLL(self, cube):
        edges = [YB, YR, YG, YO]
        for edge in edges:
            moves = []
            new_cube = copy.deepcopy(cube)
            edge_loc = np.argwhere(new_cube.positions == edge).squeeze()

            if edge == YB:
                if np.array_equal(edge_loc, [2, 1, 2]):
                    moves = ['U1']
                elif np.array_equal(edge_loc, [2, 0, 1]):
                    moves = ['U2']
                elif np.array_equal(edge_loc, [2, 1, 0]):
                    moves = ['U3']

                new_cube.perform_moves(moves)
                pos = new_cube.positions[2, :, :].copy().reshape(9)
                moves = []

                if np.array_equal(pos, [YGR, YG, YBR, YO, 22, YR, YBO, YB, YGO]):
                    moves = ['R3', 'F1', 'R3', 'B2', 'R1', 'F3', 'R3', 'B2', 'R2']
                elif np.array_equal(pos, [YGO, YG, YBO, YO, 22, YR, YBR, YB, YGR]):
                    moves = ['R1', 'B3', 'R1', 'F2', 'R3', 'B1', 'R1', 'F2', 'R2']
                elif np.array_equal(pos, [YBO, YR, YGO, YO, 22, YG, YBR, YB, YGR]):
                    moves = ['U3', 'R2', 'U1', 'R1', 'U1', 'R3', 'U3', 'R3', 'U3', 'R3', 'U1', 'R3']
                elif np.array_equal(pos, [YGR, YO, YBR, YG, 22, YR, YGO, YB, YBO]):
                    moves = ['U1', 'R1', 'U3', 'R1', 'U1', 'R1', 'U1', 'R1', 'U3', 'R3', 'U3', 'R2']
                elif np.array_equal(pos, [YBR, YG, YBO, YO, 22, YR, YGR, YB, YGO]):
                    moves = ['U2', 'R2', 'L2', 'D1', 'R2', 'L2', 'U2', 'R2', 'L2', 'D1', 'R2', 'L2']
                elif np.array_equal(pos, [YGO, YG, YBR, YR, 22, YO, YBO, YB, YGR]):
                    moves = ['R1', 'U1', 'R3', 'U3', 'R3', 'F1', 'R2', 'U3', 'R3', 'U3', 'R1', 'U1', 'R3', 'F3']
                elif np.array_equal(pos, [YGR, YO, YGO, YG, 22, YR, YBO, YB, YBR]):
                    moves = ['R3', 'U1', 'L3', 'U2', 'R1', 'U3', 'R3', 'U2', 'R1', 'L1', 'U3']
                elif np.array_equal(pos, [YBO, YO, YGO, YR, 22, YG, YGR, YB, YBR]):
                    moves = ['U3', 'R1', 'U1', 'R3', 'F3', 'R1', 'U1', 'R3', 'U3', 'R3', 'F1', 'R2', 'U3', 'R3', 'U3']
                elif np.array_equal(pos, [YGO, YR, YBR, YG, 22, YO, YGR, YB, YBO]):
                    moves = ['U1', 'L1', 'U2', 'L3', 'U2', 'L1', 'F3', 'L3', 'U3', 'L1', 'U1', 'L1', 'F1', 'L2', 'U1']
                elif np.array_equal(pos, [YBO, YO, YGR, YR, 22, YG, YBR, YB, YGO]):
                    moves = ['U3', 'R3', 'U2', 'R1', 'U2', 'R3', 'F1', 'R1', 'U1', 'R3', 'U3', 'R3', 'F3', 'R2', 'U3']
                elif np.array_equal(pos, [YBR, YR, YGR, YO, 22, YG, YBO, YB, YGO]):
                    moves = ['R3', 'U1', 'R3', 'U3', 'B3', 'R3', 'B2', 'U3', 'B3', 'U1', 'B3', 'R1', 'B1', 'R1']
                elif np.array_equal(pos, [YGR, YO, YBO, YR, 22, YG, YGO, YB, YBR]):
                    moves = ['R2', 'D1', 'B3', 'U1', 'B3', 'U3', 'B1', 'D3', 'R2', 'F3', 'U1', 'F1']
                elif np.array_equal(pos, [YGO, YO, YBR, YR, 22, YG, YGR, YB, YBO]):
                    moves = ['U2', 'R3', 'U3', 'R1', 'B2', 'D1', 'L3', 'U1', 'L1', 'U3', 'L1', 'D3', 'B2']
                elif np.array_equal(pos, [YBR, YR, YBO, YO, 22, YG, YGO, YB, YGR]):
                    moves = ['U3', 'R2', 'D3', 'F1', 'U3', 'F1', 'U1', 'F3', 'D1', 'R2', 'B1', 'U3', 'B3']
                elif np.array_equal(pos, [YBO, YR, YBR, YO, 22, YG, YGR, YB, YGO]):
                    moves = ['U1', 'R1', 'U1', 'R3', 'F2', 'D3', 'L1', 'U3', 'L3', 'U1', 'L3', 'D1', 'F2']
                elif np.array_equal(pos, [YGO, YG, YGR, YR, 22, YO, YBR, YB, YBO]):
                    moves = ['R3', 'U2', 'R3', 'U3', 'B3', 'R3', 'B2', 'U3', 'B3', 'U1', 'B3', 'R1', 'B1', 'U3', 'R1']
                elif np.array_equal(pos, [YBO, YG, YGO, YR, 22, YO, YBR, YB, YGR]):
                    moves = ['U3', 'R2', 'L2', 'D1', 'R2', 'L2', 'U1', 'R3', 'L1', 'F2', 'R2', 'L2', 'B2', 'R3', 'L1', 'U2']
                elif np.array_equal(pos, [YBR, YO, YGR, YG, 22, YR, YBO, YB, YGO]):
                    moves = ['F1', 'R1', 'U3', 'R3', 'U3', 'R1', 'U1', 'R3', 'F3', 'R1', 'U1', 'R3', 'U3', 'R3', 'F1', 'R1', 'F3']
                elif np.array_equal(pos, [YGO, YG, YBO, YR, 22, YO, YGR, YB, YBR]):
                    moves = ['U2', 'L1', 'U3', 'R1', 'U2', 'L3', 'U1', 'R3', 'L1', 'U3', 'R1', 'U2', 'L3', 'U1', 'R3', 'U1']
                elif np.array_equal(pos, [YBR, YG, YGR, YR, 22, YO, YBO, YB, YGO]):
                    moves = ['U2', 'R3', 'U1', 'L3', 'U2', 'R1', 'U3', 'L1', 'R3', 'U1', 'L3', 'U2', 'R1', 'U3', 'L1', 'U3']
                elif np.array_equal(pos, [YBO, YG, YBR, YO, 22, YR, YGO, YB, YGR]):
                    moves = ['R1', 'B3', 'R3', 'F1', 'R1', 'B1', 'R3', 'F2', 'L3', 'B1', 'L1', 'F1', 'L3', 'B3', 'L1']

            elif edge == YR:
                if np.array_equal(edge_loc, [2, 0, 1]):
                    moves = ['U1']
                elif np.array_equal(edge_loc, [2, 1, 0]):
                    moves = ['U2']
                elif np.array_equal(edge_loc, [2, 2, 1]):
                    moves = ['U3']

                new_cube.perform_moves(moves)
                pos = new_cube.positions[2, :, :].copy()
                pos = np.rot90(pos, 3).reshape(9)
                moves = []

                if np.array_equal(pos, [YGO, YO, YGR, YB, 22, YG, YBR, YR, YBO]):
                    moves = ['B3', 'R1', 'B3', 'L2', 'B1', 'R3', 'B3', 'L2', 'B2']
                elif np.array_equal(pos, [YBO, YO, YBR, YB, 22, YG, YGR, YR, YGO]):
                    moves = ['B1', 'L3', 'B1', 'R2', 'B3', 'L1', 'B1', 'R2', 'B2']
                elif np.array_equal(pos, [YBR, YG, YBO, YB, 22, YO, YGR, YR, YGO]):
                    moves = ['U3', 'B2', 'U1', 'B1', 'U1', 'B3', 'U3', 'B3', 'U3', 'B3', 'U1', 'B3']
                elif np.array_equal(pos, [YGO, YB, YGR, YO, 22, YG, YBO, YR, YBR]):
                    moves = ['U1', 'B1', 'U3', 'B1', 'U1', 'B1', 'U1', 'B1', 'U3', 'B3', 'U3', 'B2']
                elif np.array_equal(pos, [YGR, YO, YBR, YB, 22, YG, YGO, YR, YBO]):
                    moves = ['U2', 'B2', 'F2', 'D1', 'B2', 'F2', 'U2', 'B2', 'F2', 'D1', 'B2', 'F2']
                elif np.array_equal(pos, [YBO, YO, YGR, YG, 22, YB, YBR, YR, YGO]):
                    moves = ['B1', 'U1', 'B3', 'U3', 'B3', 'R1', 'B2', 'U3', 'B3', 'U3', 'B1', 'U1', 'B3', 'R3']
                elif np.array_equal(pos, [YGO, YB, YBO, YO, 22, YG, YBR, YR, YGR]):
                    moves = ['B3', 'U1', 'F3', 'U2', 'B1', 'U3', 'B3', 'U2', 'B1', 'F1', 'U3']
                elif np.array_equal(pos, [YBR, YB, YBO, YG, 22, YO, YGO, YR, YGR]):
                    moves = ['U3', 'B1', 'U1', 'B3', 'R3', 'B1', 'U1', 'B3', 'U3', 'B3', 'R1', 'B2', 'U3', 'B3', 'U3']
                elif np.array_equal(pos, [YBO, YG, YGR, YO, 22, YB, YGO, YR, YBR]):
                    moves = ['U1', 'F1', 'U2', 'F3', 'U2', 'F1', 'R3', 'F3', 'U3', 'F1', 'U1', 'F1', 'R1', 'F2', 'U1']
                elif np.array_equal(pos, [YBR, YB, YGO, YG, 22, YO, YGR, YR, YBO]):
                    moves = ['U3', 'B3', 'U2', 'B1', 'U2', 'B3', 'R1', 'B1', 'U1', 'B3', 'U3', 'B3', 'R3', 'B2', 'U3']
                elif np.array_equal(pos, [YGR, YG, YGO, YB, 22, YO, YBR, YR, YBO]):
                    moves = ['B3', 'U1', 'B3', 'U3', 'L3', 'B3', 'L2', 'U3', 'L3', 'U1', 'L3', 'B1', 'L1', 'B1']
                elif np.array_equal(pos, [YGO, YB, YBR, YG, 22, YO, YBO, YR, YGR]):
                    moves = ['B2', 'D1', 'L3', 'U1', 'L3', 'U3', 'L1', 'D3', 'B2', 'R3', 'U1', 'R1']
                elif np.array_equal(pos, [YBO, YB, YGR, YG, 22, YO, YGO, YR, YBR]):
                    moves = ['U2', 'B3', 'U3', 'B1', 'L2', 'D1', 'F3', 'U1', 'F1', 'U3', 'F1', 'D3', 'L2']
                elif np.array_equal(pos, [YGR, YG, YBR, YB, 22, YO, YBO, YR, YGO]):
                    moves = ['U3', 'B2', 'D3', 'R1', 'U3', 'R1', 'U1', 'R3', 'D1', 'B2', 'L1', 'U3', 'L3']
                elif np.array_equal(pos, [YBR, YG, YGR, YB, 22, YO, YGO, YR, YBO]):
                    moves = ['U1', 'B1', 'U1', 'B3', 'R2', 'D3', 'F1', 'U3', 'F3', 'U1', 'F3', 'D1', 'R2']
                elif np.array_equal(pos, [YBO, YO, YGO, YG, 22, YB, YGR, YR, YBR]):
                    moves = ['B3', 'U2', 'B3', 'U3', 'L3', 'B3', 'L2', 'U3', 'L3', 'U1', 'L3', 'B1', 'L1', 'U3', 'B1']
                elif np.array_equal(pos, [YBR, YO, YBO, YG, 22, YB, YGR, YR, YGO]):
                    moves = ['U3', 'B2', 'F2', 'D1', 'B2', 'F2', 'U1', 'B3', 'F1', 'R2', 'B2', 'F2', 'L2', 'B3', 'F1', 'U2']
                elif np.array_equal(pos, [YGR, YB, YGO, YO, 22, YG, YBR, YR, YBO]):
                    moves = ['R1', 'B1', 'U3', 'B3', 'U3', 'B1', 'U1', 'B3', 'R3', 'B1', 'U1', 'B3', 'U3', 'B3', 'R1', 'B1',
                         'R3']
                elif np.array_equal(pos, [YBO, YO, YBR, YG, 22, YB, YGO, YR, YGR]):
                    moves = ['U2', 'F1', 'U3', 'B1', 'U2', 'F3', 'U1', 'B3', 'F1', 'U3', 'B1', 'U2', 'F3', 'U1', 'B3',
                         'U1']
                elif np.array_equal(pos, [YGR, YO, YGO, YG, 22, YB, YBR, YR, YBO]):
                    moves = ['U2', 'B3', 'U1', 'F3', 'U2', 'B1', 'U3', 'F1', 'B3', 'U1', 'F3', 'U2', 'B1', 'U3', 'F1',
                         'U3']
                elif np.array_equal(pos, [YBR, YO, YGR, YB, 22, YG, YBO, YR, YGO]):
                    moves = ['B1', 'L3', 'B3', 'R1', 'B1', 'L1', 'B3', 'R2', 'F3', 'L1', 'F1', 'R1', 'F3', 'L3', 'F1']

            elif edge == YG:
                if np.array_equal(edge_loc, [2, 1, 0]):
                    moves = ['U1']
                elif np.array_equal(edge_loc, [2, 2, 1]):
                    moves = ['U2']
                elif np.array_equal(edge_loc, [2, 1, 2]):
                    moves = ['U3']

                new_cube.perform_moves(moves)
                pos = new_cube.positions[2, :, :].copy()
                pos = np.rot90(pos, 2).reshape(9)
                moves = []

                if np.array_equal(pos, [YBO, YB, YGO, YR, 22, YO, YGR, YG, YBR]):
                    moves = ['L3', 'B1', 'L3', 'F2', 'L1', 'B3', 'L3', 'F2', 'L2']
                elif np.array_equal(pos, [YBR, YB, YGR, YR, 22, YO, YGO, YG, YBO]):
                    moves = ['L1', 'F3', 'L1', 'B2', 'L3', 'F1', 'L1', 'B2', 'L2']
                elif np.array_equal(pos, [YGR, YO, YBR, YR, 22, YB, YGO, YG, YBO]):
                    moves = ['U3', 'L2', 'U1', 'L1', 'U1', 'L3', 'U3', 'L3', 'U3', 'L3', 'U1', 'L3']
                elif np.array_equal(pos, [YBO, YR, YGO, YB, 22, YO, YBR, YG, YGR]):
                    moves = ['U1', 'L1', 'U3', 'L1', 'U1', 'L1', 'U1', 'L1', 'U3', 'L3', 'U3', 'L2']
                elif np.array_equal(pos, [YGO, YB, YGR, YR, 22, YO, YBO, YG, YBR]):
                    moves = ['U2', 'L2', 'R2', 'D1', 'L2', 'R2', 'U2', 'L2', 'R2', 'D1', 'L2', 'R2']
                elif np.array_equal(pos, [YBR, YB, YGO, YO, 22, YR, YGR, YG, YBO]):
                    moves = ['L1', 'U1', 'L3', 'U3', 'L3', 'B1', 'L2', 'U3', 'L3', 'U3', 'L1', 'U1', 'L3', 'B3']
                elif np.array_equal(pos, [YBO, YR, YBR, YB, 22, YO, YGR, YG, YGO]):
                    moves = ['L3', 'U1', 'R3', 'U2', 'L1', 'U3', 'L3', 'U2', 'L1', 'R1', 'U3']
                elif np.array_equal(pos, [YGR, YR, YBR, YO, 22, YB, YBO, YG, YGO]):
                    moves = ['U3', 'L1', 'U1', 'L3', 'B3', 'L1', 'U1', 'L3', 'U3', 'L3', 'B1', 'L2', 'U3', 'L3', 'U3']
                elif np.array_equal(pos, [YBR, YO, YGO, YB, 22, YR, YBO, YG, YGR]):
                    moves = ['U1', 'R1', 'U2', 'R3', 'U2', 'R1', 'B3', 'R3', 'U3', 'R1', 'U1', 'R1', 'B1', 'R2', 'U1']
                elif np.array_equal(pos, [YGR, YR, YBO, YO, 22, YB, YGO, YG, YBR]):
                    moves = ['U3', 'L3', 'U2', 'L1', 'U2', 'L3', 'B1', 'L1', 'U1', 'L3', 'U3', 'L3', 'B3', 'L2', 'U3']
                elif np.array_equal(pos, [YGO, YO, YBO, YR, 22, YB, YGR, YG, YBR]):
                    moves = ['L3', 'U1', 'L3', 'U3', 'F3', 'L3', 'F2', 'U3', 'F3', 'U1', 'F3', 'L1', 'F1', 'L1']
                elif np.array_equal(pos, [YBO, YR, YGR, YO, 22, YB, YBR, YG, YGO]):
                    moves = ['L2', 'D1', 'F3', 'U1', 'F3', 'U3', 'F1', 'D3', 'L2', 'B3', 'U1', 'B1']
                elif np.array_equal(pos, [YBR, YR, YGO, YO, 22, YB, YBO, YG, YGR]):
                    moves = ['U2', 'L3', 'U3', 'L1', 'F2', 'D1', 'R3', 'U1', 'R1', 'U3', 'R1', 'D3', 'F2']
                elif np.array_equal(pos, [YGO, YO, YGR, YR, 22, YB, YBR, YG, YBO]):
                    moves = ['U3', 'L2', 'D3', 'B1', 'U3', 'B1', 'U1', 'B3', 'D1', 'L2', 'F1', 'U3', 'F3']
                elif np.array_equal(pos, [YGR, YO, YGO, YR, 22, YB, YBO, YG, YBR]):
                    moves = ['U1', 'L1', 'U1', 'L3', 'B2', 'D3', 'R1', 'U3', 'R3', 'U1', 'R3', 'D1', 'B2']
                elif np.array_equal(pos, [YBR, YB, YBO, YO, 22, YR, YGO, YG, YGR]):
                    moves = ['L3', 'U2', 'L3', 'U3', 'F3', 'L3', 'F2', 'U3', 'F3', 'U1', 'F3', 'L1', 'F1', 'U3', 'L1']
                elif np.array_equal(pos, [YGR, YB, YBR, YO, 22, YR, YGO, YG, YBO]):
                    moves = ['U3', 'L2', 'R2', 'D1', 'L2', 'R2', 'U1', 'L3', 'R1', 'B2', 'L2', 'R2', 'F2', 'L3', 'R1',
                         'U2']
                elif np.array_equal(pos, [YGO, YR, YBO, YB, 22, YO, YGR, YG, YBR]):
                    moves = ['B1', 'L1', 'U3', 'L3', 'U3', 'L1', 'U1', 'L3', 'B3', 'L1', 'U1', 'L3', 'U3', 'L3', 'B1', 'L1',
                         'B3']
                elif np.array_equal(pos, [YBR, YB, YGR, YO, 22, YR, YBO, YG, YGO]):
                    moves = ['U2', 'R1', 'U3', 'L1', 'U2', 'R3', 'U1', 'L3', 'R1', 'U3', 'L1', 'U2', 'R3', 'U1', 'L3',
                         'U1']
                elif np.array_equal(pos, [YGO, YB, YBO, YO, 22, YR, YGR, YG, YBR]):
                    moves = ['U2', 'L3', 'U1', 'R3', 'U2', 'L1', 'U3', 'R1', 'L3', 'U1', 'R3', 'U2', 'L1', 'U3', 'R1',
                         'U3']
                elif np.array_equal(pos, [YGR, YB, YGO, YR, 22, YO, YBR, YG, YBO]):
                    moves = ['L1', 'F3', 'L3', 'B1', 'L1', 'F1', 'L3', 'B2', 'R3', 'F1', 'R1', 'B1', 'R3', 'F3', 'R1']

            elif edge == YO:
                if np.array_equal(edge_loc, [2, 2, 1]):
                    moves = ['U1']
                elif np.array_equal(edge_loc, [2, 1, 2]):
                    moves = ['U2']
                elif np.array_equal(edge_loc, [2, 0, 1]):
                    moves = ['U3']

                new_cube.perform_moves(moves)
                pos = new_cube.positions[2, :, :].copy()
                pos = np.rot90(pos, 2).reshape(9)
                moves = []

                if np.array_equal(pos, [YBR, YR, YBO, YG, 22, YB, YGO, YO, YGR]):
                    moves = ['F3', 'L1', 'F3', 'R2', 'F1', 'L3', 'F3', 'R2', 'F2']
                elif np.array_equal(pos, [YGR, YR, YGO, YG, 22, YB, YBO, YO, YBR]):
                    moves = ['F1', 'R3', 'F1', 'L2', 'F3', 'R1', 'F1', 'L2', 'F2']
                elif np.array_equal(pos, [YGO, YB, YGR, YG, 22, YR, YBO, YO, YBR]):
                    moves = ['U3', 'F2', 'U1', 'F1', 'U1', 'F3', 'U3', 'F3', 'U3', 'F3', 'U1', 'F3']
                elif np.array_equal(pos, [YBR, YG, YBO, YR, 22, YB, YGR, YO, YGO]):
                    moves = ['U1', 'F1', 'U3', 'F1', 'U1', 'F1', 'U1', 'F1', 'U3', 'F3', 'U3', 'F2']
                elif np.array_equal(pos, [YBO, YR, YGO, YG, 22, YB, YBR, YO, YGR]):
                    moves = ['U2', 'F2', 'B2', 'D1', 'F2', 'B2', 'U2', 'F2', 'B2', 'D1', 'F2', 'B2']
                elif np.array_equal(pos, [YGR, YR, YBO, YB, 22, YG, YGO, YO, YBR]):
                    moves = ['F1', 'U1', 'F3', 'U3', 'F3', 'L1', 'F2', 'U3', 'F3', 'U3', 'F1', 'U1', 'F3', 'L3']
                elif np.array_equal(pos, [YBR, YG, YGR, YR, 22, YB, YGO, YO, YBO]):
                    moves = ['F3', 'U1', 'B3', 'U2', 'F1', 'U3', 'F3', 'U2', 'F1', 'B1', 'U3']
                elif np.array_equal(pos, [YGO, YG, YGR, YB, 22, YR, YBR, YO, YBO]):
                    moves = ['U3', 'F1', 'U1', 'F3', 'L3', 'F1', 'U1', 'F3', 'U3', 'F3', 'L1', 'F2', 'U3', 'F3', 'U3']
                elif np.array_equal(pos, [YGR, YB, YBO, YR, 22, YG, YBR, YO, YGO]):
                    moves = ['U1', 'B1', 'U2', 'B3', 'U2', 'B1', 'L3', 'B3', 'U3', 'B1', 'U1', 'B1', 'L1', 'B2', 'U1']
                elif np.array_equal(pos, [YGO, YG, YBR, YB, 22, YR, YBO, YO, YGR]):
                    moves = ['U3', 'F3', 'U2', 'F1', 'U2', 'F3', 'L1', 'F1', 'U1', 'F3', 'U3', 'F3', 'L3', 'F2', 'U3']
                elif np.array_equal(pos, [YBO, YB, YBR, YG, 22, YR, YGO, YO, YGR]):
                    moves = ['F3', 'U1', 'F3', 'U3', 'R3', 'F3', 'R2', 'U3', 'R3', 'U1', 'R3', 'F1', 'R1', 'F1']
                elif np.array_equal(pos, [YBR, YG, YGO, YB, 22, YR, YGR, YO, YBO]):
                    moves = ['F2', 'D1', 'R3', 'U1', 'R3', 'U3', 'R1', 'D3', 'F2', 'L3', 'U1', 'L1']
                elif np.array_equal(pos, [YGR, YG, YBO, YB, 22, YR, YBR, YO, YGO]):
                    moves = ['U2', 'F3', 'U3', 'F1', 'R2', 'D1', 'B3', 'U1', 'B1', 'U3', 'B1', 'D3', 'R2']
                elif np.array_equal(pos, [YBO, YB, YGO, YG, 22, YR, YGR, YO, YBR]):
                    moves = ['U3', 'F2', 'D3', 'L1', 'U3', 'L1', 'U1', 'L3', 'D1', 'F2', 'R1', 'U3', 'R3']
                elif np.array_equal(pos, [YGO, YB, YBO, YG, 22, YR, YBR, YO, YGR]):
                    moves = ['U1', 'F1', 'U1', 'F3', 'L2', 'D3', 'B1', 'U3', 'B3', 'U1', 'B3', 'D1', 'L2']
                elif np.array_equal(pos, [YGR, YR, YBR, YB, 22, YG, YBO, YO, YGO]):
                    moves = ['F3', 'U2', 'F3', 'U3', 'R3', 'F3', 'R2', 'U3', 'R3', 'U1', 'R3', 'F1', 'R1', 'U3', 'F1']
                elif np.array_equal(pos, [YGO, YR, YGR, YB, 22, YG, YBO, YO, YBR]):
                    moves = ['U3', 'F2', 'B2', 'D1', 'F2', 'B2', 'U1', 'F3', 'B1', 'L2', 'F2', 'B2', 'R2', 'F3', 'B1',
                         'U2']
                elif np.array_equal(pos, [YBO, YG, YBR, YR, 22, YB, YGO, YO, YGR]):
                    moves = ['L1', 'F1', 'U3', 'F3', 'U3', 'F1', 'U1', 'F3', 'L3', 'F1', 'U1', 'F3', 'U3', 'F3', 'L1', 'F1',
                         'L3']
                elif np.array_equal(pos, [YGR, YR, YGO, YB, 22, YG, YBR, YO, YBO]):
                    moves = ['U2', 'B1', 'U3', 'F1', 'U2', 'B3', 'U1', 'F3', 'B1', 'U3', 'F1', 'U2', 'B3', 'U1', 'F3',
                         'U1']
                elif np.array_equal(pos, [YBO, YR, YBR, YB, 22, YG, YGO, YO, YGR]):
                    moves = ['U2', 'F3', 'U1', 'B3', 'U2', 'F1', 'U3', 'B1', 'F3', 'U1', 'B3', 'U2', 'F1', 'U3', 'B1',
                         'U3']
                elif np.array_equal(pos, [YGO, YR, YBO, YG, 22, YB, YGR, YO, YBR]):
                    moves = ['F1', 'R3', 'F3', 'L1', 'F1', 'R1', 'F3', 'L2', 'B3', 'R1', 'B1', 'L1', 'B3', 'R3', 'B1']

            new_cube.perform_moves(moves)
            if new_cube.front_face[0, 1] == O:
                new_cube.perform_moves(['U1'])
            elif new_cube.front_face[0, 1] == G:
                new_cube.perform_moves(['U2'])
            elif new_cube.front_face[0, 1] == R:
                new_cube.perform_moves(['U3'])

            if new_cube.is_solved() and len(new_cube.move_list) < self.shortest_moves:
                self.best_move_list = swap_moves(new_cube.move_list, self.colour_code).copy()
                self.shortest_moves = len(new_cube.move_list)


if __name__ == "__main__":
    cube = Rubiks_Cube()
    solver = Solver()

    cube.scramble()
    moves = solver.solve(cube)
    print(moves)
    cube.perform_moves(moves)
    print(cube.is_solved())
