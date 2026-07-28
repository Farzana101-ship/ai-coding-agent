def create_execution_plan(files):

    important_files = []

    for file in files:
        if "note.model.js" in file:
            important_files.append(file)

        elif "note.controller.js" in file:
            important_files.append(file)

        elif "note.routes.js" in file:
            important_files.append(file)

    plan = {
        "repository_summary":
        "Node.js Express Notes CRUD application using MongoDB.",

    "execution_plan": [
    "Explore the repository structure",
    "Identify model, controller and route files",
    "Add tags support to organize notes",
    "Implement search functionality",
    "Update CRUD operations while preserving existing behavior",
    "Generate summary of changes"
    ],

        "files_to_modify": important_files
    }

    return plan