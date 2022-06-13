from src import database


class DBFontAnswer:

    def __init__(self,*args):
        self.id = None
        self.font_id = None
        self.answer_id = None
        if len(args) == 1 and type(args[0]) is dict:
            self.font_id = args[0]['font_id']
            self.answer_id = args[0]['answer_id']

    def save(self):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "INSERT INTO font_answer (" \
              "font_id," \
              "answer_id" \
              ") VALUES (%s,%s) RETURNING font_answer_id"
        cursor.execute(sql,[self.font_id,
                            self.answer_id
                            ]
                       )
        dbres = cursor.fetchone()
        self.id = dbres[0]
        db.commit()

    def jsonify(self):
        return {"id": self.id,
                "font_id": self.font_id,
                "answer_id": self.answer_id
                }