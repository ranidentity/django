class PrimaryReplicaRouter:
    """
    A router to control all database operations on models
    """
    route_to_postgres = {
        'users',          # Your custom User model app
        'auth',           # Django's authentication system
        'admin',          # Django's admin site
        'contenttypes',   # Used by auth permissions and generic relations
        'sessions',       # Django's session framework (if used)
    }

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to the default db.
        """
        if model._meta.app_label in self.route_to_postgres:
            return 'postgres' # Use the 'postgres' database for all other apps
        return 'default' # Use the 'default' database for models in 'accounts' app

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to the default db.
        """
        if model._meta.app_label in self.route_to_postgres:
            return 'postgres' # Use the 'postgres' database for all other apps
        return 'default' # Use the 'default' database for models in 'accounts' app

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations only if both objects are in the same database group.
        """
        db1 = self.db_for_write(obj1)
        db2 = self.db_for_write(obj2)
        return db1 == db2

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'accounts' app only appears in the 'default' database.
        And all other apps only appear in the 'postgres' database.
        """
        if db == 'postgres':
            return app_label in self.route_to_postgres
        else:  # default DB (SQLite)
            return app_label not in self.route_to_postgres