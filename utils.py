from typing import Callable, List, Tuple

from config import COMPARE_SAME

def get_pairs(all_strategies: List[Callable]) -> List[Tuple[Callable, Callable]]:
    """
    Generate pairs of elements from all_strategies based on COMPARE_SAME flag.
    
    Args:
        all_strategies (List[Callable]): A list of strategies to generate pairs from.
        Must not be None.
    
    Returns:
        List[Tuple[Callable, Callable]]: A list of tuples representing pairs of strategies.
        Will not be None.
    """
    if all_strategies is None:
        raise ValueError("all_strategies must not be None")

    pairs: List[Tuple[Callable, Callable]] = []
    # Generate all possible pairs but do not include the same strategy
    if not COMPARE_SAME:
        for i in range(len(all_strategies)):
            for j in range(i+1, len(all_strategies)):
                pairs.append((all_strategies[i], all_strategies[j]))

    # Generate all possible pairs including the same strategy
    else:
        for i in range(len(all_strategies)):
            for j in range(len(all_strategies)):
                pairs.append((all_strategies[i], all_strategies[j]))

    if pairs is None:
        raise ValueError("pairs must not be None")

    return pairs
        