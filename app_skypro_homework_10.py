from flask import Flask

from utils import load_candidates, get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates_list = []
    for candidate in load_candidates():
        candidates_list.append("<br>" + "Имя кандидата - " + candidate["name"] +
                               "<br>" + "Позиция кандидата - " + str(candidate["pk"]) +
                               "<br>" + "Навыки - " + candidate["skills"])
    return f"<pre>{'<br>'.join(candidates_list)}</pre>"


@app.route('/candidates/<int:uid>')
def candidates(uid):
    candidates_id = get_by_pk(uid)
    url_pict = candidates_id['picture']
    return f'<img src="{url_pict}"' \
           f'<pre><br>Имя кандидата - {candidates_id["name"]}' \
           f'<br> Позиция - {candidates_id["pk"]}' \
           f'<br> Навыки - {candidates_id["skills"]}</pre></br>'


@app.route('/skills/<skills_id>')
def skills(skills_id):
    return f'<pre>{get_by_skill(skills_id)}</pre>'


app.run()
