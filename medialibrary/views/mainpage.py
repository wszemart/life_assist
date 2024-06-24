from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.views.generic import TemplateView
from view_breadcrumbs import BaseBreadcrumbMixin


class MedialibraryMainPage(BaseBreadcrumbMixin, LoginRequiredMixin, TemplateView):
    template_name = "medialibrary/medialibrary_main_page.html"

    @cached_property
    def crumbs(self):
        breadcrumb_list = [
            ("Dashboard", reverse_lazy("dashboard")),
            ("Medialibrary", None),
        ]
        return breadcrumb_list
