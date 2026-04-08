import pytest
from simple_shooting_game import Player, Bullet, Game

@pytest.fixture
def game():
    return Game()

class TestCheckCollision:
    def test_path1(self, game):
        p1 = Player("p1", 200, 300)
        assert game.check_collision(p1) == False
    
    def test_path2(self, game):
        p1 = Player("p1", 200, 300)
        p2 = "incorrect type"
        assert game.check_collision(p1, p2) == False
    
    def test_path3(self, game):
        b1 = Bullet("p1_b", 200, 300)
        b2 = Bullet("p2_b", 200, 200)
        assert game.check_collision(b1, b2) == False
    
    def test_path4(self, game):
        b1 = Bullet("p1_b", 200, 300)
        p2 = Player("p2", 300, 400)
        assert game.check_collision(b1, p2) == False
    
    def test_path5(self, game):
        p1 = Player("p1", 200, 300)
        b1 = Bullet("p1_b", 200, 300)
        assert game.check_collision(p1, b1) == False
    
    def test_path6(self, game):
        p1 = Player("p1", 200, 300)
        b2 = Bullet("p2_b", 193, 293)
        assert game.check_collision(p1, b2) == True
    
    def test_path7(self, game):
        p1 = Player("p1", 200, 300)
        b2 = Bullet("p2_b", 227, 327)
        assert game.check_collision(p1, b2) == True
    
    def test_path8(self, game):
        p1 = Player("p1", 200, 300)
        b2 = Bullet("p2_b", 200, 300)
        assert game.check_collision(p1, b2) == True