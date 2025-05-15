from metaflow import FlowSpec, step, retry

class Assignment5(FlowSpec):
    """Demonstrates retries"""

    @retry(times=4, minutes_between_retries=0.5)
    @step
    def start(self):
        import time

        if int(time.time()) % 2 == 0:
            raise Exception("Bad luck! retrying...")
        else:
            print("Lucky you!")

        self.next(self.end)

    @step
    def end(self):
        print("done!")

    
if __name__ == '__main__':
    Assignment5()