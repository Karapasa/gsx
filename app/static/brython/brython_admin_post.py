from browser import document, html, bind, console, ajax, window, alert
import json

def output_data(req):
    window.location.reload(False)
    alert("Данные обновлены!")

def delete_data(req):
    window.location.replace('http://127.0.0.1:5000/admin/posts')
    alert("Данные удалены!")

@bind(document['btn_post_admin'], 'click')
def post_editing(e):
    id = document.location.pathname.split('/')[-1]
    url = 'http://127.0.0.1:5000/api/post/'+ id
    data = {
        'header': document['form_admin_post_header'].value,
        'url': document['form_admin_post_url'].value,
        'tag': document['form_admin_post_tag'].value,
        'cardtext': document['form_admin_post_cardtext'].value,
        'htmltext': document['form_admin_post_html'].value
    }
    req = ajax.Ajax()
    req.bind('complete', delete_data)
    req.open('PUT', url, True)
    req.send(json.dumps(data))

@bind(document['delete'], 'click')
def delete(e):
    id = document.location.pathname.split('/')[-1]
    url = 'http://127.0.0.1:5000/api/post/'+id
    req = ajax.Ajax()
    req.bind('complete', output_data)
    req.open('DELETE', url, True)
    req.send('')
