# TennisSimulation

TennisSimulation is designed to follow the format of a best of 5 set tennis match between two players (Andre Agassi and Pete Sampras). Tennis Simulation uses the Random module in Python to generate game, set and match scores at random and therefore the outcome of the match is not determined by user input.

The outcome of 100 matches between the two players is simulated at random. The score for each match is listed, together the winner. At the bottom of the list of 100 matches, the total number of wins for each of the two players is displayed, together with the distribution of the matches that were won over 3, 4 or 5 sets.

The next feature takes into account the ranking points of the two players contesting the match. If the match is simulated with one player holding more ranking points than the other, the percentage chance of the player with the higher number of ranking points winning is increased. If both players enter the match with the same number of ranking points, there is an equal chance of either player emerging triumphant.

The final feature uses the matplotlib module to graphically plot the probability of Player1 winning the match (in one graph) and the probability of Player1 winning the match in 3 sets (straight sets) (in the other graph).
