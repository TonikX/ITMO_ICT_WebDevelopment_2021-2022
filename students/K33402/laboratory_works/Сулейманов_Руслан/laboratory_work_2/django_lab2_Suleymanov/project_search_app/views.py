from django.shortcuts import render,redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from project_conference_app.models import Conference


class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('search')
        if question is not None:
            if question == "":
                return redirect('/')
            search_conference = Conference.objects.filter(description__search=question)

            context['last_question'] = '?search=%s' % question

            current_page = Paginator(search_conference, 3)

            page = request.GET.get('page')
            try:
                context['conference_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['conference_lists'] = current_page.page(1)
            except EmptyPage:
                context['conference_lists'] = current_page.page(current_page.num_pages)

        return render(request, template_name=self.template_name, context=context)