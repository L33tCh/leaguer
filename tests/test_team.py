from models.team import Team


class TestTeam:
    def test_team_variables(self):
        team = Team("A 1")
        # initialise a team with name and latest_score but 0 starting score
        assert team.name is "A"
        assert team.latest is 1
        assert team.score is 0
        del team

    def test_team_ordering(self):
        team_a = Team("Alpha 0")
        team_b = Team("Beta 0")
        # Same score, alphabetical ordering
        assert team_a < team_b
        team_b.name = "Active"
        assert not team_a < team_b
        # Different score means score based ordering
        team_b.score = 1
        assert not team_a < team_b
