import random


class Buscaminas():
    def __init__(self, rows=None, cols=None, bombs=None):
        self.board = []
        self.rows = rows
        self.cols = cols
        for i in range(0, rows):
            v = [" "]*cols
            self.board.append(v)
        mi = 1
        while mi <= bombs:
            fil = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            if " " in self.board[fil][col]:
                self.board[fil][col] = "B"
                mi += 1
        
        for x in range(rows):
            for y in range(cols):
                if self.board[x][y] != "B":
                    count = []
                    for a in (1,0,-1):
                        for b in (1,0,-1):
                            try:
                                if not ((a == 0 and b == 0) or (x +  a < 0 or y + b < 0)):
                                    count.append(self.board[x + a][y + b])
                            except Exception:
                                continue
                        if count.count("B") != 0:
                            self.board[x][y] = str(count.count("B")) 
                        else:
                            " "
        
    
    def play(self):
        pass

    def show_board(self):
        pass

    def show_board(self):
        pass

    def question(self, movs):
        self.move = movs
        movs = ["flag", "uncover"]

        while True:
            mov = input("Elegir Movimiento:\n1) Flag 2) Uncover\n")
            if mov not in ("flag", "uncover"):
                raise Exception()
            else:
                break

        while True:
            row = input("Ingrese la fila a cambiar: ")
            if str(row) not in [str(x) for x in range(self.rows)]:
                raise Exception()
            else:
                row = int(row)
                break

        while True:
            col = input("Ingrese la columna a cambiar: ")
            if str(col) not in [str(x) for x in range(self.cols)]:
                raise Exception()
            else:
                col = int(col)
                break

        return [mov, row, col]

    def win(self):
        count = 1
        for x in range(len(self.board)):
            if "F" in self.board[x]:
                count += 1
                print(count)
        if count != 9:
            return True
        return False

    def lose(self):
        for i in range(len(self.board)):
            if i in self.board[i] == "B":
                return False
            return True