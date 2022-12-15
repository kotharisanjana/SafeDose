# Import
import pickle
import pandas as pd
import numpy as np
import lzma

PICKLE_FILE_PATH = 'pickles/'

labels = ['ALLABUSE', 'NONALCILL', 'ALCOHOL', 'NONMEDPHARMA', 'PHARMA']

def encoding(test):
    print('Encoding start')
    data_onehot = test[['METRO', 'AGECAT', 'SEX', 'RACE', \
        'CASETYPE', 'ROUTE_1', 'TOXTEST_1', 'ROUTE_2', 'TOXTEST_2', 'ROUTE_3', 'TOXTEST_3']]

    col_count = {'METRO':14, 'AGECAT':11, 'SEX':2, 'RACE':4, \
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
        if feature in ['METRO', 'CASETYPE']:
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
    print('Encoding finish')
    
    return test_encoded


def pca(test_encoded):
    print('PCA start')
    pca_obj = pickle.load(open(PICKLE_FILE_PATH+'pca_abuse_obj.pkl', 'rb'))

    test_encoded_pca = pca_obj.transform(test_encoded)
    print('PCA end')

    return test_encoded_pca


def predictAbuse(test):
    print('Model start')
    with lzma.open(PICKLE_FILE_PATH+'compressed_randomclassifier_pickle.xz', "rb") as f:
        classifier_model = pickle.load(f)
        predicted_labels = classifier_model.predict(test)

        pred_labels = {k:0 for k in labels}

        for i in range(len(labels)):
            pred_labels[labels[i]] = predicted_labels[0][i]
        print('model end')
        
        return pred_labels


def pipeline(test_df):
    test_encoded = encoding(test_df)
    test_encoded_pca = pca(test_encoded)
    predictions = predictAbuse(test_encoded_pca)
    
    return predictions







