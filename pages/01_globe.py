import solara
from anymap import MapLibreMap


def create_map(show_routes=True, show_stations=True):
    m = MapLibreMap()
    m.add_basemap("CartoDB.DarkMatter")

    # GeoJSON 資料來源
    routes_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/routes.geojson"
    stations_url = "https://raw.githubusercontent.com/chenhao0506/1105Solara-webmap-app/main/stations.geojson"

    # 加入資料來源
    m.add_source("routes", {"type": "geojson", "data": routes_url})
    m.add_source("stations", {"type": "geojson", "data": stations_url})

    # 根據狀態加入對應圖層
    if show_routes:
        m.add_layer(
            {
                "id": "routes-layer",
                "type": "line",
                "source": "routes",
                "paint": {
                    "line-color": "#00FFFF",
                    "line-width": 3,
                },
            }
        )

    if show_stations:
        m.add_layer(
            {
                "id": "stations-layer",
                "type": "circle",
                "source": "stations",
                "paint": {
                    "circle-radius": 6,
                    "circle-color": "#FF9900",
                    "circle-stroke-width": 1,
                    "circle-stroke-color": "#FFFFFF",
                },
            }
        )

    return m


@solara.component
def Page():
    show_routes, set_show_routes = solara.use_state(True)
    show_stations, set_show_stations = solara.use_state(True)

    with solara.Card("地圖圖層控制"):
        solara.Checkbox(label="顯示 Routes", value=show_routes, on_value=set_show_routes)
        solara.Checkbox(label="顯示 Stations", value=show_stations, on_value=set_show_stations)

    # 地圖元件
    with solara.Card():
        create_map(show_routes, show_stations).element()
