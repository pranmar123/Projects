#Creating a CartPole simulation

#gym is used to create environments to run simulations using our AI
import gym

#using module gym to create the environment
environment = gym.make('CartPole-v0')

#actions that the AI will take
def basic_policy(observations):
    #observations is the where the pole is moving
    #observations[2] is the ANGLE value
    angle = observations[2]

    #one variable of the timestep. We can have multiple like angle,
    #velocity, how fast the cart is moving, etc. but in this example
    #we will only return the action based on the angle. 
    if angle < 0:
        return 0
    else:
        return 1
    return

    
#list of total rewards accumulated
totals = []

#loop for number of simulations we want to run
for episode in range(10):
    #keeps track of how long the maintence of the pole is obtained
    episode_rewards = 0
    
    #observe the variables that make up the environment in this case that is
    #the pole.
    observations = environment.reset()

    #move the cart left or right
    action = 0

    #loop that determines the action we take at each timestep and how many timesteps
    #in each episode
    for step in range(1000):
        action = basic_policy(observations) #gets the action that must be taken
        environment.render() #this enables us to see what is going on

        #observations: observations about environment
        #reward: at each timestep we see if the reward is reached
        #in this scenario we want to keep the pole balanced
        #done: represents true or false to see if the simulation is over if objective is
        #failed
        #info: variable to debugging
        observations, reward, done, info = environment.step(action) #executes the action

        #add the reward at each timestep
        episode_rewards += reward

        #if done is true then that means that the simulation is over
        if done:
            totals.append(episode_rewards)
            break

print(totals)
print("The longest number of timesteps the pole was balanced: " +str(max(totals)))
    
    
