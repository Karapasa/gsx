from browser import document, html, bind, console, ajax, window, alert
import json

@bind(document['edit'], 'click')
def cabinet_editing(e):
    login = document['login'].text
    room = document['room'].text
    email = document['email'].text
    tel = document['tel'].text
    document['login'].clear()
    document['room'].clear()
    document['email'].clear()
    document['tel'].clear()

    document['login'] <= html.INPUT(value=login)
    document['room'] <= html.INPUT(value=room)
    document['email'] <= html.INPUT(value=email)
    document['tel'] <= html.INPUT(value=tel)
    document['edit'].attrs['id'] = 'save'
    document['save'].text = '(сохранить)'
    document["save"].bind('click', edit_user)

def output_data(req):
    window.location.reload(False)
    alert("Данные обновлены!")


@bind(document['btn_user_admin'], 'click')
def edit_user(e):
    url = 'http://api.121.0.0.1:5000/edit_user'
    data = {
            'login': document['form_admin_user_login'].value,
            'apartment': document['form_admin_user_apart'].value,
            'email': document['form_admin_user_email'].value,
            'tel': document['form_admin_user_tel'].value
    }
    ajax.post(url, data=json.dumps(data), oncomplete=output_data)


@bind(document['btn_indicator_admin'], 'click')
def indicator_editing(e):
    url = 'http://api.121.0.0.1:5000/edit_indicator'
    data = {
            'cold': document['form_admin_indicator_cold'].value,
            'hot': document['form_admin_indicator_hot'].value,
            'month': document['form_admin_indicator_date'].value,
            'user_id': document['form_admin_indicator_user'].value
    }
    ajax.post(url, data=json.dumps(data), oncomplete=output_data)

@bind(document['btn_post_admin'], 'click')
def post_editing(e):
    url = 'http://api.121.0.0.1:5000/edit_post'
    data = {
            'header': document['form_admin_post_header'].value,
            'url': document['form_admin_post_url'].value,
            'tag': document['form_admin_post_tag'].value,
            'cardtext': document['form_admin_post_cardtext'].value,
            'htmltext': document['form_admin_post_html'].value,
    }
    ajax.post(url, data=json.dumps(data), oncomplete=output_data)
