import csv
import os

from metaflow import FlowSpec, IncludeFile, step

class CSVParser(FlowSpec):
    """This flow takes in an external CSV, parses it and prints the number of rows and columns"""

    file = IncludeFile(
        name="penguins",
        default="data/penguins.csv",
        is_text=True,
    )

    @step
    def start(self):
        print("Starting parsing...")
        self.file_name = "penguins"
        self.next(self.processing)

    @step
    def processing(self):
        print(f"Parsing {self.file_name} file...")

        try:
            # check if the file is loaded
            if not self.file:  
                raise ValueError("content not loaded!")
            
            # parse csv content from the loaded string
            reader = csv.reader(self.file.splitlines())
            rows = list(reader)

            if not rows:
                raise ValueError(f"{self.file_name} is empty!")
        
            num_rows = len(rows) - 1 if len(rows) > 1 else 0 # exclude header if present
            num_columns = len(rows[0])

            # check for malformed rows (different column counts)
            malformed = [i + 1 for i, row in enumerate(rows) if len(row) != num_columns]
            if malformed:
                raise ValueError(f"malformed rows detected at lines: {malformed}")
            
            print(f"{self.file_name} has {num_rows} rows")
            print(f"{self.file_name} has {num_columns} columns")

        except Exception as e:
            self.process_failed = True
            self.error_message = str(e)
        
        self.next(self.end)


    @step
    def end(self):
        if getattr(self, 'process_failed', False):
            print(f"Processing {self.file_name} failed with error: {self.error_message}")
        else:
            print(f"Processing {self.file_name} was completed successfully!")
        

if __name__ == "__main__":
    CSVParser()