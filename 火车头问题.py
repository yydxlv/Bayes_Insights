__author__ = 'xilin'
from dice import Dice
import thinkplot

class Train(Dice):
    """Represents hypotheses about how many trains the company has.
    The likelihood function for the train problem is the same as
    for the Dice problem.
    """


def main():
    hypos = range(1, 1001)
    suite = Train(hypos)

    suite.Update(60)
    print(suite.Mean())

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    thinkplot.Save(root='train1',
                   xlabel='Number of trains',
                   ylabel='Probability',
                   formats=['pdf', 'eps'])


if __name__ == '__main__':
    main()
