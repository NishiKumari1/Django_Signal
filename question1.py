"""By default, Django signals are executed synchronously, meaning that when a signal is sent, the associated receiver functions are called in the same thread as the signal and block further execution until they complete.

To demonstrate this, here's a code snippet where a signal is sent, and we log the time to show that the signal's receiver is executed synchronously before moving on to other code:"""

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
    logging.info(f"Signal received at {time.strftime('%H:%M:%S')}. Starting task...")
    time.sleep(5)  # Simulating a long-running task
    logging.info(f"Task completed at {time.strftime('%H:%M:%S')}.")

# Simulating the user save event
def save_user():
    logging.info(f"Saving user at {time.strftime('%H:%M:%S')}")
    user = User(username="testuser")
    user.save()
    logging.info(f"User saved at {time.strftime('%H:%M:%S')}.")

# Main execution
if __name__ == "__main__":
    save_user()
    logging.info(f"Main thread continues at {time.strftime('%H:%M:%S')}")

"""Explanation:
The user_saved function is a signal receiver for the post_save signal of the User model.
When a new User is saved, the signal is triggered, and the receiver is called.
In the receiver, we simulate a 5-second delay using time.sleep(5) to represent a long-running task.
The timestamps are logged before and after the task to show when it starts and finishes."""