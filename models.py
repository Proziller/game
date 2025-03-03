class roboter:
    def __init__(self, player, looks, x, y, reach):
        self.x = x
        self.y = y
        self.look = looks
        self.player = player
        self.reach = reach
        self.enegy = 100
        self.hp = 100

    def move(self, nx, ny):
        dx = self.x - nx
        dy = self.y - ny
        reach = self.reach
        if dx >= reach*-1 and dx <= reach and dy >= reach*-1 and dy <= reach:
            ret = {"x":self.x, "y":self.y, "T":True}
            self.x = nx
            self.y = ny
            return ret
        return {"x":self.x, "y":self.y, "T":False}