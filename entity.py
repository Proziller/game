import models

class entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.model = models.O()
        self.look = self.model.look