from django import forms

class NameForm(forms.Form):
    cities = [(1, 'Nokomis'),
 (2, 'Alliance'),
 (3, 'Antioch'),
 (4, 'Charlotte'),
 (5, 'Renton'),
 (6, 'Cypress'),
 (7, 'Spring Lake'),
 (8, 'Great Falls'),
 (9, 'Vero Beach'),
 (10, 'San Leandro'),
 (11, 'Hillsboro'),
 (12, 'Macungie'),
 (13, 'Panama City'),
 (14, 'Channahon'),
 (15, 'Midland Park'),
 (16, 'Woodford'),
 (17, 'Jamaica'),
 (18, 'Richardson'),
 (19, 'Hockessin'),
 (20, 'New Bern'),
 (21, 'Blue Springs'),
 (22, 'Bokeelia'),
 (23, 'Burlington Flats'),
 (24, 'Blairsville'),
 (25, 'Pasadena'),
 (26, 'Las Vegas'),
 (27, 'Owings Mills'),
 (28, 'Deland'),
 (29, 'Williamston'),
 (30, 'Escondido'),
 (31, 'Marietta'),
 (32, 'Villa Park'),
 (33, 'Covington'),
 (34, 'Lawrenceburg'),
 (35, 'Cross Junction'),
 (36, 'East Elmhurst'),
 (37, 'Huntington Beach'),
 (38, 'Midland'),
 (39, 'Ladson'),
 (40, 'Lawton'),
 (41, 'Lakeville'),
 (42, 'Scotts Valley'),
 (43, 'Conroe'),
 (44, 'Carmel'),
 (45, 'Seven Valleys'),
 (46, 'Chapel Hill'),
 (47, 'Harriman'),
 (48, 'O Fallon'),
 (49, 'Lake Jackson'),
 (50, 'Ocala'),
 (51, 'Indianapolis'),
 (52, 'Lexington'),
 (53, 'Chula Vista'),
 (54, 'Alpharetta'),
 (55, 'Kentland'),
 (56, 'Mount Prospect'),
 (57, 'Sierra Vista'),
 (58, 'Galesburg'),
 (59, 'Page'),
 (60, 'Concord'),
 (61, 'London'),
 (62, 'Vacaville'),
 (63, 'Glendora'),
 (64, 'Wake Forest'),
 (65, 'Tacoma'),
 (66, 'Columbia'),
 (67, 'Cave Springs'),
 (68, 'Waynesboro'),
 (69, 'Roosevelt'),
 (70, 'Pataskala'),
 (71, 'Phoenix'),
 (72, 'Tappan'),
 (73, 'San Ramon'),
 (74, 'Vancouver'),
 (75, 'Jackson'),
 (76, 'Fair Haven'),
 (77, 'Leesburg'),
 (78, 'Delta Junction'),
 (79, 'El Paso'),
 (80, 'Saint Francis'),
 (81, 'San Diego'),
 (82, 'Windsor Mill'),
 (83, 'Ashland'),
 (84, 'Falls Church'),
 (85, 'Matthews'),
 (86, 'Laconia'),
 (87, 'Shiloh'),
 (88, 'Tooele'),
 (89, 'Schenectady'),
 (90, 'Dover'),
 (91, 'Irving'),
 (92, 'Dallas'),
 (93, 'Stamps'),
 (94, 'Dayton'),
 (95, 'Hanover'),
 (96, 'Homestead'),
 (97, 'Lawrenceville'),
 (98, 'Forney'),
 (99, 'New York'),
 (100, 'Minneapolis'),
 (101, 'Calexico'),
 (102, 'Lees Summit'),
 (103, 'Milton'),
 (104, 'Austin'),
 (105, 'Palm Springs'),
 (106, 'Peyton'),
 (107, 'Flint'),
 (108, 'Jessup'),
 (109, 'Prescott Valley'),
 (110, 'Safford'),
 (111, 'Simpsonville'),
 (112, 'Florence'),
 (113, 'Boylston'),
 (114, 'Lafayette'),
 (115, 'Princeton'),
 (116, 'Hightstown'),
 (117, 'Strongsville'),
 (118, 'Myrtle Beach'),
 (119, 'Stafford'),
 (120, 'Moorpark'),
 (121, 'San Bernardino'),
 (122, 'Chicago'),
 (123, 'Houston'),
 (124, 'Jonesboro'),
 (125, 'Church Point'),
 (126, 'Hilliard'),
 (127, 'Monroe'),
 (128, 'Eagar'),
 (129, 'Ozark'),
 (130, 'Jacksonville'),
 (131, 'Cumming'),
 (132, 'Rock Hill'),
 (133, 'Riverdale'),
 (134, 'Hopkins'),
 (135, 'Apple Valley'),
 (136, 'Asbury Park'),
 (137, 'Superior'),
 (138, 'Kingwood'),
 (139, 'Washington'),
 (140, 'Richland'),
 (141, 'Tampa'),
 (142, 'Manchester'),
 (143, 'Prairie Village'),
 (144, 'Lenoir City'),
 (145, 'Ringgold'),
 (146, 'Mystic'),
 (147, 'Orting'),
 (148, 'Marion'),
 (149, 'Rocky Ridge'),
 (150, 'Millburn'),
 (151, 'Pinckney'),
 (152, 'Pinehurst'),
 (153, 'West Palm Beach'),
 (154, 'Paramount'),
 (155, 'Charleston'),
 (156, 'Columbus'),
 (157, 'Upper Marlboro'),
 (158, 'Gilbertsville'),
 (159, 'Wagoner'),
 (160, 'Baton Rouge'),
 (161, 'Santa Fe'),
 (162, 'Middlebury'),
 (163, 'Leesville'),
 (164, 'Northwood'),
 (165, 'New London'),
 (166, 'Pomona'),
 (167, 'Watertown'),
 (168, 'Roscommon'),
 (169, 'Lander'),
 (170, 'Peru'),
 (171, 'Girard'),
 (172, 'Portland'),
 (173, 'Cape Coral'),
 (174, 'Huntsville'),
 (175, 'Oregon'),
 (176, 'Deridder'),
 (177, 'Berry'),
 (178, 'New Lenox'),
 (179, 'Millington'),
 (180, 'Canyon'),
 (181, 'Kermit'),
 (182, 'Kennett Square'),
 (183, 'Deale'),
 (184, 'Camano Island'),
 (185, 'Kunkletown'),
 (186, 'Crossville'),
 (187, 'Middleton'),
 (188, 'Montclair'),
 (189, 'Lutz'),
 (190, 'Milton Freewater'),
 (191, 'Sacramento'),
 (192, 'Castro Valley'),
 (193, 'Durham'),
 (194, 'Seattle'),
 (195, 'Pompano Beach'),
 (196, 'Brooklyn'),
 (197, 'West Warwick'),
 (198, 'Ypsilanti'),
 (199, 'Zephyrhills'),
 (200, 'Haysville'),
 (201, 'Somerset'),
 (202, 'Maitland'),
 (203, 'Deltona'),
 (204, 'Jupiter'),
 (205, 'Pisgah'),
 (206, 'Fort Myers'),
 (207, 'Uhrichsville'),
 (208, 'Hendersonville'),
 (209, 'Milwaukee'),
 (210, 'Holly Springs'),
 (211, 'Millbury'),
 (212, 'Findlay'),
 (213, 'New Portland'),
 (214, 'Scituate'),
 (215, 'Georgetown'),
 (216, 'Roslindale'),
 (217, 'Erie'),
 (218, 'Whittier'),
 (219, 'Lincolnshire'),
 (220, 'Loveland'),
 (221, 'Saint George'),
 (222, 'Chesterton'),
 (223, 'Riverton'),
 (224, 'Lancaster'),
 (225, 'Lake Elsinore'),
 (226, 'Lake Ariel'),
 (227, 'Wilsonville'),
 (228, 'Hodgenville'),
 (229, 'San Antonio'),
 (230, 'Aiken'),
 (231, 'Glastonbury'),
 (232, 'Anaheim'),
 (233, 'Wilmette'),
 (234, 'Los Angeles'),
 (235, 'Reseda'),
 (236, 'Aberdeen'),
 (237, 'Green Valley'),
 (238, 'Tallahassee'),
 (239, 'Chardon'),
 (240, 'Prescott'),
 (241, 'Maynard'),
 (242, 'Fargo'),
 (243, 'Red Bluff'),
 (244, 'Dade City'),
 (245, 'Clarksville'),
 (246, 'Kyle'),
 (247, 'Yuma'),
 (248, 'Englewood'),
 (249, 'Clermont'),
 (250, 'Glen Carbon'),
 (251, 'Cleveland'),
 (252, 'Poway'),
 (253, 'Norfolk'),
 (254, 'Tonawanda'),
 (255, 'Jackson Heights'),
 (256, 'Arnold'),
 (257, 'Waterboro'),
 (258, 'Staten Island'),
 (259, 'Barnegat'),
 (260, 'Kings Mountain'),
 (261, 'Herkimer'),
 (262, 'Windsor'),
 (263, 'Lumberton'),
 (264, 'Nashville'),
 (265, 'Wentzville'),
 (266, 'Amarillo'),
 (267, 'Warren'),
 (268, 'West Islip'),
 (269, 'Carrollton'),
 (270, 'Mesquite'),
 (271, 'Corpus Christi'),
 (272, 'Grove Hill'),
 (273, 'Cedar Rapids'),
 (274, 'Victorville'),
 (275, 'Forest'),
 (276, 'Raleigh'),
 (277, 'Pahrump'),
 (278, 'San Jose'),
 (279, 'Golden'),
 (280, 'Syracuse'),
 (281, 'Rio Vista'),
 (282, 'Bronx'),
 (283, 'Grovetown'),
 (284, 'New Windsor'),
 (285, 'Hattiesburg'),
 (286, 'Alexandria'),
 (287, 'El Dorado'),
 (288, 'Hesperia'),
 (289, 'Birmingham'),
 (290, 'Ewa Beach'),
 (291, 'Clifton'),
 (292, 'Bowling Green'),
 (293, 'Virginia Beach'),
 (294, 'Morton'),
 (295, 'Colorado Springs'),
 (296, 'Palmdale'),
 (297, 'Lorain'),
 (298, 'Madison'),
 (299, 'Burleson'),
 (300, 'Santa Barbara'),
 (301, 'Libby'),
 (302, 'Sugar Land'),
 (303, 'Lincoln'),
 (304, 'West Jordan'),
 (305, 'West Sacramento'),
 (306, 'Montgomery Village'),
 (307, 'Spring'),
 (308, 'Fort Lauderdale'),
 (309, 'North Bend'),
 (310, 'Lewisport'),
 (311, 'Shermans Dale'),
 (312, 'Green Bay'),
 (313, 'Davison'),
 (314, 'Fairfield'),
 (315, 'Painesville'),
 (316, 'White Plains'),
 (317, 'Smithsburg'),
 (318, 'Abingdon'),
 (319, 'Unionville'),
 (320, 'Athens'),
 (321, 'Lilburn'),
 (322, 'Scottsdale'),
 (323, 'Salinas'),
 (324, 'Omaha'),
 (325, 'Danbury'),
 (326, 'De Soto'),
 (327, 'Laredo'),
 (328, 'Goose Creek'),
 (329, 'Perry Hall'),
 (330, 'New Albany'),
 (331, 'Canton'),
 (332, 'Chesterfield'),
 (333, 'Township Of Washington'),
 (334, 'Elk Grove'),
 (335, 'Whitley City'),
 (336, 'Streamwood'),
 (337, 'Rockledge'),
 (338, 'Logan'),
 (339, 'Armonk'),
 (340, 'Murrieta'),
 (341, 'Fredericksburg'),
 (342, 'Centreville'),
 (343, 'Andover'),
 (344, 'Somersworth'),
 (345, 'Orlando'),
 (346, 'Dacula'),
 (347, 'Rockford'),
 (348, 'Sioux Falls'),
 (349, 'Granbury'),
 (350, 'Scott Depot'),
 (351, 'District Heights'),
 (352, 'Camarillo'),
 (353, 'Cibolo'),
 (354, 'Cincinnati'),
 (355, 'Methuen'),
 (356, 'Benton'),
 (357, 'Teaneck'),
 (358, 'Homer Glen'),
 (359, 'Glendale'),
 (360, 'Milledgeville'),
 (361, 'Bellflower'),
 (362, 'Louisville'),
 (363, 'Bath'),
 (364, 'Kenton'),
 (365, 'Lebanon'),
 (366, 'Bellingham'),
 (367, 'Laurens'),
 (368, 'Snohomish'),
 (369, 'Saint Marys'),
 (370, 'Southgate'),
 (371, 'Kansas City'),
 (372, 'Indian Hills'),
 (373, 'Mobile'),
 (374, 'Johnston'),
 (375, 'Decatur'),
 (376, 'Garland'),
 (377, 'Ridgewood'),
 (378, 'Keller'),
 (379, 'Dublin'),
 (380, 'Medina'),
 (381, 'Modesto'),
 (382, 'Turlock'),
 (383, 'Church Hill'),
 (384, 'Red Lake Falls'),
 (385, 'Wilmington'),
 (386, 'Alameda'),
 (387, 'Cordova'),
 (388, 'Murrells Inlet'),
 (389, 'Valrico'),
 (390, 'Yucaipa'),
 (391, 'Thomasville'),
 (392, 'Westcliffe'),
 (393, 'West Orange'),
 (394, 'Mansfield'),
 (395, 'Baltimore'),
 (396, 'Fullerton'),
 (397, 'Duryea'),
 (398, 'Stockbridge'),
 (399, 'Arvada'),
 (400, 'Waterford'),
 (401, 'Fort Smith'),
 (402, 'Fremont'),
 (403, 'Atlanta'),
 (404, 'Stratford'),
 (405, 'Des Moines'),
 (406, 'Chaska'),
 (407, 'Evansville'),
 (408, 'Sylva'),
 (409, 'Yukon'),
 (410, 'El Cajon'),
 (411, 'Council Bluffs'),
 (412, 'Flagstaff'),
 (413, 'Woodbridge'),
 (414, 'Bakersfield'),
 (415, 'Mechanicsville'),
 (416, 'Warrenton'),
 (417, 'Heber Springs'),
 (418, 'Saint Paul'),
 (419, 'Buckeye'),
 (420, 'Willingboro'),
 (421, 'Plainfield'),
 (422, 'Lynn'),
 (423, 'Bridgeville'),
 (424, 'Ossining'),
 (425, 'Port Angeles'),
 (426, 'Rosamond'),
 (427, 'Chula'),
 (428, 'San Dimas'),
 (429, 'Richmond'),
 (430, 'Sebastopol'),
 (431, 'Rio Rancho'),
 (432, 'Hatley'),
 (433, 'Windham'),
 (434, 'Stevens Point'),
 (435, 'Muncie'),
 (436, 'Westerville'),
 (437, 'Red Oak'),
 (438, 'Annapolis'),
 (439, 'Reno'),
 (440, 'Mustang'),
 (441, 'Middletown'),
 (442, 'Needville'),
 (443, 'Mendocino'),
 (444, 'Evanston'),
 (445, 'Port Saint Lucie'),
 (446, 'Suquamish'),
 (447, 'Enterprise'),
 (448, 'Salt Lake City'),
 (449, 'Goodlettsville'),
 (450, 'Winters'),
 (451, 'Standish'),
 (452, 'Gastonia'),
 (453, 'Fayetteville'),
 (454, 'Saint Louis'),
 (455, 'Peabody'),
 (456, 'Miami')]
    credit_score_choices = [('3', '3'), ('5', '5'), ('7', '7'), ('9', '9')]
    veteran_choices = ((1, 'Yes'), (0, 'No'))
    bankfore_choices = ((1, 'bankruptcy'), (2, 'foreclosure'), (3, 'none'))
    property_choices = ((1, 'Investment Property'), (2, 'Owner Occupied'), (3, 'Second Home'))
    city = forms.ChoiceField(label='City of your property:', choices=cities)
    veteran = forms.ChoiceField(label='Are you a veteran?:', widget=forms.RadioSelect, choices=veteran_choices)
    bankfore = forms.ChoiceField(label='Did you ever face with Bankruptcy or ForeClosure:', widget=forms.RadioSelect, choices=bankfore_choices)
    property = forms.ChoiceField(label='What is the purpose of your property:', widget=forms.RadioSelect, choices=property_choices)
    credit_score = forms.ChoiceField(label='Your closest estimated credit score:', choices=credit_score_choices)
    prop_value = forms.CharField(label='What is your estimated property value', max_length=10)
    loan_amt = forms.CharField(label='Expected Loan Amount:', max_length=10)
    cash = forms.CharField(label='Any Additional Cash Required:', max_length=10)
