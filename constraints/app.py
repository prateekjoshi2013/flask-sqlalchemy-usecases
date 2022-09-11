from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kenrbogn:s7pyZ-IYU2MgZutBJzTcXOrQHULh6HTP@jelani.db.elephantsql.com/kenrbogn'
db = SQLAlchemy(app)

class MyTableWithConstraints(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    unique_col=db.Column(db.String(50),unique=True)
    notnull_col=db.Column(db.String(20),nullable=False)
    '''
    use server instead of server_default if you want to
    set the default value through the app and not the 
    db(postgres,oracle)server
    '''
    default_col=db.Column(db.Integer,server_default='10') 
    '''
    use check constraints only on dbs which allow it like 
    postgres and oracle
    '''
    check_col=db.Column(db.Integer,db.CheckConstraint('check_col>5'))



'''
ON UPDATE and ON DELETE
Most databases support cascading of foreign key values, that is the when a parent row is updated the new value is placed in child rows, or when the parent row is deleted all corresponding child rows are set to null or deleted. In data definition language these are specified using phrases like “ON UPDATE CASCADE”, “ON DELETE CASCADE”, and “ON DELETE SET NULL”, corresponding to foreign key constraints. The phrase after “ON UPDATE” or “ON DELETE” may also other allow other phrases that are specific to the database in use. The ForeignKey and ForeignKeyConstraint objects support the generation of this clause via the onupdate and ondelete keyword arguments. The value is any string which will be output after the appropriate “ON UPDATE” or “ON DELETE” phrase:

child = Table('child', metadata_obj,
    Column('id', Integer,
            ForeignKey('parent.id', onupdate="CASCADE", ondelete="CASCADE"),
            primary_key=True
    )
)

composite = Table('composite', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('rev_id', Integer),
    Column('note_id', Integer),
    ForeignKeyConstraint(
                ['rev_id', 'note_id'],
                ['revisions.id', 'revisions.note_id'],
                onupdate="CASCADE", ondelete="SET NULL"
    )
)
Note that these clauses require InnoDB tables when used with MySQL. They may also not be supported on other databases.

See also

For background on integration of ON DELETE CASCADE with ORM relationship() constructs, see the following sections:

Using foreign key ON DELETE cascade with ORM relationships

Using foreign key ON DELETE with many-to-many relationships
'''

'''
UNIQUE Constraint
Unique constraints can be created anonymously on a single column using the unique keyword on Column. Explicitly named unique constraints and/or those with multiple columns are created via the UniqueConstraint table-level construct.

from sqlalchemy import UniqueConstraint

metadata_obj = MetaData()
mytable = Table('mytable', metadata_obj,

    # per-column anonymous unique constraint
    Column('col1', Integer, unique=True),

    Column('col2', Integer),
    Column('col3', Integer),

    # explicit/composite unique constraint.  'name' is optional.
    UniqueConstraint('col2', 'col3', name='uix_1')
    )
'''

'''

CHECK Constraint
Check constraints can be named or unnamed and can be created at the Column or Table level, using the CheckConstraint construct. The text of the check constraint is passed directly through to the database, so there is limited “database independent” behavior. Column level check constraints generally should only refer to the column to which they are placed, while table level constraints can refer to any columns in the table.

Note that some databases do not actively support check constraints such as MySQL.

from sqlalchemy import CheckConstraint

metadata_obj = MetaData()
mytable = Table('mytable', metadata_obj,

    # per-column CHECK constraint
    Column('col1', Integer, CheckConstraint('col1>5')),

    Column('col2', Integer),
    Column('col3', Integer),

    # table level CHECK constraint.  'name' is optional.
    CheckConstraint('col2 > col3 + 5', name='check1')
    )

mytable.create(engine)
CREATE TABLE mytable (
    col1 INTEGER  CHECK (col1>5),
    col2 INTEGER,
    col3 INTEGER,
    CONSTRAINT check1  CHECK (col2 > col3 + 5)
)
'''
'''
PRIMARY KEY Constraint
The primary key constraint of any Table object is implicitly present, based on the Column objects that are marked with the Column.primary_key flag. The PrimaryKeyConstraint object provides explicit access to this constraint, which includes the option of being configured directly:

from sqlalchemy import PrimaryKeyConstraint

my_table = Table('mytable', metadata_obj,
            Column('id', Integer),
            Column('version_id', Integer),
            Column('data', String(50)),
            PrimaryKeyConstraint('id', 'version_id', name='mytable_pk')
        )
'''