import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    survival_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward(),
        interval=multi_cohort.get_PI_total_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          survival_mean_PI_text)




def print_comparative_outcomes(multi_cohort_no_drug, multi_cohort_with_drug):
    """ prints expected and percentage increase casino reward when chance of heads is 45%
    :param multi_cohort_no_drug: multiple cohorts simulated when chance of heads is 50%
    :param multi_cohort_with_drug: multiple cohorts simulated when chance of heads is 45%
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean casino rewards',
        x=multi_cohort_with_drug.get_all_total_rewards(),
        y_ref=multi_cohort_no_drug.get_all_total_rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in casino rewards and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in mean survival time
    relative_diff = Stat.RelativeDifferenceIndp(
        name='% increase in mean casino rewards',
        x=multi_cohort_with_drug.get_all_total_rewards(),
        y_ref=multi_cohort_no_drug.get_all_total_rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_PI(alpha=P.ALPHA),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Expected percentage increase in mean casino rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
