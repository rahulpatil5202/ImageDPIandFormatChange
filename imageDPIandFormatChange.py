#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time


# In[2]:


root_folder = input('Enter root folder path to process jpg images:')


# In[3]:


print("\n\nProcessing from root folder " + str(root_folder) + "\n\n")
time.sleep(3)


# In[4]:


from PIL import Image

def changeDPIandFormat(file_name):
    im = Image.open(file_name)
    #print(im.info)  # {'dpi': (96, 96), 'gamma': 0.45455}
    #nx, ny = im.size
    #im.resize((int(nx*1), int(ny*1)), Image.BICUBIC)
    dir_name,fl_name = os.path.split(file_name)
    pdf_name = str(os.path.splitext(fl_name)[0]) + ".pdf"
    tiff_name = str(os.path.splitext(fl_name)[0]) + ".tiff"
    pdf_path = os.path.join(dir_name,pdf_name)
    tiff_path = os.path.join(dir_name, tiff_name)
    im.save(pdf_path, dpi=(50,50))
    print("Saved "+str(pdf_path)+" in 50 DPI")
    im.save(tiff_path, dpi=(300,300), compression="jpeg", quality=100)
    print("Saved "+str(tiff_path)+" in 300 DPI")
    print("\n\n")


# In[5]:


all_jpgs = []


# In[6]:


for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".jpg"):
             all_jpgs.append(os.path.join(root, file))


# In[7]:


for cntr,jpg_img in enumerate(all_jpgs):
    print("\n\n")
    print("Processing "+str(cntr+1)+" of "+str(len(all_jpgs)))
    print(str(jpg_img))
    changeDPIandFormat(jpg_img)
print("Processing Done...\n")


# In[10]:


ex = ''
while ex.upper() != 'Q':
    ex = input("Press Q to exit : ")
    
    
    


# In[ ]:




