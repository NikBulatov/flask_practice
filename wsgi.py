from flask import redirect, url_for
from app.app import create_app

app = create_app()


@app.route("/")
def redirect_from_root():
    return redirect(url_for("article.article_list"), code=302)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
