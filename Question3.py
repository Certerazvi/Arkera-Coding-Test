columns = {'id': 0, 'url': 1, 'date': 2, 'rating': 3}


class Data:

    def __init__(self, data):
        if isinstance(data, Data):
            self.table = data.table
        else:
            if any(len(row) != len(columns) for row in data):
                raise ValueError(
                    "All rows need to be of size %d." % len(columns))
            self.table = data

    def query(self):
        return self.table


class GreaterThan(Data):

    def __init__(self, column, value, data):
        Data.__init__(self, data)
        valid = {'id', 'date', 'rating'}
        if column not in valid:
            raise ValueError("Column name must be one of %s when using %s "
                             "operation." % (valid, self.__class__.__name__))
        col_id = columns[column]
        self.table = [row for row in self.table if row[col_id] > value]


class LowerThan(Data):

    def __init__(self, column, value, data):
        Data.__init__(self, data)
        valid = {'id', 'date', 'rating'}
        if column not in valid:
            raise ValueError("Column name must be one of %s when using %s "
                             "operation." % (valid, self.__class__.__name__))
        col_id = columns[column]
        self.table = [row for row in self.table if row[col_id] < value]


class Equals(Data):

    def __init__(self, column, value, data):
        Data.__init__(self, data)
        valid = {'id', 'date', 'url', 'rating'}
        if column not in valid:
            raise ValueError("Column name must be one of %s when using %s "
                             "operation." % (valid, self.__class__.__name__))
        col_id = columns[column]
        self.table = [row for row in self.table if row[col_id] == value]


class In(Data):

    def __init__(self, column, value, data):
        Data.__init__(self, data)
        valid = {'id'}
        if column not in valid:
            raise ValueError("Column name must be one of %s when using %s "
                             "operation." % (valid, self.__class__.__name__))
        col_id = columns[column]
        self.table = [row for row in self.table if row[col_id] in value]


class NotIn(Data):

    def __init__(self, column, value, data):
        Data.__init__(self, data)
        valid = {'id'}
        if column not in valid:
            raise ValueError("Column name must be one of %s when using %s "
                             "operation." % (valid, self.__class__.__name__))
        col_id = columns[column]
        self.table = [row for row in self.table if row[col_id] not in value]
