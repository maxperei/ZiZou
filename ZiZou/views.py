# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'ZiZou/index.html'
    title = 'Bienvenue'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        min = 0
        max = 1000
        start = self.request.GET.get('start') or 0
        end = self.request.GET.get('end') or 100
        x = self.request.GET.get('x')
        y = self.request.GET.get('y')

        context.update({
            'min': min,
            'max': max,
            'title': self.title,
            'start': start,
            'end': end,
            'x': x,
            'y': y,
            'range': range(int(start), int(end)+1, 1)
        })
        return context
