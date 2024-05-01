# Momentum Calculator

This is a Python function for calculating the momentum of a time series data over a specified period. Momentum is a measure of the rate of change in the price of a security over a specific period, and it is commonly used by traders and analysts to identify trends and potential buying or selling signals.

## Function: `momentum`

The `momentum` function calculates the momentum of a time series data over a specified period. It takes four arguments:

- `history`: A `pandas.Series` or `pandas.DataFrame` object representing the time series data of the price or value of a security.
- `period`: An integer specifying the number of data points over which momentum is calculated.
- `differential`: An optional string argument that determines how the reference value is calculated within the period. Valid options are 'last' (the default) and 'mean'.
- `method`: An optional string argument that determines the method of calculating momentum. Valid options are 'normal' (the default), 'roc', and 'roclog'.

The function returns a `pandas.Series` object containing the calculated momentum values.

## Usage

```
Import the `momentum` function and use it to calculate the momentum of a time series data:
```python
from momentum import momentum

# Create a sample time series data
history = pd.Series(np.random.randn(100), index=pd.date_range(start='2022-01-01', periods=100))

# Calculate momentum using the default parameters
momentum_values = momentum(history, period=10)

# Calculate momentum using a custom differential and method
momentum_values_custom = momentum(history, period=20, differential='mean', method='roclog')
```
In the example above, the `momentum` function is used to calculate the momentum of a sample time series data using the default parameters (`differential='last'`, `method='normal'`) and custom parameters (`differential='mean'`, `method='roclog'`). The resulting momentum values are stored in the `momentum_values` and `momentum_values_custom` variables, respectively.