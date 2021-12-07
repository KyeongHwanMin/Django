from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post

post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#         # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q':q,
#     })


# def post_detail(request: HttpRequest, pk:int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.frilter(is_public=True))

class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenciated:
            qs = qs.filter()
        return qs


post_detail = PostDetailView.as_view()
