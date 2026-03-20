import pytest
from simple_shooting_game import Player, Bullet, Game

@pytest.fixture
def game():
    return Game()

class TestCheckCollision:
    @pytest.mark.parametrize("obj, expected", [
        (Player("p1", 200, 300), False),    # norm x, norm y
        (Player("p1", 0.001, 300), False),  # min x+, norm y
        (Player("p1", 0, 300), False),      # min x, norm y
        (Player("p1", -0.001, 300), True),  # min x-, norm y
        (Player("p1", 969.999, 300), False),# max x-, norm y
        (Player("p1", 970, 300), False),    # max x, norm y
        (Player("p1", 970.001, 300), True), # max x+, norm y
        (Player("p1", 200, 0.001), False),  # norm x, min y+
        (Player("p1", 200, 0), False),      # norm x, min y
        (Player("p1", 200, -0.001), True),  # norm x, min y-
        (Player("p1", 200, 969.999), False),# norm x, max y-
        (Player("p1", 200, 970), False),    # norm x, max y
        (Player("p1", 200, 970.001), True), # norm x, max y+
        (Bullet("p1_b", 200, 300), False),  # norm x, norm y
        (Bullet("p1_b", 0.001, 300), False),# min x+, norm y
        (Bullet("p1_b", 0, 300), False),    # min x, norm y
        (Bullet("p1_b", -0.001, 300), True),# min x-, norm y
        (Bullet("p1_b", 989.999, 300), False), # max x-, norm y
        (Bullet("p1_b", 990, 300), False),  # max x, norm y
        (Bullet("p1_b", 990.001, 300), True),# max x+, norm y
        (Bullet("p1_b", 200, 0.001), False),# norm x, min y+
        (Bullet("p1_b", 200, 0), False),    # norm x, min y
        (Bullet("p1_b", 200, -0.001), True),# norm x, min y-
        (Bullet("p1_b", 200, 989.999), False),# norm x, max y-
        (Bullet("p1_b", 200, 990), False),  # norm x, max y
        (Bullet("p1_b", 200, 990.001), True),# norm x, max y+
    ])  
    def test_single_object_norm(self, game, obj, expected):
        assert game.check_collision(obj) == expected

    # x means delta x = x2 - x1
    @pytest.mark.parametrize("p1, p2, expected", [
        (Player("p1", 200, 300), Player("p2", 300, 500), False),        # norm x, norm y
        (Player("p1", 200, 300), Player("p2", 230.001, 500), False),    # max x+, norm y
        (Player("p1", 200, 300), Player("p2", 230, 500), False),        # max x, norm y
        (Player("p1", 200, 300), Player("p2", 229.999, 500), False),    # max x-, norm y
        (Player("p1", 200, 300), Player("p2", 170.001, 500), False),    # min x+, norm y
        (Player("p1", 200, 300), Player("p2", 170, 500), False),        # min x, norm y
        (Player("p1", 200, 300), Player("p2", 169.999, 500), False),    # min x-, norm y
        
        (Player("p1", 200, 300), Player("p2", 300, 330.001), False),        # norm x, max+ y
        (Player("p1", 200, 300), Player("p2", 230.001, 330.001), False),    # max x+, max+ y
        (Player("p1", 200, 300), Player("p2", 230, 330.001), False),        # max x, max+ y
        (Player("p1", 200, 300), Player("p2", 229.999, 330.001), False),    # max x-, max+ y
        (Player("p1", 200, 300), Player("p2", 170.001, 330.001), False),    # min x+, max+ y
        (Player("p1", 200, 300), Player("p2", 170, 330.001), False),        # min x, max+ y
        (Player("p1", 200, 300), Player("p2", 169.999, 330.001), False),    # min x-, max+ y
        
        (Player("p1", 200, 300), Player("p2", 300, 330), False),        # norm x, max y
        (Player("p1", 200, 300), Player("p2", 230.001, 330), False),    # max x+, max y
        (Player("p1", 200, 300), Player("p2", 230, 330), False),        # max x, max y
        (Player("p1", 200, 300), Player("p2", 229.999, 330), False),    # max x-, max y
        (Player("p1", 200, 300), Player("p2", 170.001, 330), False),    # min x+, max y
        (Player("p1", 200, 300), Player("p2", 170, 330), False),        # min x, max y
        (Player("p1", 200, 300), Player("p2", 169.999, 330), False),    # min x-, max y
        
        (Player("p1", 200, 300), Player("p2", 300, 329.999), False),        # norm x, max- y
        (Player("p1", 200, 300), Player("p2", 230.001, 329.999), False),    # max x+, max- y
        (Player("p1", 200, 300), Player("p2", 230, 329.999), False),        # max x, max- y
        (Player("p1", 200, 300), Player("p2", 229.999, 329.999), True),    # max x-, max- y
        (Player("p1", 200, 300), Player("p2", 170.001, 329.999), True),    # min x+, max- y
        (Player("p1", 200, 300), Player("p2", 170, 329.999), False),        # min x, max- y
        (Player("p1", 200, 300), Player("p2", 169.999, 329.999), False),    # min x-, max- y
        
        (Player("p1", 200, 300), Player("p2", 300, 270.001), False),        # norm x, min+ y
        (Player("p1", 200, 300), Player("p2", 230.001, 270.001), False),    # max x+, min+ y
        (Player("p1", 200, 300), Player("p2", 230, 270.001), False),        # max x, min+ y
        (Player("p1", 200, 300), Player("p2", 229.999, 270.001), True),    # max x-, min+ y
        (Player("p1", 200, 300), Player("p2", 170.001, 270.001), True),    # min x+, min+ y
        (Player("p1", 200, 300), Player("p2", 170, 270.001), False),        # min x, min+ y
        (Player("p1", 200, 300), Player("p2", 169.999, 270.001), False),    # min x-, min+ y
        
        (Player("p1", 200, 300), Player("p2", 300, 270), False),        # norm x, min y
        (Player("p1", 200, 300), Player("p2", 230.001, 270), False),    # max x+, min y
        (Player("p1", 200, 300), Player("p2", 230, 270), False),        # max x, min y
        (Player("p1", 200, 300), Player("p2", 229.999, 270), False),    # max x-, min y
        (Player("p1", 200, 300), Player("p2", 170.001, 270), False),    # min x+, min y
        (Player("p1", 200, 300), Player("p2", 170, 270), False),        # min x, min y
        (Player("p1", 200, 300), Player("p2", 169.999, 270), False),    # min x-, min y
        
        (Player("p1", 200, 300), Player("p2", 300, 269.999), False),        # norm x, min- y
        (Player("p1", 200, 300), Player("p2", 230.001, 269.999), False),    # max x+, min- y
        (Player("p1", 200, 300), Player("p2", 230, 269.999), False),        # max x, min- y
        (Player("p1", 200, 300), Player("p2", 229.999, 269.999), False),    # max x-, min- y
        (Player("p1", 200, 300), Player("p2", 170.001, 269.999), False),    # min x+, min- y
        (Player("p1", 200, 300), Player("p2", 170, 269.999), False),        # min x, min- y
        (Player("p1", 200, 300), Player("p2", 169.999, 269.999), False),    # min x-, min- y
    ])
    def test_player_player_collision(self, game, p1, p2, expected):
        assert game.check_collision(p1, p2) == expected
    
    @pytest.mark.parametrize("p1, b, expected", [
        # Center of bullet is on the player when casting on one of the axes
        (Player("p1", 200, 300), Bullet("p2_b", 210, 310), True),       # norm x, norm y
        (Player("p1", 200, 300), Bullet("p2_b", 190.001, 310), True),   # min+ x, norm y
        (Player("p1", 200, 300), Bullet("p2_b", 190, 310), False),      # min x, norm y
        (Player("p1", 200, 300), Bullet("p2_b", 189.999, 310), False),  # min- x, norm y
        (Player("p1", 200, 300), Bullet("p2_b", 229.999, 310), True),   # max- x, norm y
        (Player("p1", 200, 300), Bullet("p2_b", 230, 310), False),      # max x, norm y
        (Player("p1", 200, 300), Bullet("p2_b", 230.001, 310), False),  # max+ x, norm y
        
        (Player("p1", 200, 300), Bullet("p2_b", 210, 289.999), False),   # norm x, min- y
        (Player("p1", 200, 300), Bullet("p2_b", 210, 290), False),           # norm x, min y
        (Player("p1", 200, 300), Bullet("p2_b", 210, 290.001), True),    # norm x, min+ y
        (Player("p1", 200, 300), Bullet("p2_b", 210, 329.999), True),    # norm x, max- y
        (Player("p1", 200, 300), Bullet("p2_b", 210, 330), False),           # norm x, max y
        (Player("p1", 200, 300), Bullet("p2_b", 210, 330.001), False),   # norm x, max+ y

        # Center of bullet is not on the player when casting on any axis
        (Player("p1", 200, 300), Bullet("p2_b", 190, 290), False),          # norm diff
        (Player("p1", 200, 300), Bullet("p2_b", 193, 290.417), False),      # min+ diff
        (Player("p1", 200, 300), Bullet("p2_b", 193, 290.418), True),       # min- diff, can't find exact min diff
        
        # Hitting by its own bullet
        (Player("p1", 200, 300), Bullet("p1_b", 210, 310), False),          # other case above
    ])
    def test_player_bullet_collision(self, game, p1, b, expected):
        assert game.check_collision(p1, b) == expected

    @pytest.mark.parametrize("b1, b2, expected", [
        (Bullet("p1_b", 200, 300), Bullet("p2_b", 300, 500), False),    # max diff: not colliding
        (Bullet("p1_b", 200, 300), Bullet("p2_b", 205, 300), False),    # min diff: overlapping but not colliding
    ])
    def test_bullet_bullet_collision(self, game, b1, b2, expected):
        assert game.check_collision(b1, b2) == expected