import solara
from anymap import MapLibreMap


def create_map():
    m = MapLibreMap()
    m.add_basemap("CartoDB.DarkMatter")

    # 加入 GitHub 上的 GeoJSON 檔案
    routes_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/routes.geojson"
    stations_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/stations.geojson"

    # 加入圖層
    m.add_geojson(routes_url, name="Routes")
    m.add_geojson(stations_url, name="Stations")

    m.add_layer_control(collapsed=False)
    return m


@solara.component
def Page():
    with solara.Card():
        create_map().element()