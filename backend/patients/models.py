from django.db import models

# Create your models here.

import hashlib, hmac
from django.db import models
from django.conf import settings
from fernet_fields import EncryptedCharField, EncryptedTextField
from django.utils.crypto import get_random_string

def name_hash(name: str) -> str:
    """Generate a stable hash of the name for searching without storing plaintext."""
    key = settings.SECRET_KEY.encode()
    return hmac.new(key, name.encode(), hashlib.sha256).hexdigest()

class Patient(models.Model):
    # Public ID for references (not sensitive)
    public_id = models.CharField(max_length=32, unique=True, default= get_random_string(16))

    # Encrypted personal data
    name = EncryptedCharField(max_length=200)
    notes = EncryptedTextField(null=True, blank=True)

    # Hash for search
    name_hash = models.CharField(max_length=64, db_index=True, editable=False)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.name:
            # At save, compute hash from decrypted value
            self.name_hash = name_hash(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Patient {self.public_id}"