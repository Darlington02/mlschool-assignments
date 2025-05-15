from metaflow import FlowSpec, step

class Assignment3(FlowSpec):
    """Initialize artifact, split into branches"""

    @step
    def start(self):
        self.variable = 1
        self.next(self.branch1, self.branch2)

    @step
    def branch1(self):
        self.variable += 2
        self.next(self.join)

    @step
    def branch2(self):
        self.variable *= 2
        self.next(self.join)

    @step
    def join(self, inputs):
        self.merge_artifacts(inputs, exclude=["variable"])

        print("branch1 value: ", inputs.branch1.variable)
        print("branch2 value: ", inputs.branch2.variable)

        self.total = sum(i.variable for i in inputs)
        self.next(self.end)

    @step
    def end(self):
        print("final value: ", self.total)


if __name__ == "__main__":
    Assignment3()
        
        