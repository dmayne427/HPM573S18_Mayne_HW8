import Parameters as P
import Classes as Cls
import HW8_SupportTS as Support

# create multiple cohorts for when the drug is not available
multiCohortNoDrug = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.MORTALITY_PROB]*P.NUM_SIM_COHORTS  # [p, p, ...]
)
# simulate all cohorts
multiCohortNoDrug.simulation()

# create multiple cohorts for when the drug is available
multiCohortWithDrug = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.MORTALITY_PROB*P.DRUG_EFFECT_RATIO]*P.NUM_SIM_COHORTS
)
# simulate all cohorts
multiCohortWithDrug.simulation()

# print outcomes of each cohort
Support.print_outcomes(multiCohortNoDrug, 'When chance of heads is 50%:')
Support.print_outcomes(multiCohortWithDrug, 'When chance of heads is 45%:')


# print comparative outcomes
Support.print_comparative_outcomes(multiCohortNoDrug, multiCohortWithDrug)
