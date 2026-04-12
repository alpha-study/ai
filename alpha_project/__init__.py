from .celery import app as celery_app

# ── MySQL driver ─────────────────────────────────────────────────────────────
# The remote server uses mysql_native_password authentication which is not
# supported by mysqlclient compiled against MySQL 9.x.  Use PyMySQL instead.
# Django 6.x checks for mysqlclient >= 2.2.1 so we patch the version PyMySQL
# reports when masquerading as MySQLdb.
import pymysql

pymysql.version_info = (2, 2, 7, 'final', 0)
pymysql.install_as_MySQLdb()

__all__ = ('celery_app',)
