#!/usr/bin/python3
"""
    initialize uniq FileStorage to reload bd
"""
from models.engine.file_storage import FileStorage

#create variable storage
storage = FileStorage()
#call reload on storage variable
storage.reload()