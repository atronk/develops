from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=0)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    # update the URL to obj with its ID
    def _update_link(self):
        id = self.id
        Post.objects.filter(id=id).update(
            link="http://localhost:8000/api/detail/" + str(id) + "/"
        )

    # update the URL when saved
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        self._update_link()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField("author name", max_length=50)
    content = models.CharField("comment text", max_length=350)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
