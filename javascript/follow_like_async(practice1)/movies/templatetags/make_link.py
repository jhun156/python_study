# movies/templatetags/make_link.py

from django import template

register = template.Library()


@register.filter 
def hashtag_link(word):
    content = word.description + ' '
    hashtags = word.hashtags.all()
    for hashtag in hashtags:
        content = content.replace(hashtag.content + ' ', 
                f'<a href="/movies/{hashtag.pk}/hashtag/">{hashtag.content}</a> ')
    return content 