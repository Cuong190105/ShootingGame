import pytest
from simple_shooting_game import Player, Bullet, Game

@pytest.fixture
def game():
    return Game()

class TestCheckCollision:
    def test_single_object_norm(self, game):
        player = Player("Player1", 200, 300)
        assert game.check_collision(player) == False

    def test_single_object_near_bound_min_x(self, game):
        player = Player("Player1", 1, 300)
        assert game.check_collision(player) == False

    def test_single_object_on_bound_min_x(self, game):
        player = Player("Player1", 0, 300)
        assert game.check_collision(player) == False

    def test_single_object_out_of_bound_min_x(self, game):
        player = Player("Player1", -1, 300)
        assert game.check_collision(player) == True

    def test_single_object_near_bound_max_x(self, game):
        player = Player("Player1", game.BOARDWIDTH - 2, 300)
        assert game.check_collision(player) == False

    def test_single_object_on_bound_max_x(self, game):
        player = Player("Player1", game.BOARDWIDTH - 1, 300)
        assert game.check_collision(player) == False

    def test_single_object_out_of_bound_max_x(self, game):
        player = Player("Player1", game.BOARDWIDTH, 300)
        assert game.check_collision(player) == True

    def test_single_object_near_bound_min_y(self, game):
        player = Player("Player1", 200, 1)
        assert game.check_collision(player) == False

    def test_single_object_on_bound_min_y(self, game):
        player = Player("Player1", 200, 0)
        assert game.check_collision(player) == False

    def test_single_object_out_of_bound_min_y(self, game):
        player = Player("Player1", 200, -1)
        assert game.check_collision(player) == True

    def test_single_object_near_bound_max_y(self, game):
        player = Player("Player1", 200, game.BOARDHEIGHT - 2)
        assert game.check_collision(player) == False

    def test_single_object_on_bound_max_y(self, game):
        player = Player("Player1", 200, game.BOARDHEIGHT - 1)
        assert game.check_collision(player) == False

    def test_single_object_out_of_bound_max_y(self, game):
        player = Player("Player1", 200, game.BOARDHEIGHT)
        assert game.check_collision(player) == True

    # def test_two_players_no_axis_overlap(self, game):
    #     p1 = Player("Player1", 100, 100)
    #     p2 = Player("Player2", 300, 300)
    #     assert game.check_collision(p1, p2) == False
    
    # def test_two_players_no_axis_overlap_2(self, game):
    #     p1 = Player("Player1", 300, 300)
    #     p2 = Player("Player2", 100, 100)
    #     assert game.check_collision(p1, p2) == False
    
    # def test_two_players_no_axis_overlap_3(self, game):
    #     p1 = Player("Player1", 300, 100)
    #     p2 = Player("Player2", 100, 300)
    #     assert game.check_collision(p1, p2) == False

    # def test_two_players_axis_x_overlap_no_collision(self, game):
    #     p1 = Player("Player1", 100, 100)
    #     p2 = Player("Player2", 100, 300)
    #     assert game.check_collision(p1, p2) == False

    # def test_two_players_axis_y_overlap_no_collision(self, game):
    #     p1 = Player("Player1", 100, 100)
    #     p2 = Player("Player2", 300, 100)
    #     assert game.check_collision(p1, p2) == False