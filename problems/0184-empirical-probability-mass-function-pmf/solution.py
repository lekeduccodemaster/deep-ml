def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    b = list(set(samples))
    st = []
    for element in b:
        st.append((element, samples.count(element) / len(samples)))
    return st
    pass