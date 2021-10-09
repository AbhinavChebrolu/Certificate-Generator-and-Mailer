from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
for index,j in df.iterrows():
    img = Image.open('Winner Certificate.png')
    draw = ImageDraw.Draw(img)
    w,h = draw.textsize(df)

    #Name
    font = ImageFont.truetype('arlrdbd.ttf',65)
    Margins = [310, 1420]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,623),text='{}'.format(j['Name of Winner']),anchor='ms',fill=(0,0,0),font=font)
    
    #Position
    font = ImageFont.truetype('arlrdbd.ttf',50)
    Margins = [518, 580]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,769),text='{}'.format(j['Position']),anchor='ms',fill=(0,0,0),font=font)    
    
    #Event Name
    font = ImageFont.truetype('arlrdbd.ttf',50)
    Margins = [949, 1429]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,769),text='{}'.format(j['Event Name']),anchor='ms',fill=(0,0,0),font=font) 
    
    #Club Name
    font = ImageFont.truetype('arlrdbd.ttf',50)
    Margins = [503, 1065]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,866),text='{}'.format(j['Club & Chapter Name']),anchor='ms',fill=(0,0,0),font=font)    
    
    #Date
    font = ImageFont.truetype('arlrdbd.ttf',50)
    Margins = [1176, 1446]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,866),text='{}'.format(j['Date of Event']),anchor='ms',fill=(0,0,0),font=font)    
        
    #Certificate Number
    font = ImageFont.truetype('arlrdbd.ttf',35)
    Margins = [503, 644]
    x1, x2 = Margins
    draw.text(xy=((x2-x1-w)/2+x1,1083),text='{}'.format(j['Certificate_ID']),anchor='ms',fill=(0,0,0),font=font)

    im=img.convert('RGB')
    #Printing
    if os.path.exists('Certificates/{}'.format(j['Club & Chapter Name'])):
        if os.path.isfile('Certificates/{}.pdf'.format(j['Club & Chapter Name'] + '/' + j['Rename Certificate']+j['Name of Winner'])):
            continue;
        else:
            im.save('Certificates/{}.pdf'.format(j['Club & Chapter Name'] + '/' + j['Rename Certificate']+j['Name of Winner']))
            print(j['sl.no'], 'Printing Certificate of', j['Name of Winner'])
    else:
        os.mkdir('Certificates/{}'.format(j['Club & Chapter Name']))
        im.save('Certificates/{}.pdf'.format(j['Club & Chapter Name'] + '/' + j['Rename Certificate']+j['Name of Winner']))
        print(j['sl.no'], 'Printing Certificate of', j['Name of Winner'])
        
print('----------------------------------')
print("All Certificates are printed")