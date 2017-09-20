from peewee import SqliteDatabase, Model, TextField, IntegerField

database = SqliteDatabase('test.db', **{})


class Categories(Model):
    category = TextField(db_column='category_id', null=True)
    level = IntegerField(null=True)
    name = TextField(null=True)
    parent = TextField(db_column='parent_id', null=True)

    class Meta:
        database = database
        db_table = 'categories'
        primary_key = False


class Products1(Model):
    category = TextField(db_column='category_id', null=True)
    plu = TextField(null=True)
    title = TextField(null=True)

    class Meta:
        database = database
        db_table = 'products_1'
        primary_key = False


class Products2(Model):
    eshop_category = TextField(db_column='eshop_category_id', null=True)
    eshop_category_name = TextField(null=True)
    plu = TextField(null=True)
    title = TextField(null=True)

    class Meta:
        database = database
        db_table = 'products_2'
        primary_key = False
