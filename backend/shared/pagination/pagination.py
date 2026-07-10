import math

from rest_framework.pagination import PageNumberPagination

from shared.responses.responses import ApiResponse


class StandardPagination(PageNumberPagination):
    """
    Standard pagination for all list APIs.
    """

    page_size = 20

    page_size_query_param = "page_size"

    max_page_size = 100

    def get_paginated_response(self, data):
        pagination = {
            "page": self.page.number,
            "page_size": self.get_page_size(self.request),
            "total_records": self.page.paginator.count,
            "total_pages": math.ceil(
                self.page.paginator.count
                / self.get_page_size(self.request)
            ),
            "has_next": self.page.has_next(),
            "has_previous": self.page.has_previous(),
        }

        return ApiResponse.success(
            data=data,
            pagination=pagination,
        )