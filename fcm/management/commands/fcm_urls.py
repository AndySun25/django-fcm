from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Show FCM urls"

    def show_line(self):
        self.stdout.write("%s\n" % ("-" * 30))

    def handle(self, **options):
        register_url = 'fcm/v1/devices'
        unregister_url = 'fcm/v1/devices/<pk>'
        self.show_line()
        self.stdout.write("FCM urls:\n")
        self.stdout.write("* Register device\n    %s\n" % register_url)
        self.stdout.write("* Unregister device\n    %s\n" % unregister_url)
        self.show_line()
