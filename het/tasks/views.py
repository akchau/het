from django.shortcuts import render

from tasks.models import Task


def done(request, pk: Task.pk):
    task: Task = Task.objects.get(pk=pk)
    task.status = task.DONE
    new_task: Task = Task.objects.create(
        status=Task.CREATE,
        user=request.user,
        regularity=task.regularity,
        text=task.text,
        date=task.next_data
    )
    new_task.save()
    task.save()

