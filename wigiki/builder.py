import re

class Builder(object):

    @classmethod
    def gist(cls, gistid):
        """gistid must be in a username/id form"""
        url = "https://gist.github.com/{}.js".format(gistid)
        script = "<script src=\"{}\"></script>".format(url)
        return script


    @classmethod
    def page_list(cls, pages, base_url='/'):
        """transform a list of page titles in a list of html links"""
        plist = []
        for page in pages:
            url = "<a href=\"{}{}\">{}</a>".format(base_url, cls.slugify(page), page)
            plist.append(url)
        return plist


    @classmethod
    def slugify(cls, s):
        """Return the slug version of the string ``s``"""
        slug = re.sub("[^0-9a-zA-Z-]", "-", s)
        return re.sub("-{2,}", "-", slug).strip('-')
