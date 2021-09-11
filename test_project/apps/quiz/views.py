from django.shortcuts import render

import datetime
import logging

from rest_framework import viewsets, decorators, response

from .serializers import *

from .models import *

from .permissions import *


logger = logging.getLogger(__name__)


class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (QuizPermission, )


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (QuestionPermission, )


class SolutionViewSet(viewsets.ModelViewSet):

    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    http_method_names = ('get', 'post')

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)

        return super().perform_create(serializer)
