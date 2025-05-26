import os

from metaflow import FlowSpec, environment, step

class Environment(FlowSpec):
    """A flow that compares the use of @environment and python-dotenv"""
    
    @step
    def start(self):
        print("This flow compares the use of @environment and python-dotenv when accessing environment variables.")
        self.next(self.use_metaflow_env)


    @environment(
        vars={
            "METAFLOW_VARIABLE": os.getenv("ENV_VAR")
        }
    )
    @step
    def use_metaflow_env(self):
        print(f"Environment variable from @environment: {os.getenv('METAFLOW_VARIABLE')}")
        self.next(self.use_dotenv)


    @step
    def use_dotenv(self):
        print(f"Environment variable from python-dotenv: {os.getenv('ENV_VAR')}")
        self.next(self.compare)


    @environment(
        vars={
            "METAFLOW_VARIABLE": os.getenv("ENV_VAR")
        }
    )
    @step
    def compare(self):
        if os.getenv("METAFLOW_VARIABLE") and os.getenv("ENV_VAR"):
            print("This was ran locally, both env variables were retrieved successfully.")
        elif os.getenv("METAFLOW_VARIABLE") and not os.getenv("ENV_VAR"):
            print("This was ran in a remote env, only the @environment variable was retrieved successfully.")
        else:
            print("There was an issue retrieving the environment variables.")

        self.next(self.end)


    @step
    def end(self):
        print("Flow completed.")
        

if __name__ == "__main__":
    Environment()
