import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

dates = pd.date_range("20240605", periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))       # random numbers generate around standard normal distribution (mean 0, stand devi 1)
# print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20240605"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "baa",
    }
)
# print(df2)

def viewData(df):
    print(df.dtypes)         # types of data (float, integer, category...)
    print(df.head(3))        # first 3 rows
    print(df.tail(3))        # last 3 rows
    print(df.index)          # gives indexs
    print(df.columns)        # gives columns
    print(df.to_numpy())     # just data
    print(df.describe())     # gives summary of data
    print(df.T)              # rows = column, column = rows
    print(df.sort_index(axis=1, ascending=False))   # sorts by index
    print(df.sort_values(by="B"))                   # sorts by value

# viewData()

def selection(df):
    print(df["A"])                    # gets only row A and the index and type of data
    print(df[0:3])                    # gets the matching rows
    print(df["20240605":"20240608"])  # gets matching row from index 
    print(df.loc[dates[0]])           # gets a row matching a label/index
    print(df.loc[:, ["A", "B"]])      # gets data for coloumnS mentioned
    print(df.loc["20240605":"20260608", ["A", "B"]])     # gets data for index mentioned and column mentioned
    print(df.loc[dates[0], "A"])      # gets term from point
    print(df.at[dates[0], "A"])       # same thing
    print(df.iloc[3])                 # gets the row using idex at mentioned index
    print(df.iloc[3:5, 0:2])          # gets mentioned rows then mentioned columns    [row, index]
    print(df.iloc[[1, 2, 4], [0, 2]]) # selects specific rows then columns
    print(df.iloc[1:3, :])            # selects rows then all columns
    print(df.iloc[:, 1:3])            # selects columns then all rows
    print(df.iloc[1, 1])              # gets term at specific point 
    print(df.iat[1, 1])               # same thing
    print(df[df["A"] > 0])            # gets values in slected column that meets condition
    print(df[df > 0])                 # shows value that meet condition, others become NaN
    df2 = df.copy()                   # copies a data_frame
    df2["E"] = ["one", "one", "two", "three", "four", "three"]       # adds a column to the data frame
    print(df2)                        # prints new data frame
    print(df2[df2["E"].isin(["two", "four"])])            # prints rows/index where mentioned coloumn meets either condition
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20240605", periods=6))
    print(s1)                         # prints data with only index no top bar
    df["F"] = s1                      # new row "F" becomes s1 is added to df
    df.at[dates[0], "A"] = 0          # mentioned term becomes 0
    df.iat[0, 1] = 0                  # mentioned term becomes 0
    df.loc[:, "D"] = np.array([5] * len(df))              # all rows/index terms in coloumn mentioned becomes number before len(df), len(df) cannot be changed
    print(df)                         # print updated data_frame
    df2 = df.copy()                   # df is copied onto df2
    df2[df2 > 0] = -df2               # df2 positive terms become negative

# selection(df)

def missingdata(df):
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20240605", periods=6))
    print(s1)
    df["F"] = s1
    df.at[dates[0], "A"] = 0          
    df.iat[0, 1] = 0                  
    df.loc[:, "D"] = np.array([5] * len(df))
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])     # adds another column E and remove the index/rows not mentioned
    df1.loc[dates[0] : dates[1], "E"] = 1   # sets the first two items in column E to 1
    print(df1)
    print(df1.dropna(how="any"))            # prints data but drops rows with NaN in it
    print(df1.fillna(value=5))              # replaces NaNs with 5
    print(pd.isna(df1))                     # replaces values with true or false, NaN = true

# missingdata(df)

def operations(df):
    print(df.mean())                               # gets the mean value for each column, does not get missing data
    print(df.mean(axis=1))                         # gets the mean value for each row, does not get missing data
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)    # creates s as a series using the df index and removes extras and fills extras with NaN and shifts by mentione dvalue
    print(df.sub(s, axis="index"))                 # uses s to determine rows/index to generate random numbers following df rules along
    print(df.agg(lambda x: np.mean(x) * 5.6))      # gets the mean of each row and multiplies it by 5.6
    print(df.transform(lambda x: x * 101.2))       # multiplies each value by 101.2
    s = pd.Series(np.random.randint(0, 7, size=10))                 # creates a series with 10 terms randomizing between 0 and 7
    print(s.value_counts())                        # it gives the number that occurs the most to occurs the least in order and how many times it occured
    s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
    print(s.str.lower())                           # gives the series but all lowercase letters

# operations(df)

def merge(df):
    df = pd.DataFrame(np.random.randn(10, 4))      # gives a 10x4 array with random numbers
    pieces = [df[:3], df[3:7], df[7:]]             # seperates the data frame into segments row 0 to 3, 3 to 7, and 7 to the end
    print(pd.concat(pieces))                       # puts dataframe "pieces" together stacking vertically from left to right
    left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})        # creates a data frame where key and lval are on the top and the terms are put together correspondingly
    right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})       # creates a data frame where key and rval are on the top and the terms are put together correspondingly
    print(pd.merge(left, right, on="key"))         # merges data frames lef tand right based on key similar to multiplication 1 4 1 5 and 2 4 2 5 in order
    left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
    right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
    print(pd.merge(left, right, on="key"))         # merges data frames lef tand right based on key but is in order 1 4 and 2 5 (only when they are different)

# merge(df)

def grouping(df):
    df = pd.DataFrame(                              # new data frame
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.random.randn(8),
        }
    )
    print(df)
    print(df.groupby("A")[["C", "D"]].sum())        # groups the data frame into foos and bars/unique terms ten takes the sum of the terms in row C and D for each group
    df.groupby(["A", "B"]).sum()                    # groups the data frame into foos and bars and sub sections of one two or threes then adds up the sums for C and D

# grouping(df)

def reshaping(df):
    arrays = [                                      # create a list of lists or list of arrays
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    ]
    index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])         # lines up the terms and pairs them
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])    # it uses the groups created during index and creates columns A and B assigning random values
    df2 = df[:4]                                    # uses only the first 4 rows of the data frame and assigns it to df2
    print(df2)
    stacked = df2.stack(future_stack=True)          # stacks the groups vertically in a  long list
    print(stacked)
    print(stacked.unstack())                        # creates column B and A and align them with the ones and twos (unstacking the last row)
    print(stacked.unstack(1))                       # unstacks the second row
    print(stacked.unstack(0))                       # unstacks the first row
    df = pd.DataFrame(                              # creates a 12 * 5 data frame where * n means repeating it n times
        {
            "A": ["one", "one", "two", "three"] * 3,
            "B": ["A", "B", "C"] * 4,
            "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
            "D": np.random.randn(12),
            "E": np.random.randn(12),
        }
    )
    print(df)

# reshaping(df)

def timeseries():
    rng = pd.date_range("6/5/2024", periods=100, freq="s")           # creates 100 data points 1 point = 1 second
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)   # gives a array of random integers and becomes a series using values from rng
    print(ts.resample("5Min").sum())                                 # calculates the sum of values withen 5 minute interval
    rng = pd.date_range("6/5/2024 00:00", periods=5, freq="D")       # same as line 159 but 1 point = 1 day and it starts at 00:00
    ts = pd.Series(np.random.randn(len(rng)), rng)                   # same as line 160
    print(ts)                                                        # prints as a series with dates and values
    ts_utc = ts.tz_localize("UTC")                                   # sets it to UTC timezone
    print(ts_utc)
    ts_utc.tz_convert("US/Eastern")                                  # sets it to another timezone
    print(ts_utc)
    print(rng)
    print(rng + pd.offsets.BuisnessDay(5))

timeseries()

def categorials():
    df = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
    )
    df["grade"] = df["raw_grade"].astype("category")
    df["grade"]