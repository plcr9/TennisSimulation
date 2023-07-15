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



