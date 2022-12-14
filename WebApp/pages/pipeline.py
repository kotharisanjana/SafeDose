# Import
import pickle
import pandas as pd
import numpy as np

PICKLE_FILE_PATH = 'Pickled Files/'

labels = ['ALLABUSE', 'NONALCILL', 'ALCOHOL', 'NONMEDPHARMA', 'PHARMA']

def encoding(test):
    data_onehot = test[['METRO', 'AGECAT', 'SEX', 'RACE', 'PHARMA', 'NONMEDPHARMA', 'ALCOHOL', 'NONALCILL', 'ALLABUSE', \
        'CASETYPE', 'ROUTE_1', 'TOXTEST_1', 'ROUTE_2', 'TOXTEST_2', 'ROUTE_3', 'TOXTEST_3']]

    col_count = {'METRO':14, 'AGECAT':11, 'SEX':3, 'RACE':5, 'PHARMA':2, 'NONMEDPHARMA':2, 'ALCOHOL':2, 'NONALCILL':2, 'ALLABUSE':2, \
        'CASETYPE':8, 'ROUTE_1':7, 'TOXTEST_1':2, 'ROUTE_2':7, 'TOXTEST_2':2, 'ROUTE_3':7, 'TOXTEST_3':2}

    drug_hashencode = test[['DRUGID_1', 'CATID_1_1', 'CATID_2_1', 'CATID_3_1', 'sdled_1_1', 'sdled_2_1', 'sdled_3_1', 'sdled_4_1',
        'DRUGID_2', 'CATID_1_2', 'CATID_2_2', 'CATID_3_2', 'sdled_1_2', 'sdled_2_2', 'sdled_3_2', 'sdled_4_2',
        'DRUGID_3', 'CATID_1_3', 'CATID_2_3', 'CATID_3_3', 'sdled_1_3', 'sdled_2_3', 'sdled_3_3', 'sdled_4_3']]

    data_onehot_encode = pd.DataFrame()
    landing_list = []
    for feature in data_onehot.columns: 
        arr = [0]*(col_count[feature]+1)
        present_value = int(data_onehot[feature].iloc[0])
        arr[present_value] = 1
        if feature not in ['AGECAT', 'SEX', 'RACE']:
            arr.remove(0)
        landing_list.append(arr)

    landing_list = list(np.concatenate(landing_list).flat)

    data_onehot_encode = pd.DataFrame(landing_list).T.reset_index(drop=True)


    encode_drug_data = drug_hashencode.copy()

    for c in encode_drug_data.columns:
        encode_drug_data[c] = encode_drug_data[c].astype('category')

    drughashencode = pd.DataFrame()
    for feature in encode_drug_data.columns:
        encoder = pickle.load(open(PICKLE_FILE_PATH+feature+'.pkl', 'rb'))
        data = encoder.transform(encode_drug_data[feature])
        drughashencode = pd.concat([drughashencode, data], axis = 1)

    drughashencode = drughashencode.reset_index(drop = True)

    test_encoded = pd.concat([data_onehot_encode, drughashencode], axis = 1)
    
    return test_encoded


def pca(test_encoded):
    pca_obj = pickle.load(open(PICKLE_FILE_PATH+'pca_abuse_obj.pkl', 'rb'))

    test_encoded_pca = pca_obj.transform(test_encoded)

    return test_encoded_pca


def predictAbuse(test):
    model = pickle.load(open(PICKLE_FILE_PATH+'randomclassifier.pkl', 'rb'))
    predicted_labels = model.predict(test)

    pred_labels = {k:0 for k in labels}

    for i in range(len(labels)):
        pred_labels[labels[i]] = predicted_labels[0][i]
    
    return pred_labels


def pipeline(test_df):
    test_encoded = encoding(test_df)
    test_enocded_pca = pca(test_encoded)
    predictions = predictAbuse(test_enocded_pca)
    
    return predictions


'''if __name__ == '__main__':
    df = pd.read_csv('abuse_indicator_data.csv')
    test = df.iloc[1].to_frame().T
    test.drop(['Unnamed: 0', 'ALLABUSE', 'NONALCILL', 'ALCOHOL', 'NONMEDPHARMA', 'SUICIDE', 'SEEKING_DETOX', 'sdled_5_1', 'sdled_6_1', 'sdled_5_2', 'sdled_6_2', 'sdled_5_3',
       'sdled_6_3'], axis = 1, inplace = True)
    test.replace({-7:0, -8:0, -9:0}, inplace = True)
    pred = pipeline(test)
    print(pred)'''





