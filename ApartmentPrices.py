# Rosanna De Leon R.

# Data Science

# Final Project
#http://streeteasy.com/for-rent/nyc/beds:2?view=map
#http://docs.python-guide.org/en/latest/scenarios/scrape/

#program to extract all the data from xml file. We need latitud, Longitud and Prices
p=[]
la=[]
log=[]

f = open('aptsXML.tex','r+')
for line in f:
    if '<price>' in line:       
        price=line.replace("<price>"," ")
        price = price.replace("</price>"," ")
#        print int(price)
        p.append(int(price))
print p
#        
for line in f:
    if '<addr_lon>' in line:       
        longitud=line.replace("<addr_lon>"," ")
        longitud = longitud.replace("</addr_lon>"," ")
#        print int(longitud)
        la.append(float(longitud))
print la

for line in f:
    if '<addr_lat>' in line:       
        latitud=line.replace("<addr_lat>"," ")
        latitud = latitud.replace("</addr_lat>"," ")
#        print int(latitud)
        log.append(float(latitud))
print log





#sample from source
#{"1":{"id":1742009,"price":7200,"bedrooms":2.0,"bathrooms":2.0,"half_baths":0,"size_sqft":null,"unittype":"R",
#      "area_id":130,"addr_street":"30 Park Avenue","addr_unit":"#PHK","addr_hood":"Murray Hill","addr_city":"Manhattan",
#      "price_delta":-300,"addr_lon":-73.981,"addr_lat":40.7483,"addr_zip":"10016","title":"30 Park Avenue","building_id":14630,
#      "private_building_id":14630,"source":"the_monterey_nyc_rent","small_image_uri":"http://cdn-img0.streeteasy.com/nyc/image/0/210561900.jpg",
#      "data":{"open_house_last_tweeted":"2016-04-24T14:28:20-04:00"},"type":"featured","noFee":true},

