from tennis import Player, Match

agassi = Player("Andre Agassi", 2000)
sampras = Player("Pete Sampras", 1200)

test_match = Match(agassi, sampras)

test_match.simulate_match()
test_match.play_match()
