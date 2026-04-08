import pytest
from simple_shooting_game import Player, Bullet, Game

@pytest.fixture
def game():
    return Game()

class TestCheckCollision:
    def test_path1(self, game):
        obj1 = Bullet("p1_b", 193, 293)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == True

    def test_path2(self, game):
        obj1 = "abc"
        obj2 = 123
        assert game.check_collision(obj1, obj2) == False
    
    def test_path3(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Bullet("p2_b", 227, 327)
        assert game.check_collision(obj1, obj2) == True
    
    def test_path4(self, game):
        obj1 = Bullet("p1_b", 200, 300)
        assert game.check_collision(obj1) == False
    
    def test_path5(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = 123
        assert game.check_collision(obj1, obj2) == False
    
    def test_path6(self, game):
        obj1 = Bullet("p1_b", 200, 300)
        obj2 = Bullet("p2_b", 200, 300)
        assert game.check_collision(obj1, obj2) == False
    
    def test_path7(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == True
    
    def test_path8(self, game):
        obj1 = Bullet("p1_b", 1010, 300)
        assert game.check_collision(obj1) == True
    
    def test_path9(self, game):
        obj1 = Bullet("p1_b", 200, -10)
        assert game.check_collision(obj1) == True

    def test_path10(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Player("p2", 100, 300)
        assert game.check_collision(obj1, obj2) == False
    
    def test_path11(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Player("p2", 250, 300)
        assert game.check_collision(obj1, obj2) == False

    def test_path12(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Bullet("p2_b", 193, 293)
        assert game.check_collision(obj1, obj2) == True
    
    def test_path13(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Bullet("p2_b", 210, 310)
        assert game.check_collision(obj1, obj2) == True
    
    def test_path14(self, game):
        obj1 = Bullet("p1_b", 100, 300)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == False
    
    def test_path15(self, game):
        obj1 = Bullet("p1_b", 300, 500)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == False

    def test_path16(self, game):
        obj1 = Bullet("p1_b", 227, 293)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == True
    
    def test_path17(self, game):
        obj1 = Bullet("p1_b", 210, 293)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == True

    def test_path18(self, game):
        obj1 = Bullet("p1_b", 200, 1010)
        assert game.check_collision(obj1) == True
    
    def test_path19(self, game):
        obj1 = Bullet("p1_b", 200, 300)
        assert game.check_collision(obj1) == False

    def test_path20(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Player("p2", 210, 200)
        assert game.check_collision(obj1, obj2) == False

    def test_path21(self, game):
        obj1 = Bullet("p1_b", 210, 500)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == False

    def test_path22(self, game):
        obj1 = Bullet("p1_b", 210, 200)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == False

    def test_path23(self, game):
        obj1 = Bullet("p1_b", 210, 500)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == False

    def test_path24(self, game):
        obj1 = Bullet("p1_b", 210, 327)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == True

    def test_path25(self, game):
        obj1 = Bullet("p1_b", 193, 310)
        obj2 = Player("p2", 200, 300)
        assert game.check_collision(obj1, obj2) == True

    def test_path26(self, game):
        obj1 = Player("p1", 200, 300)
        obj2 = Bullet("p1_b", 210, 327)
        assert game.check_collision(obj1, obj2) == False
    
    def test_path27(self, game):
        obj1 = Bullet("p1_b", 200, 300)
        obj2 = Player("p1", 193, 310)
        assert game.check_collision(obj1, obj2) == False