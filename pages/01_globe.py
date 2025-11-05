import solara
from anymap import MapLibreMap


class Map(MapLibreMap):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().add_basemap("CartoDB.DarkMatter")

        # 加入 GitHub 上的 GeoJSON 檔案
        routes_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/routes.geojson"
        stations_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/stations.geojson"

        # 加入圖層
        super().add_geojson(routes_url, name="Routes")
        super().add_geojson(stations_url, name="Stations")

        super().add_layer_control(collapsed=False)


@solara.component
def Page():
    with solara.Card():
        Map().element()


Page()
