import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon, MultiPolygon

def create_multipolygon(file):
    pass

def import_intersection(data_street, *args):

    # df_area = pd.read_csv(args[0], sep=";")
    # js_area = json.loads(df_area['Geo Shape'][0])
    
    # df = pd.read_csv("data/tempo-30-zonen.csv", sep=";")
    # js = json.loads(df['Geo Shape'][0])
    # data = np.array(js['coordinates'][0])
    # print(data_street)
    df_street = pd.read_csv(str(data_street), sep=";")
    #print(tuple(df_street))

    js_street = json.loads(df_street['Geo Shape'][0])
    # print(df_street)
    street = np.array(js_street['coordinates'][0])
    #print(street)
  
    
    df_area = pd.read_csv(str(args[0]), sep=";")
    js_area_s = json.loads(df_area['Geo Shape'][0])
    area_np = np.array(js_area_s['coordinates'][0])
    poly_area = Polygon (area_np)
    i=0
    for zone in df_area['Geo Shape']:
        #print (zone, 'ZONE')
        js_points = json.loads(zone)
        points = np.array(js_points['coordinates'][0])
        if points.ndim == 3:
            points = points[0]
        print(points, 'points')
        print(points.shape, 'shape')
        i+=1
        print(i)
        poly_area_new = Polygon(tuple(points))
        poly_area=poly_area.union(poly_area_new)
        
    fig, ax = plt.subplots()
    for poly in poly_area:
        x,y=poly.exterior.xy

        ax.plot(x, y)
     
    plt.show()
    #fig, axes= plt.subplots(1,2)
    #axes[0].plot(street[:,0],street[:,1])
    #axes[1].plot(area[:,0],area[:,1])
    plt.show()

    for arg in args:
        if (arg != args[0]):
            df_next_area = pd.read_csv(str(arg), sep=";")
            js_next_area = json.loads(df_next_area['Geo Shape'][0])
            next_area = np.array(js_next_area['coordinates'][0])
            area = np.append(area, next_area,axis=0)
            #print(area)
    #print(area, 'appended')
    polygon_area = Polygon(area)
    print(polygon_area, 'AREA')
  
    
    polygon_street= Polygon(street)
    fig, axes= plt.subplots(1,2)
    axes[0].plot(polygon_area.exterior.xy)
    axes[1].plot(polygon_street.exterior.xy)
    intersection = polygon_area.intersection(polygon_street)
    print(intersection)
    plt.show()
    

    intersetion = 0
    return intersection



if __name__ == "__main__": 
    path_data_30 = "code/data/tempo-30-zonen.csv"
    path_strassenplan = "code/data/gemeindestrassenplan.csv"
    path_begegnungszonen = "code/data/begegnungszonen.csv"
    intersection = import_intersection(path_strassenplan, path_data_30, path_begegnungszonen)
    
    