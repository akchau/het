from django.core.paginator import Paginator


def get_page_obj(request, models, num_in_page):
    """Получение списка с пагинацией"""
    paginator = Paginator(models, num_in_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj
