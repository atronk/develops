from post.models import Post


# clearing upvotes job
def clear_votes():
    posts = Post.objects.all()
    for post in posts:
        post.votes_total = 0
        post.save()
