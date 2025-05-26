from metaflow import FlowSpec, step
import openai
import json
import os

class Students(FlowSpec):
    """This flow generates a list of dictionaries with an LLM, representing students with a name and score.
        We further then use a foreach loop to process each student on a separate branch, transforming student's
        name to uppercase and increasing their score by a fixed amount.
        We finally aggregate all scores, printing both the updated dictionaries and the agg results.
    """

    @step
    def start(self):
        print("generating dictionary of students with GPT-4...")

        # generate list of dictionaries with GPT-4
        openai.api_key = os.getenv("API_KEY")

        prompt = (
            "Generate a JSON list of 5 fictional students. Each student should have: \n"
            "1. name (string) \n"
            "2. score (integer between 10 and 100) \n"
            "Only return the json list"
        )

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        # fallback data if LLM fails to generate dictionaries
        student1 = { "name": "Darlington", "score": 92 }
        student2 = { "name": "Kevin", "score": 74 }
        student3 = { "name": "Emeka", "score": 82 }
        students = [student1, student2, student3]

        # extract and parse the generated JSON string
        content = response.choices[0].message.content
        
        try:
            self.students = json.loads(content)
        except json.JSONDecodeError:
            print("failed to parse LLM output using fallback data..")
            self.students = students
        
        print(f"Students: ", self.students)

        self.next(self.capitalize_and_increase_score, foreach="students")


    @step
    def capitalize_and_increase_score(self):
        student = self.input or ""

        print(f"capitalizing and increasing {student["name"]} score..")
        new_name = student["name"].upper()
        new_score = student["score"] + 10
        self.student = {"name": new_name, "score": new_score}

        self.next(self.join)


    @step
    def join(self, inputs):
        self.students = [i.student for i in inputs]
        self.next(self.end)

    
    @step
    def end(self):
        # print the final list of students
        print(f"Modified Students: ", self.students)

        # print the aggregated scores
        agg_score = sum([student["score"] for student in self.students])
        print(f"Aggregated scores: ", agg_score)
    

if __name__ == "__main__":
    Students()