from browser import document, html, bind, console, ajax, window, alert
import json


def output_data(req):
    window.location.reload(False)
    alert("Данные обновлены!")

def delete_data(req):
    window.location.replace('http://127.0.0.1:5000/admin/indicators')
    alert("Данные удалены!")

@bind(document['btn_indicator_admin'], 'click')
def indicator_editing(e):
    id = document.location.pathname.split('/')[-1]
    url = 'http://127.0.0.1:5000/api/indicator/'+id
    data = {
        'cold': int(document['form_admin_indicator_cold'].value),
        'hot': int(document['form_admin_indicator_hot'].value),
        'user_id': int(document['form_admin_indicator_user'].value)
    }
    req = ajax.Ajax()
    req.bind('complete', output_data)
    req.open('PUT', url, True)
    req.send(json.dumps(data))

@bind(document['delete'], 'click')
def delete(e):
    id = document.location.pathname.split('/')[-1]
    url = 'http://127.0.0.1:5000/api/indicator/'+id
    req = ajax.Ajax()
    req.bind('complete', delete_data)
    req.open('DELETE', url, True)
    req.send('')
