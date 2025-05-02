

CREATE TABLE dichvu (
  dichvu_id INTEGER PRIMARY KEY AUTOINCREMENT,
  tendichvu TEXT,
  category TEXT,
  gia INTEGER,
  gioi_thieu TEXT
);
INSERT INTO dichvu (tendichvu, category, gia, gioi_thieu) VALUES
('Làm sạch răng', 'Nha khoa', 300000, 'Dịch vụ lấy cao răng và làm sạch răng chuyên sâu giúp bảo vệ nướu và ngăn ngừa viêm.'),
('Tẩy trắng răng', 'Nha khoa', 1200000, 'Sử dụng công nghệ tẩy trắng hiện đại giúp răng sáng lên từ 2-3 tông, an toàn và không ê buốt.'),
('Kiểm tra răng', 'Nha khoa', 150000, 'Kiểm tra tổng quát sức khỏe răng miệng định kỳ để phát hiện sớm các vấn đề.'),
('Trám răng', 'Nha khoa', 400000, 'Trám răng bằng vật liệu thẩm mỹ cao cấp, phục hồi chức năng và thẩm mỹ.'),
('Niềng răng', 'Nha khoa', 30000000, 'Dịch vụ niềng răng chuyên sâu giúp cải thiện khớp cắn và nụ cười thẩm mỹ.'),
('Dán sứ Veneer', 'Nha khoa', 10000000, 'Dán sứ Veneer siêu mỏng, bảo tồn răng gốc và cải thiện thẩm mỹ răng vượt trội.');

-----------------------
CREATE TABLE loiich_dich_vu (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dichvu_id INTEGER,
  mo_ta_loi_ich TEXT,
  FOREIGN KEY (dichvu_id) REFERENCES dichvu(dichvu_id)
);
INSERT INTO loiich_dich_vu (dichvu_id, mo_ta_loi_ich) VALUES
-- L�m s?ch r?ng (dichvu_id = 1)
(1, 'Lo?i b? m?ng b�m v� cao r?ng'),

-- T?y tr?ng r?ng (dichvu_id = 2)
(2, 'Gi�p r?ng tr?ng s�ng t? nhi�n'),
-- Ki?m tra r?ng (dichvu_id = 3)
(3, 'Ph�t hi?n s?m s�u r?ng v� c�c b?nh l� kh�c'),
-- Tr�m r?ng (dichvu_id = 4)
(4, 'Ph?c h?i h�nh d�ng v� ch?c n?ng r?ng'),
-- Ni?ng r?ng (dichvu_id = 5)
(5, 'C?i thi?n kh?p c?n v� th?m m? r?ng'),
-- D�n s? Veneer (dichvu_id = 6)
(6, 'Kh�ng c?n m�i nhi?u r?ng, b?o t?n m� r?ng th?t');


------------------------
CREATE TABLE quy_trinh_dich_vu (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dichvu_id INTEGER,
  TT_thien INTEGER,
  tieu_de TEXT,
  mo_ta TEXT,
  FOREIGN KEY (dichvu_id) REFERENCES dichvu(dichvu_id)
);
-- L�m s?ch r?ng (dichvu_id = 1)
INSERT INTO quy_trinh_dich_vu (dichvu_id, TT_thien, tieu_de, mo_ta) VALUES
(1, 1, 'Kh�m v� t? v?n', 'B�c s? ki?m tra t?ng qu�t t�nh tr?ng r?ng mi?ng'),
(1, 2, 'L�m s?ch cao r?ng', 'S? d?ng m�y si�u �m l?y cao r?ng v� m?ng b�m'),
(1, 3, '?�nh b�ng r?ng', '?�nh b�ng b? m?t r?ng gi�p r?ng s�ng v� s?ch h?n');

-- T?y tr?ng r?ng (dichvu_id = 2)
INSERT INTO quy_trinh_dich_vu (dichvu_id, TT_thien, tieu_de, mo_ta) VALUES
(2, 1, 'Ki?m tra men r?ng', '??m b?o r?ng ?? ?i?u ki?n ?? t?y tr?ng'),
(2, 2, 'B�i thu?c t?y tr?ng', 'S? d?ng thu?c chuy�n d?ng v� thi?t b? �nh s�ng h? tr?'),
(2, 3, 'H??ng d?n ch?m s�c', 'T? v?n ch? ?? ?n u?ng, tr�nh th?c ph?m s?m m�u');

-- Ki?m tra r?ng (dichvu_id = 3)
INSERT INTO quy_trinh_dich_vu (dichvu_id, TT_thien, tieu_de, mo_ta) VALUES
(3, 1, 'Kh�m t?ng qu�t', 'B�c s? ki?m tra r?ng, n??u v� kh?p c?n'),
(3, 2, 'Ch?p X-quang (n?u c?n)', 'Ch?n ?o�n s�u r?ng ho?c c�c v?n ?? ?n'),
(3, 3, 'T? v?n ?i?u tr?', '??a ra k? ho?ch ch?m s�c v� ?i?u tr? n?u c?n');

-- Tr�m r?ng (dichvu_id = 4)
INSERT INTO quy_trinh_dich_vu (dichvu_id, TT_thien, tieu_de, mo_ta) VALUES
(4, 1, 'V? sinh v� g�y t�', 'L�m s?ch v�ng s�u v� g�y t� nh?'),
(4, 2, 'Tr�m r?ng', 'D�ng v?t li?u tr�m th?m m? ?? ph?c h?i r?ng'),
(4, 3, '?i?u ch?nh kh?p c?n', 'Ki?m tra v� ch?nh s?a n?u c?m ho?c l?ch');

-- Ni?ng r?ng (dichvu_id = 5)
INSERT INTO quy_trinh_dich_vu (dichvu_id, TT_thien, tieu_de, mo_ta) VALUES
(5, 1, 'Th?m kh�m v� l?y d?u r?ng', 'X�c ??nh t�nh tr?ng v� l�n ph�c ?? ?i?u tr?'),
(5, 2, 'G?n m?c c�i', 'Ti?n h�nh g?n h? th?ng d�y cung v� m?c c�i'),
(5, 3, 'T�i kh�m ??nh k?', '?i?u ch?nh l?c k�o h�ng th�ng theo ti?n ??');

-- D�n s? Veneer (dichvu_id = 6)
INSERT INTO quy_trinh_dich_vu (dichvu_id, TT_thien, tieu_de, mo_ta) VALUES
(6, 1, 'T? v?n v� thi?t k? n? c??i', 'L�n k? ho?ch h�nh d�ng v� m�u s?c r?ng mong mu?n'),
(6, 2, 'M�i r?ng nh? v� l?y d?u', 'Chu?n b? m?t r?ng v� g?i m?u cho labo'),
(6, 3, 'D�n m?t s?', 'G?n veneer l�n r?ng b?ng keo chuy�n d?ng v� ?i?u ch?nh ho�n t?t');

------------------------
CREATE TABLE KHNX_dichvu (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dichvu_id INTEGER,
  ten_KH TEXT,
  biet_danh TEXT,
  NX TEXT,
  ten_anh TEXT,
  FOREIGN KEY (dichvu_id) REFERENCES dichvu(dichvu_id)
);
-- L�m s?ch r?ng (dichvu_id = 1)
INSERT INTO KHNX_dichvu (dichvu_id, ten_KH, biet_danh, NX, ten_anh) VALUES
(1, 'Nguy?n Minh Anh', 'MinhA', 'D?ch v? l�m s?ch r?t nh? nh�ng, kh�ng ?au v� b�c s? t? v?n k?.', 'minh_anh.jpg'),
(1, 'L� Ho�ng', 'HoangLe', 'Sau khi l�m s?ch xong c?m gi�c mi?ng s?ch v� d? ch?u h?n h?n.', 'le_hoang.jpg');

-- T?y tr?ng r?ng (dichvu_id = 2)
INSERT INTO KHNX_dichvu (dichvu_id, ten_KH, biet_danh, NX, ten_anh) VALUES
(2, 'Tr?n Th?o', 'ThaoT', 'R?ng m�nh tr?ng s�ng r� r?t sau khi l�m, r?t h�i l�ng!', 'tran_thao.jpg'),
(2, 'Ph?m V?n H�ng', 'HungPV', 'D?ch v? chuy�n nghi?p, hi?u qu? nhanh.', 'van_hung.jpg');

-- Ki?m tra r?ng (dichvu_id = 3)
INSERT INTO KHNX_dichvu (dichvu_id, ten_KH, biet_danh, NX, ten_anh) VALUES
(3, '?? Th? Lan', 'LanDT', 'B�c s? kh�m c?n th?n v� ch? r� v?n ?? ?ang g?p.', 'thi_lan.jpg');

-- Tr�m r?ng (dichvu_id = 4)
INSERT INTO KHNX_dichvu (dichvu_id, ten_KH, biet_danh, NX, ten_anh) VALUES
(4, 'Ng� ??c Minh', 'MinhND', 'Tr�m xong nh�n kh�ng bi?t l� r?ng t?ng b? s�u lu�n.', 'duc_minh.jpg');

-- Ni?ng r?ng (dichvu_id = 5)
INSERT INTO KHNX_dichvu (dichvu_id, ten_KH, biet_danh, NX, ten_anh) VALUES
(5, 'L??ng Ng?c H�', 'HaNg', 'Ni?ng ???c 6 th�ng v� ?� th?y r?ng ??u h?n nhi?u.', 'ngoc_ha.jpg');

-- D�n s? Veneer (dichvu_id = 6)
INSERT INTO KHNX_dichvu (dichvu_id, ten_KH, biet_danh, NX, ten_anh) VALUES
(6, 'V? Qu?nh Trang', 'TrangVu', 'R?ng tr?ng ??p t? nhi�n, nh�n kh�ng ai bi?t l� r?ng s? lu�n.', 'quynh_trang.jpg');


----------------------
CREATE TABLE cauhoi_dichvu (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dichvu_id INTEGER,
  mota TEXT,
  traloi TEXT,
  FOREIGN KEY (dichvu_id) REFERENCES dichvu(dichvu_id)
);
INSERT INTO cauhoi_dichvu (dichvu_id, mota, traloi) VALUES
(1, 'Th?i gian kh�m m?t bao l�u?', 'Kho?ng 30 ph�t.'),
(2, 'C� c?n ??t l?ch tr??c kh�ng?', 'N�n ??t tr??c ?? tr�nh ch? l�u.');

CREATE TABLE hinhanh_dichvu (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dichvu_id INTEGER,
  ten_anh TEXT,
  loai INTEGER
  FOREIGN KEY (dichvu_id) REFERENCES dichvu(dichvu_id)
);
INSERT INTO hinhanh_dichvu (dichvu_id, ten_anh) VALUES
(1, 'lam_sach_rang.jpg'),      -- L�m s?ch r?ng
(2, 'tay_trang_rang.jpg'),     -- T?y tr?ng r?ng
(3, 'kiem_tra_rang.jpg'),      -- Ki?m tra r?ng
(4, 'tram_rang.jpg'),          -- Tr�m r?ng
(5, 'nieng_rang.jpg'),         -- Ni?ng r?ng
(6, 'dan_su_veneer.jpg');      -- D�n s? Veneer


CREATE TABLE bacsi (
  bacsi_id INTEGER PRIMARY KEY AUTOINCREMENT,
  ten TEXT,
  kinh_nghiem INTEGER,
  ten_anh TEXT,
  hoc_vi TEXT,
  chung_chi TEXT,
  chuyen_mon TEXT,
  ngon_ngu TEXT
);
INSERT INTO bacsi (ten, kinh_nghiem, ten_anh, hoc_vi, chung_chi, chuyen_mon, ngon_ngu) VALUES
('BS. Nguy?n V?n An', 10, 'nguyen_van_an.jpg', 'Ti?n s? R?ng-H�m-M?t', 'Ch?ng ch? nha khoa qu?c t? ICOI', 'Ch?nh nha v� ni?ng r?ng', 'Ti?ng Vi?t, Ti?ng Anh'),
('BS. Tr?n Th? Mai', 8, 'tran_thi_mai.jpg', 'Th?c s? Nha khoa', 'Ch?ng nh?n ph?c h�nh th?m m? Veneer', 'Th?m m? r?ng s?, d�n veneer', 'Ti?ng Vi?t'),
('BS. L� Quang Huy', 12, 'le_quang_huy.jpg', 'B�c s? chuy�n khoa II', 'Ch?ng ch? ?i?u tr? n?i nha chuy�n s�u', '?i?u tr? n?i nha v� t?y tr?ng r?ng', 'Ti?ng Vi?t, Ti?ng Anh');

CREATE TABLE bacsi_tag (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bacsi_id INTEGER,
  mo_ta TEXT,
  FOREIGN KEY (bacsi_id) REFERENCES bacsi(bacsi_id)
);
INSERT INTO bacsi_tag (bacsi_id, mo_ta) VALUES
(1, 'Chuy�n gia ni?ng r?ng kh�ng m?c c�i'),
(1, 'T? v?n ?i?u tr? kh?p c?n ph?c t?p'),
(2, 'Ph?c h�nh r?ng th?m m? to�n di?n'),
(2, 'D�n s? Veneer kh�ng m�i r?ng'),
(3, '?i?u tr? t?y kh�ng ?au'),
(3, 'T?y tr?ng r?ng b?ng c�ng ngh? laser Zoom');



CREATE TABLE thanhtuu_bacsi (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bacsi_id INTEGER,
  mo_ta TEXT,
  FOREIGN KEY (bacsi_id) REFERENCES bacsi(bacsi_id)
);
INSERT INTO thanhtuu_bacsi (bacsi_id, mo_ta) VALUES
(1, 'Gi?i nh?t H?i thi B�c s? ch?nh nha tr? to�n qu?c 2020'),
(2, '???c vinh danh t?i H?i ngh? Ph?c h�nh Th?m m? ASEAN 2022'),
(3, 'H?n 500 ca ?i?u tr? t?y th�nh c�ng m?i n?m');



CREATE TABLE benhnhan (
  benhnhan_id INTEGER PRIMARY KEY AUTOINCREMENT,
  tenBN TEXT,
  gioi_tinh TEXT,
  bacsi_id INTEGER,
  lan_kham_cuoi TEXT, -- SQLite uses TEXT for datetime
  ghi_chu TEXT,
  sdt TEXT,
  email TEXT,
  ngaysinh TEXT,
  FOREIGN KEY (bacsi_id) REFERENCES bacsi(bacsi_id)
);
INSERT INTO benhnhan (tenBN, gioi_tinh, bacsi_id, lan_kham_cuoi, ghi_chu, sdt, email, ngaysinh) VALUES
('Nguy?n Th? H??ng', 'N?', 1, '2024-12-01', 'C� ti?n s? vi�m l?i', '0912345678', 'huongnt@gmail.com', '1996-08-15'),
('Tr?n V?n Minh', 'Nam', 2, '2025-03-20', 'Chu?n b? ni?ng r?ng', '0987654321', 'minhtv@gmail.com', '1990-11-22'),
('L� Ng?c H�', 'N?', 3, '2025-04-01', 'T?y tr?ng ??nh k?', '0978123456', 'haln@gmail.com', '1995-05-05');


CREATE TABLE lichhen (
  lichhen_id INTEGER PRIMARY KEY AUTOINCREMENT,
  bacsi_id INTEGER,
  benhnhan_id INTEGER,
  dichvu_id INTEGER,
  thoigianbatdau TEXT,
  thoigianketthuc TEXT,
  FOREIGN KEY (bacsi_id) REFERENCES bacsi(bacsi_id),
  FOREIGN KEY (benhnhan_id) REFERENCES benhnhan(benhnhan_id),
  FOREIGN KEY (dichvu_id) REFERENCES dichvu(dichvu_id)
);
INSERT INTO lichhen (bacsi_id, benhnhan_id, dichvu_id, thoigianbatdau, thoigianketthuc) VALUES
(1, 1, 1, '2025-05-05 09:00', '2025-05-05 09:30'), -- L�m s?ch r?ng
(2, 2, 5, '2025-05-06 10:00', '2025-05-06 11:30'), -- Ni?ng r?ng
(3, 3, 2, '2025-05-07 14:00', '2025-05-07 14:45'); -- T?y tr?ng r?ng

CREATE TABLE bacsi_dangnhap (
  tendn TEXT PRIMARY KEY,
  bacsi_id INTEGER,
  password TEXT,
  FOREIGN KEY (bacsi_id) REFERENCES bacsi(bacsi_id)
);


INSERT INTO bacsi_dangnhap (tendn, password, bacsi_id) VALUES
('admin', '12345', 1),
('cuong', '12341', 2);
