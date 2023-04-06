import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df = pd.read_excel("bb/LB1.xlsx")


def get_recommendation(sum_for_vocation, city_preference, age, vacation_preference, transport_preference, family_members):

    x = df.drop("target", axis=1)
    y=df.target
    X_dummies = pd.get_dummies(x, columns=["city_preference", "vacation_preference", "transport_preference"])
    model = RandomForestClassifier()
    model.fit(X_dummies, y)
    model.score(X_dummies, y)
    example = {'sum_for_vocation': [int(sum_for_vocation)], 'age': [int(age)], 'family_members': [0],
               'city_preference_Владивосток': [0],
               'city_preference_Екатеринбург': [0], 'city_preference_Москва': [0], 'city_preference_Новосибирск': [0],
               'city_preference_Петербург': [0], 'city_preference_Хабаровск': [0], 'city_preference_Благовещенск': [0],
               'vacation_preference_Архитектура': [0], 'vacation_preference_Пляжный отдых': [0],
               'vacation_preference_Шоппинг': [0], 'transport_preference_Морской транспорт': [0],
               'transport_preference_Поезд': [0], 'transport_preference_Самолет': [0]}
    if family_members=='alone':
        example['family_members']=[0]
    elif family_members=='1':
        example['family_members']=[1]
    elif family_members=='2':
        example['family_members']=[2]
    elif family_members=='3':
        example['family_members']=[3]
    elif family_members=='4':
        example['family_members']=[4]
    example[city_preference]=[1]
    example[vacation_preference]=[1]
    example[transport_preference]=[1]


    example_df = pd.DataFrame(data=example, columns=X_dummies.columns)
    best_choose_city=model.predict(example_df)[0]
#     # array_choose=model.classes_
#     # array_choose_proba=model.predict_proba(example_df)
    return best_choose_city


