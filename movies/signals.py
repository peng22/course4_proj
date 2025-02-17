from django.db.models.signals import post_save,request_finished
from django.dispatch import receiver

from movies.models import SearchTerm

from movies.tasks import notify_of_new_search_term


@receiver(request_finished)
def signal_receiver(sender, **kwargs):
    print(f"Received signal from {sender}")


@receiver(post_save, sender=SearchTerm, dispatch_uid="search_term_saved")
def search_term_saved(sender, instance, created, **kwargs):
    if created:
        print(f"A new SearchTerm was created: '{instance.term}'")



notify_of_new_search_term.delay(instance.term)
