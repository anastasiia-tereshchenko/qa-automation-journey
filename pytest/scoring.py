letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

letter_to_points = {key:value for key, value in zip(letters, points)}

def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter, 0)
  return point_total 
