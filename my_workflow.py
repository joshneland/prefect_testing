from prefect import flow, task
import time

@flow(log_prints=True)
def my_workflow():
    print("Kicking off workflow")

    for i in range(10):
        print(f"Processing item {i}")
        process(i)
        time.sleep(1)

    print("Workflow completed")

@task(log_prints=True)
def process(i: int):
    print(f"Processing item {i}")


if __name__ == "__main__":
    my_workflow()