from Core.AppSettings import api


def point(point_name):
    return api.points[point_name]
    
    
def getHeader(user, logined=False):
    if logined:
        header = {
           "No-Authentication" : 'True',
           "Authorization" : f'Basic {user.backoffice_login}'
        }
    else:
        header = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {user.bearer_token}"
            }
    
    return header