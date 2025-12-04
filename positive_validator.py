def require_positive(function):
    def wrapper(lam, mu, *args, **kwargs):
        if lam <= 0 or mu <=0:
            raise ValueError("λ and μ must be positive numbers.")
        return function(lam, mu, *args, **kwargs)
    return wrapper