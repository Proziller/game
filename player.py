class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, nx, ny):
        dx = self.x - nx
        dy = self.y - ny
        if dx >= -1 and dx <= 1 and dy >= -1 and dy <= 1:
            ret = {"x":self.x, "y":self.y, "T":True}
            self.x = nx
            self.y = ny
            return ret
        return {"x":self.x, "y":self.y, "T":False}