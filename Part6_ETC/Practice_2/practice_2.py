import csv

# f = open('large_bike_1.csv', 'r')
# rdr = csv.reader(f)
data = pd.read_csv('large_bike.csv')

my = data[data['location'] == 'busan']

new_data = my.iloc[:, [1, 9, 10]]
dic = {1: {'casual': 0, 'registered': 0}, 2: {'casual': 0, 'registered': 0},
       3: {'casual': 0, 'registered': 0}, 4: {'casual': 0, 'registered': 0}}

for i in range(1, 5):
    season = new_data[new_data['season'] == i]
    dic[i]['casual'] = season.sum(axis=0).casual
    dic[i]['registered'] = season.sum(axis=0).registered

season_all = ['봄', '여름', '가을', '겨울']
for i in range(1, 5):
    print(season_all[i-1]+': casual:', dic[i]['casual'],
          'registered:', dic[i]['registered'])
