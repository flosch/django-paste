# -*- coding: utf-8 -*-

import datetime

from simpleapi import Namespace

from models import Snippet

class PasteNamespace(Namespace):
    
    def new(self, content, title='', author='', expires=60*60):
        
        new_snippet = Snippet(
            title=title,
            author=author,
            content=content,
            expires=datetime.datetime.now() + datetime.timedelta(seconds=expires)
        )
        new_snippet.save()
        
        return new_snippet.get_absolute_url()
    new.published = True
    new.constraints = {'expires': int}