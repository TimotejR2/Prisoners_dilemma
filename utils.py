
from config import COMPARE_SAME
from typing import Callable, List, Tuple

def get_pairs(ALL_STRATEGIES: List[Callable]) -> List[Tuple[Callable, Callable]]:
    """
    Generate pairs of elements from ALL_STRATEGIES based on COMPARE_SAME flag.
    
    Args:
        ALL_STRATEGIES (List[Callable]): A list of strategies to generate pairs from.
        Must not be None.
    
    Returns:
        List[Tuple[Callable, Callable]]: A list of tuples representing pairs of strategies.
        Will not be None.
    """
    if ALL_STRATEGIES is None:
        raise ValueError("ALL_STRATEGIES must not be None")
    
    pairs: List[Tuple[Callable, Callable]] = []
    # Generate all possible pairs but do not include the same strategy
    if not COMPARE_SAME:
        for i in range(len(ALL_STRATEGIES)):
            for j in range(i+1, len(ALL_STRATEGIES)):
                pairs.append((ALL_STRATEGIES[i], ALL_STRATEGIES[j]))

    # Generate all possible pairs including the same strategy
    else:
        for i in range(len(ALL_STRATEGIES)):
            for j in range(len(ALL_STRATEGIES)):
                pairs.append((ALL_STRATEGIES[i], ALL_STRATEGIES[j]))
                
    if pairs is None:
        raise ValueError("pairs must not be None")
        
    return pairs

        