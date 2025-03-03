import tkinter as tk
import player as p

class GameMap:
    def __init__(self, size):
        self.size = size
        self.gamemap = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.tiles = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.pla = p.player(1, 1)  # Player starting position
        self.click_player = False

    def left_click(self, x, y):
        if self.gamemap[y][x] == "X":  # Selecting player
            self.tiles[y][x].config(bg="green")
            self.click_player = True
            
        elif self.click_player:  # Trying to move
            vals = self.pla.move(x, y)
            if vals["T"]:  # Valid move
                # Clear old position
                self.gamemap[vals["y"]][vals["x"]] = 0
                self.tiles[vals["y"]][vals["x"]].config(bg="light green", text="")

                # Update new position
                self.gamemap[y][x] = "X"
                self.tiles[y][x].config(bg="blue", text="X")
                
                self.click_player = False
            else:  # Invalid move
                self.tiles[y][x].config(bg="red")  # Highlight invalid move
                self.root.after(300, lambda: self.tiles[y][x].config(bg="light green"))  # Reset color

    def right_click(self, x, y):
        """Handles right-click events (currently does nothing)."""
        print(f"Right-clicked on ({x}, {y})")  # Placeholder for future functionality

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
                btn.bind("<Button-1>", lambda e, x=x, y=y: self.left_click(x, y))
                btn.bind("<Button-3>", lambda e, x=x, y=y: self.right_click(x, y))

                self.tiles[y][x] = btn

        # Place player at start position
        print(self.pla.x, self.pla.y)
        self.gamemap[self.pla.y][self.pla.x] = "X"
        self.tiles[self.pla.y][self.pla.x].config(text="X", bg="blue")

        self.root.mainloop()
