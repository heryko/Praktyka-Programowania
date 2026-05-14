class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0
        self.score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        # Naprawiony błąd: używamy przekazanej nazwy zamiast sztywnego "player1"
        if player_name == self.player1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    #

    def score(self):
        if self.p1_points == self.p2_points:
            return self._get_equal_score()
        if self.p1_points >= 4 or self.p2_points >= 4:
            return self._get_end_game_score()
        return self._get_regular_score()

    def _get_equal_score(self):
        if self.p1_points < 3:
            return f"{self.score_names[self.p1_points]}-All"
        return "Deuce"

    def _get_end_game_score(self):
        diff = self.p1_points - self.p2_points
        if diff == 1:
            return f"Advantage {self.player1_name}"
        if diff == -1:
            return f"Advantage {self.player2_name}"
        if diff >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _get_regular_score(self):
        p1_res = self.score_names[self.p1_points]
        p2_res = self.score_names[self.p2_points]
        return f"{p1_res}-{p2_res}"