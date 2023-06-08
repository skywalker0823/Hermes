from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# # 建立資料庫物件
db = SQLAlchemy()

# db.Model 是所有 Model 的基礎，所以我們定義一個基礎的 BaseModel 來繼承 db.Model
class BaseModel(db.Model):
    # __abstract__ = True 代表這個 Model 不會被實體化
    # __abstract__ = True

    # id 是每個 Model 都會有的欄位，所以我們在這裡定義一個
    id = db.Column(db.Integer, primary_key=True)

    # created_at 記錄資料建立時間
    created_at = db.Column(db.DateTime, default=datetime.now)

    # updated_at 記錄資料更新時間
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


# User 繼承了 BaseModel，所以 User 會有 id、created_at、updated_at 這三個欄位
class User(BaseModel):
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)



# db.session 是資料庫的 session 物件，我們可以透過它來新增、修改、刪除資料  # 這裡我們定義一個基礎的 CRUD 操作