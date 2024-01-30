def water_jug(jug1_size, jug2_size, target_amount):
 operations = {
   "fill1": lambda state: (jug1_size, state[1]),
   "fill2": lambda state: (state[0], jug2_size),
   "empty1": lambda state: (0, state[1]),
   "empty2": lambda state: (state[0], 0),
   "pour1_to_2": lambda state: (max(0, state[0] - min(state[1], jug2_size)), min(state[1] + state[0], jug2_size)),
   "pour2_to_1": lambda state: (min(state[0] + state[1], jug1_size), max(0, state[1] - min(state[1], jug1_size))),
 }

 visited = set()
 queue = [(0, 0)]

 while queue:
   state = queue.pop(0)
   if state in visited:
     continue
   visited.add(state)

   if state[0] == target_amount:
     steps = []
     while state != (0, 0):
       for op_name, op_fn in operations.items():
         previous_state = op_fn(state)
         if previous_state in visited:
           steps.append(op_name)
           state = previous_state
           break
     return steps[::-1]

   for op_name, op_fn in operations.items():
     next_state = op_fn(state)
     if next_state not in visited:
       queue.append(next_state)

 return None

jug1_size = 4
jug2_size = 3
target_amount = 2
steps = water_jug(jug1_size, jug2_size, target_amount)

if steps:
 print("Steps to achieve", target_amount, "gallons in the", jug1_size, "gallon jug:")
 for step in steps:
   print(step)
else:
 print("Target", target_amount, "gallons is not achievable with these jug sizes.")
