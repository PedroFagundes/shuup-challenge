# -*- coding: utf-8 -*-

from django.views.generic import ListView
from django.db.models import Count, Sum

from mailer.models import Company


class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100

    queryset = Company.objects.all().prefetch_related('contacts', 'contacts__orders').annotate(
        order_count=Count('orders'), order_sum=Sum('orders__total'))
