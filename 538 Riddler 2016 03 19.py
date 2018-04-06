import random

successes = []
gains = []
reps = 100000
for start_guess in range(745,746):
  success = 0
  gain = 0
  for i in range(reps):
    target = random.randrange(1000)
    current_guess = start_guess
    step = 128
  ##  print target
    for j in range(8):
  ##    print current_guess, step
      if current_guess == target:
        break
      elif current_guess > target:
        current_guess -= step
      else:
        current_guess += step
      if step % 2 == 0:
        step /= 2
      else:
        step = (step + 1)/2
  ##  print current_guess, target, j+2
      if current_guess == target:
        success += 1
        gain += target
  successes.append(success)
  gains.append(gain)
print max(gains), gains.index(max(gains))
print gains


 
