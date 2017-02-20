class Paddle:
    def __init__(self, column, color, speed, size):
        self.size = size
        self.pos = [column, (SCREEN_HEIGHT / 2) + (size[1] / 2)]
        self.speed = speed
        self.color = color
        objects.append(self)

    def make_rect(self):
        return (self.pos[0], self.pos[1], self.size[0], self.size[1])

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.make_rect(), 0)

    def move(self, dy):
        self.pos[1] += dy

    def update(self):
        return False
