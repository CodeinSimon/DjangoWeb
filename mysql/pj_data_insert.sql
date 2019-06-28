-- this is a sql file to insert data into fudan schema
use fudan;

insert ignore into fdusystem_school values
('COMP', '计算机科学技术学院'),
('FORE','外文学院'),
('INFO','信息学院'),
('ECON','经济学院'),
('MANA','管理学院'),
('MICR','微电子学院'),
('SOFT','软件学院'),
('LAWS', '法学院');

insert ignore into fdusystem_major values
('COMP0001', '计算机科学与技术', 'COMP'),
('COMP0002', '信息安全', 'COMP'),
('COMP0003', '保密管理','COMP'),
('FORE0001', '西班牙语', 'FORE'),
('FORE0002', '法语', 'FORE'),
('FORE0003', '英语', 'FORE'),
('FORE0004', '德语', 'FORE'),
('INFO0001', '电子工程', 'INFO'),
('INFO0002', '通信工程', 'INFO'),
('INFO0003', '电光源', 'INFO'),
('INFO0004', '材料学', 'INFO'),
('ECON0001', '国际金融', 'ECON'),
('ECON0002', '金融工程', 'ECON'),
('ECON0003', '会计学', 'ECON'),
('MANA0001', '物流管理', 'MANA'),
('MANA0002', '统计学', 'MANA'),
('MANA0003', '人力资源', 'MANA'),
('MICR0001','微电子工程', 'MICR'),
('SOFT0001', '软件工程', 'SOFT'),
('LAWS0001', '刑法学', 'LAWS'),
('LAWS0002', '民法学', 'LAWS'),
('LAWS0003', '诉讼法', 'LAWS');


insert ignore into fdusystem_teacher values
('00001','何震瀛', 'male', 43, 'Professor',  9900.0, 'COMP'),
('00002','郭跃飞', 'male', 44, 'Associate Professor', 8900.0, 'COMP'),
('00003','孙未未', 'male', 41, 'Professor', 9300.0, 'COMP'),
('00004','汪卫', 'male', 43, 'Associate Professor', 8500.0, 'COMP'),
('00005','赵二鸣', 'male', 42, 'Professor', 9800.0, 'COMP'),
('00006','张亮', 'male', 44, 'Associate Professor', 9900.0, 'COMP'),
('00007','金城', 'male', 38, 'Professor', 9700.0, 'COMP'),
('00008','薛向阳', 'male', 40, 'Associate Professor', 8700.0, 'COMP'),
('00009','梅西', 'male', 32, 'Professor', 19999.0, 'FORE'),
('00010','皮克', 'male', 32, 'Associate Professor', 15900.0, 'FORE'),
('00011','Simon', 'male', 29, 'Associate Professor', 19900.0, 'FORE'),
('00012','梁州', 'male', 26, 'Lecturer', 5900.0, 'FORE'),
('00013','马克龙', 'male', 39, 'Professor', 12900.0, 'FORE'),
('00014','孔庆生', 'male', 48, 'Associate Professor', 11900.0, 'INFO'),
('00015','黄芳', 'female', 37, 'Associate Professor', 11900.0, 'INFO'),
('00016','蒋耿明', 'male', 42, 'Associate Professor', 12930.0, 'INFO'),
('00017','徐丰', 'male', 41, 'Professor', 16900.0, 'INFO'),
('00018','朱晓松', 'male', 38, 'Associate Professor', 10900.0, 'INFO'),
('00019','朱芳', 'female', 35, 'Associate Professor', 13540.0, 'ECON'),
('00020','曾舒怡', 'female', 32, 'Associate Professor', 18900.0, 'ECON'),
('00021','陈民', 'male', 38, 'Associate Professor', 13900.0, 'ECON'),
('00022','陈琳', 'female', 32, 'Associate Professor', 15900.0, 'ECON'),
('00023','张程', 'male', 38, 'Associate Professor', 13900.0, 'MANA'),
('00024','李子明', 'male', 38, 'Professor', 12346.0, 'MANA'),
('00025','程寅', 'female', 35, 'Associate Professor', 12543.0, 'MANA'),
('00026','孙晓佳', 'female', 55, 'Professor', 19890.0, 'MANA'),
('00027','林青', 'male', 58, 'Associate Professor', 16900.0, 'MICR'),
('00028','赵铭', 'male', 48, 'Associate Professor', 16700.0, 'MICR'),
('00029','赵一鸣', 'male', 48, 'Associate Professor', 13200.0, 'SOFT'),
('00030','聂涛', 'male', 28, 'Lecturer', 9900.0, 'SOFT'),
('00031','徐美丽', 'female', 38, 'Associate Professor', 13900.0, 'LAWS'),
('00032','黄韬', 'male', 38, 'Associate Professor', 13900.0, 'LAWS'),
('00033','马云', 'male', 48, 'Associate Professor', 20000.0, 'ECON');


-- select * from fdusystem_teacher where fdusystem_teacher.teacher_id = '00010';

insert ignore into fdusystem_student values
('16307130001', '王自如', 'male', 19, 'COMP0001'),
('16307130002', '李楠', 'male', 19, 'COMP0001'),
('16307130003', '雷军', 'male', 20, 'COMP0001'),
('16307130004', '余承东', 'male', 19, 'COMP0001'),
('16307130005', '吴恩达', 'male', 20, 'COMP0002'),
('16307130006', '韩正', 'male', 20, 'LAWS0001'),
('16307130008', '王沪宁', 'male', 20, 'LAWS0002'),
('16307130007', '董明珠', 'male', 20, 'ECNO0001'),
('16307130008', '郑子健', 'male', 20, 'ECNO0001'),
('16307130009', '赵子杰', 'male', 21, 'MANA0001'),
('16307130010', '朱航宇', 'male', 21, 'INFO0001'),
('16307130011', '俞曦晨', 'male', 22, 'INFO0002'),
('16307130012', '陈卓然', 'male', 22, 'INFO0002'),
('16307130013', '赵雷', 'male', 21, 'INFO0003'),
('16307130014', '内马尔', 'male', 29, 'FORE0001'),
('16307130015', '拉莫斯', 'male', 32, 'FORE0002'),
('16307130016', '王霜', 'female', 26, 'FORE0003'),
('16307130017', '徐仁进', 'male', 20, 'LAWS0002'),
('16307130018', '林山青', 'male', 20, 'MICR0001'),
('16307130019', '邓子明', 'male', 20, 'SOFT0001'),
('16307130020', '潘菁', 'female', 20, 'MANA0001');

insert ignore into fdusystem_classroom values
('Z2101', 40),
('Z2102', 40),
('Z2103', 40),
('Z2104', 80),
('Z2105', 40),
('Z2106', 80),
('Z2201', 40),
('Z2202', 40),
('Z2203', 40),
('Z2204', 80),
('Z2205', 40),
('Z2206', 80),
('Z2207', 80),
('Z2208', 40),
('H3101', 50),
('H3102', 25),
('H3103', 30),
('H3104', 60),
('H3105', 70),
('H3106', 90),
('H3107', 80),
('H3108', 100);

insert ignore into fdusystem_course values
('COMP00001', 'C语言程序设计', 40, 'Z2101', '00001'),
('COMP00002', '数学分析', 40, 'Z2103', '00002'),
('COMP00003', '线性代数', 40, 'Z2105', '00002'),
('COMP00004', '数据结构', 40, 'Z2101', '00003'),
('COMP00005', '数据库引论', 60, 'Z2108', '00004'),
('COMP00006', '计算机系统基础', 20, 'Z2105', '00007'),
('COMP00007', '集合与图论', 40, 'Z2201', '00005'),
('INFO00001', '模拟电子学基础', 40, 'H3101', '00014'),
('INFO00002', '电路分析基础', 50, 'H3101', '00014'),
('COMP00008', '数字信号处理', 40, 'Z2101', '00008'),
('INFO00003', '概率论与数理统计', 80, 'H3106', '00018'),
('ECON00001', '微观经济学', 80, 'H3107', '00022'),
('ECON00002', '宏观经济学', 80, 'H3107', '00022'),
('ECON00003', '财务会计',  80, 'H3108', '00020'),
('FORE00001', '西班牙语基础', 40, 'Z2105', '00010'),
('FORE00002', '基础法语', 40, 'Z2101', '00012'),
('FORE00003', '实用交际英语口语', 40, 'Z2106', '00013'),
('ECON00004', '马云教你投资', 40, 'H3105', '00033');

-- insert ignore into fdusystem_selectcourse values();

insert ignore into fdusystem_precourse values
(1, 'COMP00001','COMP00002');




