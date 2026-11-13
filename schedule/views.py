from django.shortcuts import render

def show_timetable(request):
    return render(request, 'timetable.html')
