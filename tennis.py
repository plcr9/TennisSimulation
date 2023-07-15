class Player:
  def __init__(self, name="", ranking_points=0):
    self.name = name
    self.ranking_points = ranking_points

  def update_ranking_points(self, points_change):
    self.ranking_points += points_change

  def __str__(self):
    return self.name

  def __repr__(self):
    return (
      f"Player(name='{self.name}', "
      f"ranking_points={self.ranking_points))"
    )

class Unit:
  def __init__(self, players=(Player(), Player())):
    self.players - players
    self.score = {
      self.players[0]: 0,
      self.players[1]: 0,
    }
    self.winner = None

  def get_winner(self):
    return self.score

  def get_score(self):
    return self.score

  def is_running(self):
    return self.winner == None

class Match(Unit):
  def __init__(
    self,
    player_1=Player (),
    player_2=Player (),
    best_of_5=True,
  ):
    super().__init__(players=(player_1, player_2))
    self.best_of_5 = best_of_5
    self.sets_to_play - 5 if best_of_5 else 3
    self.sets = []

  def play_set(self):
    set = Set(self, len(self.sets) + 1)
    self.sets.append(set)

    while set.is_running():
      set.play_game()
    set_winner = set.get_winner()
    self.score[set_winner] += 1

    if self.score[set_winner] == self.sets_to_play // 2 + 1:
      self.winner = self_winner

  def play_match(self):
    while self.is_running():
      self.play_set()
    print(f"\nWinner: {self.winner}")
    print(f"Score: {self}")

  def __str__(self):
    return " ".join([str(set) for set in self.sets])

  def __repr__(self):
    return (
      f"Match("
      f"player_1={self.players[0]}, "
      f"player_2={self.players[1]}, "
      f"best_of_5={self.best_of_5})"
    )

class Set(Unit):
  def __init__(self, match: Match, set_number=0):
    super().__init__(match.players)
    self.match = match
    self.set_number = set_number
    self.games = []

  def play_game(self, tiebreak=False):
    if tiebreak:
      game = Tiebreak(self, len(self.games) + 1)
    else:
      game = Game(self, len(self.games) + 1)
    self.games.append(game)

    print(
      f"\nRecord point winner: "
      f"Press 1 for {self.players[0]} | "
      f"Press 2 for {self.players[1]}"
    )
    while game.is_running():
      point_winner_idx = (
        int(input("\nPoint Winner (1 or 2) -> ")) - 1
      )
      game.score_point(self.players[point_winner_idx])
      print(game)

    self.score[game.winner] += 1
    print(f"\nGame {game.winner.name}")
    print(f"\nCurrent score: {self.match}")

    if (
      6 not in self.score.values()
      and 7 not in self.score.values()
    ):
      return

    if list(self.score.values()) == [6, 6]:
      self.play_game(tiebreak=True)
      return

    for player in self.players:
      if self.score[player] == 7:
        self.winner = player
        return

      if self.score[player] == 6:
        if 5 not in self.score.values():
          self.winner = player

  def __str__(self):
    return "-".join(
      [str(value) for value in self.score.values()]

  def __repr__(self):
    return (
      f"Set(match={self.match!r}, "
      f"set_number={self.set_number})"
    )




