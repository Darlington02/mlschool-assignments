from metaflow import FlowSpec, step

class Assignment4(FlowSpec):
    """Use a foreach loop to square values in different steps then collect squared results and sum"""

    @step
    def start(self):
        self.numbers = [2, 3, 5, 7, 10]
        self.next(self.square, foreach="numbers")

    @step
    def square(self):
        self.squared_value = self.input ** 2
        self.next(self.join)

    @step
    def join(self, inputs):
        squared_values = [i.squared_value for i in inputs]
        total = sum(squared_values)

        print("squared numbers: ", squared_values)
        print("total: ", total)
        self.next(self.end)

    @step
    def end(self):
        print("Ended")


if __name__ == "__main__":
    Assignment4()