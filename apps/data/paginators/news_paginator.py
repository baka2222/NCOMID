from rest_framework.pagination import PageNumberPagination


class NewPaginator(PageNumberPagination):
    page_size = 8