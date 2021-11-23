#lung# Initialization from a BayesianModel object
from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel
from GibbsSamplingWithEvidence import GibbsSampling
from pgmpy.inference import VariableElimination
import numpy as np
import pandas as pd
import argparse
import re
import math
import warnings

warnings.simplefilter(action='ignore',category=FutureWarning)

# This parses the inputs from test_asia.py (You don't have to modify this!)

parser = argparse.ArgumentParser(description='Asia Bayesian network')
parser.add_argument('--evidence', nargs='+', dest='eVars')
parser.add_argument('--query', nargs='+', dest='qVars')
parser.add_argument('-N', action='store', dest='N')
parser.add_argument('--exact', action="store_true", default=False)
parser.add_argument('--gibbs', action="store_true", default=False)
parser.add_argument('--ent', action="store_true", default=False)

args = parser.parse_args()

print('\n-----------------------------------------------------------')

evidence={}
for item in args.eVars:
    evidence[re.split('=|:', item)[0]]=int(re.split('=|:',item)[1])

print('evidence:', evidence)

query = args.qVars
print('query:', args.qVars)

if args.N is not None:
    N = int(args.N)

#*************************************************************************************************************************
# Using TabularCPD, defines the conditional probability distribution table for each of the node
cpd_asia = TabularCPD(variable ='asia', variable_card=2,
                      values =[[0.99], [0.01]])

cpd_smoke = TabularCPD(variable ='smoke', variable_card=2,
                       values =[[0.5], [0.5]])

cpd_tub = TabularCPD(variable ='tub', variable_card=2,
                     values =[[0.99, 0.95], [0.01, 0.05]],
                     evidence=['asia'], evidence_card=[2])

cpd_lung = TabularCPD(variable ='lung', variable_card=2,
                      values =[[0.99, 0.9], [ 0.01, 0.1]],
                      evidence=['smoke'], evidence_card=[2])

cpd_bron= TabularCPD(variable ='bron', variable_card=2,
                     values =[[0.7, 0.4], [0.3, 0.6]],
                     evidence=['smoke'], evidence_card=[2])

cpd_either = TabularCPD(variable ='either', variable_card=2,
                        values =[[0.999, 0.001, 0.001, 0.001], [0.001, 0.999, 0.999, 0.999]],
                        evidence=['lung', 'tub'], evidence_card=[2,2])

cpd_xray = TabularCPD(variable ='xray', variable_card=2,
                      values =[[0.95, 0.02], [0.05, 0.98]],
                      evidence=['either'], evidence_card=[2])

cpd_dysp = TabularCPD(variable ='dysp', variable_card=2,
                      values =[[0.9, 0.2, 0.3, 0.1], [0.1, 0.8, 0.7, 0.9]],
                      evidence=['either', 'bron'], evidence_card=[2,2])
#*************************************************************************************************************************
# Defining the edges of the asia_model (defines the whole network structure)
asia_model = BayesianModel([('asia', 'tub'),('smoke', 'lung'),('smoke', 'bron'),
                            ('tub', 'either'),('lung', 'either'),('either', 'xray'),('either', 'dysp'),
                            ('bron', 'dysp')])

# Associate the parameters with the model structure. Adding the cpds onto the network
asia_model.add_cpds(cpd_asia, cpd_tub, cpd_bron, cpd_either, cpd_smoke, cpd_lung, cpd_xray, cpd_dysp)
#*************************************************************************************************************************
# Find exact solution if args.exact is True:
#VariableElimination is used to eliminate variables and use inference
asia_model_infer = VariableElimination(asia_model)
#loop through the queries given in test_asia and printing the inference for each of the queries using VariableElimination
for var in query:
    q = asia_model_infer.query(variables=query, evidence=evidence)
    print (q[var])
#*************************************************************************************************************************
#calculating the approximate posterior probabilities for query variables using GibbsSampling
gibbs_sampler = GibbsSampling (asia_model)
#GibbsSampling used to generate samples, using the evidence and size provided (N)
samples = gibbs_sampler.sample(size=N, evidence=evidence)
#this is followed by printing out the approximate probabilities
print ('\n', samples)
print ('\n')
print ('***** Approximate Posterior Probabilities *****')
print('-----------------------------------------------------------')

#looping though anf adding up the samples needed for queries specified in test file
for i in query:
    #queries are then divided by N to get approx prob for true values and subtracted by one to get prob for false values
    Total = samples[i].sum()
    approx_prob = Total/N
    rem_prob = 1-approx_prob
    print('Approximate Posterior probability for',i, '_1 = ', approx_prob)
    print('Approximate Posterior probability for', i, '_0 = ', rem_prob, '\n')
    # Find approximate solution and cross entropy if args.gibbs is True:
    #following the total cross-entropy formula
    #cross entropy between false and true Posterior prob's for query variables
    cross_en = (rem_prob* math.log10(q[i].values[0]) + approx_prob*math.log10(q[i].values[1]))
    cross_en +=cross_en
print('-----------------------------------------------------------')
print('\nCross Entropy:', -cross_en)
#print('\n-----------------------------------------------------------')
#*************************************************************************************************************************
