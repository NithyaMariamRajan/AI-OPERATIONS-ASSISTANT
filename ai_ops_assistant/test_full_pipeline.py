from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import generate_response

user_query = "Find top 2 AI repositories and weather in Bangalore"

# Step 1: Plan
plan = create_plan(user_query)
print("PLAN:")
print(plan)

# Step 2: Execute
execution_result = execute_plan(plan)
print("\nEXECUTION:")
print(execution_result)

# Step 3: Final Response
final_answer = generate_response(user_query, execution_result)
print("\nFINAL ANSWER:")
print(final_answer)