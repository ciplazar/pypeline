"""
A toy implementation of the forward function application
operator found in functional programming languages.
"""
from functools import partial, total_ordering


@total_ordering
class p:
    """
    Expressions like
    >>> result = pow(2, sum(map(lambda x: x+1, [1, 2, 3])))
    >>> result
    512

    can instead be written in an easier to read format that allows you
    to visually follow the flow of data through the expression:
    >>> pipe_result = p([1,2,3]) >> p(map, lambda x: x+1) >> p(sum) >> p(pow, 2)
    >>> pipe_result
    p(512)
    >>> pipe_result == result
    True

    To get the actual computed value out of the pipe use the `val` attribute:
    >>> pipe_result.val
    512
    >>> pipe_result.val == result
    True
    """
    __slots__ = ('val', 'args', 'kwargs')

    def __init__(self, val, *args, **kwargs):
        self.val = val
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return f'p({str(self.val)})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.val == other.val
        return self.val == other

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.val > other.val
        return self.val > other

    def __rshift__(self, other):
        next_func = partial(other.val, *other.args, **other.kwargs)
        self.val = next_func(self.val)
        return self


if __name__ == "__main__":
    import doctest
    doctest.testmod()
