class Team(object):
    score = 0

    def __init__(self, result):
        """
        Initialise Team object
        :param str result: the string representation of a team result (<name score>)
        """
        parsed = self.parse_result(result)
        self.name = parsed["name"]
        self.latest = parsed["score"]

    def add_points(self, points):
        """
        Update score with input points
        :param int points: Integer point value
        :return:
        """
        self.score += points

    def parse_result(self, result):
        """
        Parse game score to retrieve name as string and score as integer
        :param str result: Result in the format <team_name team_score>
        :return: Dictionary including name and score
        """
        result_list = result.split()
        score_index = len(result_list) - 1
        score = result_list[score_index]
        name = " ".join(result_list[:score_index])
        return {
            "name": name,
            "score": int(score)
        }

    def __str__(self):
        """
        Override string output of Team object
        :return:
        """
        return "%s, %d %s" % (self.name, self.score, "pt" if self.score is 1 else "pts")

    def __lt__(self, other):
        """
        Override less-than operation on Team object for control of list sort result
        :param Team other: Other Team object to compare with
        :return: Ordered from highest to lowest by score but lowest to highest by name
        """
        if self.score == other.score:
            return self.name.lower() < other.name.lower()
        return self.score > other.score
