"""Tasks file for commands that are run regularly"""
import os
from invoke import task

# Set the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

@task
def quality_all(c):
    """
    Run all pytest tests verbosely.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -vv")

@task
def quality_stack_unit(c):
    """
    Run Stack Unit Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m stack_unit_test -vv")

@task
def quality_stack_bdd(c):
    """
    Run Stack BDD Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m stack_bdd_test -vv")

@task
def quality_stack_acceptance(c):
    """
    Run Stack Acceptance (UI) Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m stack_acceptance_test -vv")


@task
def quality_integration(c):
    """
    Run integration tests
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m graph_integration_test -vv")

@task
def quality_queue_acceptance(c):
    """
    Run Stack Acceptance (UI) Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m queue_acceptance_test -vv")


@task
def quality_queue_unit(c):
    """
    Run Queue Unit Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m queue_unit_test -vv")

@task
def quality_queue_bdd(c):
    """
    Run Queue BDD Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m queue_bdd_test -vv")

@task
def quality_graph_unit(c):
    """
    Run Graph Unit Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m graph_unit_test -vv")

@task
def quality_graph_bdd(c):
    """
    Run Graph BDD Tests.
    """
    with c.cd(project_root):
        c.run("python3 -m pytest -m graph_bdd_test -vv")

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

@task
def app(c):
    """
    Run the web application.
    """
    with c.cd(project_root):
        c.run("python3 run.py")
