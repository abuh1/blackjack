points = {'a' : 4, 'b' : 20}
player_hand = ['a', 'b']

p_score = sum(points[n] for n in player_hand)
print(p_score)