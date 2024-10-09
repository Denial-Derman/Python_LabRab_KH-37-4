def sport(M,K):
  target_distance = 50
  current_distance = M
  days = 1

  while current_distance <= target_distance:
    current_distance += current_distance * (K / 100)
    days += 1

  return days