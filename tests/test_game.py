from models.team import Team
from models.game import Game


class TestGame:
    def test_game_variables(self):
        game = Game()
        game.register_game("A 1, B 2")
        # Create 2 teams from game
        assert len(game.teams) is 2

    def test_team_matching(self):
        game = Game()
        game.register_game("A 1, B 2")
        # team A is not created twice
        game.register_game("A 1, C 2")
        assert len(game.teams) is 3

    def test_game_result_ordering(self):
        game = Game()
        team_a = Team("A 0")
        team_b = Team("B 0")
        team_c = Team("c 0")
        team_a.score = 0
        team_b.score = 3
        team_c.score = 3
        # Ensure team ordering follows through to team list sorting
        game.teams = {"A": team_a, "B": team_b, "c": team_c}
        assert str(game.results()) == str([team_b, team_c, team_a])
        team_b.name = "d"
        game.teams["B"].name = "d"
        assert str(game.results()) == str([team_c, team_b, team_a])
