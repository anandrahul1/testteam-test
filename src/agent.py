from bedrock_agentcore import BedrockAgentCoreApp
from crewai import Agent, Task, Crew, Process
import os

app = BedrockAgentCoreApp()

# Set AWS region for litellm (used by CrewAI)
os.environ["AWS_DEFAULT_REGION"] = os.environ.get("AWS_REGION", "us-west-2")

# Template variables - will be replaced by DevEx platform
TEAM_NAME = "testteam"
AGENT_NAME = "test"
MODEL_ID = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"

# Create agent with template configuration
researcher = Agent(
    role=f"{TEAM_NAME} Research Assistant",
    goal="Provide helpful and accurate information for the team",
    backstory=f"You are a knowledgeable research assistant working for {TEAM_NAME} team",
    verbose=False,
    llm=f"bedrock/{MODEL_ID}",
    max_iter=2
)

@app.entrypoint
def invoke(payload):
    try:
        user_message = payload.get("prompt", "Hello!")
        
        # Create task for the agent
        task = Task(
            description=user_message,
            agent=researcher,
            expected_output="A helpful and informative response"
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[researcher],
            tasks=[task],
            process=Process.sequential,
            verbose=False
        )
        
        result = crew.kickoff()
        return {"result": result.raw}
        
    except Exception as e:
        app.logger.error(f"Agent error: {e}")
        return {"error": "An error occurred processing your request"}

if __name__ == "__main__":
    app.run()
