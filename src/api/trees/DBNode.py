from src import database


class DBNode:
    def __init__(self, id, left_child, right_child, feature_id, class_id):
        self.id = id
        self.left_child = left_child
        self.right_child = right_child
        self.feature_id = feature_id
        self.class_id = class_id

    def is_leaf(self):
        return self.left_child == self.right_child

    def saveRadix(self):
        cnx = database.getDbConnection()
        cursor = cnx.cursor()
        sql = "INSERT INTO node () VALUES () "
        cursor.execute(sql)
        self.id = int(cursor.lastrowid)
        self.addRadixId(self.id)
        self.update()
        return self.id

    def addRadixId(self, radix_id):
        self.right_child += radix_id
        self.left_child += radix_id

    def update(self):
        cnx = database.getDbConnection()
        cursor = cnx.cursor()
        sql = "UPDATE node SET left_child_id=%s, " \
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

    def saveNode(self,radix_id):
        cnx = database.getDbConnection()
        self.addRadixId(radix_id)
        cursor = cnx.cursor()
        sql = "INSERT INTO  node (left_child_id,right_child_id,question_id,font_id)" \
              " VALUES " \
              "(%integer ,%integer, %integer, %integer )"
        data = (self.left_child,
                self.right_child,
                self.feature_id,
                self.class_id,)
        cursor.execute(sql, data)

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
