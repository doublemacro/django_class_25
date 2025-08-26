from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

    # ready() gets called after django is setup successfully:
    def ready(self):
        print("Django setup successfully! Initializing books signal!")
        # Register implemented signals in app. Won't get triggered without this.
        import books.signals
