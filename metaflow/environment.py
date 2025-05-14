import os

from metaflow import FlowSpec, environment, step

class Environment(FlowSpec):
    """A flow that showcases how to use environment variables"""

    @environment(
        vars={
            "VARIABLE": f"The value is {os.getenv("METAFLOW_VARIABLE")}"
        },
    )

    @step
    def start(self):
        """Print the value of the environment variable"""
        print(os.getenv("VARIABLE"))
        self.next(self.end)

    @step
    def end(self):
        """Print the contents of the included file"""
        print(os.getenv("METAFLOW_VARIABLE"))


if __name__ == "__main__":
    Environment()