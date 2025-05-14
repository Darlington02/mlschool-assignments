from metaflow import FlowSpec, step

class Introduction(FlowSpec):
    """
    A basic, linear flow with four steps.
    """

    @step
    def start(self):
        """
        Every flow must start with a step called `start`.
        """
        print("Starting the flow!")
        self.next(self.step_a)

    @step
    def step_a(self):
        """Follows the 'start' step."""
        print("Step A")
        self.next(self.step_b)

    @step
    def step_b(self):
        """Follows the 'step_a' step."""
        print("Step B")
        self.next(self.end)

    @step
    def end(self):
        """The last step in the flow."""
        print("Ending the flow!")

if __name__ == "__main__":
    Introduction()
        
    