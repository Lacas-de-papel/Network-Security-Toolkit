import geocoder
import folium
import socket
import webbrowser as w
import time

def get_loc(url):
    ip = socket.gethostbyname(url)

    g = geocoder.ip(ip)
    myaddress = g.latlng

    myMap = folium.Map(location=myaddress, zoom_start=12)
    folium.Marker(myaddress, popup="").add_to(myMap)
    folium.CircleMarker(myaddress, radius=50, color='red', fill_color='red').add_to(myMap)

    myMap.save("map.html")
    w.open_new_tab("map.html")
    return f'Latitude: {myaddress[0]} Longitude: {myaddress[1]}\nLocation saved to map.html'



if __name__ == "__main__":
    url = input("Enter a url: ")
    print(get_loc(url))