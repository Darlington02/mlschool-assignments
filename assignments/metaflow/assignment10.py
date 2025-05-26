import os
import openai

from metaflow import FlowSpec, Parameter, card, step

class PromptResponse(FlowSpec):
    """Prompt an LLM, get a response and visualize the prompt/response pair with a card"""

    prompt = Parameter("prompt", default="Ask the user to enter a prompt", help="prompt the LLM")

    @step
    def start(self):
        print("prompting GPT-4...")

        openai.api_key = os.getenv("API_KEY")

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": self.prompt}],
            temperature=0.7
        )

        self.content = response.choices[0].message.content
        print(self.content)

        self.next(self.visualize)

    
    @card(type="html")
    @step
    def visualize(self):
        print("visualizing prompt/response pair...")

        self.html = f"""
        <h1>Prompt/Response Pair</h1>
        <p style="background: orange; padding: 8px; width: 300px;">
            Prompt: {self.prompt}
        </p>
        <p style="background: red; padding: 8px; width: 300px;">
            Response: {self.content}
        </p>
        """
        self.next(self.end)


    @step
    def end(self):
        print("process completed!")

    
if __name__ == "__main__":
    PromptResponse()