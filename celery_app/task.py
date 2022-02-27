from celery import shared_task


@shared_task(bind=True)
def test_celery(self):
    import time

    time.sleep(3)
    for i in range(10):
        print(i)
    return "Done"
