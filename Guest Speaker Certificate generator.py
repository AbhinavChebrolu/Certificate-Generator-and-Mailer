from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list1.csv')
for index,j in df.iterrows():
    img = Image.open('certificate.png')
    draw = ImageDraw.Draw(img)
    w,h = draw.textsize(df)

    #Name
    font = ImageFont.truetype('Lato-Bold.ttf',96)
    Margins = [173, 2073]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,1495),text='{}'.format(j['Name of Guest Speaker']),anchor='ms',fill=(96,79,67),font=font)
    
    #Event Details
    font = ImageFont.truetype('Lato-Bold.ttf',90)
    Margins = [234, 1994]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,2080),text='{}'.format(j['Event Name']),anchor='ms',fill=(96,79,67),font=font)    
    
    #Date
    font = ImageFont.truetype('Lato-Bold.ttf',75)
    Margins = [1096, 1783]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,2225),text='{}'.format(j['Date of Event']),anchor='ms',fill=(96,79,67),font=font)    
        
    #Club Name
    font = ImageFont.truetype('Lato-Bold.ttf',80)
    Margins = [620, 1880]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,2420),text='{}'.format(j['Club & Chapter Name']),anchor='ms',fill=(96,79,67),font=font)    
    
    im=img.convert('RGB')
    #Printing
    #Checking directory exits
    if os.path.exists('Certificates/{}'.format(j['Club & Chapter Name'])):
        #Checking File Exists
        if os.path.isfile('Certificates/{}.pdf'.format(j['Club & Chapter Name'] + '/' + j['Rename Date Org']+j['Name of Guest Speaker'])):
            continue;
        else:
            im.save('Certificates/{}.pdf'.format(j['Club & Chapter Name'] + '/' + j['Rename Date Org']+j['Name of Guest Speaker']))
            print(j['sl.no'], 'Printing Certificate of', j['Name of Guest Speaker'])
    else:
        os.mkdir('Certificates/{}'.format(j['Club & Chapter Name']))
        im.save('Certificates/{}.pdf'.format(j['Club & Chapter Name'] + '/' + j['Rename Date Org']+j['Name of Guest Speaker']))
        print(j['sl.no'], 'Printing Certificate of', j['Name of Guest Speaker'])
        
print('----------------------------------')
print("All Certificates are printed")