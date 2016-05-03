class NonPositiveError(BaseException):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        super().append(x)

pl = PositiveList()
pl.append(1)
pl.append(2)
pl.append(-1)