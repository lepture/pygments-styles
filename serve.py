from livereload import Server, shell

shell("make build-docs")()


app = Server()
app.watch("src/pygments_styles", shell("python scripts/build.py"), delay=2)
app.watch("docs", shell("make build-docs"), delay=2)
app.serve(root="build/_html")
