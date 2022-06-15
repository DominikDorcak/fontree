
from src import database


class DBEntry:
    def __init__(self, *args):
        self.entry_time = None
        self.id = None
        self.age = None
        self.sex = None
        self.highest_education = None
        self.assigned_font = None
        self.result_font = None
        self.time_in_milis = None
        self.question_count = None
        if type(args[0]) is dict:
            entry = args[0]
            self.age = entry["age"]
            self.sex = entry["sex"]
            self.highest_education = entry["highest_education"]
            self.assigned_font = entry["assigned_font"]
            self.result_font = entry["result_font"]
            self.time_in_milis = entry["time_in_milis"]
            self.question_count = entry["question_count"]
        if type(args[0]) is tuple:
            entry = args[0]
            self.id = entry[0]
            self.age = entry[1]
            self.sex = entry[2]
            self.highest_education = entry[3]
            self.assigned_font = entry[4]
            self.result_font = entry[5]
            self.time_in_milis = entry[6]
            self.question_count = entry[7]
            self.entry_time = entry[8]

    def save(self):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "INSERT INTO experiment_entry (" \
              "age," \
              "sex," \
              "highest_education," \
              "assigned_font," \
              "result_font," \
              "time_in_milis," \
              "question_count" \
              ") VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id,entry_time"
        cursor.execute(sql, [self.age if not (self.age == 'NaN') else None,
                             self.sex,
                             self.highest_education,
                             self.assigned_font,
                             self.result_font,
                             self.time_in_milis,
                             self.question_count])
        dbres = cursor.fetchone()
        self.id = dbres[0]
        self.entry_time = dbres[1]
        db.commit()

    @staticmethod
    def getall():
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM experiment_entry"
        cursor.execute(sql)
        dbres = cursor.fetchall()
        entries = []
        for line in dbres:
            e = DBEntry(line)
            entries.append(e)
        return [e.jsonify() for e in entries]




    def jsonify(self):
        return {"id": self.id,
                "age": self.age,
                "sex": self.sex,
                "highest_education": self.highest_education,
                "asigned_font": self.assigned_font,
                "result_font": self.result_font,
                "time_in_milis": self.time_in_milis,
                "question_count": self.question_count,
                "entry_time": self.entry_time.isoformat()}
