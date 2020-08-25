# Driver function 
import os 
if __name__ == "__main__": 
    rt=[]
    dr=[]
    fl=[]
    for (root,dirs,files) in os.walk('/home/navin/Tractwise_data/hsc-release.mtk.nao.ac.jp/archive/filetree/pdr2_wide/', topdown=True): 
    #for (root,dirs,files) in os.walk('/home/navin/Tractwise_data/useful_codes_techniques', topdown=True):   
        rt.append(root)
        dr.append(dirs)
        fl.append(files)
        #print (root) 
        #print (dirs) 
        #print (files) 
        print('--------------------------------')

    # see the printed form of output to understand what roo,dirs,files can give:
    for ii in range(len(rt)):
        print(rt[ii],'/',dr[ii])
    # notice: len(rt)==len(dr)=len(fl)    

    for ii in range(int(len(dr)/5)):
        print(rt[ii],'/',dr[ii],'/',len(fl[ii]))
        print(fl[ii]) 
