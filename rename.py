import os

dir_list = ['series2014-01-23_2dTB_User_beta10_5e5MCS',
'series2014-01-24_2dTB_User_beta10_5e3MCS',
'series2014-01-24_2dTB_User_beta10_5e6MCS',
'series2014-01-26_2dTB_User_beta10_2e6MCS',
'series2014-01-27_2dTB_User_beta10_3e6MCS']

for name in dir_list:
    cmd = 'mv '+name +' '+name+'_mu_is_0.5U'
    os.system(cmd)



