import schedule
import time


def run_scheduled_task(job_function, time_str):
    schedule.every().day.at(time_str).do(job_function)
    print(f"[🕒] Scheduled job at {time_str}")

    while True:
        schedule.run_pending()
        time.sleep(60)