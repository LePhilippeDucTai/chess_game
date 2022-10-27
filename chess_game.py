import itertools as it

import numpy as np

N = 8


def is_in_grid(position):
    x, y = position
    return (0 <= x < N) and (0 <= y < N)


def it_compute_positions(x, y, deltas):
    return map(lambda p: (x + p[0], y + p[1]), deltas)


class ChessPiece:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.deltas = self.piece_deltas()

    def piece_deltas():
        pass

    def possible_moves(self):
        x, y = self.position
        new_positions = it_compute_positions(x, y, self.deltas)
        filtred = filter(is_in_grid, new_positions)
        return list(filtred)


class Knight(ChessPiece):
    def __init__(self, position, color):
        super().__init__(position, color)

    @staticmethod
    def piece_deltas():
        move = [-2, -1, 1, 2]
        all_positions = it.product(move, move)
        positions = filter(lambda tup: sum(map(abs, tup)) == 3, all_positions)
        return list(positions)

    def __repr__(self):
        return str(1)


class Tower(ChessPiece):
    def __init__(self, position, color):
        super().__init__(position, color)

    @staticmethod
    def piece_deltas():
        right = zip(range(1, N), [0] * N)
        left = zip(range(-N + 1, 0), [0] * N)
        up = zip([0] * N, range(1, N))
        down = zip([0] * N, range(-N + 1, 0))
        moves = it.chain(up, down, left, right)
        return list(moves)

    def __repr__(self):
        return str(2)


class Bishop(ChessPiece):
    def __init__(self, position, color):
        super().__init__(position, color)

    @staticmethod
    def piece_deltas():
        move = range(-N + 1, N)
        anti_move = range(N - 1, -N, -1)
        diagonal = zip(move, move)
        inverse_diagonal = zip(anti_move, move)
        all_diagonals = it.chain(diagonal, inverse_diagonal)
        filter_null = filter(lambda p: p != (0, 0), all_diagonals)
        return list(filter_null)

    def __repr__(self):
        return str(3)


class ChessGrid:
    def __init__(self, pieces):
        self.pieces = pieces

    def __repr__(self):
        grid = np.zeros((N, N), dtype="int")
        for piece in self.pieces:
            grid[piece.position] = str(piece)
        return str(np.array(grid))
    
def main():
    knight = Knight((1, 1), 1)
    tower = Tower((5, 5), 1)
    bishop = Bishop((3, 3), 1)
    grid = ChessGrid([knight, tower, bishop])

    print(knight.possible_moves())
    print(bishop.possible_moves())
    print(grid)


if __name__ == "__main__":
    main()