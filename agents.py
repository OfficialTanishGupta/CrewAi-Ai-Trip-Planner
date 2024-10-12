from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from Tools.serach_tools import SearchTools
from Tools.calculator_tools import CalculatorTools


"""Creating Agents Cheat Sheet:
    -Think like a boss.Work backwards from the goal and think which
       employee you need to hire to get the job done.
    -define the captain of the crew who orient the other agents towards the goal.
    -define which experts the captain needs to communicate with delegate tasks to 
       Build a top down structure of the crew.

    Goal:
    -create a 7-day travel Planner ,itinearary with detailed per-day plans,
      including budget, packagind suggestions , and safety tips.
    
    Captain/Manager/Boss:
    -Expert Travel Agent
    
    Employees/Experts to hire:
    -City Selection Expert
    -Local Tour Guide
    
    
    Notes:
    -agents should be result driven and have a clear goal in mind
    -role is their job title
    -Goals shold actionable
    -Backstory should be their resume
    """

model_name="gpt-3.5-turbo"  # Verify if this is accepted in your langchain_openai version
# model_name="gpt-4"  # Check if this name is supported


class TravelAgents:
    def __init__(self):
       self.OpenAIGPT35 = ChatOpenAI(model=model_name,temperature=0.7)  # Remove model_name
    #    self.OpenAIGPT4 = ChatOpenAI(temperature=0.7)  # Remove model_name
        
    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logisitcs. I have decades of experience making travel iteneraries"""),
            goal=dedent(f"""Create a 7-day travel itinerary with detailed per-day plans,
                        including budget, packaging suggestions, and safty tips."""),
            tools=[SearchTools.search_internet,
                   CalculatorTools.calculate],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analysing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best Cities based on weather, season,prices,travel intrest."""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city, it's attractions and
                             customs"""),
            goal=dedent(f"""Provide the best insights about the selected city"""),
            tools=[SearchTools.search_internet],
            # allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )