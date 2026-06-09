import json


def load_workflow(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        workflow = json.load(
            file
        )

    return workflow


if __name__ == "__main__":

    workflow_path = input(
        "Workflow File: "
    )

    workflow = load_workflow(
        workflow_path
    )

    print(
        "\nWorkflow Loaded"
    )

    print(workflow)