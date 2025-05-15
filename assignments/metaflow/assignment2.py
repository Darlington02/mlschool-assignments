from metaflow import FlowSpec, step

class Assignment2(FlowSpec):
    """Simple flow that tracks a sequence of numerical operations"""

    @step
    def start(self):
        self.variable = 1
        self.list = [1]
        self.next(self.add)

    @step
    def add(self):
        self.variable += 5
        self.list.append(self.variable)
        self.next(self.subtract)

    @step
    def subtract(self):
        self.variable -= 2
        self.list.append(self.variable)
        self.next(self.multiply)

    @step
    def multiply(self):
        self.variable *= 2
        self.list.append(self.variable)
        self.next(self.end)

    @step
    def end(self):
        "Print the entire history of values, the sum and average"
        total = sum(self.list)
        average = total / len(self.list)

        print("values history: ", self.list)
        print("values sum: ", total)
        print("values average: ", average)


if __name__ == "__main__":
    Assignment2()