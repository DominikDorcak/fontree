class DBNode:
    def __init__(self, id, left_child, right_child, feature_id, class_id):
        self.id = id
        self.left_child = left_child
        self.right_child = right_child
        self.feature_id = feature_id
        self.class_id = class_id

    def is_leaf(self):
        return self.left_child == self.right_child

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
