import Parameters as P
import Classes as Cls
import HW8_SupportSS as Support

# create a set of fair games
cohortNoDrug = Cls.MultipleGameSets(
    ids=1,
    n_games_in_a_set=P.SIM_POP_SIZE,
    prob_head=P.MORTALITY_PROB)
# simulate the cohort
noDrugOutcome = cohortNoDrug.simulation()

# create a set of unfair games
cohortWithDrug = Cls.MultipleGameSets(
    ids=2,
    n_games_in_a_set=P.SIM_POP_SIZE,
    prob_head=P.MORTALITY_PROB*P.DRUG_EFFECT_RATIO)
# simulate the cohort
withDrugOutcome = cohortWithDrug.simulation()

# print outcomes of each cohort
Support.print_outcomes(noDrugOutcome, 'When chance of heads is 50%:')
Support.print_outcomes(withDrugOutcome, 'When chance of heads is 45%:')


# print comparative outcomes
Support.print_comparative_outcomes(noDrugOutcome, withDrugOutcome)
