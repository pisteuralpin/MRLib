# ----------------------------------------------------------- #
#                       Display module                        #
#                   ©2023 Mathurin Roulier                    #
# ----------------------------------------------------------- #

"""
This module contains functions missing in the standard libraries.

mov_avg
----
Calculates the moving average of a list of numbers.

"""

def mov_avg(data:list, n:int) -> list[float]:
    """Calculates the moving average of a list of numbers."""
    return [sum(data[i:i+n])/n for i in range(len(data)-n+1)]