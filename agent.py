class Agent:
    def __init__(self, values:list[int]) -> None:
        self.__values = values

    def value(self, option:int) -> float:
        """
        INPUT: The index of an option
        OUTPUT: The value of the option (to the agent).
        """
        return self.__values[option]

    def len(self):
        return len(self.__values)