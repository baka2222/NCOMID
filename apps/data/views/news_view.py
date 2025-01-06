from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from ..models.news_model import New
from ..serializers.news_serializers import NewSerializer
from ..paginators.news_paginator import NewPaginator


class NewListView(ListAPIView):
    queryset = New.objects.all().order_by('-id')
    serializer_class = NewSerializer
    pagination_class = NewPaginator

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)  # Применяем пагинацию

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data

            for item in data:
                if 'img' in item and item['img']:
                    item['img'] = request.build_absolute_uri(item['img'])

            return self.get_paginated_response({'news': data})

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for item in data:
            if 'img' in item and item['img']:
                item['img'] = request.build_absolute_uri(item['img'])

        return Response(data={'news': data}, status=status.HTTP_200_OK)


class NewDetailView(RetrieveAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])

        return Response(data={'news': data}, status=status.HTTP_200_OK)