# -*- coding: utf-8 -*-

from simpleapi import Namespace

from models import Snippet

class PasteNamespace(Namespace):
    
    def new(self, content, title='', author=''):
        
        new_snippet = Snippet(
            title=title,
            author=author,
            content=content
        )
        new_snippet.save()
        
        return new_snippet.get_absolute_url()
    new.published = True