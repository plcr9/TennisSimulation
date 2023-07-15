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

