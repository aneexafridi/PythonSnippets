# pandas.DataFrame
# class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)[source]
# Two-dimensional, size-mutable, potentially heterogeneous tabular data.

# Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure.

# Parameters
# datandarray (structured or homogeneous), Iterable, dict, or DataFrame
# Dict can contain Series, arrays, constants, dataclass or list-like objects. If data is a dict, column order follows insertion-order.

# Changed in version 0.25.0: If data is a list of dicts, column order follows insertion-order.

# indexIndex or array-like
# Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.

# columnsIndex or array-like
# Column labels to use for resulting frame. Will default to RangeIndex (0, 1, 2, …, n) if no column labels are provided.

# dtypedtype, default None
# Data type to force. Only a single dtype is allowed. If None, infer.

# copybool, default False
# Copy data from inputs. Only affects DataFrame / 2d ndarray input.
#-_______________________Note________________
# all parameters are optional


from pandas import DataFrame,Series
print(DataFrame())