
class Player:
    def __init__(self, team_name, team_no):
        self.team_name = team_name
        self.team_no = team_no
        self.score = 0

    def get_score(self):
        return self.score

    def get_name(self):
        return self.team_name

    def get_team_no(self):
        return self.team_no

    def set_score(self, score):
        self.score = score
