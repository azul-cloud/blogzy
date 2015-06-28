from django.views.generic import TemplateView


class Blog(TemplateView):
    template_name = "dashboardcontent/blog.html"

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context['page'] = 'blog'
        return context


class Posts(TemplateView):
    template_name = "dashboardcontent/posts.html"

    def get_context_data(self, **kwargs):
        context = super(Posts, self).get_context_data(**kwargs)
        context['page'] = 'posts'
        return context


class PostCreate(Posts):
    template_name = "dashboardcontent/post_create.html"


class PostEdit(Posts):
    template_name = "dashboardcontent/post_edit.html"


class Stats(TemplateView):
    template_name = "dashboardcontent/stats.html"

    def get_context_data(self, **kwargs):
        context = super(Stats, self).get_context_data(**kwargs)
        context['page'] = 'stats'
        return context


"""
@login_required
def create_post(request):
    '''
    user will create a blog post
    '''
    status = ""
    alert_message = ""
    form = BlogPostCreateForm()

    if request.method == "POST":
        # attempt save the blog object
        form = BlogPostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                # TODO: need to change this code to take multiple values
                # if request.POST['topic']:
                #     topic = Topic.objects.get(id=request.POST["topic"])
                # else:
                #     topic = None

                user = get_user_model().objects.get(username = request.user)

                post = form.save(commit=False)
                post.author = user
                post.blog = PersonalBlog.objects.get(owner=user)
                post.save()

                # saved and redirect to view the post
                post_url = reverse('blog-post', kwargs={'blog':post.blog.slug,
                                                        'post':slugify(post.title)})
                return redirect(post_url)

            except IntegrityError as e:
                status = "error"
                alert_message = "Your form did not validate. Have you already used this post title?"
        else:
            alert_message = "Please fix the errors on the form"
            status = "error"

    return render(request, "blogcontent/post_create.html", {'form':form, 'status':status,
                                                    'alert_message':alert_message})


@login_required
def edit_post(request, **kwargs):
    '''
    edit an existing blog post
    TODO: edit and create share a lot of the same logic
    '''

    # check to make sure current user is the owner of the blog
    id = kwargs['pk']
    post = get_object_or_404(Post, id=id)
    status = ""
    alert_message = ""

    if post.blog.owner == request.user:
        if request.method == "POST":
            # save the edited post instance
            form = BlogPostEditForm(request.POST, request.FILES, instance=post)

            if 'submit' in request.POST:
                # user is saving the updated data. They are not trying to delete.

                if form.is_valid():
                    try:
                        user = request.user

                        # if request.POST['topic']:
                        #     topic = Topic.objects.get(id=request.POST["topic"]),
                        # else:
                        #     topic = None

                        # begin saving the model instance
                        form.topic = topic
                        form.save()

                        # saved and redirect to view the post
                        post_url = reverse('blog-post', kwargs={'blog':post.blog.slug, 'post':slugify(post.title)})
                        return HttpResponseRedirect(post_url)

                    except IntegrityError:
                        status = "error"
                        alert_message = "You have already used that blog post title. Please choose another title."
                        pass
                else:
                    alert_message = "Your blog post data was not valid! Please fix the errors."
                    status = "error"
            elif 'delete' in request.POST:
                # user is deleting a post
                form.delete()
        else:
            # request get, show the form with default
            form = BlogPostEditForm(instance=post)
            return render(request, "blogcontent/post_edit.html", {'post':post, 'form':form})
    else:
        # request user is not the author
        return HttpResponseRedirect('blog-recent-posts')

    return render(request, "blogcontent/post_edit.html", {'form':form, 'status':status,
                                                    'alert_message':alert_message})

@login_required
def dashboard(request, **kwargs):
    '''
    perform managerial and administrative tasks for a blog. Only
    available to the blog owner
    '''
    alert_message = ""
    status = ""

    blog_slug = kwargs['blog']

    if request.user.is_superuser:
        blog = get_object_or_404(PersonalBlog, slug=blog_slug)
    else:
        blog = get_object_or_404(PersonalBlog, slug=blog_slug, owner=request.user)

    # handle the form submit to update blog data
    if request.method == "POST":
        if blog.owner == request.user:
            form = BlogEditForm(request.POST, request.FILES, instance=blog)

            if form.is_valid():
                form.save()

                alert_message = "Your blog data has been updated successfully"
                status = "saved"
            else:
                alert_message = form.instance.slug
                status = "error"
        else:
            alert_message = "You do not have access to update this blog's information."
            status = "error"
    else:
        # get request
        form = BlogEditForm(instance=blog)



    return render(request, "blogcontent/dashboard.html",
                  {'myblog':blog, 'alert_message':alert_message, 'status':status, 'form':form})
"""
