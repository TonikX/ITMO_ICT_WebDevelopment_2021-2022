from django.shortcuts import render, get_object_or_404, redirect
from project_conference_app.models import Conference, Comments, Performance
from project_conference_app.forms import CommentForm,PerformanceForm
# Create your views here.


def conference_detail(request, pk):
    conference = get_object_or_404(Conference, id=pk)
    topics = conference.topics.all()
    comments = Comments.objects.filter(conference=pk, moderation=True)
    perfs = Performance.objects.filter(conference=pk, result=True)

    if request.method == 'POST' and 'btnform2' in request.POST:
        # создание комментария
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.conference = conference
            form.save()
        return redirect(conference_detail, pk)
    elif request.method == 'POST' and 'btnform1' in request.POST:
        # Удаление коментария
        id_comment = request.POST.get("delete_comment")
        comment = Comments.objects.get(id=id_comment)
        comment.delete()
        return redirect(conference_detail, pk)

    elif request.method == 'POST' and 'btnform3' in request.POST:
        # Создание заявки
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.conference = conference
            form.save()
        return redirect(conference_detail, pk)
    elif request.method == 'POST' and 'btnform4' in request.POST:
        # Удаление заявки
        id_perf = request.POST.get("delete_comment")
        performance = Performance.objects.get(id=id_perf)
        performance.delete()
        return redirect(conference_detail, pk)

    else:
        comments_form = CommentForm()
        performance_form = PerformanceForm()

    return render(request, "conference/conference_detail.html", {"conference": conference,
                                                                 "perf": perfs,
                                                                 "topics": topics,
                                                                 "comments": comments,
                                                                 "comments_form": comments_form,
                                                                 "user": request.user,
                                                                 "performance_form": performance_form
                                                                 })


