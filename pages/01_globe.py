import solara
from anymap import MapLibreMap


def create_map():
    # 建立地圖並設定中心點與縮放
    m = MapLibreMap(
        center=[121.55555, 25.08722],  # 經度、緯度（台北市某處）
        zoom=16                        # 縮放層級
    )

    # 加入底圖
    m.add_basemap("CartoDB.DarkMatter")

    # GeoJSON 資料來源
    routes_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/routes.geojson"
    stations_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/stations.geojson"

    # 加入資料來源
    m.add_source("routes", {"type": "geojson", "data": routes_url})
    m.add_source("stations", {"type": "geojson", "data": stations_url})

    # 加入路線圖層
    m.add_layer(
        {
            "id": "routes-layer",
            "type": "line",
            "source": "routes",
            "paint": {
                "line-color": "#00FFFF",
                "line-width": 3
            },
        }
    )

    # 加入站點圖層
    m.add_layer(
        {
            "id": "stations-layer",
            "type": "circle",
            "source": "stations",
            "paint": {
                "circle-radius": 6,
                "circle-color": "#FF9900",
                "circle-stroke-width": 1,
                "circle-stroke-color": "#FFFFFF"
            },
        }
    )

    return m


@solara.component
def Page():
    with solara.Card("地圖展示"):
        create_map().element()