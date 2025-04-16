from prefect import flow

SOURCE_REPO="https://github.com/joshneland/prefect_testing.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="my_workflow.py:my_workflow",
    ).deploy(
        name="my-workflow",
        work_pool_name="my-work-pool",
        parameters={"numruns": 10},
    )
