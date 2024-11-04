from flask import Flask, render_template_string
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_cloud_vendors():
    """Fetch cloud vendors from the database."""
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM cloud_vendors")
        vendors = cursor.fetchall()

        column_names = [desc[0] for desc in cursor.description] if vendors else []
        return vendors, column_names
    except Exception as e:
        print("Error while connecting to PostgreSQL", e)
        return [], []
    finally:
        if connection is not None:
            cursor.close()
            connection.close()


@app.route("/")
def hello():
    vendors, column_names = get_cloud_vendors()
    return render_template_string(
        """
        <h1>Cloud Vendors</h1>
        <table border="1">
            <thead>
                <tr>
                    {% for column in column_names %}
                        <th>{{ column }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for vendor in vendors %}
                    <tr>
                        {% for item in vendor %}
                            <td>{{ item }}</td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    """,
        vendors=vendors,
        column_names=column_names,
    )


if __name__ == "__main__":
    app.run()
