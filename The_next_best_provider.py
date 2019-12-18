# Importing the required libraries
import numpy as np
import pandas as pd
import codecs, json

def provider_recommander_cat(data,cat,p_id):
    """Bu İşlev, kategorideki en başarılı sağlayıcıların liste tabanını döndürür  """
    import numpy as np
    import pandas as pd
    import codecs, json 
    re = data[data['category_id']==cat]
    rm = re[re['provider_id']==p_id]
    ls = rm['couple_id']
    lm = ls.to_numpy()
    rs = csv_n.couple_id.isin(lm)
    rd = csv_n[rs]
    lss= rd[rd['category_id']==cat]
    lk = lss.groupby(['provider_id']).sum().sort_values('weight',ascending=False).index.get_level_values(0)
    lk = lk[lk != p_id]
    return json.dumps(lk.tolist())


# Creating an empty Dataframe with column names only
M = pd.DataFrame(columns=['category_id', 'provider_id', 'offer'])


# finding the provider lit in each category and creating categort, provider couple
gk =  csv_n.groupby(['category_id','provider_id'])
cp = gk.groups.keys()

# processing all te data according to our recommander algorithm 
x = 0
for i in range(len(cp)):
    clist=list(cp)[i][0]
    plist=list(cp)[i][1]
    ff = provider_recommander_cat(csv_n,clist,plist)
    M.at[x, 'category_id'] = clist
    M.at[x, 'provider_id'] = plist
    M.at[x, 'offer'] = ff
    x+=1

