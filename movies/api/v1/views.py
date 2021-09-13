from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.models import Filmwork, PersonRoles


class FilmworkMixinView:
    model = Filmwork
    default_values_list = ('id', 'title', 'description', 'creation_date', 'rating', 'type')
    http_method_names = ['get']

    def get_queryset(self):
        return Filmwork.objects.values(*self.default_values_list).annotate(
            genres=ArrayAgg('filmworkgenre__genre__name', distinct=True),
            writers=ArrayAgg('personfilmwork__person__full_name', filter=Q(personfilmwork__role=PersonRoles.WRITER),
                             distinct=True),
            actors=ArrayAgg('personfilmwork__person__full_name', filter=Q(personfilmwork__role=PersonRoles.ACTOR),
                            distinct=True),
            directors=ArrayAgg('personfilmwork__person__full_name', filter=Q(personfilmwork__role=PersonRoles.DIRECTOR),
                               distinct=True)
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListView(FilmworkMixinView, BaseListView):
    model = Filmwork
    http_method_names = ['get']
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        paginator, page, queryset = self.paginate_queryset(
            self.get_queryset(),
            self.paginate_by
        )

        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'result': list(queryset),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class SingleMovieView(FilmworkMixinView, BaseDetailView):

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_object()
