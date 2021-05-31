import random

#The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. 
class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            self.contents += ((key+ " ")*value).split()
        self.original = self.contents[:]


    #The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.
    def draw(self, amount):
        self.contents = self.original[:]
        balls_drawn = []
        if amount >= len(self.contents):
            return self.contents
        else:
            for onedraw in range(amount):
                drawn = random.choice(self.contents)
                self.contents.remove(drawn)
                balls_drawn.append(drawn)
        return balls_drawn


#Next, create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:
# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
# The experiment function should return a probability.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #checking if there draws are possible
    if sum(expected_balls.values()) > num_balls_drawn:
        return 0 #not enough balls drawn
    for ball, amount in expected_balls.items():
        if hat.contents.count(ball) < amount:
            return 0 #not enough balls of required kind
        
    successes = 0
    for tries in range(num_experiments):
        outcome = hat.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if outcome.count(key) < value:
                successes -= 1
                break
        successes += 1
        
    return successes/num_experiments
