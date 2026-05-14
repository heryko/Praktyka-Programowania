class TennisGame4:
    def __init__(self, player1_name, player2_name):
        self.server = player1_name
        self.receiver = player2_name
        self.server_score = 0
        self.receiver_score = 0
        self.score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.server:
            self.server_score += 1
        else:
            self.receiver_score += 1

    def score(self):
        # Sprawdzamy stany gry w kolejności priorytetu
        if self._is_win():
            return f"Win for {self._get_leader()}"

        if self._is_advantage():
            return f"Advantage {self._get_leader()}"

        if self._is_deuce():
            return "Deuce"

        if self.server_score == self.receiver_score:
            return f"{self.score_names[self.server_score]}-All"

        return f"{self.score_names[self.server_score]}-{self.score_names[self.receiver_score]}"

    # Prywatne metody pomocnicze
    def _is_deuce(self):
        return self.server_score >= 3 and self.server_score == self.receiver_score

    def _is_advantage(self):
        return (self.server_score >= 4 or self.receiver_score >= 4) and \
            abs(self.server_score - self.receiver_score) == 1

    def _is_win(self):
        return (self.server_score >= 4 or self.receiver_score >= 4) and \
            abs(self.server_score - self.receiver_score) >= 2

    def _get_leader(self):
        return self.server if self.server_score > self.receiver_score else self.receiver