import numpy as np

# Created by my good friend Tony Liu: https://github.com/Tony-xy-Liu

class Section:
    def __init__(self, type: str, values: list[tuple[int, int, int]]) -> None:
        self.type = type
        self.values = values

    def __repr__(self) -> str:
        return f'{self.type}:{self.values}'

class Board:
    def __init__(self, board: np.ndarray|list[list[int]]|None=None) -> None:
        self._board = np.array(board)
        w, h = self._board.shape
        assert w == h
        self._l = w
        sl = np.sqrt(w)
        assert sl % 1 == 0
        self._sl, sl = int(sl), int(sl)

        self.rows: list[Section] = []
        for y in range(w):
            s = Section("row", [(x, y, v) for x, v in enumerate(self._board[:, y])])
            self.rows.append(s)
        
        self.cols: list[Section] = []
        for x in range(w):
            s = Section("col", [(x, y, v) for y, v in enumerate(self._board[x, :])])
            self.cols.append(s)

        def _iter_sec(xo: int, yo: int):
            vals = []
            for i in range(sl):
                for j in range(sl):
                    x = j+xo
                    y = i+yo
                    vals.append((x, y, self._board[x, y]))
            return Section("sqr", vals)

        self.sqrs: dict[tuple[int, int], Section] = {}
        for sx in range(sl):
            x_off = sx*sl
            for sy in range(sl):
                y_off = sy*sl
                self.sqrs[(sx, sy)] = _iter_sec(x_off, y_off)

    def GetRelated(self, x:int, y:int):
        r = self.rows[x]
        c = self.cols[y]
        s = self.sqrs[(x//self._sl, y//self._sl)]
        return r, c, s

    def Iterate(self):
        for row in self.rows:
            for x, y, val in row.values:
                yield x, y, val