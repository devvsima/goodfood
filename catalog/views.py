from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Goods, Categories
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline 
from django.db.models import Q

# Create your views here.
def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None) 


    if category_slug == "all":
        goods = Goods.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Goods.objects.filter(category__slug=category_slug)


    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)


    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))

    context = {
        "products": current_page,
        "slug_url": category_slug,
    }

    return render(request, 'catalog/catalog.html', context)

def product(request, product_slug=False, product_id=False):
    if product_slug:
        product = Goods.objects.get(slug=product_slug)
    elif product_id:
        product = Goods.objects.get(id=product_id)

    context = {"product": product}
    return render(request, "catalog/product.html", context)


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Goods.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Goods.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result