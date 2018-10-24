from users.models import User
from django.utils import timezone
def createBasicUser(username):
    user = User.objects.create(
            username=username,
            create_time=timezone.now()
        )
    user.save()
