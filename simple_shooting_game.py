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

# Player will have square shape
class Player(Object):
    def __init__(self, name, x, y, size = 30):
        super().__init__(name, x, y, size)
        self.health = 100
        self.damage = 10
        self.speed = 5
        self.move_dir = [0] * 4  # up, down, left, right
        self.bullet_speed = 40
    
    def change_direction(self, direction, val):
        self.move_dir[direction] = val

    def move(self):
        x_part = (self.move_dir[0] * -1 + self.move_dir[1])
        y_part = (self.move_dir[2] * -1 + self.move_dir[3])
        magnitude = (x_part ** 2 + y_part ** 2) ** 0.5
        if magnitude > 0:
            norm_x = x_part / magnitude
            norm_y = y_part / magnitude
            dx = norm_x * self.speed
            dy = norm_y * self.speed
            super().move(dx, dy)

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

# Bullet will have circular shape
class Bullet(Object):
    def __init__(self, name, damage, speedX, speedY, x, y, size = 10):
        super().__init__(name, x, y, size)
        self.damage = damage
        self.dx = speedX
        self.dy = speedY

    def __str__(self):
        return f"Bullet: {self.name} at ({self.x}, {self.y}) with damage {self.damage}"
    
    def move(self):
        super().move(self.dx, self.dy)
    
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
        # Spacial partitioning
        grid = {}
        CELLSIZE = 100

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
        
        # Handle collisions within each cell
        
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
                    if self.check_collision(p1):
                        if p1.x < 0:
                            p1.x = 0
                        elif p1.x + p1.size >= self.BOARDWIDTH:
                            p1.x = self.BOARDWIDTH - p1.size
                        if p1.y < 0:
                            p1.y = 0
                        elif p1.y + p1.size >= self.BOARDHEIGHT:
                            p1.y = self.BOARDHEIGHT - p1.size

            # Check for bullet hits
            for bullet in cell['bullets']:
                for p in cell['players']:
                    if self.check_collision(bullet, p):
                        p.take_damage(bullet.damage)
                        self.bullets.remove(bullet)
                        break
                else:
                    if self.check_collision(bullet):
                        self.bullets.remove(bullet)
            
    def check_collision(self, obj1, obj2 = None):
        # If only one object is provided, check for collisions with world bound
        if obj2 is None:
            return (obj1.x < 0 or obj1.x + obj1.size >= self.BOARDWIDTH or
                    obj1.y < 0 or obj1.y + obj1.size >= self.BOARDHEIGHT)

        # Check for correct type, raise Error if not, maybe?
        if not (isinstance(obj1, Object) and isinstance(obj2, Object)):
            return False

        if isinstance(obj1, Bullet):
            # No bullet-bullet collision
            if isinstance(obj2, Bullet):
                return False
            
            # Obj1 should be player, otherwise swap
            obj1, obj2 = obj2, obj1
    
        # Simple AABB collision check
        firstCheck = (obj1.x < obj2.x + obj2.size and
                    obj1.x + obj1.size > obj2.x and
                    obj1.y < obj2.y + obj2.size and
                    obj1.y + obj1.size > obj2.y)

        # Bullet may have its bounding box collided, but for its circular
        # shape there is still a chance that only the corner of player 
        # hits the bullet's bounding box, not the bullet itself.
        if firstCheck and isinstance(obj2, Bullet):
            centerX = obj2.x + obj2.size / 2
            centerY = obj2.y + obj2.size / 2
            closestX = obj1.x if centerX < obj1.x else obj1.x + obj1.size
            closestY = obj1.y if centerY < obj1.y else obj1.y + obj1.size
            distanceX = centerX - closestX
            distanceY = centerY - closestY
            return (distanceX ** 2 + distanceY ** 2) < (obj2.size / 2) ** 2
        
        return firstCheck

# Simple text-based interface. May use Pygame or other framework for graphics and input handling.

# game = Game()
# player1 = Player("Player1", 100, 100)
# player2 = Player("Player2", 200, 200)
# player3 = Player("Player3", 300, 300)
# game.add_player(player1)
# game.add_player(player2)
# game.add_player(player3)

# while True:
#     inp1 = input("Input for Player1 (WASD to move, F to shoot, <blank> to stand still): ")
#     inp2 = input("Input for Player2 (WASD to move, F to shoot, <blank> to stand still): ")
#     inp3 = input("Input for Player3 (WASD to move, F to shoot, <blank> to stand still): ")

#     for inp, player in zip([inp1, inp2, inp3], [player1, player2, player3]):
#         if 'W' in inp:
#             player.change_direction(0, 1)
#         else:
#             player.change_direction(0, 0)
#         if 'S' in inp:
#             player.change_direction(1, 1)
#         else:
#             player.change_direction(1, 0)
#         if 'A' in inp:
#             player.change_direction(2, 1)
#         else:
#             player.change_direction(2, 0)
#         if 'D' in inp:
#             player.change_direction(3, 1)
#         else:
#             player.change_direction(3, 0)

#         if 'F' in inp:
#             target_x = int(input(f"Enter target X for {player.name}: "))
#             target_y = int(input(f"Enter target Y for {player.name}: "))
#             bullet = player.shoot(target_x, target_y)
#             if bullet:
#                 game.add_bullet(bullet)
#     game.update()