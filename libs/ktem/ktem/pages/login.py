# import hashlib
#
# import gradio as gr
# from ktem.app import BasePage
# from ktem.db.models import User, engine
# from sqlmodel import Session, select
#
# fetch_creds = """
# function() {
#     const username = getStorage('username', '')
#     const password = getStorage('password', '')
#     return [username, password, null];
# }
# """
#
# signin_js = """
# function(usn, pwd) {
#     setStorage('username', usn);
#     setStorage('password', pwd);
#     return [usn, pwd];
# }
# """
#
#
# class LoginPage(BasePage):
#
#     public_events = ["onSignIn"]
#
#     def __init__(self, app):
#         self._app = app
#         self.on_building_ui()
#
#     def on_building_ui(self):
#         gr.Markdown(f"# Welcome to {self._app.app_name}!")
#         self.usn = gr.Textbox(label="Username", visible=False)
#         self.pwd = gr.Textbox(label="Password", type="password", visible=False)
#         self.btn_login = gr.Button("Login", visible=False)
#
#     def on_register_events(self):
#         onSignIn = gr.on(
#             triggers=[self.btn_login.click, self.pwd.submit],
#             fn=self.login,
#             inputs=[self.usn, self.pwd],
#             outputs=[self._app.user_id, self.usn, self.pwd],
#             show_progress="hidden",
#             js=signin_js,
#         ).then(
#             self.toggle_login_visibility,
#             inputs=[self._app.user_id],
#             outputs=[self.usn, self.pwd, self.btn_login],
#         )
#         for event in self._app.get_event("onSignIn"):
#             onSignIn = onSignIn.success(**event)
#
#     def toggle_login_visibility(self, user_id):
#         return (
#             gr.update(visible=user_id is None),
#             gr.update(visible=user_id is None),
#             gr.update(visible=user_id is None),
#         )
#
#     def _on_app_created(self):
#         onSignIn = self._app.app.load(
#             self.login,
#             inputs=[self.usn, self.pwd],
#             outputs=[self._app.user_id, self.usn, self.pwd],
#             show_progress="hidden",
#             js=fetch_creds,
#         ).then(
#             self.toggle_login_visibility,
#             inputs=[self._app.user_id],
#             outputs=[self.usn, self.pwd, self.btn_login],
#         )
#         for event in self._app.get_event("onSignIn"):
#             onSignIn = onSignIn.success(**event)
#
#     def on_subscribe_public_events(self):
#         self._app.subscribe_event(
#             name="onSignOut",
#             definition={
#                 "fn": self.toggle_login_visibility,
#                 "inputs": [self._app.user_id],
#                 "outputs": [self.usn, self.pwd, self.btn_login],
#                 "show_progress": "hidden",
#             },
#         )
#
#     def login(self, usn, pwd):
#         if not usn or not pwd:
#             return None, usn, pwd
#
#         hashed_password = hashlib.sha256(pwd.encode()).hexdigest()
#         with Session(engine) as session:
#             stmt = select(User).where(
#                 User.username_lower == usn.lower().strip(),
#                 User.password == hashed_password,
#             )
#             result = session.exec(stmt).all()
#             if result:
#                 return result[0].id, "", ""
#
#             gr.Warning("Invalid username or password")
#             return None, usn, pwd

import hashlib
import gradio as gr
from ktem.app import BasePage
from ktem.db.models import User, engine
from sqlmodel import Session, select

# JavaScript pour récupérer les credentials depuis le localStorage
fetch_creds = """
function() {
    const username = getStorage('username', '')
    const password = getStorage('password', '')
    return [username, password, null];
}
"""

# JavaScript pour sauvegarder les credentials dans le localStorage
signin_js = """
function(usn, pwd) {
    setStorage('username', usn);
    setStorage('password', pwd);
    return [usn, pwd];
}
"""


class LoginPage(BasePage):
    public_events = ["onSignIn"]

    def __init__(self, app):
        self._app = app
        self.on_building_ui()

    def on_building_ui(self):
        # UI du formulaire de connexion
        gr.Markdown(f"# Welcome to {self._app.app_name}!")
        self.usn = gr.Textbox(label="Username", visible=False)
        self.pwd = gr.Textbox(label="Password", type="password", visible=False)
        self.btn_login = gr.Button("Login", visible=False)

    def on_register_events(self):
        # Événements pour déclencher la connexion
        onSignIn = gr.on(
            triggers=[self.btn_login.click, self.pwd.submit],
            fn=self.login,
            inputs=[self.usn, self.pwd],
            outputs=[self._app.user_id, self.usn, self.pwd],
            show_progress="hidden",
            js=signin_js,
        ).then(
            self.toggle_login_visibility,
            inputs=[self._app.user_id],
            outputs=[self.usn, self.pwd, self.btn_login],
        )
        for event in self._app.get_event("onSignIn"):
            onSignIn = onSignIn.success(**event)

    def toggle_login_visibility(self, user_id):
        # Fonction pour cacher ou afficher les champs de login en fonction de l'état de connexion
        return (
            gr.update(visible=user_id is None),
            gr.update(visible=user_id is None),
            gr.update(visible=user_id is None),
        )

    def _on_app_created(self):
        # Charger les credentials et essayer une connexion automatique
        onSignIn = self._app.app.load(
            self.login,
            inputs=[self.usn, self.pwd],
            outputs=[self._app.user_id, self.usn, self.pwd],
            show_progress="hidden",
            js=fetch_creds,
        ).then(
            self.toggle_login_visibility,
            inputs=[self._app.user_id],
            outputs=[self.usn, self.pwd, self.btn_login],
        )
        for event in self._app.get_event("onSignIn"):
            onSignIn = onSignIn.success(**event)

    def on_subscribe_public_events(self):
        # Abonner aux événements pour la déconnexion
        self._app.subscribe_event(
            name="onSignOut",
            definition={
                "fn": self.toggle_login_visibility,
                "inputs": [self._app.user_id],
                "outputs": [self.usn, self.pwd, self.btn_login],
                "show_progress": "hidden",
            },
        )

    def login(self, usn, pwd):
        # Vérification des credentials
        if not usn or not pwd:
            return None, usn, pwd

        # Hash du mot de passe pour la comparaison
        hashed_password = hashlib.sha256(pwd.encode()).hexdigest()

        # Connexion à la base de données pour vérifier les credentials
        with Session(engine) as session:
            stmt = select(User).where(
                User.username_lower == usn.lower().strip(),
                User.password == hashed_password,
            )
            result = session.exec(stmt).all()

            # Si l'utilisateur est trouvé, on initialise la session
            if result:
                user = result[0]
                return user.id, "", ""  # Connexion réussie, on retourne l'ID utilisateur

            # Message d'erreur en cas d'identifiants incorrects
            gr.Warning("Invalid username or password")
            return None, usn, pwd  # Connexion échouée
