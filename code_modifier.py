from pathlib import Path

REPO = Path("../node-easy-notes-app")


def update_note_model():

    file = REPO / "app/models/note.model.js"

    text = file.read_text()

    if "tags: [String]" not in text:

        text = text.replace(
            "content: String",
            "content: String,\n    tags: [String]"
        )

        file.write_text(text)

        print("✔ Updated note.model.js")

    else:
        print("✔ note.model.js already updated")


def update_controller():

    file = REPO / "app/controllers/note.controller.js"

    text = file.read_text()

    if "tags: req.body.tags || []" not in text:

        # Add tags while creating
        text = text.replace(
            """const note = new Note({
        title: req.body.title || "Untitled Note",
        content: req.body.content
    });""",

            """const note = new Note({
        title: req.body.title || "Untitled Note",
        content: req.body.content,
        tags: req.body.tags || []
    });"""
        )

        # Add tags while updating
        text = text.replace(
            """title: req.body.title || "Untitled Note",
        content: req.body.content""",

            """title: req.body.title || "Untitled Note",
        content: req.body.content,
        tags: req.body.tags || []"""
        )

        file.write_text(text)

        print("✔ Updated note.controller.js")

    else:
        print("✔ note.controller.js already updated")


def update_routes():

    file = REPO / "app/routes/note.routes.js"

    text = file.read_text()

    if "app.get('/notes/search'" not in text:

        text = text.replace(
            "// Retrieve a single Note with noteId",

            """// Search Notes
    app.get('/notes/search', notes.findAll);

    // Retrieve a single Note with noteId"""
        )

        file.write_text(text)

        print("✔ Updated note.routes.js")

    else:
        print("✔ note.routes.js already updated")


def modify_repository():

    print("\nModifying repository...\n")

    update_note_model()
    update_controller()
    update_routes()

    print("\nRepository updated successfully.")