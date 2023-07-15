from tennis import Player, Match

n_simulations = 100

agassi = Player("Andre Agassi", 2005)
sampras = Player("Pete Sampras", 2000)

winners = {agassi: 0, sampras: 0}
n_sets = {3: 0, 4: 0, 5: 0}

for _ in range(n_simulations):
  match = Match(agassi, sampras)
  match.simulate_match()
  match.suppress_output()
  match.play_match()

  print(match,",", "Winner:", match.winner)

  winners[match.winner] += 1
  n_sets[len(match.sets)] += 1

print(winners)
print(n_sets)
