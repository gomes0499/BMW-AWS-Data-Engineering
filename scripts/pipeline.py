from prefect import task, Flow
import subprocess
from datetime import timedelta
from prefect.server.schemas.schedules import CronSchedule


schedule = CronSchedule(cron="5 * * * *")


@task
def run_data_process():
    subprocess.run(["python", "data-process.py"])
    print("Data process executed successfully")

@Flow
def my_favorite_function():
    print("executed my_favorite_function successfully")
    run_data_process()

# Register the flow with Prefect
print(my_favorite_function())
