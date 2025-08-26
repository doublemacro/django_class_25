from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import Book
from books.utils import send_whatsapp_message

# Register a post_save signal to trigger our notify_admin() function() whenever a Book is created in our DB.
@receiver(post_save, sender=Book)
def notify_admin(sender, instance, created, **kwargs):
    # after Book db instance created, created=True
    if created:
        # print("Message for admin: Book created in DB, with data: {}".format(instance))
        send_whatsapp_message("+4073453462", "New book created! {}".format(instance))
        # CREATE Notification in DB

print("Initialized books signal successfully!")
