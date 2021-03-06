from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Student
from django.utils import timezone
from .forms import PostForm

def post_list(request):
	students=Student.objects.order_by('created_date')
	posts = Post.objects.order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts':posts,'students':students})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form=PostForm()
	return render(request,'blog/post_edit.html', {'form':form})

def post_delete(request,pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	posts = Post.objects.order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

