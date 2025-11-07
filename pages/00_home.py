import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## Solara 台北 GIS 儀表板
        歡迎來到宸晧的 Solara 台北 GIS 儀表板!
        """

        solara.Markdown(markdown)