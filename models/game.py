from models.team import Team


class Game(object):
    def __init__(self):
        """
        Initialise a game object, no input accepted
        """
        self.teams = dict()

    def register_game(self, result):
        """
        Register a game result ("name1 score, name2 score")
        :param str result: the string representation of a game result
        """
        parsed = self.parse_result(result)
        for i in range(2):
            if parsed[i].name not in self.teams.keys():
                self.teams[parsed[i].name] = parsed[i]

        self.score_game(parsed[0], parsed[1])

    def score_game(self, t1, t2):
        """
        Pull through 2 Team object prepopulated with name and latest score
        and add or update team list with latest results
        :param Team t1: First scored team
        :param Team t2: Second scored team
        :return:
        """
        if t1.latest < t2.latest:
            self.teams[t2.name].add_points(3)
        elif t1.latest > t2.latest:
            self.teams[t1.name].add_points(3)
        else:
            self.teams[t1.name].add_points(1)
            self.teams[t2.name].add_points(1)

    def parse_result(self, result):
        """
        Parse a string input into 2 Team strings which are used to create and return 2 Team objects
        :param str result: Game result in the format <team1_name team1_score, team2_name team2_score>
        :return: List of 2 Team objects
        """
        sides = [t.strip() for t in result.split(",")]
        teams = [Team(t) for t in sides]
        return teams

    def print(self):
        """
        Iterate through results to print a sorted results table
        :return:
        """
        count = 0
        current = [1, 0]
        for team in self.results():
            count += 1
            current = current if team.score == current[1] else [count, team.score]
            print("%d. %s" % (current[0], team))

    def results(self):
        """
        Sort and return team results in a list
        :return: List of all Team objects
        """
        sorted_list = [self.teams[a] for a in self.teams]
        sorted_list.sort()
        return sorted_list
