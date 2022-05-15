from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notes
from .serializers import NotesSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notes(request):
    user = request.user
    # notes = Notes.objects.all()
    notes = user.notes_set.all()
    serializers = NotesSerializers(notes, many=True)
    return Response(serializers.data)
