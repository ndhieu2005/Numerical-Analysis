#Cho số lần lặp và cho khoảng cách ly nghiệm
import numpy as np
import sympy as sp
def newton_method(f_str,df_str,d2f_str,a,b,n):
    #Khởi tạo biến x và biểu thức toán học
    x=sp.symbols('x')
    #Chuyển các chuỗi hàm thành biểu thức toán học
    f_expr = sp.sympify(f_str)
    df_expr = sp.diff(f_expr,x)
    d2f_expr=sp.diff(df_expr,x)
    #Hàm và các đạo hàm dưới dạng hàm số
    f=sp.lambdify(x,f_expr,"numpy")
    df=sp.lambdify(x,df_expr,"numpy")
    d2f = sp.lambdify(x,d2f_expr,"numpy")
    #Kiểm tra dấu
    def check_sign_consistency(func,a,b,num_points=100):
        xs=np.linspace(a,b,num_points)
        signs = [np.sign(func(x)) for x in xs]
        return len(set(signs)) ==1
    #Kiểm tra xem f' và f'' có thay đổi dấu không
    if not check_sign_consistency(df,a,b):
        print(f"chú ý:đạo hàm f'(x) thay đổi dấu trên khoảng [{a},{b}]")
    if not check_sign_consistency(d2f,a,b):
        print(f"Chú ý: Đạo hàm f''(x) thay đổi dấu trên khoảng [{a},{b}]")
    #Bước 2: xét dấu của f'(x) và f''(x)
    x0 = a #khởi tạo x0
    if df(a) * d2f(a) > 0:
        x0 = b
    elif df(a) * d2f(a) <0:
        x0 =a
    print(f"Giá trị khởi tạo x0:{x0}")
    #Bước 3: Tìm nghiệm gần đúng
    for _ in range (n):
        #tính giá trị hàm f(x) và đạo hàm f'(x) tại x0
        fx = f(x0)
        dfx = df(x0)
        #kiểm tra nếu đạo hàm f'(x) = 0, tránh chia cho 0
        if dfx == 0:
            print("Đạo hàm bằng 0, không thể tiếp tục.")
            return None
        #Cập nhật giá trị x theo công thức Newton
        x_new = x0 - fx/dfx
        #kiểm tra sai số và dừng nếu sai số đủ nhỏ
        if abs(x_new - x0) < 1e-6:
            print(f"Sai số nhỏ hơn ngường, dừng lại.")
            return x_new
        #Cập nhật x0 cho vòng lặp tiếp theo
        x0 = x_new

    print(f"Không hội tự sau {n} vòng lặp.")
    return None
#Nhập các chuỗi hàm f(x),f'(x),f''(x) từ người dùng
f_str = input("Nhập hàm f(x) dưới dạng chuỗi (ví dụ: 'x**2 - 2'):")
df_str = input("Nhập đạo hàm f'(x) dưới dạng chuỗi(ví dụ:'2*x'):")
d2f_str = input("Nhập đạo hàm bậc 2 f''(x) dưới dạng chuỗi (ví dụ: '2'):")
#Nhập giá trị cho a,b và số lần lặp n
a = float(input("Nhập giá trị a:"))
b = float(input("Nhập giá trị b:"))
n = int(input("Nhập số lần lặp n:"))

# Sử dụng phương pháp Newton để tìm nghiệm
result = newton_method(f_str,df_str,d2f_str,a,b,n)

if result is not None:
    print(f"Nghiệm gần đúng là: {result}")
