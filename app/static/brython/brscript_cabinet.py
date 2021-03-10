from browser import document, html, bind, console, ajax, window, alert
import json


def output_data(req):
    alert("Данные обновлены!")
    window.location.reload(False)


def edit_user(e):
    id = document.location.pathname.split('/')[-1]
    url = 'http://127.0.0.1:5000/api/owner/' + id
    data = {
        'apartment': document['room'].children[0].value,
        'email': document['email'].children[0].value,
        'phone_number': document['tel'].children[0].value
    }

    req = ajax.Ajax()
    req.bind('complete', output_data)
    req.open('PUT', url, True)
    req.send(json.dumps(data))

@bind(document['edit'], 'click')
def cabinet_editing(e):
    room = document['room'].text
    email = document['email'].text
    tel = document['tel'].text
    document['room'].clear()
    document['email'].clear()
    document['tel'].clear()

    document['room'] <= html.INPUT(value=room)
    document['email'] <= html.INPUT(value=email)
    document['tel'] <= html.INPUT(value=tel)


    document['edit'].clear()
    document['edit'] <= html.SMALL(html.A('(сохранить)', href='#', id='save'))
    document['save'].bind('click', edit_user)
