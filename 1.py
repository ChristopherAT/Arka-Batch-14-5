import json
def biodata(nama,umur):
    output = {}
    output['name'] = str(nama)
    output['age'] = int(umur)
    output['address'] = 'Jl. Martadireja I No 29, Purwokerto, Jawa Tengah'
    output['hobbies'] = ['Nonton Film', 'Baca buku//vn', 'Main JRPG']
    output['is_married'] = False
    output['list_school'] = {'name':'UGM','year_in':2012,'year_out':2019,'major':'Mathematics'}
    output['skills'] = [{'skill_name':'web development','level':'beginner'},
		  {'skill_name':'android development','level':'beginner'},
		  {'skill_name':'data analysis','level':'expert'},
		  {'skill_name':'machine learning','level':'advanced'}]
    output['interest_in_coding'] = True
    return json.dumps(output)