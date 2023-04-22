import os

from sqlalchemy import create_engine, text


class MySQLConn:
    """Connecting to MySQL."""

    def __init__(self):
        """Instantiating connection."""
        self.db_engine = create_engine(
            "mysql://{username}:{password}@{host}:{port}/{db}?charset={ch}".format(
                username=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                host=os.getenv("MYSQL_HOST"),
                port=os.getenv("MYSQL_PORT"),
                db=os.getenv("MYSQL_DATABASE"),
                ch="utf8",
            )
        )

    def __enter__(self):
        """conncect to database."""
        self.conn = self.db_engine.connect()
        return self.conn

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            raise Exception(exc_type)
        self.conn.close()
        self.db_engine.dispose()
        return True


def initialize_mysql(project_name):
    """Create table based on project name."""
    create_query = text(
        f"""
    CREATE TABLE IF NOT EXISTS `{project_name}` (
        `id` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
        `href` text NOT NULL,
        `title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
        `deposit` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
        `rent` varchar(20) DEFAULT NULL,
        `region` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    )

    with MySQLConn() as conn:
        conn.execute(create_query)


def filter_new_items(items):
    """Check with database, then insert and return new items"""
    new_items = []
    with MySQLConn() as conn:
        for item in items:
            item_lookpup = conn.execute(
                text(
                    f"SELECT id FROM {os.getenv('PROJECT_NAME')} WHERE id = '{item['id']}'"
                )
            ).fetchone()

            # If item does not exists insert it and add it to new item list
            if not item_lookpup:
                ins_query = text(
                    f"""
                INSERT INTO `{os.getenv("PROJECT_NAME")}` (`id`, `href`, `title`, `deposit`, `rent`, `region`)
                VALUES ('{item["id"]}', '{item["href"]}', '{item["title"]}', '{item["deposit"]}', '{item["rent"]}', '{item["region"]}');
                """
                )
                conn.execute(ins_query)
                conn.commit()
                new_items.append(item)
    return new_items
