import scr.FormatFunctions as Format
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param sim_output: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of average game rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          survival_mean_CI_text)



def print_comparative_outcomes(sim_output_no_drug, sim_output_with_drug):
    """ prints expected and percentage increase in survival time when drug is available
    :param sim_output_no_drug: output of a fair game
    :param sim_output_with_drug: output of an unfair game
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in casino rewards',
        x=sim_output_with_drug.get_rewards(),
        y_ref=sim_output_no_drug.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Average increase in casino rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in survival time
    relative_diff = Stat.RelativeDifferenceIndp(
        name='Average % increase in casino rewards',
        x=sim_output_with_drug.get_rewards(),
        y_ref=sim_output_no_drug.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Average percentage increase in survival time and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
