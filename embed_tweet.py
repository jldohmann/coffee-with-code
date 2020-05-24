from pelican import signals
import re


def embed_tweet(instance):
    if not instance._content:
        return

    instance._content = re.sub(
        r'(^|[^/])(t)@(\w{1,15})(\b[^\/])',
        '\\1<a href="https://twitter.com/\\3">@\\3</a>\\4',
        re.sub(
            r'(^|[^/])(t)@(\w{1,15})/status/(\d+)\b',
            '\\1<blockquote class="twitter-tweet" align="center"><a href="https://twitter.com/\\3/status/\\4">Tweet of \\3/\\4</a></blockquote>',
            instance._content
        )
    ) + '<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>'


def register():
    signals.content_object_init.connect(embed_tweet)