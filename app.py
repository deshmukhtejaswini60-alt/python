# app.py - Flask To-Do List Application
# A simple web-based to-do list using Flask and Jinja2 templates.

from flask import Flask, render_template, request, redirect, url_for
import os

# Initialize the Flask application
app = Flask(__name__)

# In-memory task storage (list of dicts)
# Each task has:
#   - id: unique integer identifier
#   - title: the task text
#   - completed: boolean indicating if task is done
tasks = []

# Counter to generate unique task IDs
next_id = 1


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """
    Home page: displays all tasks.
    Renders index.html with the current task list.
    """
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    """
    Add a new task (POST only).
    Reads 'title' from the form, creates a new task dict,
    appends it to the tasks list, then redirects to home.
    """
    global next_id

    title = request.form.get("title", "").strip()

    # Only add the task if the title is not empty
    if title:
        tasks.append({
            "id": next_id,
            "title": title,
            "completed": False
        })
        next_id += 1  # Increment the ID counter for the next task

    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete(task_id):
    """
    Toggle the completed status of a task.
    Finds the task by ID and flips its 'completed' boolean.
    Redirects back to home after the update.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]  # Toggle completion
            break

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    """
    Delete a task by its ID.
    Removes the matching task from the list and redirects to home.
    """
    global tasks
    # Keep all tasks except the one we want to delete
    tasks = [task for task in tasks if task["id"] != task_id]

    return redirect(url_for("index"))


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Read the port from the environment variable (set by Replit)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
