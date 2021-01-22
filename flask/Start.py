import decimal

from flask import Flask, request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from collections import OrderedDict
import json
from sqlalchemy import func

pymysql.install_as_MySQLdb()

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/NationalDefense'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Data_user(db.Model):
    __tablename__ = 'User'
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    idcard = db.Column(db.String(255))
    age = db.Column(db.String(255))
    sex = db.Column(db.String(255))
def data_user_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        name=Data.name,
        idcard=Data.idcard,
        age=Data.age,
        sex=Data.sex
    )
@app.route('/user', methods=['GET'])
def get_data_user():
    # print(Data.query.count())
    MyData = Data_user.query.all()
    js = list(map(data_user_to_dict, MyData))
    print(js)
    return(jsonify(js))






class Data_user_account(db.Model):
    __tablename__ = 'User_account'
    ID = db.Column(db.Integer, primary_key=True)
    Card_id = db.Column(db.String)
    bank = db.Column(db.String)
    balance = db.Column(db.Integer)
    User_id = db.Column(db.Integer)
def data_user_account_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        Card_id=Data.Card_id,
        bank=Data.bank,
        balance=Data.balance,
        User_id=Data.User_id,
    )
@app.route('/user_account', methods=['GET'])
def get_data_video():
    # print(Data.query.count())
    MyData = Data_user_account.query.all()
    js = list(map(data_user_account_to_dict, MyData))
    print(js)
    return(jsonify(js))






class Data_payment_record(db.Model):
    __tablename__ = 'Payment_record'
    ID = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255))
    amount = db.Column(db.Integer)
    Commodity_ID = db.Column(db.Integer)
    User_account_ID = db.Column(db.String(255))
    Store_account_ID = db.Column(db.String(255))
def data_payment_record_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        date=Data.date,
        amount=Data.amount,
        Commodity_ID=Data.Commodity_ID,
        User_account_ID=Data.User_account_ID,
        Store_account_ID=Data.Store_account_ID,
    )
@app.route('/payment_record', methods=['GET'])
def get_data_payment_record():
    # print(Data.query.count())
    MyData = Data_payment_record.query.all()
    js = list(map(data_payment_record_to_dict, MyData))
    print(js)
    return(jsonify(js))






class Data_text(db.Model):
    __tablename__ = 'text'
    Author = db.Column(db.String, primary_key=True)
    Language = db.Column(db.String)
    Face = db.Column(db.String)

def data_text_to_dict(Data):
    return OrderedDict(
        Author=Data.Author,
        Language=Data.Language,
        Face=Data.Face,
    )

@app.route('/text', methods=['GET'])
def get_data_text():
    # print(Data.query.count())
    MyData = Data_text.query.all()
    js = list(map(data_text_to_dict, MyData))
    print(js)
    return(jsonify(js))



class Data_picture(db.Model):
    __tablename__ = 'picture'
    id = db.Column(db.Integer, primary_key=True)
    Memory = db.Column(db.Integer)
    Pixel = db.Column(db.String)
    Size = db.Column(db.String)

def data_picture_to_dict(Data):
    return OrderedDict(
        id=Data.id,
        Memory=Data.Memory,
        Pixel=Data.Pixel,
        Size=Data.Size,
    )

@app.route('/picture', methods=['GET'])
def get_data_picture():
    # print(Data.query.count())
    MyData = Data_picture.query.all()
    js = list(map(data_picture_to_dict, MyData))
    print(js)
    return(jsonify(js))




class Data_cof(db.Model):
    __tablename__ = 'cof'
    Author = db.Column(db.String, primary_key=True)
    Time = db.Column(db.String)
    Location = db.Column(db.String)
    Favor = db.Column(db.Integer)
    Comment = db.Column(db.String)

def data_cof_to_dict(Data):
    return OrderedDict(
        Author=Data.Author,
        Time=Data.Time,
        Location=Data.Location,
        Favor=Data.Favor,
        Comment=Data.Comment,
    )

@app.route('/cof', methods=['GET'])
def get_data_cof():
    # print(Data.query.count())
    MyData = Data_cof.query.all()
    js = list(map(data_cof_to_dict, MyData))
    print(js)
    return(jsonify(js))


















class Data_test(db.Model):
    __tablename__ = 'test'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Password = db.Column(db.String)
    Sex = db.Column(db.String)
    WeChatID=db.Column(db.String)
    Signature=db.Column(db.String)
    Region=db.Column(db.String)

def data_test_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        Name=Data.Name,
        Password=Data.Password,
        Sex=Data.Sex,
        WeChatID=Data.WeChatID,
        Signature=Data.Signature,
        Region=Data.Region,
    )

@app.route('/test/get', methods=['GET'])
def get_test():
    # print(Data.query.count())
    MyData = Data_test.query.all()
    js = list(map(data_test_to_dict, MyData))
    print(js)
    return(jsonify(js))

# @app.route('/test/update', methods=['POST'])
# def update_test():
#     if request.method == 'POST':
#         print('hh')
#         ID = request.form.get('ID')
#         print(ID)
#         Name = request.form.get('Name')
#         print(Name)
#         Password = request.form.get('Password')
#         print(Password)
#         Data_test.query.filter_by(ID=ID).update({'Password': Password})
#         Data_test.query.filter_by(ID=ID).update({'Name': Name})
#         db.session.commit()
#         # recognize_info = {'id': postdata, 'info': '收到' + file.filename}
#         # return jsonify(recognize_info), 201

@app.route('/test/search', methods=['POST'])
def search_test():
    if request.method == 'POST':
        print('hh')
        # ID = request.form.get('ID')
        # print(ID)
        Name = request.form.get('Name')
        Sex = request.form.get('Sex')
        print(Name)
        print(Sex)
        # Password = request.form.get('Password')
        # print(Password)
        # Data_test.query.filter_by(ID=ID).update({'Password': Password})
        temp=Data_test.query.filter_by(Name=Name, Sex=Sex)
        js = list(map(data_test_to_dict, temp))
        print(js)
        return (jsonify(js))
        # db.session.commit()
        # print(type(temp))

@app.route('/test/add', methods=['POST'])
def add_test():
    if request.method == 'POST':
        print('hh')
        # ID = request.form.get('ID')
        # print(ID)
        ID = request.form.get('ID')
        Name = request.form.get('Name')
        Password = request.form.get('Password')
        Sex = request.form.get('Sex')
        WeChatID = request.form.get('WeChatID')
        Signature = request.form.get('Signature')
        Region = request.form.get('Region')
        print(ID+Name+Password+Sex+WeChatID+Signature+Region)

        user1=Data_test(ID=ID, Name=Name, Password=Password, Sex=Sex, WeChatID=WeChatID, Signature=Signature, Region=Region)
        db.session.add(user1)
        db.session.commit()

        # Password = request.form.get('Password')
        # print(Password)
        # Data_test.query.filter_by(ID=ID).update({'Password': Password})
        # temp=Data_test.query.filter_by(Name=Name, Sex=Sex)
        # js = list(map(data_test_to_dict, temp))
        # print(js)
        # return (jsonify(js))
        # db.session.commit()
        # print(type(temp))

@app.route('/test/update', methods=['POST'])
def update_test():
    if request.method == 'POST':
        print('hh')
        # ID = request.form.get('ID')
        # print(ID)
        ID = request.form.get('ID')
        Name = request.form.get('Name')
        Password = request.form.get('Password')
        Sex = request.form.get('Sex')
        WeChatID = request.form.get('WeChatID')
        Signature = request.form.get('Signature')
        Region = request.form.get('Region')
        print(ID+Name+Password+Sex+WeChatID+Signature+Region)

        user1=Data_test.query.filter(Data_test.ID==ID).first()
        user1.Name=Name
        user1.Password=Password
        user1.Sex=Sex
        user1.WeChatID=WeChatID
        user1.Signature=Signature
        user1.Region=Region
        db.session.commit()

@app.route('/test/delete', methods=['POST'])
def delete_test():
    if request.method == 'POST':
        print('hh')
        # ID = request.form.get('ID')
        # print(ID)
        ID = request.form.get('ID')
        print(ID)

        user1=Data_test.query.filter(Data_test.ID==ID).first()
        db.session.delete(user1)
        db.session.commit()

        # user1=Data_test.query.filter(Data_test.ID==ID).first()
        # user1.Name=Name
        # user1.Password=Password
        # user1.Sex=Sex
        # user1.WeChatID=WeChatID
        # user1.Signature=Signature
        # user1.Region=Region
        # db.session.commit()








class Data_store(db.Model):
    __tablename__ = 'store'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Score=db.Column(db.String)
def data_store_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        Name=Data.Name,
        Score=Data.Score
    )
@app.route('/store', methods=['GET'])
def get_store():
    # print(Data.query.count())
    MyData = Data_store.query.all()
    js = list(map(data_store_to_dict, MyData))
    print(js)
    return(jsonify(js))







class Data_store2(db.Model):
    __tablename__ = 'store2'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Quantity=db.Column(db.Integer)
    Price=db.Column(db.Integer)

def data_store2_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        Name=Data.Name,
        Quantity=Data.Quantity,
        Price=Data.Price
    )

@app.route('/store2/get', methods=['GET'])
def get_store2():
    # print(Data.query.count())
    MyData = Data_store2.query.all()
    js = list(map(data_store2_to_dict, MyData))
    print(js)
    return(jsonify(js))









class Data_store3(db.Model):
    __tablename__ = 'store3'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Quantity=db.Column(db.Integer)
    Price=db.Column(db.Integer)

def data_store3_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        Name=Data.Name,
        Quantity=Data.Quantity,
        Price=Data.Price
    )

@app.route('/store3/get', methods=['GET'])
def get_store3():
    # print(Data.query.count())
    MyData = Data_store3.query.all()
    js = list(map(data_store3_to_dict, MyData))
    print(js)
    return(jsonify(js))



class Data_store1(db.Model):
    __tablename__ = 'store1'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Quantity=db.Column(db.Integer)
    Price=db.Column(db.Integer)
def data_store1_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        Name=Data.Name,
        Quantity=Data.Quantity,
        Price=Data.Price
    )
@app.route('/store1/get', methods=['GET'])
def get_store1():
    # print(Data.query.count())
    MyData = Data_store1.query.all()
    js = list(map(data_store1_to_dict, MyData))
    print(js)
    return(jsonify(js))








class Data_show(db.Model):
    __tablename__ = 'show'
    ID = db.Column(db.Integer, primary_key=True)
    From = db.Column(db.String)
    Year = db.Column(db.String)
    Account_Title = db.Column(db.String)
    Budget_Activity_Title=db.Column(db.String)
    Organization=db.Column(db.String)
    TOA_Amount=db.Column(db.String)

def data_show_to_dict(Data):
    return OrderedDict(
        ID=Data.ID,
        From=Data.From,
        Year=Data.Year,
        Account_Title=Data.Account_Title,#Password
        Budget_Activity_Title=Data.Budget_Activity_Title,#WeChatID
        Organization=Data.Organization,#Signature
        TOA_Amount=Data.TOA_Amount,#Region
    )

@app.route('/show/get', methods=['GET'])
def get_show():
    # print(Data.query.count())
    MyData = Data_show.query.all()
    js = list(map(data_show_to_dict, MyData))
    print(js)
    return(jsonify(js))

# @app.route('/test/update', methods=['POST'])
# def update_test():
#     if request.method == 'POST':
#         print('hh')
#         ID = request.form.get('ID')
#         print(ID)
#         Name = request.form.get('Name')
#         print(Name)
#         Password = request.form.get('Password')
#         print(Password)
#         Data_test.query.filter_by(ID=ID).update({'Password': Password})
#         Data_test.query.filter_by(ID=ID).update({'Name': Name})
#         db.session.commit()
#         # recognize_info = {'id': postdata, 'info': '收到' + file.filename}
#         # return jsonify(recognize_info), 201

@app.route('/show/search', methods=['POST'])
def search_show():
    if request.method == 'POST':


        From = request.form.get('From')
        Year = request.form.get('Year')
        Organization = request.form.get('Organization')
        # print(From)
        # print(Year)

        run_str='Data_show.query.filter_by('
        if  From not in ['',"undefined"]:
            run_str+="From='"+From+"',"
        if Year not in ['',"undefined"]:
            run_str+="Year='"+Year+"',"
        if Organization not in ['',"undefined"]:
            run_str+="Organization='"+Organization+"',"
        run_str=run_str[:-1]+")"
        print(run_str)
        if run_str=='Data_show.query.filter_by)':
            temp = Data_show.query.all()
        else:
            temp=eval(run_str)

        # run_str=''
        # if From!="undefined":
        #     run_str+="From='"+From+"',"
        # if Year:
        #     run_str+="Year='"+Year+"',"
        # run_str=run_str[:-1]+")"
        # print(run_str)
        # if run_str==')':
        #     temp = Data_show.query.all()
        # else:
        #     temp = Data_show.query.filter_by(run_str)

        # if From:
        #     if Year:
        #         temp=Data_show.query.filter_by(From=From, Year=Year)
        #     else:
        #         temp = Data_show.query.filter_by(From=From)
        # else:
        #

        js = list(map(data_show_to_dict, temp))
        # print(js)
        return (jsonify(js))
        # db.session.commit()
        # print(type(temp))

@app.route('/show/add', methods=['POST'])
def add_show():
    if request.method == 'POST':
        print('hh')
        # ID = request.form.get('ID')
        # print(ID)
        ID = request.form.get('ID')
        From = request.form.get('From')
        Account_Title = request.form.get('Account_Title')
        Year = request.form.get('Year')
        Budget_Activity_Title = request.form.get('Budget_Activity_Title')
        Organization = request.form.get('Organization')
        TOA_Amount = request.form.get('TOA_Amount')
        print(ID+From+Account_Title+Year+Budget_Activity_Title+Organization+TOA_Amount)

        user1=Data_test(ID=ID, From=From, Account_Title=Account_Title, Year=Year, Budget_Activity_Title=Budget_Activity_Title, Organization=Organization, TOA_Amount=TOA_Amount)
        db.session.add(user1)
        db.session.commit()

        # Password = request.form.get('Password')
        # print(Password)
        # Data_test.query.filter_by(ID=ID).update({'Password': Password})
        # temp=Data_test.query.filter_by(Name=Name, Sex=Sex)
        # js = list(map(data_test_to_dict, temp))
        # print(js)
        # return (jsonify(js))
        # db.session.commit()
        # print(type(temp))

@app.route('/show/update', methods=['POST'])
def update_show():
    if request.method == 'POST':
        print('hh')
        # ID = request.form.get('ID')
        # print(ID)
        ID = request.form.get('ID')
        From = request.form.get('From')
        Account_Title = request.form.get('Account_Title')
        Year = request.form.get('Year')
        Budget_Activity_Title = request.form.get('Budget_Activity_Title')
        Organization = request.form.get('Organization')
        TOA_Amount = request.form.get('TOA_Amount')
        print(ID+From+Account_Title+Year+Budget_Activity_Title+Organization+TOA_Amount)

        user1=Data_show.query.filter(Data_show.ID==ID).first()
        user1.From=From
        user1.Account_Title=Account_Title
        user1.Year=Year
        user1.Budget_Activity_Title=Budget_Activity_Title
        user1.Organization=Organization
        user1.TOA_Amount=TOA_Amount
        db.session.commit()

@app.route('/show/delete', methods=['POST'])
def delete_show():
    if request.method == 'POST':
        print('hh')
        # ID = request.form.get('ID')
        # print(ID)
        ID = request.form.get('ID')
        print(ID)

        user1=Data_show.query.filter(Data_show.ID==ID).first()
        db.session.delete(user1)
        db.session.commit()

        # user1=Data_test.query.filter(Data_test.ID==ID).first()
        # user1.Name=Name
        # user1.Password=Password
        # user1.Sex=Sex
        # user1.WeChatID=WeChatID
        # user1.Signature=Signature
        # user1.Region=Region
        # db.session.commit()


# 以下两段代码就是按照Organization返回时间序列数据
def data_echarts_to_dict(Data):
    return OrderedDict(
        Year=Data.Year,
        sum=Data.sum,
    )
@app.route('/echarts', methods=['POST'])
def echarts():
    if request.method == 'POST':
        print('Received POST request')
        Organization=request.form.get('Organization')
        print(Organization)

    temp = db.session.query(Data_show.Year, func.sum(Data_show.TOA_Amount).label("sum")).group_by(Data_show.Year).filter_by(Organization=Organization)
    js = list(map(data_echarts_to_dict, temp))
    print(js)

    # 这个类是因为上面的查询结果temp不能直接用jsonify来返回给前端，然后我在百度找到了这个解决方法
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                return float(o)
            super(DecimalEncoder, self).default(o)

    return (json.dumps(js,cls=DecimalEncoder))




# 解决跨域问题用的
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ

if __name__ == '__main__':
    app.run(debug=True)
