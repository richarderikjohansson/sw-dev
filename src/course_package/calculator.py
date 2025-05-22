class IntCalculator:
    """
    Integer calculator
    """

    def __init__(self, expression: str):
        """Initialize class

        Args:
            expression: Expression to evaluate
        """
        self.expression = expression
        self.inp = self.parse_input()
        self.operation = self.inp[1]

    def parse_input(self):
        """Parse input

        Parse the input and throw AssertionError if the
        input is deviating
        """
        inp = self.expression.split()
        assert len(inp) == 3, "Check input"
        return inp

    def add(self):
        """Add method
        """
        return int(self.inp[0]) + int(self.inp[2])

    def subtract(self):
        """Subtract method
        """
        return int(self.inp[0]) - int(self.inp[2])

    def divide(self):
        """Divide method
        """
        return int(self.inp[0]) / int(self.inp[2])

    def multiply(self):
        """Multiply method
        """
        return int(self.inp[0]) * int(self.inp[2])

    def run(self) -> int | float:
        """Run calculator

        Returns:
            Answer
        """
        hmap = {
            "+": self.add(),
            "-": self.subtract(),
            "/": self.divide(),
            "*": self.multiply(),
        }
        res = hmap[self.operation]
        return res
