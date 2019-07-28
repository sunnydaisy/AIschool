import pandas as pd

a = pd.Series(['A','B','A','C','F','D'], name = 'grade')
b = pd.Series(['100','82','95','70','35','64'], name = 'score')
c = pd.Series([True, True, True, True, False, False], name = 'pass')

fruits = pd.DataFrame([a,b,c], index=['grade','score','pass'])
print(fruits,'\n')

def main():
    print(fruits.loc['score':],'\n')
    print(fruits.iloc[0,:],'\n')
    
    print(fruits.loc['grade':],'\n')
    print(fruits.iloc[1:],'\n')
    
    name=['Apple','Banana','Cherry','Durian','Elderberry','Fig']
    fruits.loc['name']=name
    print(fruits,'\n')

    temp = fruits.drop('score')
    print(temp,'\n')

    #columns 이름 추가하기
    

if __name__ == '__main__':
    main()