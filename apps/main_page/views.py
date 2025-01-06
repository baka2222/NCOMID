from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models.blocks_and_departments_model import Block, Department
from .serializers.blocks_and_departments_serializer import (BlockSerializer,
                                                            BlockDetailSerializer,
                                                            DepartmentSerializer,
                                                            BlockSearchSerializer)
from .models.general_structure_model import GeneralStructure
from .serializers.general_structure_serializer import GeneralSerializer
from rest_framework.views import APIView
from .models.banners_model import Banner
from .serializers.banners_serializer import BannerSerializer
from .models.counters_model import Counter
from .serializers.counters_serializer import CounterSerializer
from ..data.models.news_model import New
from ..data.serializers.news_serializers import NewSerializer
from .models.about_us_models import AboutNCOMID, History, AboutUs, Charter, Directorate
from .serializers.about_us_serializers import AboutNCOMIDSerializer, HistorySerializer, AboutUsSerializer, CharterSerializer, DirectorateSerializer
from .models.contacts_model import Contacts, SocialMedia
from .serializers.contacts_serializer import ContactSerializer, SocialMediaSerializer
from .models.scientific_activity_models import ScientificActivity, ScientificActivityContent
from .serializers.scientific_activity_serializers import ScientificActSerializer, ScientificActContentSerializer, \
    SASearchSerializer
from .models.resources_model import Link, Resource, Journal, Report
from .serializers.resources_serializer import JournalSerializer, ReportSerializer, LinkSerializer, JournalAndReportSerializer
from django.db.models import Q

# scientific activity
class ScientificActivityView(APIView):
    def get(self, request, *args, **kwargs):
        sa = ScientificActivity.objects.all().order_by('id')
        serializer = ScientificActSerializer(sa, context={'request': request}, many=True)
        data = serializer.data
        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])
        return Response(data={'scientific_activity': data}, status=status.HTTP_200_OK)


class AboutNCOMIDView(ListAPIView):
    queryset = AboutNCOMID.objects.all()
    serializer_class = AboutNCOMIDSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({})
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)


# main_page
class BannerView(APIView):
    def get(self, request, *args, **kwargs):
        banner = Banner.objects.get()
        serializer = BannerSerializer(banner, context={'request': request})
        data = serializer.data
        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])
        return Response(data={'banner': data}, status=status.HTTP_200_OK)


class CounterView(APIView):
    def get(self, request, *args, **kwargs):
        banner = Counter.objects.all().order_by('id')
        serializer = CounterSerializer(banner, context={'request': request}, many=True)
        data = serializer.data
        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])
        return Response(data={'counters': data}, status=status.HTTP_200_OK)


class ContactsView(APIView):
    def get(self, request, *args, **kwargs):
        contact = Contacts.objects.all().order_by('id')
        serializer = ContactSerializer(contact, context={'request': request}, many=True, )
        data = serializer.data
        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])
        return Response(data={'contacts': data}, status=status.HTTP_200_OK)


class SocialMediaView(APIView):
    def get(self, request, *args, **kwargs):
        contact = SocialMedia.objects.all().order_by('id')
        serializer = SocialMediaSerializer(contact, context={'request': request}, many=True, )
        data = serializer.data
        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])
        return Response(data={'social_media': data}, status=status.HTTP_200_OK)


# blocks and department
class BlockListAPIView(ListAPIView):
    queryset = Block.objects.all().order_by('id')
    serializer_class = BlockSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = serializer.data


        for item in data:
            if 'img' in item and item['img']:
                item['img'] = request.build_absolute_uri(item['img'])

        return Response(data={'blocks': data}, status=status.HTTP_200_OK)

class BlockRetrieveAPIView(RetrieveAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Block.DoesNotExist:
            return Response(
                data={'error': 'Block not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance)
        data = serializer.data

        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])

        if 'departments' in data:
            for department in data['departments']:
                if 'photo_url' in department and department['photo_url']:
                    department['photo_url'] = request.build_absolute_uri(department['photo_url'])

        return Response(data={'block': data}, status=status.HTTP_200_OK)

class DepartmentRetrieveAPIView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data


        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])

        return Response(data={'departament': data}, status=status.HTTP_200_OK)
    
# generalstructure 
class GeneralAPIView(ListAPIView):
    queryset = GeneralStructure.objects.all().order_by('id')
    serializer_class = GeneralSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = serializer.data


        for item in data:
            if 'img' in item and item['img']:
                item['img'] = request.build_absolute_uri(item['img'])

        return Response(data={'general_structure': data}, status=status.HTTP_200_OK)


class JournalAndReportAPIView(ListAPIView):
    queryset = Resource.objects.all().order_by('id')
    serializer_class = JournalAndReportSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = serializer.data


        for item in data:
            if 'img' in item and item['img']:
                item['img'] = request.build_absolute_uri(item['img'])

        return Response(data={'journal_and_report': data}, status=status.HTTP_200_OK)

# resource Link

class LinkListAPIView(ListAPIView):
    queryset = Link.objects.all().order_by('id')
    serializer_class = LinkSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = serializer.data


        for item in data:
            if 'img' in item and item['img']:
                item['img'] = request.build_absolute_uri(item['img'])

        return Response(data={'links': data}, status=status.HTTP_200_OK)

class LinkRetrieveAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data


        if 'img' in data and data['img']:
            data['img'] = request.build_absolute_uri(data['img'])

        return Response(data={'links': data}, status=status.HTTP_200_OK)

# Search

class SearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            query = request.query_params['q']

            try:
                endings = [
                    "а", "я", "и", "ы", "о", "е", "у", "ю", "ь", "ей", "ой", "ий", "ия", "ём", "ем", "ам", "ям",
                    "ом", "ем", "ами", "ями", "ах", "ях", "ого", "его", "ому", "ему", "ым", "им", "ой",
                    "ей", "ую", "юю", "ого", "его", "ому", "ему", "ым", "им", "ое", "ее", "их", "ых",
                    "им", "ым", "их", "ых", "ему", "ой", "ей", "ая", "яя", "ое", "ее", "и", "ы", "у",
                    "ю", "ем", "ом", "ей", "ой", "ию", "ею", "у", "я", "ов", "ев", "е", "ё", "ем", "ями"
                ]

                if any(query.endswith(ending) for ending in endings):
                    query = query[:-2]
            except:
                pass


        except KeyError:
            return Response({'error': 'Query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        models_serializer = {
            History: (HistorySerializer, 'description'),
            AboutUs: (AboutUsSerializer, 'description'),
            Charter: (CharterSerializer, 'title'),
            Directorate: (DirectorateSerializer, 'name'),
            GeneralStructure: (GeneralSerializer, 'title'),
            Journal: (JournalSerializer, 'title'),
            Report: (ReportSerializer, 'title'),
            Link: (LinkSerializer, 'title'),
            ScientificActivity: (SASearchSerializer, 'title'),
            New: (NewSerializer, 'title'),
            Department: (DepartmentSerializer, 'name')
        }

        results = {}

        try:
            for model, (serializer, field) in models_serializer.items():
                queryset = model.objects.filter(Q(**{f"{field}__icontains": query}))
                if queryset.exists():
                    results[model.__name__.lower()] = serializer(queryset, many=True).data


            for i in results.values():
                for item in i:
                    if 'photo_url' in item and item['photo_url']:
                        item['photo_url'] = request.build_absolute_uri(item['photo_url'])
                    if 'files' in item and item['files']:
                        item['files'] = request.build_absolute_uri(item['files'])
                    if 'photo' in item and item['photo']:
                        item['photo'] = request.build_absolute_uri(item['photo'])
                    if 'img' in item and item['img']:
                        item['img'] = request.build_absolute_uri(item['img'])

                    try:

                        for j in item['departments']:
                            if 'photo_url' in j and j['photo_url']:
                                j['photo_url'] = request.build_absolute_uri(j['photo_url'])
                            if 'files' in j and j['files']:
                                j['files'] = request.build_absolute_uri(j['files'])
                            if 'photo' in item and item['photo']:
                                j['photo'] = request.build_absolute_uri(j['photo'])
                            if 'img' in j and j['img']:
                                j['img'] = request.build_absolute_uri(j['img'])
                    except:
                        continue


        except ValueError:
            return Response({'message': 'Таких результатов нету'}, status=status.HTTP_404_NOT_FOUND)

        return Response(results, status=status.HTTP_200_OK)