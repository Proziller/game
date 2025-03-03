import models

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.model = models.X()
        self.look = self.model.look

    def move(self, nx, ny):
        dx = self.x - nx
        dy = self.y - ny
        if dx >= self.model.reach*-1 and dx <= self.model.reach and dy >= self.model.reach*-1 and dy <= self.model.reach:
            ret = {"x":self.x, "y":self.y, "T":True}
            self.x = nx
            self.y = ny
            return ret
        return {"x":self.x, "y":self.y, "T":False}
