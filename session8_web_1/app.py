from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"


#Trên route có parameter gì thì ở hàm phải có parameter đấy
@app.route('/say-hi/<name>')
def sayhi(name):
    return "Hi {}".format(name)

# Exercise
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return str(result)

# HTML
@app.route('/poem')
def poem():
    # Đặt thành dictionary
    # List nên đặt tên có số nhiều
    poems = [
        {
            'title'   : "Thơ con cóc",
            'content' : '''
                Râu tôm nấu với ruột bầu 
            ''',
            'author' : "...",
            'gender' : "male"
        },
        {
            'title'   : "Thơ con cóc 2",
            'content' : '''
                Râu tôm nấu với ruột bầu 
            ''',
            'author' : "...",
            'gender' : "female"
        }
    ]
    return render_template("poem.html", 
                            poems = poems
                            )
# Tách phần xử lý logic, server ra 1 bên, file HTML ra 1 bên
# html ở trong thư mục templates(phải viết chính xác)
# template là 1 file html chưa hoàn chỉnh, còn chỗ trống để fill vào
if __name__ == '__main__':
    app.run(port = 8080, debug=True)
# Nếu không có port = ... => port mặc định là 5000
# Nếu server chết thì chạy lại app.py
# Server chết vì để chế độ auto-save, đang code dở => code k có nghĩa => server chết
