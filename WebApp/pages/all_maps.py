import dash

AGECAT_map = {0:'NA', 1:'<= 5', 2:'6-11',3:'12-17', 4:'18-20', 5:'21-24', 6:'25-29', 7:'30-34', 8:'35-44', 9:'45-54', 10:'55-64',11:'>= 65'}
SEX_map = {0:'NA', 1:'Male', 2:'Female'}
RACE_map = {0:'NA', 1:'White', 2:'Black/African American',3:'Any Hispanic/Latino', 4:'All Other'}
METRO_map = {0:'NA', 1:'MA-NH', 2:'NY-NJ-PA',3:'IL-IN-WI', 4:'MI', 5:'MN-WI', 6:'FL', 7:'FL', 8:'TX', 9:'CO', 10:'AZ',11:'CA', 12:'CA', 13:'WA', 14:'Other'}
CASETYPE_map = {0: 'NA', 1:'Suicide Attempt', 2:'Seeking Detox',3:'Alcohol Only(Age<21)', 4:'Adverse Reaction', 5:'Overmedication', 6:'Malicious Poisoning', 7:'Accidental Injestion', 8:'Other'}
# DISPOSITION_map = {0:'NA', 1:'Discharged home', 2:'Released to police/Jail',3:'Referred to detox/Treatment', 4:'ICU/Critical care', 5:'Surgery', 6:'Chemical dependency/detox, Psychiatric unit', 7:'Other inpatient unit', 8:'Transferred', 9:'Left agaist medical advice', 10:'Died',11:'Other'}
# ALCOHOL_map = {0:'Alcohol not mentioned', 1: 'Alcohol mentioned'}
# NONALCILL_map = {0:'Episode doesn\'t involve illicit drugs', 1: 'Episode involves illicit drugs'}
PHARMA_map = {0:'Episode doesn\'t involve pharmaceuticals', 1: 'Episode involves pharmaceuticals'}
# NONMEDPHARMA_map = {0:'Episode doesn\'t involve non-medical use of pharmaceuticals', 1: 'Episode involves non-medical use of pharmaceuticals'}
# ALLABUSE_map = {0:'Not an All Misuse and Abuse episode', 1:'Is an All Misuse and Abuse episode'}

DRUGID_1_map = {865: 'ALCOHOL (ETHANOL)', 1254: 'COCAINE', 1253: 'HEROIN', 1255: 'MARIJUANA', 2420: 'DRUG UNKNOWN', 21: 'WARFARIN', 2427: 'ANTINEOPLASTICS-NOS', 2343: 'NARCOTIC ANALGESICS-NOS',
 1016: 'ACETAMINOPHEN-HYDROCODONE', 505: 'METHAMPHETAMINE', 85: 'AMOXICILLIN'}
DRUGID_2_map = {1254: 'COCAINE', 1255: 'MARIJUANA', 1253: 'HEROIN', 2420: 'DRUG UNKNOWN', 152: 'ALPRAZOLAM'}
DRUGID_3_map = {1255: 'MARIJUANA', 1254: 'COCAINE', 1253: 'HEROIN', 2343: 'NARCOTIC ANALGESICS-NOS', 2420: 'DRUG UNKNOWN'}

ROUTE_map = {1:'Oral', 2:'Injected', 3:'Inhaled/Sniffed/Snorted', 4:'Smoked', 5:'Other', 6:'Transdermal', 98:'Multiple routes', 0:'No Value'}
TOXTEST_map = {1:'Confirmed', 2:'Unconfirmed', 0:'No Value'}

ALL_ABUSE_INPUT_ROW_1 = {
    'METRO': {'label': 'Metro', 'map': METRO_map}, 
    'AGECAT': {'label': 'Age', 'map': AGECAT_map}, 
    'SEX': {'label': 'Gender', 'map': SEX_map}, 
    'RACE': {'label': 'Race', 'map': RACE_map}
}

ALL_ABUSE_INPUT_ROW_2 = {
    'CASETYPE': {'label': 'Type of case', 'map': CASETYPE_map}, 
    # 'PHARMA': {'label': 'Episode involves pharmaceuticals', 'map': PHARMA_map},
    # 'CASEWGT': {'label': 'Total weight of drugs involved'} 
}

ALL_ABUSE_INPUT_ROW_3 = {
    'DRUGID_1': {'label': 'Drug mention 1' ,'map': DRUGID_1_map},
    'ROUTE_1': {'label': 'Route of administration', 'map': ROUTE_map},
    'TOXTEST_1': {'label': 'Confirmed by Toxicology test', 'map': TOXTEST_map}
}

ALL_ABUSE_INPUT_ROW_4 = {
    'DRUGID_2': {'label': 'Drug mention 2' ,'map': DRUGID_2_map},
    'ROUTE_2': {'label': 'Route of administration', 'map': ROUTE_map},
    'TOXTEST_2': {'label': 'Confirmed by Toxicology test', 'map': TOXTEST_map}
}

ALL_ABUSE_INPUT_ROW_5 = {
    'DRUGID_3': {'label': 'Drug mention 3' ,'map': DRUGID_3_map},
    'ROUTE_3': {'label': 'Route of administration', 'map': ROUTE_map},
    'TOXTEST_3': {'label': 'Confirmed by Toxicology test', 'map': TOXTEST_map}
}


# CATID_1_1_map = {105:'MISCELLANEOUS AGENTS', 57:'CENTRAL NERVOUS SYSTEM AGENTS', 1:'ANTI-INFECTIVES', 242:'PSYCHOTHERAPEUTIC AGENTS', 40:'CARDIOVASCULAR AGENTS', 2006:'DRUG UNKNOWN'}
# CATID_2_1_map = {114:'ILLICIT (STREET) DRUGS', 110:'MISCELLANEOUS UNCATEGORIZED AGENTS', 58:'ANALGESICS'}
# CATID_3_1_map = {0:'NO VALUE', 2032:'ILLICIT MAJOR SUBSTANCE OF ABUSE', 2005:'ALCOHOL IN COMBINATION'}
# CATID_1_2_map = {105:'MISCELLANEOUS AGENTS', 57:'CENTRAL NERVOUS SYSTEM AGENTS', 1:'ANTI-INFECTIVES', 242:'PSYCHOTHERAPEUTIC AGENTS', 2006:'DRUG UNKNOWN', 0:'NO VALUE'}
# CATID_2_2_map = {114:'ILLICIT (STREET) DRUGS', 67:'ANXIOLYTICS,SEDATIVES AND HYPNOTICS', 58:'ANALGESICS', 71:'CNS STIMULANTS', 0:'NO VALUE'}
# CATID_3_2_map = {2032:'ILLICIT MAJOR SUBSTANCE OF ABUSE', 2047:'NARCOTIC ANALGESICS/COMBINATIONS', 69:'BENZODIAZEPINES', 0:'NO VALUE'}
# CATID_1_3_map = {105:'MISCELLANEOUS AGENTS', 57:'CENTRAL NERVOUS SYSTEM AGENTS', 0:'NO VALUE'}
# CATID_2_3_map = {114:'ILLICIT (STREET) DRUGS', 67:'ANXIOLYTICS, SEDATIVES, AND HYPNOTICS', 58:'ANALGESICS', 0:'NO VALUE'}
# CATID_3_3_map = {2032:'ILLICIT MAJOR SUBSTANCE OF ABUSE', 2047:'NARCOTIC ANALGESICS/COMBINATIONS', 0:'NO VALUE'}

# sdled_1_1_map = {1:'MAJOR SUBSTANCES OF ABUSE', 17:'OTHER SUBSTANCES'}
# sdled_2_1_map = {33:'CNS AGENTS', 2.5:'NON-ALCOHOL ILLICITS', 2:'ALCOHOL'}
# sdled_3_1_map = {0:'NO VALUE', 34:'ANALGESICS'}
# sdled_4_1_map = {0:'NO VALUE', 36.5:'OPIATES/OPIOIDS'}
# sdled_5_1_map = {0:'NO VALUE', 37.5:'NARCOTIC ANALGESICS'}
# sdled_6_1_map = {0:'NO VALUE', 37.5:'NARCOTIC ANALGESICS'}
# sdled_1_2_map = {1:'MAJOR SUBSTANCES OF ABUSE', 17:'OTHER SUBSTANCES', 0:'NO VALUE'}
# sdled_2_2_map = {33:'CNS AGENTS', 2.5:'NON-ALCOHOL ILLICITS', 0:'NO VALUE'}
# sdled_3_2_map = {0:'NO VALUE', 34:'ANALGESICS', 3:'COCAINE'}
# sdled_4_2_map = {0:'NO VALUE', 5.01:'MARIJUANA'}
# sdled_5_2_map = {0:'NO VALUE', 37.5:'NARCOTIC ANALGESICS'}
# sdled_6_2_map = {0:'NO VALUE', 37.5:'NARCOTIC ANALGESICS'}
# sdled_1_3_map = {17:'OTHER SUBSTANCES', 0:'NO VALUE'}
# sdled_2_3_map = {2.5:'NON-ALCOHOL ILLICITS', 0:'NO VALUE'}
# sdled_3_3_map = {0:'NO VALUE', 34:'ANALGESICS'}
# sdled_4_3_map = {0:'NO VALUE', 5.01:'MARIJUANA'}
# sdled_5_3_map = {0:'NO VALUE', 37.5:'NARCOTIC ANALGESICS'}
# sdled_6_3_map = {0:'NO VALUE', 37.5:'NARCOTIC ANALGESICS'}


# ALL_ABUSE_INPUT_ROW_1 = {
#     'DRUGID_1': {'label': 'Drug', 'map': DRUGID_1_map},
#     'CATID_1_1': {'label': 'Category 1', 'map': CATID_1_1_map},
#     'CATID_2_1': {'label': 'Category 2', 'map': CATID_2_1_map},
#     'CATID_3_1': {'label': 'Category 3', 'map': CATID_3_1_map}, 
#     'ROUTE_1': {'label': 'Route of administration', 'map': ROUTE_map}, 
#     'TOXTEST_1': {'label': 'Confirmed by Toxicology test', 'map': TOXTEST_map}, 
#     'sdled_1_1': {'label': 'Sdled 1', 'map': sdled_1_1_map}, 
#     'sdled_2_1': {'label': 'Sdled 2', 'map': sdled_2_1_map}, 
#     'sdled_3_1': {'label': 'Sdled 3', 'map': sdled_3_1_map}, 
#     'sdled_4_1': {'label': 'Sdled 4', 'map': sdled_4_1_map}, 
#     'sdled_5_1': {'label': 'Sdled 5', 'map': sdled_5_1_map}, 
#     'sdled_6_1': {'label': 'Sdled 6', 'map': sdled_6_1_map}
# }

# ALL_ABUSE_INPUT_ROW_2 = {
#     'DRUGID_2': {'label': 'Drug', 'map': DRUGID_2_map},
#     'CATID_1_2': {'label': 'Category 1', 'map': CATID_1_2_map},
#     'CATID_2_2': {'label': 'Category 2', 'map': CATID_2_2_map},
#     'CATID_3_2': {'label': 'Category 3', 'map': CATID_3_2_map}, 
#     'ROUTE_2': {'label': 'Route of administration', 'map': ROUTE_map}, 
#     'TOXTEST_2': {'label': 'Confirmed by Toxicology test', 'map': TOXTEST_map}, 
#     'sdled_1_2': {'label': 'Sdled 1', 'map': sdled_1_2_map}, 
#     'sdled_2_2': {'label': 'Sdled 2', 'map': sdled_2_2_map}, 
#     'sdled_3_2': {'label': 'Sdled 3', 'map': sdled_3_2_map}, 
#     'sdled_4_2': {'label': 'Sdled 4', 'map': sdled_4_2_map}, 
#     'sdled_5_2': {'label': 'Sdled 5', 'map': sdled_5_2_map}, 
#     'sdled_6_2': {'label': 'Sdled 6', 'map': sdled_6_2_map}
# }

# ALL_ABUSE_INPUT_ROW_3 = {
#     'DRUGID_3': {'label': 'Drug', 'map': DRUGID_3_map},
#     'CATID_1_3': {'label': 'Category 1', 'map': CATID_1_3_map},
#     'CATID_2_3': {'label': 'Category 2', 'map': CATID_2_3_map},
#     'CATID_3_3': {'label': 'Category 3', 'map': CATID_3_3_map}, 
#     'ROUTE_3': {'label': 'Route of administration', 'map': ROUTE_map}, 
#     'TOXTEST_3': {'label': 'Confirmed by Toxicology test', 'map': TOXTEST_map}, 
#     'sdled_1_3': {'label': 'Sdled 1', 'map': sdled_1_3_map}, 
#     'sdled_2_3': {'label': 'Sdled 2', 'map': sdled_2_3_map}, 
#     'sdled_3_3': {'label': 'Sdled 3', 'map': sdled_3_3_map}, 
#     'sdled_4_3': {'label': 'Sdled 4', 'map': sdled_4_3_map}, 
#     'sdled_5_3': {'label': 'Sdled 5', 'map': sdled_5_3_map}, 
#     'sdled_6_3': {'label': 'Sdled 6', 'map': sdled_6_3_map}
# }




# ALL_ABUSE_INPUT_ROW_4 = {
#     'ALCOHOL': {'label': 'Disposition', 'map': DISPOSITION_map}, 
#     'NONALCILL': {'label': 'Episode involves illicit drugs', 'map': NONALCILL_map}, 
#     'PHARMA': {'label': 'Episode involves pharmaceuticals', 'map': PHARMA_map}, 
#     'NONMEDPHARMA': {'label': 'Episode involves non-medical use of pharmaceuticals', 'map': NONMEDPHARMA_map}, 
#     'CASETYPE': {'label': 'Type of case', 'map': CASETYPE_map}, 
#     'DISPOSITION': {'label': 'Disposition', 'map': DISPOSITION_map}
# }
