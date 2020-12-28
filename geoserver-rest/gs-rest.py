from geo.Geoserver import Geoserver
geo = Geoserver('http://127.0.0.1:8080/geoserver',
                username='admin', password='geoserver')

# geo.create_workspace('demo')
# geo.create_coveragestore(
#     lyr_name='raster1', path=r'C:\Users\gic\Desktop\geoserver-rest\data\raster\raster1.tif', workspace='demo')

# geo.create_featurestore('postgis', workspace='demo', db='postgres',
#                         pg_user='postgres', pg_password='gicait123', host='127.0.0.1')

# geo.publish_featurestore(store_name='postgis',
#                          pg_table='jamoat-db', workspace='demo')


# geo.upload_style(
#     path=r'C:\Users\gic\Desktop\geoserver-rest\data\style\raster1.sld', workspace='demo')

# geo.publish_style(layer_name='raster1',
#                   style_name='raster-new', workspace='demo')

# geo.create_coveragestyle(raster_path=r'C:\Users\gic\Desktop\geoserver-rest\data\raster\raster1.tif',
#  style_name='raster-new', workspace='demo', color_ramp='hsv')

# geo.create_outline_featurestyle('polygon-style', workspace='demo')
geo.publish_style(layer_name='jamoat-db',
                  style_name='polygon-style', workspace='demo')
