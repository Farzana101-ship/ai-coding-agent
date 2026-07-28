from repository_explorer import explore_repository
from planner import create_execution_plan
from code_modifier import modify_repository
from summarizer import summarize

repo_path = "../node-easy-notes-app"

print("Scanning repository...\n")

files = explore_repository(repo_path)

plan = create_execution_plan(files)

print("\nRepository Summary")
print("-" * 40)
print(plan["repository_summary"])

print("\nExecution Plan")
print("-" * 40)

for step in plan["execution_plan"]:
    print("•", step)

print("\nFiles to Modify")
print("-" * 40)

for file in plan["files_to_modify"]:
    print(file)

modify_repository()

summarize()