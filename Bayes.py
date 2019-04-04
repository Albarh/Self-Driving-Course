# Given three input probabilities, complete this function
# so that it returns the posterior probability

def bayes(p_A, p_B_given_A, p_notB_given_notA):
    
    ## TODO: Calculate the posterior probability
    ## and change this value
    Joint_A = p_A * p_B_given_A ; 
    Joint_B = (1.0 - p_A) * (1.0 - p_notB_given_notA) ; 
    posterior = Joint_A/(Joint_A+Joint_B);
    
    return posterior


## TODO: Change these values, run your code with them, and use print 
## statements to see the output of your function and get feedback
p_A = 0.2
p_B_given_A = 0.9
p_notB_given_notA = 0.5

posterior = bayes(p_A, p_B_given_A, p_notB_given_notA)
print('Your function returned that the posterior is: ' + str(posterior))
