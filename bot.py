from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://br.linkedin.com/?trk=BR-SEM_google-adwords_Jordan-brand-sign-up&mcid=6821526239111716925&trk2=ga_campid=12619604099_asid=122510712920_crid=509739556235_kw=linkedin%20site_d=c_tid=kwd-327301955753_n=g_mt=e_geo=1001773_slid=&gclid=EAIaIQobChMImsWl6K_T9gIVAwqRCh1OxAnuEAAYASAAEgJjTfD_BwE&gclsrc=aw.ds")

input('')