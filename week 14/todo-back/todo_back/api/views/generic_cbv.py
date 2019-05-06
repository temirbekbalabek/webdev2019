from api.models import Task, TaskList
from django.contrib.auth.models import User
from api.serializers import TaskListSerializer2, TaskListSerializer,TaskSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import TaskFilter
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class TaskLists(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)


class TaskListTasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filterset_fields = ('name', 'status')
    filter_class = TaskFilter
    # pagination_class = LimitOffsetPagination
    search_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('-name', )

    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise Http404
        queryset = task_list.tasks.all()
        # name = self.request.query_params.get('name', None)
        # status = self.request.query_params.get('status', None)
        # if name is not None and status is not None:
        #     queryset = queryset.filter(name=name).filter(status=status)
        return queryset

