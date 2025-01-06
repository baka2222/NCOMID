from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.main_page.views import LinkListAPIView, JournalAndReportAPIView
from .views import BlockListAPIView, BlockRetrieveAPIView, DepartmentRetrieveAPIView
from .views import GeneralAPIView
from .views import (ScientificActivityView,
                    BannerView,
                    CounterView,
                    ContactsView,
                    AboutNCOMIDView,
                    SocialMediaView)
from .views import SearchAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # documentation
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    ## blocks and department
      path('api/v1/medical_work_block/', BlockListAPIView.as_view(), name='block_list'),
    path('api/v1/medical_work_block/<int:pk>/', BlockRetrieveAPIView.as_view(), name='block_list_detail'),
   #  path('api/v1/department/block_id/<int:pk>/', DepartmentListAPIView.as_view(), name='department_list'),
    path('api/v1/department/<int:pk>/', DepartmentRetrieveAPIView.as_view(), name='department_list_detail'),
    ##  resource
    path('api/v1/journal_and_report/', JournalAndReportAPIView.as_view()),
    path('api/v1/resource_link/', LinkListAPIView.as_view()),
        
    ## general structure 
    path('api/v1/general_structure/', GeneralAPIView.as_view(), name='general_list'),
    ## main page  
    path('api/v1/banner/', BannerView.as_view()),
    path('api/v1/counter/', CounterView.as_view()),
    path('api/v1/contacts/', ContactsView.as_view()),
    path('api/v1/social_media/', SocialMediaView.as_view()),
    ## about us
    path('api/v1/about_ncomid', AboutNCOMIDView.as_view()),
    ## scientific activity
    path('api/v1/scientific_activity/', ScientificActivityView.as_view()),
    ## search
    path('api/v1/search/', SearchAPIView.as_view(), name='search'),

]
