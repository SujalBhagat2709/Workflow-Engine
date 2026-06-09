import time

from workflow_parser import (
    load_workflow
)


def execute_step(step):

    action = step["action"]

    print(
        f"\n▶ Executing: "
        f"{action}"
    )

    time.sleep(1)

    print(
        f"✓ Completed: "
        f"{action}"
    )


def run_workflow(
    workflow_path
):

    workflow = load_workflow(
        workflow_path
    )

    print(
        "\n===================="
    )

    print(
        "WORKFLOW ENGINE"
    )

    print(
        "===================="
    )

    print(
        f"\nWorkflow: "
        f"{workflow['name']}"
    )

    for step in workflow[
        "steps"
    ]:

        execute_step(step)

    print(
        "\n🚀 Workflow Finished"
    )


if __name__ == "__main__":

    workflow_path = input(
        "Workflow File: "
    )

    run_workflow(
        workflow_path
    )