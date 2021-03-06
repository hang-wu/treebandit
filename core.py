# Convenience functions
def ind_max(x):
  m = max(x)
  return x.index(m)

# Need access to random numbers
import random
import numpy as np

# Definitions of bandit arms
from arms.adversarial import *
from arms.bernoulli import *
from arms.normal import *
from arms.tree import *

# Definitions of bandit algorithms
from algorithms.epsilon_greedy.standard import *
from algorithms.epsilon_greedy.annealing import *
from algorithms.softmax.standard import *
from algorithms.softmax.annealing import *
from algorithms.ucb.ucb1 import *
from algorithms.ucb.ucb2 import *
from algorithms.exp3.exp3 import *
from algorithms.hedge.hedge import *
from algorithms.racing.racing import *
from algorithms.bast.bast import *
from algorithms.bast2.bast2 import *
#from algorithms.bast_exp.bast_exp import *
from algorithms.bast_exp.bast_exp2 import *
from algorithms.LUCB.LUCB import *

# Confidence methods
from algorithms.methods.confidence_methods import *

# Testing framework
from testing_framework.tests import *
from testing_framework.tests_for_PE import *
