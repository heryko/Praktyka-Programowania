class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0
        self.point_descriptions = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, name):
        # Naprawiono błąd: używamy zmiennej zamiast stałego ciągu "player1"
        if name == self.player1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        if self._is_regular_play():
            return self._get_regular_score()

        if self.p1_points == self.p2_points:
            return "Deuce"

        return self._get_endgame_score()

    def _is_regular_play(self):
        # Warunek uproszczony: gra toczy się standardowo, póki nikt nie ma 4 pkt
        # i nie doszło do sytuacji Deuce (suma < 6)
        return self.p1_points < 4 and self.p2_points < 4 and (self.p1_points + self.p2_points < 6)

    def _get_regular_score(self):
        p1_desc = self.point_descriptions[self.p1_points]
        if self.p1_points == self.p2_points:
            return f"{p1_desc}-All"
        return f"{p1_desc}-{self.point_descriptions[self.p2_points]}"

    def _get_endgame_score(self):
        leader = self.player1_name if self.p1_points > self.p2_points else self.player2_name
        diff = abs(self.p1_points - self.p2_points)

        if diff == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"