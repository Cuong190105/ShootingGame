class Object:
    def __init__(self, name, x, y, size):
        self.name = name
        self.x = x
        self.y = y
        self.size = size

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"Object: {self.name} at ({self.x}, {self.y}) with size {self.size}"

class Player(Object):
    def __init__(self, name, x, y, size = 20):
        super().__init__(name, x, y, size)
        self.health = 100
        self.damage = 10
        self.speed = 5
        self.move_dir = [0] * 2
        self.bullet_speed = 20
    
    def change_direction(self, direction, val):
        self.move_dir[direction] = val

    def shoot(self, target_x, target_y):
        direction_x = target_x - self.x
        direction_y = target_y - self.y
        magnitude = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if magnitude == 0:
            return None
        norm_x = direction_x / magnitude
        norm_y = direction_y / magnitude
        bullet_speed_x = norm_x * self.bullet_speed
        bullet_speed_y = norm_y * self.bullet_speed
        return Bullet(f"{self.name}_bullet", self.damage, bullet_speed_x, bullet_speed_y, self.x, self.y, 5)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def __str__(self):
        return f"Player: {self.name} at ({self.x}, {self.y}) with health {self.health}"

class Bullet(Object):
    def __init__(self, name, damage, speed, x, y, size = 5):
        super().__init__(name, x, y, size)
        self.damage = damage
        self.speed = speed

    def __str__(self):
        return f"Bullet: {self.name} at ({self.x}, {self.y}) with damage {self.damage}"
    
class Game:
    def __init__(self):
        self.players = []
        self.bullets = []
        self.BOARDWIDTH = 1000
        self.BOARDHEIGHT = 1000

    def add_player(self, player):
        self.players.append(player)

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def update(self):
        for player in self.players:
            player.move()
        for bullet in self.bullets:
            bullet.move()
        self.handle_collisions()
        # draw()

    def handle_collisions(self):
        grid = {}
        CELLSIZE = 50
        for player in self.players:
            col_start = player.x // CELLSIZE
            col_end = (player.x + player.size) // CELLSIZE
            row_start = player.y // CELLSIZE
            row_end = (player.y + player.size) // CELLSIZE
            for col in range(col_start, col_end + 1):
                for row in range(row_start, row_end + 1):
                    if (col, row) not in grid:
                        grid[(col, row)] = {}
                        grid[(col, row)]['players'] = []
                        grid[(col, row)]['bullets'] = []
                    grid[(col, row)]['players'].append(player)

        for bullet in self.bullets:
            col_start = bullet.x // CELLSIZE
            col_end = (bullet.x + bullet.size) // CELLSIZE
            row_start = bullet.y // CELLSIZE
            row_end = (bullet.y + bullet.size) // CELLSIZE
            for col in range(col_start, col_end + 1):
                for row in range(row_start, row_end + 1):
                    if (col, row) not in grid:
                        grid[(col, row)] = {}
                        grid[(col, row)]['players'] = []
                        grid[(col, row)]['bullets'] = []
                    grid[(col, row)]['bullets'].append(bullet)
        
        for cell in grid.values():
            # Resolve player-player collisions multiple times
            for _ in range(4):
                for p1 in cell['players']:
                    for p2 in cell['players']:
                        if p1 != p2 and self.check_collision(p1, p2):
                            diffX = (p1.x - p2.x) / 2
                            diffY = (p1.y - p2.y) / 2
                            overlapX = p1.size - abs(diffX)
                            overlapY = p1.size - abs(diffY)
                            if overlapX < overlapY:
                                shiftX = overlapX / 2 if diffX > 0 else -overlapX / 2
                                p1.move(shiftX, 0)
                                p2.move(-shiftX, 0)
                            else:
                                shiftY = overlapY / 2 if diffY > 0 else -overlapY / 2
                                p1.move(0, shiftY)
                                p2.move(0, -shiftY)

            # Check for bullet hits
            for p1 in cell['players']:
                for bullet in cell['bullets']:
                    if self.check_collision(bullet, p1):
                        p1.take_damage(bullet.damage)
                        self.bullets.remove(bullet)
            
    def check_collision(self, obj1, obj2):
        return (obj1.x < obj2.x + obj2.size and
                obj1.x + obj1.size > obj2.x and
                obj1.y < obj2.y + obj2.size and
                obj1.y + obj1.size > obj2.y)