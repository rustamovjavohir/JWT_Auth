from rest_framework.serializers import ModelSerializer
from .models import Notes


class NotesSerializers(ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
