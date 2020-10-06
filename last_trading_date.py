import datetime
import pandas as pd
from pandas.tseries.offsets import BDay


def last_trading_date():
    """Function that returns a string of the last business day as a string in the form YYYY-MM-DD"""

    # String storing the last business day and start time
    with_time = str(datetime.date.today() - BDay(1))

    # Remove the time from the string
    return with_time[0:11]

