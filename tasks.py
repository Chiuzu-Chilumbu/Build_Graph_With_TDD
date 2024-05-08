"""Tasks file for commands that are run regularly"""
import os
from invoke import task

# Set the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

@task
def quality(c):
    """
    Run the pytest tests verbosely.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -vv")

@task
def coverage(c):
    """
    Run the pytest tests with coverage report.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest --cov=./ --cov-report html:coverage")

@task
def reports(c):
    """
    Run the pytest tests and generate JUnit XML report.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest --junitxml=reports/test-results.xml")


