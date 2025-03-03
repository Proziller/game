import tkinter as tk
import player as p
import entity as e

class GameMap:
    def __init__(self, size):
        self.size = size
        self.gamemap = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.tiles = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.highlighted_tiles = []

        self.pla = p.player(1, 1)  # Player starting position
        self.plalook = self.pla.look

        self.click_player = False

        self.entity1 = e.entity(2, 2)


    def move_player(self, x, y):
        # Clear old highlighted tiles (if any)
        for hx, hy in self.highlighted_tiles:
            self.tiles[hy][hx].config(bg="light green")
        self.highlighted_tiles = []

        if self.gamemap[y][x] == "P":  # Selecting player
            self.tiles[y][x].config(bg="green")
            self.click_player = True

            # Highlight movement range
            reach = self.pla.model.reach

            for dy in range(-reach, reach + 1):
                for dx in range(-reach, reach + 1):
                    nx, ny = x + dx, y + dy

                    # Bounds check
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        # Skip highlighting the player tile itself
                        if (nx, ny) != (x, y) and self.gamemap[ny][nx] == 0:
                            self.tiles[ny][nx].config(bg="light blue")
                            self.highlighted_tiles.append((nx, ny))

        elif self.click_player:
            if self.gamemap[y][x] == 0:  # Trying to move

                vals = self.pla.move(x, y)

                if vals["T"]:  # Valid move
                    # Clear old position
                    self.gamemap[vals["y"]][vals["x"]] = 0
                    self.tiles[vals["y"]][vals["x"]].config(bg="light green", text="")

                    # Clear movement highlights after moving
                    for hx, hy in self.highlighted_tiles:
                        self.tiles[hy][hx].config(bg="light green")
                    self.highlighted_tiles = []

                    # Update new position
                    self.gamemap[y][x] = "P"
                    self.tiles[y][x].config(bg="blue", text=self.plalook)
            
            self.click_player = False
            for y in range(self.size):
                for x in range(self.size):
                    if self.gamemap[y][x] == "P":
                        self.tiles[y][x].config(bg="blue", text=self.plalook)


    #def player_change(self, px, py, ex, ey):
    #    if px-ex >= -1 and px-ex <= 1 and py-ey >= -1 and py-ey <= 1:
            


    def attack(self, x, y):
        """Handles right-click events (currently does nothing)."""
        print(f"Left-clicked on ({x}, {y})")  # Placeholder for future functionality


    def setup(self):
        self.root = tk.Tk()
        frame = tk.Frame(self.root)
        frame.pack()

        for y in range(self.size):
            for x in range(self.size):
                btn = tk.Label(frame, text="", width=4, height=2, relief="ridge", borderwidth=2, 
                               font=("Arial", 12), bg="light green", highlightbackground="pink", highlightthickness=0.5)
                btn.grid(row=y, column=x)

                # Bind click events
                btn.bind("<Button-1>", lambda e, x=x, y=y: self.attack(x, y))
                btn.bind("<Button-3>", lambda e, x=x, y=y: self.move_player(x, y))

                self.tiles[y][x] = btn

        # Place player at start position
        self.gamemap[self.pla.y][self.pla.x] = "P"
        self.tiles[self.pla.y][self.pla.x].config(text=self.plalook, bg="blue")

        self.gamemap[self.entity1.y][self.entity1.x] = "E"
        self.tiles[self.entity1.y][self.entity1.x].config(text=self.entity1.look, bg="red")

        self.root.mainloop()
