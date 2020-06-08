import os


duong_dan_goc = os.getcwd()
duong_dan_danh_sach = os.path.join(duong_dan_goc,
                                    r'danhsachbocai.txt')
def liet_ke_thu_muc(duong_dan_thu_muc_cha):
    print(r'Lấy danh sách thư mục trong:')
    print(duong_dan_thu_muc_cha)
    if os.path.exists(duong_dan_thu_muc_cha):
        noi_dung_thu_muc_cha = os.listdir(duong_dan_thu_muc_cha)
        danh_sach_thu_muc_con = []
        for noi_dung in noi_dung_thu_muc_cha:
            duong_dan_noi_dung = os.path.join(duong_dan_thu_muc_cha,
                                                noi_dung)
            if os.path.isdir(duong_dan_noi_dung):
                danh_sach_thu_muc_con.append(duong_dan_noi_dung)
        return danh_sach_thu_muc_con
    return None

def kiem_tra_bo_cai(duong_dan_thu_muc, ten_bo_cai):
    print(r'Kiểm tra bộ cài trong thư mục:')
    print(duong_dan_thu_muc)
    if os.path.exists(duong_dan_thu_muc):
        noi_dung_thu_muc = os.listdir(duong_dan_thu_muc)
        if ten_bo_cai in noi_dung_thu_muc:
            return os.path.join(duong_dan_thu_muc, ten_bo_cai)
        return None

def lay_duong_dan_bo_cai(duong_dan_thu_muc, ten_phan_mem):
    if os.path.exists(duong_dan_thu_muc):
        print(r'Tìm thư mục con trong:')
        print(duong_dan_thu_muc)
        danh_sach_thu_muc_con = liet_ke_thu_muc(duong_dan_thu_muc)
        if not len(danh_sach_thu_muc_con) == 0:
            print(r'Tìm thấy %s thư mục' %
                    (len(danh_sach_thu_muc_con)))
            for thu_muc in danh_sach_thu_muc_con:
                lay_duong_dan_bo_cai(thu_muc,ten_phan_mem)
        else:
            duong_dan_bo_cai = kiem_tra_bo_cai(duong_dan_thu_muc,
                                                ten_phan_mem)
            if duong_dan_bo_cai is not None:
                print(r'Tìm thấy bộ cài trong:')
                print(duong_dan_bo_cai)
                print(r'Ghi vào file %s' % (duong_dan_danh_sach))
                with open(duong_dan_danh_sach, 'a',
                        encoding='utf16') as danh_sach:
                    danh_sach.write('%s\n' % (
                        duong_dan_bo_cai))

if __name__ == '__main__':
    ten_phan_mem = r'MasterTest.exe'
    lay_duong_dan_bo_cai(duong_dan_goc, ten_phan_mem)
