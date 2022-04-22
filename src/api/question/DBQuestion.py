from src import database
from src.api.exceptions.NotFoundException import NotFoundException
from src.api.question.DBAnswer import DBAnswer


class DBQuestion:
    def __init__(self, id):
        self.id = id
        self.text = None
        self.answers = []
        self.load(id)

    def load(self, id):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM question WHERE question_id=%s"
        cursor.execute(sql, [id])
        res = cursor.fetchone()
        if res is None:
            raise NotFoundException
        self.id = res[0]
        self.text = res[1]
        self.answers = DBAnswer.loadByQuestionId(self.id)

    def jsonify(self):
        return {"question_id": self.id,
                "text": self.text,
                "answers": [a.jsonify() for a in self.answers]}
