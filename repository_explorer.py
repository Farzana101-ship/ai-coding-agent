import os

IMPORTANT_FILES = [
    "README.md",
    "Readme.md",
    "package.json",
    "note.model.js",
    "note.controller.js",
    "note.routes.js"
]


def explore_repository(repo_path):
    print("🔍 Scanning Repository...\n")

    important_files = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in ["node_modules", ".git"]]

        for file in files:

            if file in IMPORTANT_FILES:
                filepath = os.path.join(root, file)
                important_files.append(filepath)

    return important_files


def read_file(filepath):

    print("\n" + "=" * 60)
    print(f"📄 {filepath}")
    print("=" * 60)

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

    return content