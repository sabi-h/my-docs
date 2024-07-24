import json
import logging

from airflow import settings
from airflow.models import Connection


def create_conn(conn_id, conn_type, host, login, pwd, port, desc, extra: dict = {}):
    """Add connection to airflow."""
    conn = Connection(
        conn_id=conn_id,
        conn_type=conn_type,
        host=host,
        login=login,
        password=pwd,
        port=port,
        description=desc,
        extra=json.dumps(extra),
    )
    session = settings.Session()
    conn_name = (
        session.query(Connection).filter(Connection.conn_id == conn.conn_id).first()
    )

    if str(conn_name) == str(conn.conn_id):
        logging.warning(f"Connection {conn.conn_id} already exists")
        return None

    session.add(conn)
    session.commit()
    logging.info(Connection.log_info(conn))
    logging.info(f"Connection {conn_id} is created")
    return conn


if __name__ == "__main__":
    create_conn(
        "test_conn_id",
        "HTTP",
        "test_host",
        "test_login",
        "test_pwd",
        "test_port",
        "test_desc",
        {"Hey": 1},
    )
