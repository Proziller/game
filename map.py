import tkinter as tk
import models as m

class GameMap:
    def __init__(self, size):
        self.size = size
        self.gamemap = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.tiles = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.highlighted_tiles = []

        self.pla = m.roboter(True, "X", 1, 1, 1)
        self.plalook = self.pla.look
        self.click_player = False

        self.entity1 = m.roboter(False, "O", 2, 2, 2)

        self.gamemap[self.pla.y][self.pla.x] = self.pla
        self.gamemap[self.entity1.y][self.entity1.x] = self.entity1

        self.setup()


    def move_player(self, x, y):
        self.clear_highlights()

        if self.gamemap[y][x] is self.pla:
            self.tiles[y][x].config(bg="green")
            self.click_player = True

            reach = self.pla.reach
            for dy in range(-reach, reach + 1):
                for dx in range(-reach, reach + 1):
                    nx, ny = self.pla.x + dx, self.pla.y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size and self.gamemap[ny][nx] is None:
                        self.tiles[ny][nx].config(bg="light blue")
                        self.highlighted_tiles.append((nx, ny))

        elif self.click_player:
            if self.gamemap[y][x] is None:
                move_result = self.pla.move(x, y)

                if move_result["T"]:
                    old_x, old_y = move_result["x"], move_result["y"]
                    self.update_tile(old_x, old_y, "", "light green")

                    self.gamemap[old_y][old_x] = None
                    self.gamemap[y][x] = self.pla

                    self.update_tile(x, y, self.pla.look, "blue")

            elif isinstance(self.gamemap[y][x], m.roboter):
                self.player_change(self.gamemap[y][x])

            self.click_player = False
            self.clear_highlights()
            self.refresh_map()


    def player_change(self, enemy):
        px, py = self.pla.x, self.pla.y  # Player's position
        ex, ey = enemy.x, enemy.y  # Enemy's position

        if abs(px - ex) <= 1 and abs(py - ey) <= 1:  # Ensure adjacency

            # Swap objects, fully exchanging player and enemy models
            self.pla, self.entity1 = enemy, self.pla  # Swap player and enemy completely

            # Update their positions correctly
            self.pla.x, self.pla.y = ex, ey  # Player moves to enemy's old position
            self.entity1.x, self.entity1.y = px, py  # Enemy moves to player's old position

            # Update the game map accordingly
            self.gamemap[py][px] = self.entity1  # Old player is now an enemy
            self.gamemap[ey][ex] = self.pla  # New player (was enemy)

            # Update the visuals (ensure the swapped looks are applied)
            self.update_tile(px, py, self.entity1.look, "red")  # Former player (now enemy)
            self.update_tile(ex, ey, self.pla.look, "blue")  # Former enemy (now player)

            self.clear_highlights()
            self.refresh_map()


    def attack(self, x, y):
        pass


    def update_tile(self, x, y, text, color):
        self.tiles[y][x].config(text=text, bg=color)


    def clear_highlights(self):
        for hx, hy in self.highlighted_tiles:
            self.tiles[hy][hx].config(bg="light green")
        self.highlighted_tiles = []


    def refresh_map(self):
        for y in range(self.size):
            for x in range(self.size):
                entity = self.gamemap[y][x]
                if entity is self.pla:
                    self.update_tile(x, y, self.pla.look, "blue")
                elif entity is self.entity1:
                    self.update_tile(x, y, self.entity1.look, "red")
                elif entity is None:
                    self.update_tile(x, y, "", "light green")


    def setup(self):
        self.root = tk.Tk()
        frame = tk.Frame(self.root)
        frame.pack()

        for y in range(self.size):
            for x in range(self.size):
                btn = tk.Label(frame, text="", width=4, height=2, relief="ridge", borderwidth=2,
                               font=("Arial", 12), bg="light green", highlightbackground="pink", highlightthickness=0.5)
                btn.grid(row=y, column=x)

                btn.bind("<Button-1>", lambda e, x=x, y=y: self.attack(x, y))
                btn.bind("<Button-3>", lambda e, x=x, y=y: self.move_player(x, y))

                self.tiles[y][x] = btn

        self.update_tile(self.pla.x, self.pla.y, self.pla.look, "blue")
        self.update_tile(self.entity1.x, self.entity1.y, self.entity1.look, "red")

        self.root.mainloop()
