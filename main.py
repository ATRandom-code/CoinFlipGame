# Import the random module to generate random numbers
import random

# Define a function that simulates a coin flip
def flip_coin():
  # Generate a random number between 0 and 1
  value = random.randint(0, 1)

  # Return "heads" if the number is 0 and "tails" if the number is 1
  if value == 0:
    return "heads"
  else:
    return "tails"

# Set the initial score to 0
score = 0

# Print the instructions for the game
print("Welcome to the coin flipping game!")
print("I will flip a coin and you have to guess if it will be heads or tails.")

# Start the game loop
while True:
  # Flip the coin and store the result
  result = flip_coin()

  # Ask the player for their guess
  guess = input("Guess heads or tails: ")

  # If the guess is correct, increase the score
  if guess == result:
    score += 1
    print("Correct! Your score is now {}".format(score))

  # If the guess is incorrect, the game ends
  else:
    print("Sorry, that's not correct. The result was {}".format(result))
    print("Your final score is {}".format(score))
    break
