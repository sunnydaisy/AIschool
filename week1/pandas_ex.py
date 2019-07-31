import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = pd.Series(['A','B','A','C','F','D'], name = 'grade')
b = pd.Series([95,82,100,70,35,64], name = 'score')
c = pd.Series([True, True, True, True, False, False], name = 'pass')

fruits = pd.DataFrame([a,b,c], index=['grade','score','pass'])
print(fruits,'\n')

def main():
    global fruits
    print(fruits.loc['score':],'\n')
    print(fruits.iloc[0,:],'\n')
    
    print(fruits.loc['grade':],'\n')
    print(fruits.iloc[1:],'\n')
    
    name=['Apple','Banana','Cherry','Durian','Elderberry','Fig']
    fruits.loc['name']=name
    print(fruits,'\n')

    temp = fruits.drop('name')
    print(temp,'\n')

    #columns 이름 추가하기
    fruits.columns = name
    print(fruits,'\n')

    fruits = fruits.drop('name')
    print(fruits,'\n')

    review = [85,70,100,75,10,80]
    fruits.loc['review'] = review
    print(fruits,'\n')

    #grade열에 대해 오름차순 정렬
    col_grade = fruits.sort_values('grade', axis=1, ascending=True)
    print(col_grade,'\n')
    #score열에 대해 내림차순 정렬
    col_score = fruits.sort_values('score',1,False)
    print(col_score,'\n')

def draw():
    fig,axes = plt.subplots(2,1)
    x = np.arange(len(fruits.columns))
    axes[0,0].bar(fruits.columns ,fruits['score'])

    p1 = fruits['score']
    p2 = fruits['review']
    res = fruits[p1, p2]

    x_ax = np.arange(len(fruits.columns))
    for i in x_ax:
        axes[1,0].bar(x_ax, res[i], bottom=np.sum(res[:i],axis=0))
    axes[1,0].set_xticks(x_ax)
    axes[1,0].set_xticklabels(fruits.columns)

    plt.show()

if __name__ == '__main__':
    main()