from metaflow import FlowSpec, step

class Artifacts(FlowSpec):
    """
    A flow that showcases how artifacts work
    """

    @step
    def start(self):
        """Initialize the variable"""
        self.variable = 1
        print("Initial value: ", self.variable)
        self.next(self.increment)

    @step
    def increment(self):
        """Increments the value of the variable"""
        self.variable += 2
        self.next(self.end)

    @step
    def end(self):
        """Prints the final value of the variable"""
        print("Final value: ", self.variable)
        
if __name__ == "__main__":
    Artifacts()