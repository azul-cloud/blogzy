from django.shortcuts import get_object_or_404

from blog.models import Post, UserFavorite


def get_favorites(user):
    '''
    get a list of favorites for a specific user
    '''
    try:
        if user.is_authenticated():
            # get the post ids of the favorite objects
            favorites = UserFavorite.objects.filter(user=user)
            post_id_list = []
            for f in favorites:
                post_id_list.append(f.post.id)

            # add post ids to the list object
            post_qs = Post.objects.filter(id__in=post_id_list)
            favorite_ids = []
            for p in post_qs:
                favorite_ids.append(p.id)
        else:
            # anonymous user, return none
            favorite_ids = None
            favorites = None
    except ValueError:
        # no favorites
        favorite_ids = None
        favorites = None

    return {'favorite_ids':favorite_ids, 'objects':favorites }


def get_wave_blog_list(user):
    # get the blogs that are in a user's wave
    wave_blog_list = user.blog_wave.all()

    return wave_blog_list


def get_map_posts(posts):
    # get the posts that should be shown on a map from a list of posts
    map_posts = []
    for p in posts:
        if p.lat and p.long:
            map_posts.append(p)

    if map_posts:
        # assign the most recent post's loc to center loc
        center_lat = map_posts[0].lat
        center_long = map_posts[0].long
    else:
        center_lat = None
        center_long = None

    return map_posts