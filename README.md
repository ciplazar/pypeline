Pypeline
--------

A toy implementation of the forward function application
operator found in functional programming languages.

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

The module includes doctests. To run them:
> python pypeline.py
