import pyautogui
import os
from time import sleep, process_time

pyautogui.PAUSE = 0
thoi_gian = process_time()
duong_dan_goc = os.path.abspath(r'.')
link_anh = duong_dan_goc
link_de_thi = os.path.join(duong_dan_goc,
                r'dethi.docx')
link_noi_luu_de = os.path.join(duong_dan_goc, r'ketqua', r'dethi')

def dang_nhap(link_icon, noi_dung):
    hop_thong_tin = pyautogui.locateOnScreen(link_icon)
    while hop_thong_tin is None:
        hop_thong_tin = pyautogui.locateOnScreen(link_icon)
    pyautogui.doubleClick(x=hop_thong_tin.left+hop_thong_tin.width+10,
                            y=(hop_thong_tin.top
                            +hop_thong_tin.height
                            +(hop_thong_tin.height/2)))
    pyautogui.typewrite([r'delete',])
    pyautogui.typewrite(noi_dung)

def click_nut(link_anh):
    nut_can_click = pyautogui.locateOnScreen(link_anh)
    while nut_can_click is None:
        nut_can_click = pyautogui.locateOnScreen(link_anh)
    pyautogui.click(pyautogui.center(nut_can_click))

def click_tiep_tuc():
    print(r'Ấn tiếp tục')
    link_tiep_tuc = os.path.join(link_anh, r'nuttieptuc.png')
    click_nut(link_tiep_tuc)

def kiem_tra_noi_luu(duong_dan, so_thu_tu):
    duong_dan_file = '%s %s' % (duong_dan, so_thu_tu)
    if os.path.exists(duong_dan_file):
        duong_dan_moi = kiem_tra_noi_luu(duong_dan, so_thu_tu+1)
        return duong_dan_moi
    return duong_dan_file

#Chay phan mem, nhap thong tin dang nhap
print(r'Ấn icon phần mềm')
link_icon_test = os.path.join(link_anh, r'icon_mastertest.png')
icon_test = pyautogui.locateOnScreen(link_icon_test)
icon_test_trung_tam = pyautogui.center(icon_test)
while icon_test_trung_tam is None:
    icon_test_trung_tam = pyautogui.center(icon_test)
pyautogui.doubleClick(icon_test_trung_tam)

#Nhap thong tin dang nhap he thong
print(r'Nhập tên đăng nhập')
icon_tendangnhap = os.path.join(link_anh, r'tendangnhap.png')
link_tendangnhapnull = os.path.join(link_anh, r'tendangnhap_null.png')
tendangnhap_noidung = r'admin'
dang_nhap(icon_tendangnhap,
                   tendangnhap_noidung)
print(r'Nhập mật khẩu')
icon_matkhau = os.path.join(link_anh, r'nhapmatkhau.png')
link_matkhaunull = os.path.join(link_anh, r'matkhau_null1.png')
#matkhau_noidung = pyautogui.password(text=r'Nhap mat khau',
#                                     title=r'nhap mat khau',
#                                     default=r'admin')
matkhau_noidung = r'admin'
dang_nhap(icon_matkhau,
                   matkhau_noidung)

#Dang nhap he thong
print(r'Ấn nút đồng ý')
link_dong_y = os.path.join(link_anh, r'dongy.png')
click_nut(link_dong_y)

#Lam de tu file
print(r'Ấn thiết lập đề thi')
link_thiet_lap_de_thi = os.path.join(link_anh, r'nutthietlapde.png')
click_nut(link_thiet_lap_de_thi)
link_lam_de_tu_file = os.path.join(link_anh, r'nutlamdetufile.png')
print(r'Chọn làm đề từ file')
click_nut(link_lam_de_tu_file)
link_chon_file_word = os.path.join(link_anh, r'nutchonfileword.png')
print(r'Ấn chọn file word')
click_nut(link_chon_file_word)
link_hop_nhap_duong_dan = os.path.join(link_anh, r'hopnhapduongdan.png')
print(r'Nhập đường dẫn file')
click_nut(link_hop_nhap_duong_dan)
pyautogui.typewrite(link_de_thi)
link_nut_open = os.path.join(link_anh, r'nutopen.png')
print(r'Chọn Open')
click_nut(link_nut_open)
print(r'Chọn tất cả')
link_chon_tat_ca = os.path.join(link_anh, r'nutchontatca.png')
chon_tat_ca = pyautogui.locateOnScreen(link_chon_tat_ca)
while chon_tat_ca is None:
    chon_tat_ca = pyautogui.locateOnScreen(link_chon_tat_ca)
print(r'Chọn vào đề thi')
pyautogui.click(x=chon_tat_ca.left+74,
                y=chon_tat_ca.top+(chon_tat_ca.height/2))
link_cho_vao_de_thi = os.path.join(link_anh, r'nutchonvaodethi.png')
click_nut(link_cho_vao_de_thi)
click_tiep_tuc()
print(r'Nhập tiêu đề')
link_tieu_de = os.path.join(link_anh, r'tieude.png')
click_nut(link_tieu_de)
pyautogui.typewrite(r'Kiem tra hoc ky 1')
print(r'Nhập số lượng đề')
link_so_luong_de = os.path.join(link_anh, r'soluongde.png')
so_luong_de = pyautogui.locateOnScreen(link_so_luong_de)
while so_luong_de is None:
    so_luong_de = pyautogui.locateOnScreen(link_so_luong_de)
pyautogui.doubleClick(pyautogui.center(so_luong_de))
pyautogui.typewrite([r'delete', r'1', r'0'])
print(r'Nhập thời gian')
link_thoi_gian_thi = os.path.join(link_anh, r'thoigian.png')
click_nut(link_thoi_gian_thi)
pyautogui.typewrite(r'90')
click_tiep_tuc()
print(r'Ấn nút ...')
link_chon_noi_luu = os.path.join(link_anh, r'nut3cham.png')
click_nut(link_chon_noi_luu)
print(r'Nhập tên lưu file')
link_nhap_ten = os.path.join(link_anh, r'hopnhaptenfile.png')
click_nut(link_nhap_ten)
link_noi_luu_de_thi = kiem_tra_noi_luu(link_noi_luu_de, 0)
pyautogui.typewrite(link_noi_luu_de_thi)
print(r'Ấn nút lưu')
link_nut_save = os.path.join(link_anh, r'nutsave.png')
click_nut(link_nut_save)
print(r'Ấn nút xuất đề')
link_nut_xuat_de = os.path.join(link_anh, r'nutxuatde.png')
thoigian_annut = process_time()
click_nut(link_nut_xuat_de)
print(r'Xuất đề xong')
link_thong_bao = os.path.join(link_anh, r'trondexong.png')
thong_bao = pyautogui.locateOnScreen(link_thong_bao)
while thong_bao is None:
    thong_bao = pyautogui.locateOnScreen(link_thong_bao)
print(r'Ấn nút đồng ý')
link_dong_y = os.path.join(link_anh, r'dongy1.png')
click_nut(link_dong_y)
thoi_gian_tron_de = process_time() - thoigian_annut
print(r'Thời gian xuất đề: %s' % (thoi_gian_tron_de))


#Tong thoi gian chay chuong trinh
thoi_gian_xu_ly = process_time() - thoi_gian
print(r'Tổng thời gian xử lý: %s' % (thoi_gian_xu_ly))
exit(1)
