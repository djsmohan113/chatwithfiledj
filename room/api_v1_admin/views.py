from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from room.models import roomMessageModel
from .serializers import roomMessageSerializer



# @api_view(['GET'])
# def get_room_data(request, room_id):
#     try:
#         room_msg = roomMessageModel.objects.filter(room__id=room_id)
#         serializer = roomMessageSerializer(room_msg, many=True)
#         return Response(serializer.data)
#     except roomMessageModel.DoesNotExist:
#         return Response(status=404)


class roomAdminGetUserMessagesGenericsView(generics.ListAPIView):
    serializer_class = roomMessageSerializer
    queryset = roomMessageModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = LimitOffsetPagination
    # search_fields = ['status', 'vehicle__vehicle_name', 'vehicle__vehicle_number', 'vehicle__type__title']
    # filter_backends = (filters.SearchFilter, dj_filter.DjangoFilterBackend)
    # filterset_class = vehicleAdminBreakDownDateFilter

    def list(self, request,room_id, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset().filter(
            room__id=room_id))), many=True, context={"request": request}
        )
        return self.get_paginated_response(serializer.data)