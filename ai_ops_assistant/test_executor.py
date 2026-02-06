from agents.planner import create_plan
from agents.executor import execute_plan

plan = create_plan("Find top 2 AI repositories and weather in Bangalore")

result = execute_plan(plan)

print(result)