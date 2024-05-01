import numpy as np
import pandas as pd

def momentum(history, period, differential='last', method='normal'):
    """
    Calculates the momentum of a time series data over a specified period.

    Momentum measures the rate of change in the price of a security over a specific period.
    It is commonly used by traders and analysts to identify trends and potential buying or selling signals.

    Parameters:
    - history (pd.Series or pd.DataFrame): Time series data representing the price or value of a security.
    - period (int): The number of data points over which momentum is calculated.
    - differential (str, default='last'): Determines how the reference value is calculated within the period.
        - 'last': Uses the last value within the rolling window as the reference value.
        - 'mean': Uses the mean (average) value within the rolling window as the reference value.
    - method (str, default='normal'): Determines the method of calculating momentum.
        - 'normal': Calculates the difference between the current value and the reference value.
        - 'roc': Calculates the Rate of Change (ROC) as a percentage.
        - 'roclog': Calculates the logarithmic Rate of Change (ROC) as a percentage.

    Returns:
    - pd.Series: Series containing the calculated momentum values.
    """
    # Calculate the reference values based on the selected method
    if differential == 'last':
        ctx = history.rolling(window=period).apply(lambda x: x[0], raw=True).dropna()
    elif differential == 'mean':
        ctx = history.rolling(window=period).mean().dropna()

    # Reindex the original history to align with the reference values
    ct = history.reindex(ctx.index)

    # Calculate momentum based on the selected method
    if method == 'normal':
        mo = ct - ctx
    elif method == 'roc':
        mo = 100 * ct / ctx
    elif method == 'roclog':
        mo = 100 * np.log(np.array(ct / ctx))
        mo = pd.Series(mo, index=history.index[-len(ct):])
    return mo
