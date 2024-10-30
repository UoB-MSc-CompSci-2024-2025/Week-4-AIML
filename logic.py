import inspect

# Algorithm 8.1 model-checking of entailment: P ⊨ Q ⇔ M(P) ⊆ M(Q)
def model_check(P,Q):

    sig = inspect.signature(P)
    # inspect.signature() returns the arguments given to a callable (a function, for example)
    # in Problem-2.py. model_check is called with the functions 'KB() and Y()', so 'sig' holds the parameters for the function
    # 'KB()', which are 'C, O, P'

    Nparams = len(sig.parameters)
    # returns the amount of parameters there are for the function (3)

    Ntruth = 2**Nparams
    # returns two to the power of Nparams (if there are 3 parameters, returns 8 (2*2*2))

    # Step 1. Generate all possible combinations of truth values of the parameters, and the given propositions
    models = [[bool(n//(2**p)%2) for p in range(Nparams-1,-1,-1)] for n in range(Ntruth)]
    # Gives a list of all possible boolean permutations, for example, [[False, False, False], [True, True, False]] etc
    # This is so we can feed all of these permutations into the functions KB and Y, and create an exhaustive list of the outcome
    # of every single possible combination

    truthvalP = [P(*vars) for vars in models]
    # This evaluates P for each truth combination in 'models', and returns a list of 'True' or 'False'

    truthvalQ = [Q(*vars) for vars in models]
    # Does the same, but for Q
    # This value may be different than P, if the logical inference of Q is different and the same truth values don't come to the
    # same conclusion 

    # Step 2. Compute indices of models M(P), M(Q) where P and Q hold
    modelPi = [i for i in range(Ntruth) if truthvalP[i]]
    # Returns a list of index values that are 'True' in 'truthvalP', and skips any index that is 'False'
    # For example, it may look like: '[0, 2, 3, 4, 6, 7]'

    modelQi = [i for i in range(Ntruth) if truthvalQ[i]]
    # Also just does the same, but for Q

    # Step 3. Test subset -- of all models where P true, test Q also true, i.e. compute M(P) ⊆ M(Q)
    entails = set(modelPi).issubset(modelQi)
    # .issubset() returns true only if ALL items in set 'modelPi' are also existent in 'model Qi'

    return models, modelPi, modelQi, entails
