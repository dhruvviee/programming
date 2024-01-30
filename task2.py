def valid(state):
  left, right = state
  missionaries_l, cannibals_l, boat_l = left
  missionaries_r, cannibals_r, boat_r = right
  return (
      # No cannibals outnumbering missionaries on either side
      (missionaries_l >= cannibals_l or boat_l) and
      (missionaries_r >= cannibals_r or not boat_l) and
      # Boat can't be empty on either side
      missionaries_l + cannibals_l + boat_l > 0 and
      missionaries_r + cannibals_r + boat_r > 0
  )

def explore(state, queue):
  left, right = state
  missionaries_l, cannibals_l, boat_l = left
  missionaries_r, cannibals_r, boat_r = right
  for m in range(missionaries_l + 1):
    for c in range(cannibals_l + 1):
      if m + c == 0 or boat_l == 0: continue
      next_left = (missionaries_l - m, cannibals_l - c, not boat_l)
      next_right = (missionaries_r + m, cannibals_r + c, boat_l)
      if valid((next_left, next_right)) and (next_left, next_right) not in queue:
        queue.append((next_left, next_right))

def solve(start, goal):
  queue = [start]
  visited = set()
  while queue:
    state = queue.pop(0)
    if state in visited: continue
    visited.add(state)
    if state == goal: return True
    explore(state, queue)
  return False

start = ((3, 3, 1), (0, 0, 0))  # Initial state
goal = ((0, 0, 0), (3, 3, 1))  # Final state
solvable = solve(start, goal)

if solvable:
  print("Solution found!")
else:
  print("No solution exists for this problem.")
