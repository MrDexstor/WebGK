from django.core.files.storage import FileSystemStorage
from django.core.files.locks import lock

class NoLockFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        # Disable file locking
        lock.lock = lambda *args, **kwargs: None
        lock.unlock = lambda *args, **kwargs: None
        return super()._save(name, content)
