from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import RoundForm, CourseForm, ShotsForm
from .models import Round, Shots
from .functions import calcHandicap, yearAverages, strokesGraph


def home(request):
    year_stats = []
    years_played = []
    rounds = Round.objects.all()
    for round in rounds:
        if round.get_year() not in years_played:
            years_played.append(round.get_year())
    for year in years_played:
        year_rounds = Round.objects.filter(date__year=year)
        year_stats.append(yearAverages(year_rounds))
    return render(request, 'GBGolf/home.html', {'year_stats': year_stats})


def manage(request):
    return render(request, 'GBGolf/manage.html',{})

def round_new(request):
    if request.method == "POST":
        form = RoundForm(request.POST)
        if form.is_valid():
            round = form.save()
            # Add user save at later point here
            round.save()
            return redirect('GBGolfmanage')
    else:
        form = RoundForm()
        return render(request, 'GBGolf/round_edit.html', {'form': form} )

def delete_round(request):
    if request.method == 'POST':
        id = int(request.path.replace("/GBGolf/delete_round/", ""))
        round = Round.objects.get(pk=id)
        round.delete()
        return redirect('GBGolfrounds')
    else:
        return HttpResponse("Did not post")


def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            # Add user save at later point here
            course.save()
            return redirect('GBGolfmanage')
    else:
        form = CourseForm()
        return render(request, 'GBGolf/course_edit.html', {'form': form})

def shots_new(request):
    if request.method == "POST":
        form = ShotsForm(request.POST)
        if form.is_valid():
            shots = form.save()
            # Add user save at later point here
            shots.save()
            return redirect('GBGolfmanage')
    else:
        form = ShotsForm()
        return render(request, 'GBGolf/shots_edit.html', {'form': form})


def rounds(request):
        round_stats = Round.objects.all().order_by('-date')
        return render(request, 'GBGolf/rounds.html', {'round_stats': round_stats})

def handicap(request):
    round_stats = Round.objects.all().order_by('date')
    round_handicap = []
    diffList = []
    handicapTotal = 0
    round_count = 0
    for round in round_stats:
        round_count += 1
        diffList.append(round.handicap_diff())
        #There is probably a more efficent way to do this instead of copying the list each time (yield? enumerate?)
        diffUsed = diffList[:]
        if round_count > 20:
            diffUsed = diffUsed[(round_count-20):round_count]
        handicapTotal = calcHandicap((round_count), diffUsed)
        round_handicap.append((round, round.handicap_diff(), handicapTotal))
    round_handicap.reverse()
    return render(request, 'GBGolf/handicap.html',
                  {'round_handicap': round_handicap})


def sop(request):
    sop_stats = Shots.objects.all()
    return render(request, 'GBGolf/sop.html', {'sop_stats': sop_stats})