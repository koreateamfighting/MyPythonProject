#Read Excel file 소스 코드 예
import pandas as pd
import time
from collections import defaultdict
from itertools import chain




ko_KR_dic = {};en_US_dic = {};es_MX_dic = {};fr_US_dic = {};en_AU_dic = {}
en_GB_dic = {};de_DE_dic = {};fr_FR_dic = {};it_IT_dic = {};es_ES_dic = {}
pt_PT_dic = {};nl_NL_dic = {};da_DK_dic = {};sv_SE_dic = {};nb_NO_dic = {}
pl_PL_dic = {};cz_CZ_dic = {};ru_RU_dic = {};bg_BG_dic = {};el_GR_dic = {}
fi_FI_dic = {};tr_TR_dic = {}





total_dic = defaultdict(list)
dataset = pd.read_excel(r'C:/Users/MEDIAZEN/Desktop/VR language library_HMC_20240125.xlsx',sheet_name = '1. Prompt_0122',\
                        usecols="E,U,V,Y,AB,AQ,AT,AW,AZ,BC,BF,BI,BO,BR,BU,BX,CA,CD,CJ,CV,CY,DB,DH",
                            names = ['Index','Korean','English','Mexican Spanish','Canadian French',                                
                                    'English AU','English UK (영국영어)','German (독일어)','French','Italian','Spanish','Portuguese',
                                    'Dutch','Danish','Swedish','Norwegian','Polish','Czech',
                                    'Russian','Bulgarian','Greek','Finnish','Turkish']    

                                ,skiprows =2)
#print(dataset)

for i in dataset.index:   
    ko_KR_dic.update({dataset['Index'][i] : dataset['Korean'][i]})
    en_US_dic.update({dataset['Index'][i] : dataset['English'][i]})
    es_ES_dic.update({dataset['Index'][i] : dataset['Mexican Spanish'][i]})
    en_AU_dic.update({dataset['Index'][i] : dataset['Canadian French'][i]})
    fr_US_dic.update({dataset['Index'][i] : dataset['English AU'][i]})
    en_GB_dic.update({dataset['Index'][i] : dataset['English UK (영국영어)'][i]})
    de_DE_dic.update({dataset['Index'][i] : dataset['German (독일어)'][i]})
    fr_FR_dic.update({dataset['Index'][i] : dataset['French'][i]})
    it_IT_dic.update({dataset['Index'][i] : dataset['Italian'][i]})
    es_ES_dic.update({dataset['Index'][i] : dataset['Spanish'][i]})
    pt_PT_dic.update({dataset['Index'][i] : dataset['Portuguese'][i]})
    nl_NL_dic.update({dataset['Index'][i] : dataset['Dutch'][i]})
    da_DK_dic.update({dataset['Index'][i] : dataset['Danish'][i]})
    sv_SE_dic.update({dataset['Index'][i] : dataset['Swedish'][i]})
    nb_NO_dic.update({dataset['Index'][i] : dataset['Norwegian'][i]})
    pl_PL_dic.update({dataset['Index'][i] : dataset['Polish'][i]})
    cz_CZ_dic.update({dataset['Index'][i] : dataset['Czech'][i]})
    ru_RU_dic.update({dataset['Index'][i] : dataset['Russian'][i]})
    bg_BG_dic.update({dataset['Index'][i] : dataset['Bulgarian'][i]})
    el_GR_dic.update({dataset['Index'][i] : dataset['Greek'][i]})
    fi_FI_dic.update({dataset['Index'][i] : dataset['Finnish'][i]})
    tr_TR_dic.update({dataset['Index'][i] : dataset['Turkish'][i]})



for k, v in chain(ko_KR_dic.items(), en_AU_dic.items(),es_ES_dic.items(),fr_US_dic.items(),en_AU_dic.items(),
                  en_GB_dic.items(),de_DE_dic.items(),fr_FR_dic.items(),it_IT_dic.items(),es_ES_dic.items(),
                  pt_PT_dic.items(),nl_NL_dic.items(),da_DK_dic.items(),sv_SE_dic.items(),nb_NO_dic.items(),
                  pl_PL_dic.items(),cz_CZ_dic.items(),ru_RU_dic.items(),bg_BG_dic.items(),el_GR_dic.items(),
                  fi_FI_dic.items(),tr_TR_dic.items()):
    total_dic[k].append(v)
    
# for k , v in total_dic.items():
#     print(k,v)    


#print(ko_dic)
#print(en_dic)
#total_dic.update(ko_dic)
#total_dic.update(en_dic)

start = time.time()
print(len(total_dic))

print(total_dic.get('LID_PRM_0054_1'))
# print(total_dic)

end = time.time()
print(f"{end - start:.5f}초 나온다.")
