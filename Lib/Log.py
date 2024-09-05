from Core.models import ErrorLog


def register(error_text):
    Error = ErrorLog(error_text=error_text)
    Error.save()
    