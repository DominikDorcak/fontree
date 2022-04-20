from src import database
from src.api.exceptions.NotFoundException import NotFoundException


class DBNode:
    def __init__(self, *args):
        if len(args) == 5:
            self.id = int(args[0])
            self.left_child = int(args[1])
            self.right_child = int(args[2])
            self.feature_id = int(args[3]) if args[3] is not None else 0
            self.class_id = int(args[4])
            return
        if len(args) == 1:
            self.load(args[0])

    def is_leaf(self):
        return self.left_child == self.right_child

    def loadData(self, args):
        self.id = int(args[0])
        self.left_child = int(args[1])
        self.right_child = int(args[2])
        self.feature_id = int(args[3]) if args[3] is not None else 0
        self.class_id = int(args[4])

    def load(self, id):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * from node WHERE node_id=%s"
        cursor.execute(sql, [id])
        dbres = cursor.fetchone()
        if dbres is None:
            raise NotFoundException
        self.loadData(dbres)

    def saveRadix(self):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "INSERT INTO node (left_child_id,right_child_id,question_id,font_id) VALUES (%s,%s,%s,%s)"
        data = (None, None, None, None)
        cursor.execute(sql, data)
        db.commit()
        self.id = int(cursor.lastrowid)
        self.addRadixId(self.id)
        self.update()
        return self.id

    def addRadixId(self, radix_id):
        self.right_child += radix_id
        self.left_child += radix_id

    def update(self):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "UPDATE node SET " \
              "left_child_id=%s, " \
              "right_child_id=%s, " \
              "question_id=%s, " \
              "font_id=%s " \
              "WHERE node_id=%s "
        data = (self.left_child,
                self.right_child,
                self.feature_id,
                self.class_id,
                self.id)
        cursor.execute(sql, data)
        db.commit()

    def saveNode(self, radix_id):
        self.addRadixId(radix_id)
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "INSERT INTO  node (left_child_id,right_child_id,question_id,font_id)" \
              " VALUES " \
              "(%s ,%s, %s, %s )"
        data = (self.left_child,
                self.right_child,
                self.feature_id,
                self.class_id,)
        cursor.execute(sql, data)
        db.commit()

    def toString(self):
        res = 'NODE:\n' \
              '\tid:{id}\n' \
              '\tleft child:{lch}\n' \
              '\tright child:{rch}\n' \
              '\tfeature:{f}\n' \
              '\tclass:{c}\n' \
            .format(
            id=self.id,
            lch=self.left_child,
            rch=self.right_child,
            f=self.feature_id,
            c=self.class_id
        )
        return res

    def jsonify(self):
        return {"node_id": self.id,
                "left_child": self.left_child,
                "right_child": self.right_child,
                "question_id": self.feature_id,
                "font_id": self.class_id,
                "is_leaf": self.is_leaf()}
