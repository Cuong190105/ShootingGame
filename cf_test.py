import pytest
from simple_shooting_game import Player, Bullet, Game

@pytest.fixture
def game():
    return Game()

class TestCheckCollision:
    def test_path1(self, game):
        p1 = Player("p1", 200, 300)
        game.check_collision(p1)
    
    def test_path2(self, game):
        p1 = Player("p1", 200, 300)
        p2 = "incorrect type"
        game.check_collision(p1, p2)
    
    def test_path3(self, game):
        b1 = Bullet("p1_b", 200, 300)
        b2 = Bullet("p2_b", 200, 200)
        game.check_collision(b1, b2)
    
    def test_path4(self, game):
        b1 = Bullet("p1_b", 200, 300)
        p2 = Player("p2", 300, 400)
        game.check_collision(b1, p2)
    
    def test_path5(self, game):
        p1 = Player("p1", 200, 300)
        b1 = Bullet("p1_b", 200, 300)
        game.check_collision(p1, b1)
    
    def test_path6(self, game):
        p1 = Player("p1", 200, 300)
        b2 = Bullet("p2_b", 205, 310)
        game.check_collision(p1, b2)
    
    def test_path7(self, game):
        p1 = Player("p1", 200, 300)
        b2 = Bullet("p2_b", 195, 310)
        game.check_collision(p1, b2)