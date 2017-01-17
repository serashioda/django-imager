from django.db import models

# Create your models here.

class User(AbstractUser):
    """."""

class Meta(AbstractUser.Meta):
    swappable = 'AUTH_USER_MODEL'

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """."""
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
        )