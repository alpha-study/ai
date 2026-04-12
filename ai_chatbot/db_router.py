"""
Database router for the ai_chatbot app.

PURPOSE:
  - Allow Django to create / migrate ONLY its own tables (ai_chatbot app +
    Django internal apps like auth, contenttypes, sessions, admin, etc.).
  - Prevent Django from ever touching tables owned by the Node.js application.

Any model with  ``managed = False``  is automatically excluded from migrations
by Django's migration framework, but this router adds an extra safety layer.
"""

# Apps whose tables Django is allowed to create & migrate.
DJANGO_INTERNAL_APPS = {
    'auth',
    'contenttypes',
    'sessions',
    'admin',
    'messages',
}

ALLOWED_APPS = DJANGO_INTERNAL_APPS | {'ai_chatbot'}


class ChatbotRouter:
    """Route all chatbot models to the default database and block migrations
    for any app outside the allow-list."""

    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Only allow migrations for Django internals + ai_chatbot."""
        if app_label in ALLOWED_APPS:
            return True
        # Block everything else – protects Node.js-owned tables.
        return False
