from browser import document, html, bind, console, ajax, window, alert
import json

def output_data(req):
    window.location.reload(False)
    alert("Данные обновлены!")

def delete_data(req):
    window.location.replace('http://127.0.0.1:5000/admin/users')
    alert("Данные удалены!")

@bind(document['btn_user_admin'], 'click')
def edit_user(e):
    id = document.location.pathname.split('/')[-1]
    url = 'http://127.0.0.1:5000/api/owner/'+id
    data = {
        'apartment': document['form_admin_user_apart'].value,
        'email': document['form_admin_user_email'].value,
        'phone_number': document['form_admin_user_tel'].value
    }
    req = ajax.Ajax()
    req.bind('complete', output_data)
    req.open('PUT', url, True)
    req.send(json.dumps(data))

@bind(document['delete'], 'click')
def delete(e):
    id = document.location.pathname.split('/')[-1]
    url = 'http://127.0.0.1:5000/api/owner/'+id
    req = ajax.Ajax()
    req.bind('complete', delete_data)
    req.open('DELETE', url, True)
    req.send('')
