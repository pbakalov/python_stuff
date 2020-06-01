import quantopian.algorithm as algo
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.filters import QTradableStocksUS
from quantopian.pipeline.filters import StaticAssets, Q500US

from quantopian.pipeline.factors import SimpleMovingAverage
import quantopian.optimize as opt


from quantopian.pipeline.data.user_5e418228b06032004658abd6 import wikipedia_pageviews


def initialize(context):
    """
    Called once at the start of the algorithm.
    """
    # Rebalance every day, 1 hour after market open.
    algo.schedule_function(
        my_rebalance,
        algo.date_rules.every_day(),
        algo.time_rules.market_open(hours=1),
    )

    '''
    # Record tracking variables at the end of each day.
    algo.schedule_function(
        record_vars,
        algo.date_rules.every_day(),
        algo.time_rules.market_close(),
    )
    '''

    # Create our dynamic stock selector.
    my_pipe = make_pipeline()
    algo.attach_pipeline(my_pipe, 'my_pipeline')

def make_pipeline():
    
    base_universe = Q500US()


    price_moving_average_20 = SimpleMovingAverage(
        inputs=[USEquityPricing.close], 
        window_length=20,
        mask = base_universe
    )
    
    current_price = USEquityPricing.close.latest
    
    
    twenty_day_momentum = (current_price - price_moving_average_20)/price_moving_average_20
    
#     '''             
    wiki_views = wikipedia_pageviews.views.latest
    wiki_views_sma10 = SimpleMovingAverage(
        inputs = [wikipedia_pageviews.views],
        window_length=10,
        mask = base_universe
    )
    
    last_open = USEquityPricing.open.latest
    one_day_momentum = (current_price - last_open)/last_open
    
    views_spike_filter = (wiki_views - wiki_views_sma10)/ wiki_views_sma10 >.2
#     '''
    
    factor1 = twenty_day_momentum  + 5*one_day_momentum    
   
    longs = factor1.top(75)
    shorts = factor1.bottom(75)
    securities_to_trade = (shorts | longs) & views_spike_filter
    
    return Pipeline(
        columns = {'longs': longs,
                   'shorts': shorts },
        screen = securities_to_trade 
    )

def compute_target_weights(context, data):
    """
    Compute ordering weights.
    """

    # Initialize empty target weights dictionary.
    # This will map securities to their target weight.
    weights = {}

    # If there are securities in our longs and shorts lists,
    # compute even target weights for each security.
    if context.longs and context.shorts:
        long_weight = 0.5 / len(context.longs)
        short_weight = -0.5 / len(context.shorts)
    else:
        return weights

    # Exit positions in our portfolio if they are not
    # in our longs or shorts lists.
    for security in context.portfolio.positions:
        if security not in context.longs and security not in context.shorts and data.can_trade(security):
            weights[security] = 0

    for security in context.longs:
        weights[security] = long_weight

    for security in context.shorts:
        weights[security] = short_weight

    return weights



def before_trading_start(context, data):
    """
    Get pipeline results.
    """

    # Gets our pipeline output every day.
    pipe_results = algo.pipeline_output('my_pipeline')

    # Go long in securities for which the 'longs' value is True,
    # and check if they can be traded.
    context.longs = []
    for sec in pipe_results[pipe_results['longs']].index.tolist():
        if data.can_trade(sec):
            context.longs.append(sec)

    # Go short in securities for which the 'shorts' value is True,
    # and check if they can be traded.
    context.shorts = []
    for sec in pipe_results[pipe_results['shorts']].index.tolist():
        if data.can_trade(sec):
            context.shorts.append(sec)

def my_rebalance(context, data):

    # Calculate target weights to rebalance
    target_weights = compute_target_weights(context, data)

    # If we have target weights, rebalance our portfolio
    if target_weights:
        algo.order_optimal_portfolio(
            objective=opt.TargetWeights(target_weights),
            constraints=[],
        )

