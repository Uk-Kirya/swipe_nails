from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class CustomErrorMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 500 > response.status_code > 400:
            return render(
                request,
                template_name='errors/400.html',
                status=response.status_code
            )
        elif response.status_code >= 500:
            return render(
                request,
                template_name='errors/500.html',
                status=response.status_code
            )

        return response
