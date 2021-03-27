from model.contact import Contact

def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(firstname='user', lastname='user_lastname', nickname='nickname'))
    app.open_home_page()
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(firstname='', lastname='', nickname=''))
    app.open_home_page()
    app.session.logout()
