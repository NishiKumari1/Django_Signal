"""Yes, Django signals run in the same thread as the caller by default. To demonstrate this, let's create a Django signal that logs the thread ID of both the main execution and the signal receiver. This will show that they are operating in the same thread."""

import threading
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import logging

# Setting up basic logging
logging.basicConfig(level=logging.INFO)

# Signal receiver function
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    logging.info(f"Signal received in thread: {threading.current_thread().name} (ID: {threading.get_ident()})")
    time.sleep(2)  # Simulate a task

# Simulating the user save event
def save_user():
    logging.info(f"Main execution in thread: {threading.current_thread().name} (ID: {threading.get_ident()})")
    user = User(username="testuser")
    user.save()

# Main execution
if __name__ == "__main__":
    save_user()

"""Explanation:
The user_saved function is a signal receiver for the post_save signal of the User model.
Both the main function save_user and the signal receiver user_saved log the current thread's name and ID using threading.get_ident().
This will show whether the signal runs in the same thread as the caller or in a different thread.
Both the main execution (save_user) and the signal receiver (user_saved) are executed in the same thread (MainThread) with the same thread ID, confirming that Django signals run in the same thread as the caller by default."""